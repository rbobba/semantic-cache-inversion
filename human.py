"""Turns the writers' filled sheets into datasets the study's code runs on
(README section 18).

  python human.py --sheet A=<path> --sheet B=<path> --sheet C=<path> [--out data_human]

For each domain, data_human/<domain>/questions.jsonl holds that domain's
cached questions from data_md, unchanged, followed by the writers' questions
as queries. A writer's question carries the gold parameters of its spec: the
cached question's parameters, with the period replaced for a
neighbouring-period spec. It is grouped with the cached question it was
written from, so the bootstrap resamples a spec's three versions together.

The writers' initials are not copied. Writers are A, B and C, in the order
the sheets are given.

Also written, before any extraction or result exists:
  screen.json         the naturalness screen of section 18, and every row
                      whose spec columns differ from the blank sheet
  meaning_check.csv   one row per question, for the agent's meaning check
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import statistics
from pathlib import Path

from domains import REFERENCE_DATE, _period_ranges

HERE = Path(__file__).parent
SPEC_COLUMNS = ("context", "goal", "details", "period")
# A question that repeats this many consecutive words of its row's goal is
# flagged as copied (section 18).
COPY_RUN = 5


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def _words(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", s.lower())


def _copies_goal(question: str, goal: str) -> bool:
    q, g = " ".join(_words(question)), _words(goal)
    return any(" ".join(g[i : i + COPY_RUN]) in q for i in range(len(g) - COPY_RUN + 1))


def _read_sheet(path: Path) -> list[dict]:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")  # a sheet saved by Excel without UTF-8
    return list(csv.DictReader(text.splitlines()))


def _period(label: str) -> str:
    start, end = _period_ranges(REFERENCE_DATE)[label]
    return f"{start.isoformat()}/{min(end, REFERENCE_DATE).isoformat()}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--sheet", action="append", required=True, metavar="W=PATH")
    ap.add_argument("--data", type=Path, default=HERE / "data_md")
    ap.add_argument("--out", type=Path, default=HERE / "data_human")
    args = ap.parse_args()

    blank = {r["spec_id"]: r for r in _read_sheet(args.data / "human_spec_sheet.csv")}
    with (args.data / "human_spec_key.jsonl").open(encoding="utf-8") as f:
        key = {r["spec_id"]: r for r in map(json.loads, f)}

    rows, spec_changed, missing, sheets = [], [], [], {}
    for item in args.sheet:
        writer, _, path = item.partition("=")
        path = Path(path)
        sheets[writer] = {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size,
        }
        got = {r["spec_id"]: r for r in _read_sheet(path) if r.get("spec_id")}
        if set(got) != set(blank):
            raise SystemExit(f"{writer}: spec ids differ from the blank sheet")
        for sid, r in got.items():
            changed = [c for c in SPEC_COLUMNS if _norm(r.get(c)) != _norm(blank[sid][c])]
            if changed:
                spec_changed.append({"writer": writer, "spec_id": sid, "columns": changed})
            q = _norm(r.get("question"))
            if not q:
                missing.append({"writer": writer, "spec_id": sid})
                continue
            rows.append({"writer": writer, "spec_id": sid, "text": q})

    # Exact repeats across writers, after case and punctuation are ignored.
    by_spec: dict[str, list[dict]] = {}
    for r in rows:
        by_spec.setdefault(r["spec_id"], []).append(r)
    duplicate = {
        (r["writer"], r["spec_id"])
        for rs in by_spec.values()
        for r in rs
        if sum(_words(o["text"]) == _words(r["text"]) for o in rs) > 1
    }

    flagged, out_q = [], {}
    for r in rows:
        k = key[r["spec_id"]]
        domain = k["domain"]
        anchors = out_q.setdefault(domain, {})
        if not anchors:
            with (args.data / domain / "questions.jsonl").open(encoding="utf-8") as f:
                for q in map(json.loads, f):
                    if q["is_anchor"]:
                        anchors[q["id"]] = q
        a = anchors[k["anchor_id"]]
        values = json.loads(k["values"])
        params = {**a["params"], "period": _period(values["period"])}
        if k["kind"] == "same_meaning" and params != a["params"]:
            raise SystemExit(f"{r['spec_id']}: same-meaning spec does not match its anchor")
        copied = _copies_goal(r["text"], k["goal"])
        dup = (r["writer"], r["spec_id"]) in duplicate
        if copied or dup:
            flagged.append(
                {"writer": r["writer"], "spec_id": r["spec_id"], "copied": copied, "duplicate": dup}
            )
        hid = f"h{r['writer']}_{r['spec_id']}"
        anchors[hid] = {
            "id": hid,
            "text": r["text"],
            # No gold spans exist for a writer's wording, so the oracle
            # designs that need them are not reported on this data.
            "masked_text": r["text"],
            "intent": k["intent"],
            "params": params,
            "values": values,
            "slots": a["slots"],
            "group": a["group"],
            "is_anchor": False,
            "split": "query",
            "template_id": None,
            "writer": r["writer"],
            "spec_id": r["spec_id"],
            "anchor_id": k["anchor_id"],
            "kind": k["kind"],
            "copied": copied,
            "duplicate": dup,
        }

    for domain, qs in out_q.items():
        base = json.loads((args.data / domain / "manifest.json").read_text(encoding="utf-8"))
        d = args.out / domain
        d.mkdir(parents=True, exist_ok=True)
        lines = "".join(json.dumps(q) + "\n" for q in qs.values())
        (d / "questions.jsonl").write_text(lines, encoding="utf-8", newline="\n")
        (d / "manifest.json").write_text(
            json.dumps(
                {
                    "domain": domain,
                    "reference_date": base["reference_date"],
                    "source": "data_md cached questions + human_spec_sheet answers",
                    "n_cached": sum(q["is_anchor"] for q in qs.values()),
                    "n_human": sum(not q["is_anchor"] for q in qs.values()),
                    "sha256": {"questions.jsonl": hashlib.sha256(lines.encode()).hexdigest()},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def stats(rs: list[dict]) -> dict:
        n = [len(_words(r["text"])) for r in rs]
        q = statistics.quantiles(n, n=4)
        return {
            "n": len(rs),
            "words_median": statistics.median(n),
            "words_iqr": [q[0], q[2]],
            "share_without_question_mark": round(
                sum(not r["text"].endswith("?") for r in rs) / len(rs), 4
            ),
            "share_starting_lowercase": round(sum(r["text"][0].islower() for r in rs) / len(rs), 4),
        }

    screen = {
        "sheets": sheets,
        "empty_rows": missing,
        "spec_columns_changed": spec_changed,
        "flagged": flagged,
        "per_writer": {w: stats([r for r in rows if r["writer"] == w]) for w in sheets},
        "all": stats(rows),
    }
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "screen.json").write_text(json.dumps(screen, indent=2) + "\n", encoding="utf-8")
    with (args.out / "meaning_check.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "goal", "details", "period", "question", "same_meaning (Y/N)", "note"])
        for r in sorted(rows, key=lambda r: (r["spec_id"], r["writer"])):
            k = key[r["spec_id"]]
            w.writerow(
                [
                    f"h{r['writer']}_{r['spec_id']}",
                    k["goal"],
                    k["details"],
                    k["period"],
                    r["text"],
                    "",
                    "",
                ]
            )
    print(
        f"{len(rows)} questions, {len(missing)} empty, {len(spec_changed)} with changed spec "
        f"columns, {len(flagged)} flagged by the screen; written to {args.out}"
    )


if __name__ == "__main__":
    main()
