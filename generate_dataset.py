"""Generate the labelled dataset for the parameter near-miss study.

Every question is rendered from (intent, template, parameter values, surface
forms), so its meaning is known by construction. Labels are then COMPUTED,
never typed:

    same_sql       the two questions have the same intent AND the same
                   normalised parameters, so reusing one's SQL for the other
                   is correct.
    same_template  the two questions have the same intent, so reusing one's
                   SQL *template* with the other's parameters filled in is
                   correct.

A computed label cannot disagree with itself, and it cannot be nudged after
anyone has seen a similarity score. Freeze the output (see README step 1)
before embedding anything.

Usage:
    python generate_dataset.py --out data                # v1, frozen
    python generate_dataset.py --v2 --out data_v2        # v2, README section 11
    python generate_dataset.py --multi-domain --out data_md   # 4 domains, section 14

v2 changes, each answering a defect v1 exposed (v1 itself is never altered):
  - "last year" gains a date-free alias ("in the previous year"). v1 had none,
    so comparison B could not test its 17 cached questions.
  - Every alias is used, not just the first two.
  - Each intent's templates are split into a cache half and a query half.
    Cached questions use only the first; reworded queries only the second, and
    are marked split="query", so `evaluate.py --holdout` can run the cache on
    wording it has never stored (threat 1).
  - A spec sheet for human-written questions (README step 4a) is written
    beside the dataset.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import random
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# Re-exported: earlier code and the README refer to these names here.
from domains import (  # noqa: F401
    CATEGORY_SURFACES,
    DOMAINS,
    FILTERED_INTENTS,
    FINANCE,
    HUMAN_PERIODS,
    INTENT_RELATIONS,
    INTENTS,
    PERIOD_NEIGHBORS,
    PERIOD_SURFACES,
    REFERENCE_DATE,
    SLOTS,
    Domain,
    _period_ranges,
)

GENERATOR_VERSION = "1.0.0"


def slots_of(domain: Domain, template: str) -> list[str]:
    return [s for s in domain.slots if "{" + s + "}" in template]


# ── Rendering ────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Question:
    intent: str
    template_id: int
    values: tuple[tuple[str, object], ...]  # (slot, value key), slot order
    surface_idx: tuple[tuple[str, int], ...]  # (slot, surface index)

    def template(self, domain: Domain) -> str:
        return domain.intents[self.intent][self.template_id]

    def text(self, domain: Domain) -> str:
        surf = dict(self.surface_idx)
        return self.template(domain).format(
            **{s: domain.slots[s][0][v][surf.get(s, 0)] for s, v in self.values}
        )

    def masked_text(self, domain: Domain) -> str:
        return self.template(domain).format(**{s: domain.slots[s][3] for s, _ in self.values})

    def normalised_params(self, ranges: dict[str, tuple[date, date]]) -> dict[str, object]:
        out: dict[str, object] = {}
        for s, v in self.values:
            if s == "period":
                start, end = ranges[v]
                out[s] = f"{start.isoformat()}/{end.isoformat()}"
            else:
                out[s] = v
        return out


@dataclass
class Builder:
    domain: Domain
    rng: random.Random
    ranges: dict[str, tuple[date, date]]
    questions: dict[str, dict] = field(default_factory=dict)  # text -> record
    pairs: list[dict] = field(default_factory=list)
    # v2 only: intent -> template ids reserved for cached questions.
    cache_templates: dict[str, set[int]] | None = None

    def add(self, q: Question, *, is_anchor: bool, group: str) -> dict:
        text = q.text(self.domain)
        gold = {"intent": q.intent, "params": q.normalised_params(self.ranges)}
        if text in self.questions:
            rec = self.questions[text]
            if (rec["intent"], rec["params"]) != (gold["intent"], gold["params"]):
                raise AssertionError(f"Same text, different meaning: {text!r}")
            rec["is_anchor"] = rec["is_anchor"] or is_anchor
            return rec
        rec = {
            "id": f"q{len(self.questions) + 1:04d}",
            "text": text,
            "masked_text": q.masked_text(self.domain),
            "intent": q.intent,
            "template_id": q.template_id,
            "slots": [s for s, _ in q.values],
            "values": {s: v for s, v in q.values},
            "params": gold["params"],
            "is_anchor": is_anchor,
            "group": group,
        }
        if self.cache_templates is not None:
            rec["split"] = "cache" if q.template_id in self.cache_templates[q.intent] else "query"
        self.questions[text] = rec
        return rec

    def pair(self, anchor: dict, q: Question, relation: str, dimension: str, kind: str) -> None:
        cand = self.add(q, is_anchor=False, group=anchor["id"])
        if cand["id"] == anchor["id"]:
            return
        same_template = cand["intent"] == anchor["intent"]
        self.pairs.append(
            {
                "pair_id": f"p{len(self.pairs) + 1:05d}",
                "anchor_id": anchor["id"],
                "candidate_id": cand["id"],
                "anchor_text": anchor["text"],
                "candidate_text": cand["text"],
                "relation": relation,
                "dimension": dimension,
                "kind": kind,
                "same_wording": cand["template_id"] == anchor["template_id"] and same_template,
                "same_sql": same_template and cand["params"] == anchor["params"],
                "same_template": same_template,
            }
        )


def _with_value(
    q: Question, slot: str, value: object, surface: int = 0, template_id: int | None = None
) -> Question:
    values = tuple((s, value if s == slot else v) for s, v in q.values)
    surf = tuple((s, surface if s == slot else i) for s, i in q.surface_idx)
    return Question(q.intent, q.template_id if template_id is None else template_id, values, surf)


def _other_template(rng: random.Random, domain: Domain, intent: str, exclude: int) -> int:
    choices = [i for i in range(len(domain.intents[intent])) if i != exclude]
    return rng.choice(choices)


def build(
    seed: int, anchors_per_intent: int, v2: bool = False, domain: Domain = FINANCE
) -> Builder:
    rng = random.Random(seed)
    b = Builder(domain=domain, rng=rng, ranges=_period_ranges(REFERENCE_DATE))
    intents, slots_map = domain.intents, domain.slots
    query_templates: dict[str, list[int]] = {}
    if v2:
        b.cache_templates = {}
        for intent, templates in intents.items():
            ids = list(range(len(templates)))
            rng.shuffle(ids)
            k = (len(ids) + 1) // 2
            b.cache_templates[intent] = set(ids[:k])
            query_templates[intent] = sorted(ids[k:])

    def query_template(intent: str) -> int:
        return rng.choice(query_templates[intent])

    for intent, templates in intents.items():
        slots = slots_of(domain, templates[0])
        combos = list(itertools.product(*(slots_map[s][2] for s in slots)))
        rng.shuffle(combos)
        for combo in combos[:anchors_per_intent]:
            if v2:
                t0 = rng.choice(sorted(b.cache_templates[intent]))
            else:
                t0 = rng.randrange(len(templates))
            values = tuple(zip(slots, combo, strict=True))
            anchor_q = Question(intent, t0, values, tuple((s, 0) for s in slots))
            anchor = b.add(anchor_q, is_anchor=True, group="")
            anchor["group"] = anchor["id"]

            # 1. Paraphrases: other wordings, same meaning. In v2, every
            #    query-half wording and none the cache uses.
            others = [i for i in range(len(templates)) if i != t0]
            chosen = query_templates[intent] if v2 else rng.sample(others, min(3, len(others)))
            for t in chosen:
                b.pair(
                    anchor,
                    Question(intent, t, values, anchor_q.surface_idx),
                    "paraphrase",
                    "wording",
                    "template",
                )

            for slot, value in values:
                surfaces, neighbors, _, _ = slots_map[slot]

                # 2. Equivalent surface: one span reworded, same value, SAME
                #    template — a one-span positive to set against the
                #    one-span negatives below.
                n_surfaces = len(surfaces[value]) if v2 else min(3, len(surfaces[value]))
                for si in range(1, n_surfaces):
                    b.pair(
                        anchor,
                        _with_value(anchor_q, slot, value, si),
                        "equivalent_surface",
                        slot,
                        "alias",
                    )

                # 3. Parameter near-miss: one span changed to a confusable
                #    value. Same template (minimal edit) for every neighbour,
                #    plus one reworded version of the first.
                kinded = (
                    neighbors[value].items()
                    if slot == "period"
                    else [("neighbor", neighbors[value])]
                )
                first = True
                for kind, vals in kinded:
                    for nv in vals:
                        b.pair(
                            anchor, _with_value(anchor_q, slot, nv), "param_near_miss", slot, kind
                        )
                        if first:
                            t = (
                                query_template(intent)
                                if v2
                                else _other_template(rng, domain, intent, t0)
                            )
                            b.pair(
                                anchor,
                                _with_value(anchor_q, slot, nv, template_id=t),
                                "param_near_miss",
                                slot,
                                kind,
                            )
                            first = False

            # 4. Intent near-miss: same parameters, different computation.
            for a, c, dim in domain.intent_relations:
                if intent not in (a, c):
                    continue
                other = c if intent == a else a
                t = query_template(other) if v2 else rng.randrange(len(intents[other]))
                b.pair(
                    anchor,
                    Question(other, t, values, anchor_q.surface_idx),
                    "intent_near_miss",
                    dim,
                    other,
                )

            # 5. Filter change: drop the filter, or add one.
            vals = dict(values)
            if intent in domain.filter_drop:
                base = domain.filter_drop[intent]
                t = query_template(base) if v2 else rng.randrange(len(intents[base]))
                q = Question(base, t, (("period", vals["period"]),), (("period", 0),))
                b.pair(anchor, q, "filter_change", "filter_dropped", base)
            if domain.filter_add and intent == domain.filter_add[0]:
                _, target, slot = domain.filter_add
                value = rng.choice(list(slots_map[slot][0]))
                t = query_template(target) if v2 else rng.randrange(len(intents[target]))
                q = Question(
                    target,
                    t,
                    ((slot, value), ("period", vals["period"])),
                    ((slot, 0), ("period", 0)),
                )
                b.pair(anchor, q, "filter_change", "filter_added", target)
    return b


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ── v2: human-written questions (README step 4a) ─────────────────────────
#
# Writers get the MEANING of a question — a goal and its values — never a
# template, so their wording is their own. Goals are terse noun phrases on
# purpose: a full sentence would be copied.

HUMAN_INSTRUCTIONS = """\
# Writing questions for the personal-finance study

Thank you for helping. This takes about an hour.

Imagine a personal-finance app that has read your bank and card statements.
You can type questions to it in plain English.

**Today is Tuesday, October 27, 2026.**

Each row of `human_spec_sheet.csv` describes something you want to know:
a goal, the values involved (a merchant, a category, an account, an amount or a
number N), and a time period. Write **one question** in the `question` column,
the way you would actually type it into the app.

- **Use your own words.** Do not copy the wording of the goal or the period.
  Ask it however feels natural, short or long, casual or precise.
- **Say the time period however you naturally would.** "Last month",
  "September" and "in Sep" are all fine if they mean the period described. The
  dates are there so you know exactly which period is meant.
- **Keep the meaning exact.** If the row says "everything EXCEPT groceries",
  the question must exclude groceries. If it says "top 5", ask for five.
- **Work alone.** Do not look at anyone else's sheet, and do not ask an AI
  assistant to write or reword the questions.
- Put your initials in the `writer` column of every row.

There are no wrong answers except questions that change the meaning.
"""

HUMAN_INSTRUCTIONS_MULTI = """\
# Writing questions for an analytics study

Thank you for helping. This takes about 75 minutes, and you can stop and
resume at any time.

Imagine four different apps, each of which can answer questions about data
you look after. You type questions to them in plain English:

- **Your personal finances:** an app that has read your bank and card statements.
- **Your retail business:** your company's online, in-store and wholesale sales.
- **The outpatient clinic network you manage:** visits, waits, referrals and billing.
- **The IT support organization you lead:** tickets, teams, priorities and services.

The `context` column of each row says which one the question is for.

**Today is Tuesday, October 27, 2026.**

Each row describes something you want to know: a goal, the values involved
(for example a merchant, a product, a clinic, a ticket priority, an amount or a
number N), and a time period. Write **one question** in the `question` column,
the way you would actually type it into that app.

- **Use your own words.** Do not copy the wording of the goal or the period.
  Ask it however feels natural, short or long, casual or precise.
- **Say the time period however you naturally would.** "Last month",
  "September" and "in Sep" are all fine if they mean the period described. The
  dates are there so you know exactly which period is meant.
- **Keep the meaning exact.** If the row says "every region EXCEPT the West",
  the question must exclude the West. If it says "top 5", ask for five.
- **Work alone.** Do not look at anyone else's sheet, and do not ask an AI
  assistant to write or reword the questions.
- Put your initials in the `writer` column of every row.

There are no wrong answers except questions that change the meaning. Your
questions may be published, without your name, in an open research dataset;
please tell the person who sent you this sheet if you do not agree.
"""


def _spec(domain: Domain, a: dict, values: dict, kind: str) -> dict:
    detail = []
    for slot in domain.slot_order:
        if slot != "period" and slot in values:
            surface = domain.slots[slot][0][values[slot]][0]
            detail.append(f"{domain.slot_labels[slot]}: {surface}")
    return {
        "domain": domain.name,
        "anchor_id": a["id"],
        "kind": kind,
        "intent": a["intent"],
        "values": json.dumps(values),
        "goal": domain.human_goals[a["intent"]],
        "details": "; ".join(detail),
        "period": HUMAN_PERIODS[values["period"]],
    }


def _neighbour_period(rng: random.Random, period: str) -> str | None:
    options = [v for vs in PERIOD_NEIGHBORS.get(period, {}).values() for v in vs]
    return rng.choice(options) if options else None


def write_human_specs(b: Builder, out: Path, seed: int) -> None:
    """Finance-only v2 sheet (data_v2), kept so data_v2 regenerates exactly.
    Superseded by the multi-domain sheet (write_human_specs_multi).

    One spec per cached question: even positions ask the same thing (a
    positive), odd positions the same thing over a neighbouring period (a
    near-miss). Labels come from the spec, so the writer cannot change them."""
    rng = random.Random(seed + 2)
    anchors = sorted((r for r in b.questions.values() if r["is_anchor"]), key=lambda r: r["id"])
    rows = []
    for i, a in enumerate(anchors):
        values = dict(a["values"])
        kind = "same_meaning"
        if i % 2 == 1:
            nv = _neighbour_period(rng, values["period"])
            if nv:
                values["period"] = nv
                kind = "different_period"
        spec = _spec(b.domain, a, values, kind)
        del spec["domain"]
        rows.append({"spec_id": f"s{i + 1:03d}", **spec})
    # The writer's sheet hides everything that would hint at the study design.
    shuffled = rows[:]
    rng.shuffle(shuffled)
    with (out / "human_spec_sheet.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["spec_id", "goal", "details", "period", "question", "writer"])
        for r in shuffled:
            w.writerow([r["spec_id"], r["goal"], r["details"], r["period"], "", ""])
    with (out / "human_spec_key.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    (out / "human_writer_instructions.md").write_text(HUMAN_INSTRUCTIONS, encoding="utf-8")


def write_human_specs_multi(
    builders: list[Builder], out: Path, seed: int, per_domain: int
) -> list[str]:
    """One mixed sheet across domains (README section 14).

    Per domain, `per_domain` cached questions are drawn round-robin across
    intents so every intent is covered, alternating a same-meaning spec (a
    positive) with the same spec over a neighbouring period (a near-miss).
    All rows are shuffled together and numbered after shuffling, so neither
    the order nor the ids reveal domain, intent or kind.
    """
    rng = random.Random(seed + 3)
    rows = []
    for b in builders:
        by_intent: dict[str, list[dict]] = defaultdict(list)
        for r in sorted(b.questions.values(), key=lambda r: r["id"]):
            if r["is_anchor"]:
                by_intent[r["intent"]].append(r)
        for lst in by_intent.values():
            rng.shuffle(lst)
        picked: list[dict] = []
        while len(picked) < per_domain and any(by_intent.values()):
            for intent in b.domain.intents:
                if by_intent[intent] and len(picked) < per_domain:
                    picked.append(by_intent[intent].pop())
        for i, a in enumerate(picked):
            values = dict(a["values"])
            kind = "same_meaning"
            if i % 2 == 1:
                nv = _neighbour_period(rng, values["period"])
                if nv:
                    values["period"] = nv
                    kind = "different_period"
            rows.append({**_spec(b.domain, a, values, kind), "context": b.domain.human_context})
    rng.shuffle(rows)
    for i, r in enumerate(rows):
        r["spec_id"] = f"s{i + 1:03d}"
    with (out / "human_spec_sheet.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["spec_id", "context", "goal", "details", "period", "question", "writer"])
        for r in rows:
            w.writerow([r["spec_id"], r["context"], r["goal"], r["details"], r["period"], "", ""])
    with (out / "human_spec_key.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    (out / "human_writer_instructions.md").write_text(HUMAN_INSTRUCTIONS_MULTI, encoding="utf-8")
    return ["human_spec_sheet.csv", "human_spec_key.jsonl", "human_writer_instructions.md"]


def write(
    b: Builder,
    out: Path,
    seed: int,
    anchors_per_intent: int,
    version: str = GENERATOR_VERSION,
    human: bool = True,
    record_domain: bool = False,
) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    questions = sorted(b.questions.values(), key=lambda r: r["id"])

    with (out / "questions.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in questions:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (out / "pairs.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for p in b.pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    # The review sheet: what a second labeller reads, blind to the labels.
    # Shuffled so neighbouring rows don't give away the generator's pattern.
    review = list(b.pairs)
    random.Random(seed + 1).shuffle(review)
    with (out / "review_sheet.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair_id", "cached_question", "new_question", "reuse_sql_is_correct (Y/N)"])
        for p in review:
            w.writerow([p["pair_id"], p["anchor_text"], p["candidate_text"], ""])

    counts = Counter((p["relation"], p["dimension"], p["kind"]) for p in b.pairs)
    files = ["questions.jsonl", "pairs.jsonl", "review_sheet.csv"]
    if b.cache_templates is not None and human:
        write_human_specs(b, out, seed)
        files += ["human_spec_sheet.csv", "human_spec_key.jsonl"]
    manifest: dict = {}
    if record_domain:
        manifest["domain"] = b.domain.name
    manifest |= {
        "generator_version": version,
        "seed": seed,
        "anchors_per_intent": anchors_per_intent,
        "reference_date": REFERENCE_DATE.isoformat(),
        "n_questions": len(questions),
        "n_anchors": sum(r["is_anchor"] for r in questions),
        "n_pairs": len(b.pairs),
        "n_pairs_same_sql": sum(p["same_sql"] for p in b.pairs),
        "n_pairs_same_template": sum(p["same_template"] for p in b.pairs),
        "pairs_by_type": {"/".join(k): v for k, v in sorted(counts.items())},
        "label_rules": {
            "same_sql": "same intent AND equal normalised params (periods as absolute date ranges vs reference_date)",
            "same_template": "same intent",
        },
        "sha256": {name: _sha256(out / name) for name in files},
    }
    if b.cache_templates is not None:
        manifest["cache_templates"] = {k: sorted(v) for k, v in b.cache_templates.items()}
        manifest["n_queries_holdout"] = sum(
            1 for r in questions if not r["is_anchor"] and r.get("split") == "query"
        )
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                k: manifest[k]
                for k in manifest
                if k not in ("pairs_by_type", "sha256", "cache_templates")
            }
        )
    )
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--out", type=Path, default=Path(__file__).parent / "data")
    ap.add_argument("--seed", type=int, default=20261027)
    ap.add_argument("--anchors-per-intent", type=int, default=10)
    ap.add_argument("--v2", action="store_true", help="dataset v2 (see the module docstring)")
    ap.add_argument(
        "--multi-domain",
        action="store_true",
        help="v2 rules for every domain in domains.py, one folder each, plus one mixed "
        "human spec sheet (README section 14)",
    )
    ap.add_argument("--human-per-domain", type=int, default=40)
    args = ap.parse_args()
    if args.v2 or args.multi_domain:
        # A date-free alias for "last year", which v1 lacked. Appended, so
        # surfaces[0] stays the canonical wording.
        PERIOD_SURFACES["last_year"].append("in the previous year")
    if not args.multi_domain:
        b = build(args.seed, args.anchors_per_intent, v2=args.v2)
        write(
            b,
            args.out,
            args.seed,
            args.anchors_per_intent,
            "2.0.0" if args.v2 else GENERATOR_VERSION,
        )
        return
    builders, top = [], {"generator_version": "3.0.0", "seed": args.seed, "domains": {}}
    for d in DOMAINS.values():
        b = build(args.seed, args.anchors_per_intent, v2=True, domain=d)
        m = write(
            b,
            args.out / d.name,
            args.seed,
            args.anchors_per_intent,
            "3.0.0",
            human=False,
            record_domain=True,
        )
        builders.append(b)
        top["domains"][d.name] = {"n_questions": m["n_questions"], "sha256": m["sha256"]}
    files = write_human_specs_multi(builders, args.out, args.seed, args.human_per_domain)
    top["human_per_domain"] = args.human_per_domain
    top["sha256"] = {f: _sha256(args.out / f) for f in files}
    (args.out / "manifest.json").write_text(json.dumps(top, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
