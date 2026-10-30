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
  gemini-rel:<model>
                    The same call and prompt, except that the model labels
                    the period ("last_n_days", n=30) instead of computing its
                    dates, and code turns the label into dates, the way the
                    application's SQL leaves that to CURRENT_DATE.
  gemini-relsig:<model>
                    gemini-rel plus an operator signature (operation, excludes,
                    flow) for the guarded cache of README section 15.
  gemini-relfull:<model>
                    gemini-rel plus the full signature (operation, measure,
                    group_by, excludes) of README section 18.
  gemini:<model>    Vertex AI the way the application calls Gemini:
                    temperature 0, JSON output enforced with
                    response_json_schema, location "global". The prompt states
                    the dataset's date conventions, as a deployed system's
                    prompt would state its own.
  openai:<model>, openai-rel:<model>, openai-relsig:<model>, openai-relfull:<model>
                    The same arms with the same prompt and schema
                    through OpenAI's Responses API (README section 16), at the
                    vendor's default settings. Needs OPENAI_API_KEY.

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
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

import numpy as np
from domains import DOMAINS, FINANCE, Domain

HERE = Path(__file__).parent

# The domain being extracted. A CLI processes one dataset, hence one domain,
# per run; _use_domain() sets these once in main(), and every function below
# reads them at call time.
DOMAIN: Domain = FINANCE
SLOTS = FINANCE.slots
SLOT_ORDER = FINANCE.slot_order
PLACEHOLDER = {slot: spec[3] for slot, spec in SLOTS.items()}


def _use_domain(d: Domain) -> None:
    global DOMAIN, SLOTS, SLOT_ORDER, PLACEHOLDER
    DOMAIN, SLOTS, SLOT_ORDER = d, d.slots, d.slot_order
    PLACEHOLDER = {slot: spec[3] for slot, spec in SLOTS.items()}


def load(data_dir: Path) -> tuple[list[dict], date, Domain]:
    with (data_dir / "questions.jsonl").open(encoding="utf-8") as f:
        questions = [json.loads(line) for line in f if line.strip()]
    manifest = json.loads((data_dir / "manifest.json").read_text(encoding="utf-8"))
    # v1 and v2 manifests predate domains and are finance.
    domain = DOMAINS[manifest.get("domain", "finance")]
    return questions, date.fromisoformat(manifest["reference_date"]), domain


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
                # "over $100" comes back as an open interval; its bound is the
                # threshold the question is about.
                v = e["value"]
                bound = v.get("value", (v.get("from") or v.get("to") or {}).get("value"))
                if bound is not None:
                    params["amount"] = round(bound)
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


# The two period sections are the only difference between the absolute and
# the relative arm; everything else in the prompt is shared, so a difference
# in results can be put down to who does the date arithmetic.
_PERIOD_ABSOLUTE = """\
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
  364 days. Each ends today."""

_PERIOD_RELATIVE = """\
period (every question has one): classify it; do not compute any dates.
The span includes a leading preposition or qualifier ("in", "during", "over the",
"so far") when the question has one. "kind" is one of:
- this_week, this_month, this_year: the current week, month or year so far
  ("this month", "so far this month", "year to date").
- last_week, last_month, last_year: the whole previous calendar week, month or
  year ("last month", "the previous month").
- last_n_days, last_n_months: a rolling window ending today ("the last 30 days",
  "the past three months"). Put N in "n".
- calendar_month, calendar_quarter, calendar_year: a named period ("August 2026",
  "Q2 2026", "the second quarter of 2026", "2025"). Put the year in "year", and
  the month (1-12) or quarter (1-4) in "number".
Use null for the fields a kind does not need."""


# The operator signature (README section 15). Embeddings judge topic well and
# operators badly, so the guarded cache asks the extractor for the operators
# directly. Domain-general by design: no field names a domain's vocabulary.
SIGNATURE_OPERATIONS = [
    "sum",
    "count",
    "average",
    "maximum",
    "rate",
    "list",
    "rank",
    "difference",
]
SIGNATURE_FLOWS = ["inbound", "outbound", "net", "none"]

_SIGNATURE = """\
Also describe what the question computes, independently of its values:
operation: one of
- sum: a total amount (total spent, revenue, refunds, charges billed)
- count: how many (transactions, orders, visits, tickets, referrals)
- average: an average or mean
- maximum: the single largest, longest or most expensive item
- rate: a share or percentage
- list: every item above a threshold
- rank: the top N items by some measure
- difference: one quantity minus another (net cash flow, net sales, backlog change)
excludes: true if the question asks about everything EXCEPT a named value, otherwise false.
flow: one of
- inbound: what comes in to the user or organisation (income, refunds the user
  receives, sales revenue, incoming referrals, tickets received or opened)
- outbound: what goes out (spending, refunds or returns paid to customers,
  outgoing referrals, tickets resolved or closed)
- net: inbound minus outbound
- none: neither applies"""

# The full signature (README section 18): the operation, plus the measure and
# grouping from the domain's own lists, so that no part of what a question
# computes is left to similarity. Definitions are written to have one reading
# each; section 15's "flow" had two outside finance.
_FULL_SIGNATURE = """\
Also describe what the question computes, independently of its values:
operation: one of
- sum: a total amount of money (total spent, revenue, refunds, charges billed).
  A total of anything that is not money is a count.
- count: how many of something, including totals of things that are not money
  (transactions, orders, units sold, visits, referrals, no-shows, tickets)
- average: an average or mean (average price, average wait, average resolution time)
- maximum: the single largest, longest or most expensive item
- rate: a share or percentage, or how often something happens
- list: every item above a threshold, or whether any exist
- rank: the top N items by some measure
- difference: one quantity minus another, including any net figure (net sales,
  net cash flow, what is left after something)
measure: what is being added up, counted, averaged or ranked. For list and
maximum, it is the quantity compared with the threshold or maximised. One of
{measures}
group_by: what the question ranks or breaks its answer down by. One of
{groupings}
- none: the question asks for a single number, a single item or a list
excludes: true if the question asks about everything EXCEPT a named value, otherwise false."""


def _full_signature_block() -> str:
    from guards import FULL_GROUPINGS, FULL_MEASURES

    def lines(d: dict[str, str]) -> str:
        return "\n".join(f"- {k}: {v}" for k, v in d.items())

    return _FULL_SIGNATURE.format(
        measures=lines(FULL_MEASURES[DOMAIN.name]), groupings=lines(FULL_GROUPINGS[DOMAIN.name])
    )


def _gemini_prompt(
    ref: date, relative: bool = False, signature: bool = False, full: bool = False
) -> str:
    def ids(slot: str) -> str:
        # The full arm lists every known wording of a value, as a semantic
        # layer's synonyms would. The other arms show only the first, which
        # left "critical" = p1 unstated (section 19).
        return ", ".join(
            f"{v} ({', '.join(ss if full else ss[:1])})" for v, ss in SLOTS[slot][0].items()
        )

    slot_lines = "\n".join(
        f"{s}: {DOMAIN.slot_prompts[s].format(ids=ids(s))}" for s in SLOT_ORDER if s != "period"
    )
    if signature:
        slot_lines += "\n\n" + _SIGNATURE
    if full:
        slot_lines += "\n\n" + _full_signature_block()
    return f"""\
{DOMAIN.prompt_intro}

Today is {ref.strftime("%A")} {ref.isoformat()}.

For each parameter, return null if the question does not state it. Otherwise
return "text": the exact span of the question that expresses it, copied
character for character, plus its value.

{_PERIOD_RELATIVE if relative else _PERIOD_ABSOLUTE}

{slot_lines}
"""


PERIOD_KINDS = [
    "this_week",
    "this_month",
    "this_year",
    "last_week",
    "last_month",
    "last_year",
    "last_n_days",
    "last_n_months",
    "calendar_month",
    "calendar_quarter",
    "calendar_year",
]


def resolve_relative(v: dict, ref: date) -> str:
    """A relative period label -> 'start/end', in code rather than in the model.

    The conventions are the dataset's (generate_dataset._period_ranges), as an
    application would hold its own in one place. In production the same job
    is done by SQL such as DATE_TRUNC('month', CURRENT_DATE).
    """
    kind = v["kind"]
    week = ref - timedelta(days=ref.weekday())
    month = ref.replace(day=1)
    if kind == "this_week":
        return period_value(week, ref, ref)
    if kind == "this_month":
        return period_value(month, ref, ref)
    if kind == "this_year":
        return period_value(date(ref.year, 1, 1), ref, ref)
    if kind == "last_week":
        return period_value(week - timedelta(days=7), week - timedelta(days=1), ref)
    if kind == "last_month":
        start = (month - timedelta(days=1)).replace(day=1)
        return period_value(start, month - timedelta(days=1), ref)
    if kind == "last_year":
        return period_value(date(ref.year - 1, 1, 1), date(ref.year - 1, 12, 31), ref)
    if kind == "last_n_days":
        return period_value(ref - timedelta(days=int(v["n"]) - 1), ref, ref)
    if kind == "last_n_months":
        # 91 days per quarter: 3 -> 91, 6 -> 182, 12 -> 364, as the dataset defines them.
        return period_value(ref - timedelta(days=round(int(v["n"]) * 91 / 3)), ref, ref)
    year = int(v["year"])
    if kind == "calendar_year":
        return period_value(date(year, 1, 1), date(year, 12, 31), ref)
    if kind == "calendar_month":
        start = date(year, int(v["number"]), 1)
        return period_value(start, _grain_end(start, "month"), ref)
    if kind == "calendar_quarter":
        start = date(year, 3 * int(v["number"]) - 2, 1)
        return period_value(start, _grain_end(start, "quarter"), ref)
    raise ValueError(f"unknown period kind {kind!r}")


def _gemini_schema(relative: bool = False, signature: bool = False, full: bool = False) -> dict:
    def slot(value: dict) -> dict:
        return {
            "type": ["object", "null"],
            "properties": {"text": {"type": "string"}, "value": value},
            "required": ["text", "value"],
        }

    def enum(slot_name: str) -> dict:
        return {"type": "string", "enum": list(SLOTS[slot_name][0])}

    if relative:
        period = {
            "type": ["object", "null"],
            "properties": {
                "text": {"type": "string"},
                "kind": {"type": "string", "enum": PERIOD_KINDS},
                "n": {"type": ["integer", "null"]},
                "year": {"type": ["integer", "null"]},
                "number": {"type": ["integer", "null"]},
            },
            "required": ["text", "kind", "n", "year", "number"],
        }
    else:
        period = {
            "type": ["object", "null"],
            "properties": {
                "text": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"},
            },
            "required": ["text", "start", "end"],
        }
    # Named entities are closed sets (enums); amount and n are integers.
    properties = {"period": period}
    for s in SLOT_ORDER:
        if s != "period":
            properties[s] = slot({"type": "integer"} if s in ("amount", "n") else enum(s))
    required = list(SLOT_ORDER)
    if signature:
        properties["operation"] = {"type": "string", "enum": SIGNATURE_OPERATIONS}
        properties["excludes"] = {"type": "boolean"}
        properties["flow"] = {"type": "string", "enum": SIGNATURE_FLOWS}
        required += ["operation", "excludes", "flow"]
    if full:
        from guards import FULL_GROUPINGS, FULL_MEASURES

        properties["operation"] = {"type": "string", "enum": SIGNATURE_OPERATIONS}
        properties["measure"] = {"type": "string", "enum": list(FULL_MEASURES[DOMAIN.name])}
        properties["group_by"] = {
            "type": "string",
            "enum": [*FULL_GROUPINGS[DOMAIN.name], "none"],
        }
        properties["excludes"] = {"type": "boolean"}
        required += ["operation", "measure", "group_by", "excludes"]
    return {"type": "object", "properties": properties, "required": required}


def _from_llm_json(
    text: str,
    out: dict,
    ref: date,
    relative: bool = False,
    signature: bool = False,
    full: bool = False,
) -> dict:
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
            if slot == "period" and relative:
                params[slot] = resolve_relative(v, ref)
            elif slot == "period":
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
    result = {"params": params, "masked_text": mask(text, kept), "note": "; ".join(notes) or None}
    if signature:
        result["signature"] = {k: out.get(k) for k in ("operation", "excludes", "flow")}
    if full:
        keys = ("operation", "measure", "group_by", "excludes")
        result["signature"] = {k: out.get(k) for k in keys}
    return result


def extract_gemini(
    questions: list[dict],
    ref: date,
    model: str,
    project: str,
    location: str,
    raw_path: Path,
    workers: int,
    relative: bool = False,
    signature: bool = False,
    full: bool = False,
) -> dict[str, dict]:
    from google import genai
    from google.genai import types

    # A timeout, so a connection dropped by sleep or a network blip fails and
    # is retried instead of hanging the run (seen 2026-10-29). Results are
    # unaffected.
    client = genai.Client(
        vertexai=True,
        project=project,
        location=location,
        http_options=types.HttpOptions(timeout=120_000),
    )
    cfg = types.GenerateContentConfig(
        temperature=0.0,
        response_mime_type="application/json",
        response_json_schema=_gemini_schema(relative, signature, full),
        system_instruction=_gemini_prompt(ref, relative, signature, full),
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
        for attempt in range(8):
            if attempt:
                # 429s on the global endpoint clear in seconds to a minute;
                # retrying at once only spends the attempts. Capped at 60s.
                time.sleep(min(60.0, 2.0**attempt) + random.uniform(0, 1))
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
    with ThreadPoolExecutor(workers) as pool, raw_path.open("a", encoding="utf-8") as f:
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
    return {
        q["id"]: _from_llm_json(
            q["text"], done[q["id"]]["response"], ref, relative, signature, full
        )
        for q in questions
    }


# ── openai (README section 16: a second extractor vendor) ────────────────


def _openai_schema(relative: bool = False, signature: bool = False, full: bool = False) -> dict:
    """The Gemini schema in OpenAI's strict dialect, with nothing else changed.

    Strict structured outputs need additionalProperties false on every object,
    and take a nullable object as anyOf [object, null] (a type array is
    documented for primitives only).
    """

    def strict(s: dict) -> dict:
        if "properties" not in s:
            return s
        obj = {**s, "type": "object", "additionalProperties": False}
        obj["properties"] = {k: strict(v) for k, v in s["properties"].items()}
        return {"anyOf": [obj, {"type": "null"}]} if s["type"] == ["object", "null"] else obj

    return strict(_gemini_schema(relative, signature, full))


def extract_openai(
    questions: list[dict],
    ref: date,
    model: str,
    raw_path: Path,
    workers: int,
    relative: bool = False,
    signature: bool = False,
    full: bool = False,
) -> dict[str, dict]:
    """The same prompt and schema as the Gemini arms, through the Responses API.

    Every setting is the vendor's default except the enforced JSON output: no
    temperature and no reasoning effort are sent (the Gemini arms send none
    for thinking either). Reads OPENAI_API_KEY from the environment.
    """
    from openai import OpenAI

    # The backoff below is the only retry; the timeout stops a dropped
    # connection from hanging the run (seen 2026-10-29).
    client = OpenAI(max_retries=0, timeout=120.0)
    fmt = {
        "type": "json_schema",
        "name": "parameters",
        "strict": True,
        "schema": _openai_schema(relative, signature, full),
    }
    instructions = _gemini_prompt(ref, relative, signature, full)
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
        for attempt in range(8):
            if attempt:
                time.sleep(min(60.0, 2.0**attempt) + random.uniform(0, 1))
            try:
                res = client.responses.create(
                    model=model,
                    instructions=instructions,
                    input=q["text"],
                    text={"format": fmt},
                    # Reasoning tokens count against this; leave room so a
                    # long think cannot truncate the JSON.
                    max_output_tokens=16384,
                    store=False,
                )
                if res.status != "completed":
                    raise RuntimeError(f"status {res.status}: {res.incomplete_details}")
                u = res.usage
                thinking = u.output_tokens_details.reasoning_tokens
                return {
                    "id": q["id"],
                    "response": json.loads(res.output_text),
                    # As Gemini reports it: output excludes the thinking.
                    "usage": {
                        "prompt": u.input_tokens,
                        "output": u.output_tokens - thinking,
                        "thinking": thinking,
                    },
                }
            except Exception as exc:
                last = f"{type(exc).__name__}: {exc}"
        return {"id": q["id"], "response": None, "error": last}

    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(workers) as pool, raw_path.open("a", encoding="utf-8") as f:
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
    return {
        q["id"]: _from_llm_json(
            q["text"], done[q["id"]]["response"], ref, relative, signature, full
        )
        for q in questions
    }


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
    # Negation asymmetry (README section 14, G3): the same slot's error rate
    # in the question type that EXCLUDES the value against the one that
    # includes it, with the difference's cluster-bootstrap interval.
    negation = {}
    for exc_intent, inc_intent, slot in DOMAIN.negations:

        def wrong(intent: str, slot: str = slot) -> tuple[np.ndarray, np.ndarray]:
            sel = [q for q in questions if q["intent"] == intent]
            w = np.array(
                [ext[q["id"]]["params"].get(slot) != q["params"][slot] for q in sel], float
            )
            return w, np.array([gpos[q["group"]] for q in sel])

        we, ge = wrong(exc_intent)
        wi, gi = wrong(inc_intent)
        if not we.size or not wi.size:
            continue
        diffs = []
        for _ in range(n_boot):
            cnt = np.bincount(rng.integers(0, len(gids), len(gids)), minlength=len(gids))
            ce, cin = cnt[ge], cnt[gi]
            if ce.sum() and cin.sum():
                diffs.append(float((ce * we).sum() / ce.sum() - (cin * wi).sum() / cin.sum()))
        negation[f"{exc_intent} vs {inc_intent}"] = {
            "slot": slot,
            "excluded_wrong": f"{int(we.sum())}/{we.size}",
            "excluded_wrong_rate": round(float(we.mean()), 4),
            "included_wrong": f"{int(wi.sum())}/{wi.size}",
            "included_wrong_rate": round(float(wi.mean()), 4),
            "difference": round(float(we.mean() - wi.mean()), 4),
            "difference_ci95": [
                round(float(np.percentile(diffs, 2.5)), 4),
                round(float(np.percentile(diffs, 97.5)), 4),
            ],
        }
    return {
        "domain": DOMAIN.name,
        "negation": negation,
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
    ]
    for k, v in acc.get("negation", {}).items():
        lines.append(
            f"Negation ({k}, slot {v['slot']}): excluded value wrong {v['excluded_wrong']} "
            f"({v['excluded_wrong_rate']}) vs included {v['included_wrong']} "
            f"({v['included_wrong_rate']}); difference {v['difference']} {v['difference_ci95']}."
        )
    lines += [
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
    ap.add_argument(
        "--workers", type=int, default=8, help="parallel Gemini calls; lower it on 429s"
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=None,
        help="smoke test: extract the first N questions, print them, write no results",
    )
    ap.add_argument(
        "--tag",
        default="",
        help="suffix for a repeat run's folder (e.g. r2), so repeats never share raw.jsonl",
    )
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    questions, ref, domain = load(args.data)
    _use_domain(domain)
    if args.limit:
        questions = questions[: args.limit]
    kind, _, model = args.extractor.partition(":")
    if kind == "duckling" and domain.name != "finance":
        raise SystemExit("the Duckling arm is defined for the finance domain only")
    name = args.extractor + (f"_{args.tag}" if args.tag else "")
    out_dir = args.out / re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    if kind == "gold":
        ext = extract_gold(questions, ref)
    elif kind == "duckling":
        ext = extract_duckling(questions, ref, args.duckling_url)
    elif kind in ("gemini", "gemini-rel", "gemini-relsig", "gemini-relfull"):
        if not args.project:
            raise SystemExit("--project is required for gemini extractors")
        ext = extract_gemini(
            questions,
            ref,
            model,
            args.project,
            args.location,
            out_dir / "raw.jsonl",
            args.workers,
            relative=kind in ("gemini-rel", "gemini-relsig", "gemini-relfull"),
            signature=kind == "gemini-relsig",
            full=kind == "gemini-relfull",
        )
    elif kind in ("openai", "openai-rel", "openai-relsig", "openai-relfull"):
        ext = extract_openai(
            questions,
            ref,
            model,
            out_dir / "raw.jsonl",
            args.workers,
            relative=kind in ("openai-rel", "openai-relsig", "openai-relfull"),
            signature=kind == "openai-relsig",
            full=kind == "openai-relfull",
        )
    else:
        raise SystemExit(f"unknown extractor {args.extractor!r}")

    if args.limit:
        # Responses already sit in raw.jsonl, so the full run reuses them.
        for q in questions:
            e = ext[q["id"]]
            mark = "OK " if e["params"] == q["params"] else "BAD"
            print(f"{mark} {q['text']}\n    gold {q['params']}\n    got  {e['params']}")
            print(f"    masked {e['masked_text']!r}  note={e['note']}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "extracted.jsonl").open("w", encoding="utf-8") as f:
        for q in questions:
            f.write(json.dumps({"id": q["id"], **ext[q["id"]]}) + "\n")
    acc = score(questions, ext, args.bootstrap, args.seed)
    acc["extractor"] = name
    (out_dir / "accuracy.json").write_text(json.dumps(acc, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.extractor, acc, out_dir / "accuracy.md")
    print((out_dir / "accuracy.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
