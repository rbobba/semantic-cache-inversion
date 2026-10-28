"""Extract every question's parameters with a real extractor (README step 5).

evaluate.py ran the split cache designs on the dataset's gold parameters. A
deployed system has an extractor instead. This script produces its output in
the gold format, so that `evaluate.py --extracted` can rerun the designs on
it, and scores the extraction itself with the standard slot-filling metrics:
slot precision / recall / F1 on exact values, and frame accuracy (every slot
of the question right).

Extractors:
  gold              The labels themselves. A sanity check: evaluate.py must
                    reproduce the oracle numbers exactly from it.
  duckling          Duckling, the rule-based parser Rasa ships with, for the
                    period, the amount and top-N; an exact-match gazetteer of
                    the dataset's own entity wordings for merchant, category
                    and account. The gazetteer is an entity oracle by
                    construction, so this arm measures temporal and numeric
                    extraction only. Duckling is told nothing about the
                    dataset's date conventions; it applies its own.
  gemini:<model>    Vertex AI the way the application calls Gemini:
                    temperature 0, JSON output enforced with
                    response_json_schema, location "global". The prompt states
                    the dataset's date conventions, as a deployed system's
                    prompt would state its own.

Usage:
    python extract.py --extractor gold
    python extract.py --extractor duckling --duckling-url http://localhost:8010
    python extract.py --extractor gemini:gemini-3.1-flash-lite --project <gcp-project>

Writes results/extraction/<extractor>/extracted.jsonl, accuracy.json and
accuracy.md. Gemini responses are appended to raw.jsonl as they arrive, so an
interrupted run resumes where it stopped.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

import numpy as np
from generate_dataset import SLOTS

HERE = Path(__file__).parent
SLOT_ORDER = ["period", "merchant", "category", "account", "amount", "n"]
PLACEHOLDER = {slot: spec[3] for slot, spec in SLOTS.items()}


def load(data_dir: Path) -> tuple[list[dict], date]:
    with (data_dir / "questions.jsonl").open(encoding="utf-8") as f:
        questions = [json.loads(line) for line in f if line.strip()]
    manifest = json.loads((data_dir / "manifest.json").read_text(encoding="utf-8"))
    return questions, date.fromisoformat(manifest["reference_date"])


def mask(text: str, spans: list[tuple[int, int, str]]) -> str:
    """Replace each (start, end, slot) span with the slot's placeholder."""
    for start, end, slot in sorted(spans, reverse=True):
        text = text[:start] + PLACEHOLDER[slot] + text[end:]
    return text


def period_value(start: date, end: date, ref: date) -> str:
    # No transaction can be dated after the reference date, so a period that
    # runs past it denotes the same rows as one that stops there. The dataset
    # labels "in 2026" and "this year" equivalent on the same rule.
    return f"{start.isoformat()}/{min(end, ref).isoformat()}"


# ── gold ─────────────────────────────────────────────────────────────────


def extract_gold(questions: list[dict], ref: date) -> dict[str, dict]:
    return {
        q["id"]: {"params": q["params"], "masked_text": q["masked_text"], "note": None}
        for q in questions
    }


# ── duckling + gazetteer ─────────────────────────────────────────────────


def _grain_end(start: date, grain: str) -> date:
    if grain == "week":
        return start + timedelta(days=6)
    if grain in ("month", "quarter", "year"):
        months = {"month": 1, "quarter": 3, "year": 12}[grain]
        m = start.month - 1 + months
        return date(start.year + m // 12, m % 12 + 1, 1) - timedelta(days=1)
    return start  # day or finer


def _duckling_period(value: dict, ref: date) -> str | None:
    """Duckling time value -> 'start/end'.

    A single value with a grain covers that whole grain ("last month" is
    September 1 with grain month). An interval is closed-open in Duckling:
    "last 30 days" is from 09-27 to 10-27 exclusive, so its last day is 10-26.
    """
    if value["type"] == "interval":
        frm, to = value.get("from"), value.get("to")
        if not frm:
            return None
        start = date.fromisoformat(frm["value"][:10])
        end = date.fromisoformat(to["value"][:10]) - timedelta(days=1) if to else ref
        return period_value(start, end, ref)
    start = date.fromisoformat(value["value"][:10])
    return period_value(start, _grain_end(start, value["grain"]), ref)


def _gazetteer() -> dict[str, list[tuple[re.Pattern, str]]]:
    out = {}
    for slot in ("merchant", "category", "account"):
        surfaces = SLOTS[slot][0]
        pats = [(s, v) for v, ss in surfaces.items() for s in ss]
        pats.sort(key=lambda p: -len(p[0]))  # "grocery shopping" before "shopping"
        out[slot] = [
            (re.compile(r"(?<!\w)" + re.escape(s) + r"(?!\w)", re.IGNORECASE), v) for s, v in pats
        ]
    return out


def extract_duckling(questions: list[dict], ref: date, url: str) -> dict[str, dict]:
    reftime = int(datetime(ref.year, ref.month, ref.day, 12, tzinfo=UTC).timestamp() * 1000)
    gaz = _gazetteer()

    def parse(text: str) -> list[dict]:
        body = urllib.parse.urlencode(
            {
                "locale": "en_US",
                "text": text,
                "dims": json.dumps(["time", "amount-of-money", "number"]),
                "reftime": reftime,
                "tz": "UTC",
            }
        ).encode()
        with urllib.request.urlopen(url.rstrip("/") + "/parse", body, timeout=30) as r:
            return json.loads(r.read())

    def one(q: dict) -> tuple[str, dict]:
        text = q["text"]
        ents = parse(text)
        params: dict = {}
        spans: list[tuple[int, int, str]] = []
        taken = np.zeros(len(text), dtype=bool)

        def claim(s: int, e: int, slot: str) -> None:
            spans.append((s, e, slot))
            taken[s:e] = True

        # Longest time expression is the period; a shorter one inside it is
        # Duckling offering a sub-reading, not a second period.
        times = sorted((e for e in ents if e["dim"] == "time"), key=lambda e: e["start"] - e["end"])
        for e in times[:1]:
            v = _duckling_period(e["value"], ref)
            if v:
                params["period"] = v
                claim(e["start"], e["end"], "period")
        for e in ents:
            if (
                e["dim"] == "amount-of-money"
                and "amount" not in params
                and not taken[e["start"] : e["end"]].any()
            ):
                params["amount"] = round(e["value"]["value"])
                claim(e["start"], e["end"], "amount")
        # Any number left over is read as the N of a top-N question. Duckling
        # has no notion of which number a question is about; this is the
        # generic mapping, not one tuned to the templates.
        for e in ents:
            if (
                e["dim"] == "number"
                and "n" not in params
                and not taken[e["start"] : e["end"]].any()
            ):
                params["n"] = round(e["value"]["value"])
                claim(e["start"], e["end"], "n")
        for slot, pats in gaz.items():
            for pat, value in pats:
                m = pat.search(text)
                if m and not taken[m.start() : m.end()].any():
                    params[slot] = value
                    claim(m.start(), m.end(), slot)
                    break
        return q["id"], {"params": params, "masked_text": mask(text, spans), "note": None}

    with ThreadPoolExecutor(8) as pool:
        return dict(pool.map(one, questions))


# ── gemini ───────────────────────────────────────────────────────────────


def _gemini_prompt(ref: date) -> str:
    def ids(slot: str) -> str:
        return ", ".join(f"{v} ({ss[0]})" for v, ss in SLOTS[slot][0].items())

    return f"""\
You extract the parameters of a question about the user's personal finances, so
that a cached SQL query can be reused with the new values.

Today is {ref.strftime("%A")} {ref.isoformat()}.

For each parameter, return null if the question does not state it. Otherwise
return "text": the exact span of the question that expresses it, copied
character for character, plus its value.

period (every question has one): "start" and "end" as YYYY-MM-DD, both inclusive.
The span includes a leading preposition or qualifier ("in", "during", "over the",
"so far") when the question has one.
- No transaction exists after today, so a period never ends after today: if a
  calendar period runs past today, end it today.
- Weeks start on Monday.
- "this week", "this month", "this year", "so far this ...", "year to date": from
  the first day of the current week, month or year, to today.
- "last week", "last month", "last year", "the previous ...": the whole previous
  calendar week, month or year.
- A named month, quarter or year ("August 2026", "Q2 2026", "the second quarter of
  2026", "2025"): that calendar period. Q1 is January to March.
- "the last N days", "the past N days": the N days ending today.
- "the last 3 months" or "the past three months": start = today minus 91 days.
  "the last 6 months": today minus 182 days. "the last 12 months": today minus
  364 days. Each ends today.

merchant: one of {ids("merchant")}. Return the id.
category: a spending category named in the question, one of {ids("category")}. Return the id.
account: one of {ids("account")}. Return the id.
amount: a dollar amount in the question, as an integer number of dollars.
n: the number of items asked for in a "top N" question, as an integer.
"""


def _gemini_schema() -> dict:
    def slot(value: dict) -> dict:
        return {
            "type": ["object", "null"],
            "properties": {"text": {"type": "string"}, "value": value},
            "required": ["text", "value"],
        }

    def enum(slot_name: str) -> dict:
        return {"type": "string", "enum": list(SLOTS[slot_name][0])}

    return {
        "type": "object",
        "properties": {
            "period": {
                "type": ["object", "null"],
                "properties": {
                    "text": {"type": "string"},
                    "start": {"type": "string"},
                    "end": {"type": "string"},
                },
                "required": ["text", "start", "end"],
            },
            "merchant": slot(enum("merchant")),
            "category": slot(enum("category")),
            "account": slot(enum("account")),
            "amount": slot({"type": "integer"}),
            "n": slot({"type": "integer"}),
        },
        "required": SLOT_ORDER,
    }


def _from_llm_json(text: str, out: dict, ref: date) -> dict:
    """Model JSON -> gold-format params and masked text.

    A span the model did not copy exactly cannot be masked; the value is still
    used, and the miss is recorded in `note` so it shows in the error table.
    """
    params: dict = {}
    spans: list[tuple[int, int, str]] = []
    notes = []
    for slot in SLOT_ORDER:
        v = out.get(slot)
        if not v:
            continue
        try:
            if slot == "period":
                params[slot] = period_value(
                    date.fromisoformat(v["start"]), date.fromisoformat(v["end"]), ref
                )
            elif slot in ("amount", "n"):
                params[slot] = int(v["value"])
            else:
                params[slot] = str(v["value"])
        except (KeyError, TypeError, ValueError) as exc:
            notes.append(f"{slot}: unparseable value {v!r} ({exc})")
            continue
        i = text.find(v.get("text") or "\0")
        if i < 0:
            notes.append(f"{slot}: span {v.get('text')!r} not in question")
        else:
            spans.append((i, i + len(v["text"]), slot))
    # Overlapping spans cannot both be masked; keep the earlier-starting, longer one.
    spans.sort(key=lambda s: (s[0], s[0] - s[1]))
    kept, end = [], -1
    for s in spans:
        if s[0] >= end:
            kept.append(s)
            end = s[1]
        else:
            notes.append(f"{s[2]}: span overlaps another")
    return {"params": params, "masked_text": mask(text, kept), "note": "; ".join(notes) or None}


def extract_gemini(
    questions: list[dict], ref: date, model: str, project: str, location: str, raw_path: Path
) -> dict[str, dict]:
    from google import genai
    from google.genai import types

    client = genai.Client(vertexai=True, project=project, location=location)
    cfg = types.GenerateContentConfig(
        temperature=0.0,
        response_mime_type="application/json",
        response_json_schema=_gemini_schema(),
        system_instruction=_gemini_prompt(ref),
        # Gemini 3 bills thinking against max_output_tokens (config.py notes
        # this for the agent); leave room so a long think cannot truncate JSON.
        max_output_tokens=4096,
    )
    done: dict[str, dict] = {}
    if raw_path.exists():
        for line in raw_path.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("response") is not None:
                done[r["id"]] = r
    todo = [q for q in questions if q["id"] not in done]
    print(f"{len(done)} already extracted, {len(todo)} to go", flush=True)

    def call(q: dict) -> dict:
        last = None
        for _ in range(5):
            try:
                res = client.models.generate_content(model=model, contents=q["text"], config=cfg)
                u = res.usage_metadata
                return {
                    "id": q["id"],
                    "response": json.loads(res.text),
                    "usage": {
                        "prompt": u.prompt_token_count,
                        "output": u.candidates_token_count,
                        "thinking": getattr(u, "thoughts_token_count", None),
                    },
                }
            except Exception as exc:
                last = f"{type(exc).__name__}: {exc}"
        return {"id": q["id"], "response": None, "error": last}

    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(8) as pool, raw_path.open("a", encoding="utf-8") as f:
        for i, r in enumerate(pool.map(call, todo), 1):
            f.write(json.dumps(r) + "\n")
            f.flush()
            if r["response"] is not None:
                done[r["id"]] = r
            if i % 100 == 0:
                print(f"  {i}/{len(todo)}", flush=True)

    failed = [q["id"] for q in questions if q["id"] not in done]
    if failed:
        raise SystemExit(f"{len(failed)} questions failed, e.g. {failed[0]}; rerun to resume")
    by_id = {q["id"]: q for q in questions}
    return {i: _from_llm_json(by_id[i]["text"], r["response"], ref) for i, r in done.items()}


# ── scoring ──────────────────────────────────────────────────────────────


def score(questions: list[dict], ext: dict[str, dict], n_boot: int, seed: int) -> dict:
    """Slot P/R/F1 on exact normalised values, and frame accuracy.

    A wrong value counts as one false positive and one false negative, the
    usual convention for slot filling.
    """
    tp, fp, fn = Counter(), Counter(), Counter()
    frame_ok, groups = [], []
    by_period = defaultdict(list)
    errors = []
    for q in questions:
        gold, pred = q["params"], ext[q["id"]]["params"]
        for slot in SLOT_ORDER:
            g, p = gold.get(slot), pred.get(slot)
            if g is not None and p == g:
                tp[slot] += 1
            else:
                fp[slot] += p is not None
                fn[slot] += g is not None
        ok = gold == pred
        frame_ok.append(ok)
        groups.append(q["group"])
        by_period[q["values"]["period"]].append(gold.get("period") == pred.get("period"))
        if not ok:
            errors.append(
                {
                    "id": q["id"],
                    "text": q["text"],
                    "gold": gold,
                    "pred": pred,
                    "note": ext[q["id"]]["note"],
                }
            )

    def prf(t: int, p: int, n: int) -> dict:
        prec = t / (t + p) if t + p else float("nan")
        rec = t / (t + n) if t + n else float("nan")
        f1 = 2 * prec * rec / (prec + rec) if prec + rec else float("nan")
        return {
            "tp": t,
            "fp": p,
            "fn": n,
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4),
        }

    slots = {s: prf(tp[s], fp[s], fn[s]) for s in SLOT_ORDER if tp[s] + fn[s]}
    micro = prf(sum(tp.values()), sum(fp.values()), sum(fn.values()))

    # Cluster bootstrap over question groups, as in evaluate.py.
    rng = np.random.default_rng(seed)
    ok_a = np.array(frame_ok, dtype=float)
    gids = sorted(set(groups))
    gpos = {g: i for i, g in enumerate(gids)}
    gq = np.array([gpos[g] for g in groups])
    boots = []
    for _ in range(n_boot):
        w = np.bincount(rng.integers(0, len(gids), len(gids)), minlength=len(gids))[gq]
        boots.append(float((w * ok_a).sum() / w.sum()))
    return {
        "n_questions": len(questions),
        "frame_accuracy": round(float(ok_a.mean()), 4),
        "frame_accuracy_ci95": [
            round(float(np.percentile(boots, 2.5)), 4),
            round(float(np.percentile(boots, 97.5)), 4),
        ],
        "slot_micro": micro,
        "slots": slots,
        "period_accuracy_by_value": {
            k: {"n": len(v), "accuracy": round(sum(v) / len(v), 4)}
            for k, v in sorted(by_period.items())
        },
        "unmasked_or_bad_spans": sum(1 for e in ext.values() if e["note"]),
        "errors": errors,
    }


def write_markdown(name: str, acc: dict, path: Path) -> None:
    lines = [
        f"# Extraction: {name}",
        "",
        f"{acc['n_questions']} questions. Frame accuracy (every slot right): "
        f"**{acc['frame_accuracy']}** {acc['frame_accuracy_ci95']}. "
        f"Slot micro-F1 {acc['slot_micro']['f1']}. "
        f"Questions with a span or value note: {acc['unmasked_or_bad_spans']}.",
        "",
        "| Slot | TP | FP | FN | precision | recall | F1 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for s, m in acc["slots"].items():
        lines.append(
            f"| {s} | {m['tp']} | {m['fp']} | {m['fn']} | {m['precision']} | {m['recall']} | {m['f1']} |"
        )
    lines += [
        "",
        "## Period accuracy by gold value",
        "",
        "| Period | n | accuracy |",
        "|---|---:|---:|",
    ]
    for k, v in acc["period_accuracy_by_value"].items():
        lines.append(f"| {k} | {v['n']} | {v['accuracy']} |")
    lines += [
        "",
        "## First 40 errors",
        "",
        "| Question | gold | extracted | note |",
        "|---|---|---|---|",
    ]
    for e in acc["errors"][:40]:
        lines.append(
            f"| {e['text']} | `{json.dumps(e['gold'])}` | `{json.dumps(e['pred'])}` | {e['note'] or ''} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--data", type=Path, default=HERE / "data")
    ap.add_argument("--out", type=Path, default=HERE / "results" / "extraction")
    ap.add_argument("--extractor", required=True)
    ap.add_argument("--duckling-url", default="http://localhost:8010")
    ap.add_argument("--project", default="")
    ap.add_argument(
        "--location", default="global", help="Vertex location for Gemini (the app uses global)"
    )
    ap.add_argument("--bootstrap", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    questions, ref = load(args.data)
    kind, _, model = args.extractor.partition(":")
    out_dir = args.out / re.sub(r"[^A-Za-z0-9._-]+", "_", args.extractor)
    if kind == "gold":
        ext = extract_gold(questions, ref)
    elif kind == "duckling":
        ext = extract_duckling(questions, ref, args.duckling_url)
    elif kind == "gemini":
        if not args.project:
            raise SystemExit("--project is required for gemini extractors")
        ext = extract_gemini(
            questions, ref, model, args.project, args.location, out_dir / "raw.jsonl"
        )
    else:
        raise SystemExit(f"unknown extractor {args.extractor!r}")

    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "extracted.jsonl").open("w", encoding="utf-8") as f:
        for q in questions:
            f.write(json.dumps({"id": q["id"], **ext[q["id"]]}) + "\n")
    acc = score(questions, ext, args.bootstrap, args.seed)
    acc["extractor"] = args.extractor
    (out_dir / "accuracy.json").write_text(json.dumps(acc, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.extractor, acc, out_dir / "accuracy.md")
    print((out_dir / "accuracy.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
