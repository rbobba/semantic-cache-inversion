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
    python generate_dataset.py --out data
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import random
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

GENERATOR_VERSION = "1.0.0"

# Relative periods ("last month") only have a meaning against a date. Fixing
# it here is what lets "last month" and "in September 2026" be labelled
# equivalent without anyone arguing about it.
REFERENCE_DATE = date(2026, 10, 27)


# ── Parameter vocabularies ───────────────────────────────────────────────
#
# surfaces[0] is the canonical wording. Further surfaces are equivalent
# wordings of the SAME value — they produce positives that differ from the
# anchor by a single span, the fair counterpart to a one-span near-miss.
#
# neighbors are deliberately the most confusable other values: a corpus of
# unrelated questions would show zero false reuse at every threshold and
# prove nothing.


def _month(year: int, month: int) -> tuple[date, date]:
    start = date(year, month, 1)
    nxt = date(year + (month == 12), month % 12 + 1, 1)
    return start, nxt - timedelta(days=1)


def _period_ranges(ref: date) -> dict[str, tuple[date, date]]:
    week_start = ref - timedelta(days=ref.weekday())  # Monday
    this_month_start = ref.replace(day=1)
    prev = (ref.year, ref.month - 1) if ref.month > 1 else (ref.year - 1, 12)
    last_month = _month(*prev)
    return {
        "this_month": (this_month_start, ref),
        "last_month": last_month,
        "aug_2026": _month(2026, 8),
        "this_year": (date(ref.year, 1, 1), ref),
        "last_year": (date(ref.year - 1, 1, 1), date(ref.year - 1, 12, 31)),
        "last_12_months": (ref - timedelta(days=364), ref),
        "this_week": (week_start, ref),
        "last_week": (week_start - timedelta(days=7), week_start - timedelta(days=1)),
        "last_30_days": (ref - timedelta(days=29), ref),
        "last_3_months": (ref - timedelta(days=91), ref),
        "last_6_months": (ref - timedelta(days=182), ref),
        "q3_2026": (date(2026, 7, 1), date(2026, 9, 30)),
        "q2_2026": (date(2026, 4, 1), date(2026, 6, 30)),
    }


PERIOD_SURFACES: dict[str, list[str]] = {
    "this_month": ["this month", "so far this month", "in October 2026"],
    "last_month": ["last month", "in the previous month", "in September 2026"],
    "aug_2026": ["in August 2026", "during August 2026"],
    "this_year": ["this year", "so far this year", "year to date", "in 2026"],
    "last_year": ["last year", "in 2025", "during 2025"],
    "last_12_months": ["in the last 12 months", "over the past twelve months"],
    "this_week": ["this week", "so far this week"],
    "last_week": ["last week", "in the previous week"],
    "last_30_days": ["in the last 30 days", "over the past 30 days"],
    "last_3_months": ["in the last 3 months", "over the past three months"],
    "last_6_months": ["in the last 6 months", "over the past six months"],
    "q3_2026": ["in Q3 2026", "in the third quarter of 2026"],
    "q2_2026": ["in Q2 2026", "in the second quarter of 2026"],
}

# kind -> neighbours. "adjacent" is the same granularity shifted in time
# (this month vs last month); "granularity" is an overlapping window of a
# different shape (last month vs last 30 days). Both change the SQL.
PERIOD_NEIGHBORS: dict[str, dict[str, list[str]]] = {
    "this_month": {"adjacent": ["last_month"], "granularity": ["last_30_days", "this_week"]},
    "last_month": {"adjacent": ["this_month", "aug_2026"], "granularity": ["last_30_days"]},
    "this_year": {"adjacent": ["last_year"], "granularity": ["last_12_months"]},
    "last_year": {"adjacent": ["this_year"], "granularity": ["last_12_months"]},
    "this_week": {"adjacent": ["last_week"], "granularity": ["this_month"]},
    "last_3_months": {"adjacent": [], "granularity": ["q3_2026", "last_6_months"]},
    "q3_2026": {"adjacent": ["q2_2026"], "granularity": ["last_3_months"]},
}
ANCHOR_PERIODS = list(PERIOD_NEIGHBORS)

MERCHANT_SURFACES: dict[str, list[str]] = {
    "costco": ["Costco", "Costco Wholesale"],
    "target": ["Target"],
    "walmart": ["Walmart"],
    "amazon": ["Amazon", "Amazon.com"],
    "whole_foods": ["Whole Foods", "Whole Foods Market"],
    "trader_joes": ["Trader Joe's", "Trader Joes"],
    "starbucks": ["Starbucks"],
    "dunkin": ["Dunkin'", "Dunkin Donuts"],
    "uber": ["Uber"],
    "lyft": ["Lyft"],
    "netflix": ["Netflix"],
    "spotify": ["Spotify"],
    "shell": ["Shell"],
    "chevron": ["Chevron"],
    "home_depot": ["Home Depot"],
    "lowes": ["Lowe's", "Lowes"],
}
MERCHANT_NEIGHBORS: dict[str, list[str]] = {
    "costco": ["walmart", "target"],
    "target": ["walmart", "costco"],
    "walmart": ["target", "costco"],
    "amazon": ["target"],
    "whole_foods": ["trader_joes"],
    "trader_joes": ["whole_foods"],
    "starbucks": ["dunkin"],
    "dunkin": ["starbucks"],
    "uber": ["lyft"],
    "lyft": ["uber"],
    "netflix": ["spotify"],
    "spotify": ["netflix"],
    "shell": ["chevron"],
    "chevron": ["shell"],
    "home_depot": ["lowes"],
    "lowes": ["home_depot"],
}

# "grocery shopping" (a groceries alias, so a positive) against "shopping"
# (a different category, so a negative) is intentional: the negative shares
# more tokens with the anchor than the positive does.
CATEGORY_SURFACES: dict[str, list[str]] = {
    "groceries": ["groceries", "grocery shopping"],
    "dining": ["dining out", "restaurants", "eating out"],
    "gas": ["gas", "fuel"],
    "travel": ["travel"],
    "utilities": ["utilities", "utility bills"],
    "subscriptions": ["subscriptions", "subscription services"],
    "entertainment": ["entertainment"],
    "shopping": ["shopping"],
}
CATEGORY_NEIGHBORS: dict[str, list[str]] = {
    "groceries": ["dining", "shopping"],
    "dining": ["groceries"],
    "gas": ["travel"],
    "travel": ["gas"],
    "utilities": ["subscriptions"],
    "subscriptions": ["utilities", "entertainment"],
    "entertainment": ["subscriptions"],
    "shopping": ["groceries"],
}

ACCOUNT_SURFACES: dict[str, list[str]] = {
    "checking": ["checking account", "checking"],
    "savings": ["savings account", "savings"],
    "visa": ["Visa card", "Visa"],
    "amex": ["Amex card", "American Express card"],
}
ACCOUNT_NEIGHBORS: dict[str, list[str]] = {
    "checking": ["savings"],
    "savings": ["checking"],
    "visa": ["amex"],
    "amex": ["visa"],
}

AMOUNT_SURFACES: dict[int, list[str]] = {
    100: ["$100", "100 dollars"],
    200: ["$200", "200 dollars"],
    500: ["$500", "500 dollars"],
    1000: ["$1,000", "1,000 dollars"],
}
AMOUNT_NEIGHBORS: dict[int, list[int]] = {
    100: [200],
    200: [100, 500],
    500: [200, 1000],
    1000: [500],
}

TOPN_SURFACES: dict[int, list[str]] = {3: ["3", "three"], 5: ["5", "five"], 10: ["10", "ten"]}
TOPN_NEIGHBORS: dict[int, list[int]] = {3: [5], 5: [3, 10], 10: [5]}

# slot -> (surfaces, neighbours, anchor-eligible values, placeholder)
SLOTS: dict[str, tuple[dict, dict, list, str]] = {
    "period": (PERIOD_SURFACES, PERIOD_NEIGHBORS, ANCHOR_PERIODS, "[PERIOD]"),
    "merchant": (MERCHANT_SURFACES, MERCHANT_NEIGHBORS, list(MERCHANT_SURFACES), "[MERCHANT]"),
    "category": (CATEGORY_SURFACES, CATEGORY_NEIGHBORS, list(CATEGORY_SURFACES), "[CATEGORY]"),
    "account": (ACCOUNT_SURFACES, ACCOUNT_NEIGHBORS, list(ACCOUNT_SURFACES), "[ACCOUNT]"),
    "amount": (AMOUNT_SURFACES, AMOUNT_NEIGHBORS, list(AMOUNT_SURFACES), "[AMOUNT]"),
    "n": (TOPN_SURFACES, TOPN_NEIGHBORS, list(TOPN_SURFACES), "[N]"),
}


# ── Intents ──────────────────────────────────────────────────────────────
#
# Slot placeholders only ever appear in noun position ("at {merchant}", "on
# {category}"), so every alias reads grammatically in every template.

INTENTS: dict[str, list[str]] = {
    "merchant_spend_total": [
        "How much did I spend at {merchant} {period}?",
        "What was my total spending at {merchant} {period}?",
        "How much money went to {merchant} {period}?",
        "Total spent at {merchant} {period}",
        "What did I pay {merchant} in total {period}?",
        "Sum of my purchases at {merchant} {period}",
    ],
    "merchant_txn_count": [
        "How many transactions did I have at {merchant} {period}?",
        "How many times did I pay {merchant} {period}?",
        "Number of purchases at {merchant} {period}",
        "How often did I buy from {merchant} {period}?",
        "Count my transactions at {merchant} {period}",
    ],
    "merchant_avg": [
        "What was my average purchase at {merchant} {period}?",
        "How much did I spend per transaction at {merchant} {period}, on average?",
        "Average transaction amount at {merchant} {period}",
        "On average, how much did each purchase at {merchant} cost {period}?",
    ],
    "merchant_refunds": [
        "How much did I get refunded from {merchant} {period}?",
        "Total refunds from {merchant} {period}",
        "How much money did {merchant} give back to me {period}?",
        "What was the total of my returns to {merchant} {period}?",
    ],
    "category_spend_total": [
        "How much did I spend on {category} {period}?",
        "What was my spending on {category} {period}?",
        "Total spent on {category} {period}",
        "How much money went to {category} {period}?",
        "What did {category} cost me {period}?",
    ],
    "category_spend_excluding": [
        "How much did I spend on everything except {category} {period}?",
        "What was my total spending {period}, not counting {category}?",
        "Total spent on everything but {category} {period}",
        "How much did I spend {period} excluding {category}?",
    ],
    "account_spend_total": [
        "How much did I spend from my {account} {period}?",
        "Total outflows from my {account} {period}",
        "How much money left my {account} {period}?",
        "What went out of my {account} {period}?",
    ],
    "total_spend": [
        "How much did I spend {period}?",
        "What was my total spending {period}?",
        "How much money did I spend in total {period}?",
        "Total expenses {period}",
        "What were my overall expenses {period}?",
    ],
    "income_total": [
        "How much income did I receive {period}?",
        "What was my total income {period}?",
        "How much did I earn {period}?",
        "Total money coming in {period}",
    ],
    "net_cash_flow": [
        "What was my net cash flow {period}?",
        "How much more did I earn than I spent {period}?",
        "Income minus expenses {period}",
        "What was left over after expenses {period}?",
    ],
    "largest_purchase": [
        "What was my largest purchase {period}?",
        "What was the biggest single thing I bought {period}?",
        "Show my most expensive transaction {period}",
        "Largest charge {period}",
    ],
    "top_merchants": [
        "What were my top {n} merchants by spending {period}?",
        "Which {n} merchants did I spend the most at {period}?",
        "Show my {n} biggest merchants {period}",
        "Top {n} places I spent money {period}",
    ],
    "top_categories": [
        "What were my top {n} spending categories {period}?",
        "Which {n} categories did I spend the most on {period}?",
        "Show my {n} biggest expense categories {period}",
        "Top {n} categories by spending {period}",
    ],
    "large_transactions": [
        "Show me transactions over {amount} {period}",
        "Which purchases were above {amount} {period}?",
        "List every charge bigger than {amount} {period}",
        "Any spending above {amount} {period}?",
    ],
}

# Intent pairs that share every parameter and differ only in what is computed.
# These are the near-misses that parameter separation does NOT address — they
# are in the corpus so the paper can say so with numbers.
INTENT_RELATIONS: list[tuple[str, str, str]] = [
    ("merchant_spend_total", "merchant_txn_count", "aggregation"),
    ("merchant_spend_total", "merchant_avg", "aggregation"),
    ("merchant_txn_count", "merchant_avg", "aggregation"),
    ("merchant_spend_total", "merchant_refunds", "direction"),
    ("category_spend_total", "category_spend_excluding", "negation"),
    ("total_spend", "income_total", "direction"),
    ("total_spend", "net_cash_flow", "measure"),
    ("income_total", "net_cash_flow", "measure"),
    ("total_spend", "largest_purchase", "aggregation"),
    ("top_merchants", "top_categories", "grouping"),
]

# Anchors with a filter, whose near-miss is the same question without it.
FILTERED_INTENTS = {"merchant_spend_total", "category_spend_total", "account_spend_total"}


def slots_of(template: str) -> list[str]:
    return [s for s in SLOTS if "{" + s + "}" in template]


# ── Rendering ────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Question:
    intent: str
    template_id: int
    values: tuple[tuple[str, object], ...]  # (slot, value key), slot order
    surface_idx: tuple[tuple[str, int], ...]  # (slot, surface index)

    @property
    def template(self) -> str:
        return INTENTS[self.intent][self.template_id]

    def text(self) -> str:
        surf = dict(self.surface_idx)
        return self.template.format(**{s: SLOTS[s][0][v][surf.get(s, 0)] for s, v in self.values})

    def masked_text(self) -> str:
        return self.template.format(**{s: SLOTS[s][3] for s, _ in self.values})

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
    rng: random.Random
    ranges: dict[str, tuple[date, date]]
    questions: dict[str, dict] = field(default_factory=dict)  # text -> record
    pairs: list[dict] = field(default_factory=list)

    def add(self, q: Question, *, is_anchor: bool, group: str) -> dict:
        text = q.text()
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
            "masked_text": q.masked_text(),
            "intent": q.intent,
            "template_id": q.template_id,
            "slots": [s for s, _ in q.values],
            "values": {s: v for s, v in q.values},
            "params": gold["params"],
            "is_anchor": is_anchor,
            "group": group,
        }
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


def _other_template(rng: random.Random, intent: str, exclude: int) -> int:
    choices = [i for i in range(len(INTENTS[intent])) if i != exclude]
    return rng.choice(choices)


def build(seed: int, anchors_per_intent: int) -> Builder:
    rng = random.Random(seed)
    b = Builder(rng=rng, ranges=_period_ranges(REFERENCE_DATE))

    for intent, templates in INTENTS.items():
        slots = slots_of(templates[0])
        combos = list(itertools.product(*(SLOTS[s][2] for s in slots)))
        rng.shuffle(combos)
        for combo in combos[:anchors_per_intent]:
            t0 = rng.randrange(len(templates))
            values = tuple(zip(slots, combo, strict=True))
            anchor_q = Question(intent, t0, values, tuple((s, 0) for s in slots))
            anchor = b.add(anchor_q, is_anchor=True, group="")
            anchor["group"] = anchor["id"]

            # 1. Paraphrases: other wordings, same meaning.
            others = [i for i in range(len(templates)) if i != t0]
            for t in rng.sample(others, min(3, len(others))):
                b.pair(
                    anchor,
                    Question(intent, t, values, anchor_q.surface_idx),
                    "paraphrase",
                    "wording",
                    "template",
                )

            for slot, value in values:
                surfaces, neighbors, _, _ = SLOTS[slot]

                # 2. Equivalent surface: one span reworded, same value, SAME
                #    template — a one-span positive to set against the
                #    one-span negatives below.
                for si in range(1, min(3, len(surfaces[value]))):
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
                            t = _other_template(rng, intent, t0)
                            b.pair(
                                anchor,
                                _with_value(anchor_q, slot, nv, template_id=t),
                                "param_near_miss",
                                slot,
                                kind,
                            )
                            first = False

            # 4. Intent near-miss: same parameters, different computation.
            for a, c, dim in INTENT_RELATIONS:
                if intent not in (a, c):
                    continue
                other = c if intent == a else a
                t = rng.randrange(len(INTENTS[other]))
                b.pair(
                    anchor,
                    Question(other, t, values, anchor_q.surface_idx),
                    "intent_near_miss",
                    dim,
                    other,
                )

            # 5. Filter change: drop the filter, or add one.
            vals = dict(values)
            if intent in FILTERED_INTENTS:
                t = rng.randrange(len(INTENTS["total_spend"]))
                q = Question("total_spend", t, (("period", vals["period"]),), (("period", 0),))
                b.pair(anchor, q, "filter_change", "filter_dropped", "total_spend")
            if intent == "total_spend":
                cat = rng.choice(list(CATEGORY_SURFACES))
                t = rng.randrange(len(INTENTS["category_spend_total"]))
                q = Question(
                    "category_spend_total",
                    t,
                    (("category", cat), ("period", vals["period"])),
                    (("category", 0), ("period", 0)),
                )
                b.pair(anchor, q, "filter_change", "filter_added", "category_spend_total")
    return b


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(b: Builder, out: Path, seed: int, anchors_per_intent: int) -> None:
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
    manifest = {
        "generator_version": GENERATOR_VERSION,
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
        "sha256": {
            name: _sha256(out / name)
            for name in ("questions.jsonl", "pairs.jsonl", "review_sheet.csv")
        },
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {k: manifest[k] for k in manifest if k not in ("pairs_by_type", "sha256")}, indent=2
        )
    )


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--out", type=Path, default=Path(__file__).parent / "data")
    ap.add_argument("--seed", type=int, default=20261027)
    ap.add_argument("--anchors-per-intent", type=int, default=10)
    args = ap.parse_args()
    b = build(args.seed, args.anchors_per_intent)
    write(b, args.out, args.seed, args.anchors_per_intent)


if __name__ == "__main__":
    main()
