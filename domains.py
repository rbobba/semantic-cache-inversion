"""Domain definitions for the parameter near-miss study.

Each domain is a vocabulary of slot values (with equivalent wordings and
deliberately confusable neighbours) and a set of intents (question types,
each with several templates). Every domain is built to contain the same four
kinds of "small word" the study is about: a time period, an aggregation
(sum / count / average / max), a negation ("except X") and a direction
(money in / money out, opened / resolved).

The period vocabulary is shared. FINANCE is the original study domain, moved
here verbatim from generate_dataset.py so its output stays byte-identical.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

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


# ── Domain structure ─────────────────────────────────────────────────────


@dataclass(frozen=True)
class Domain:
    name: str
    slots: dict[str, tuple[dict, dict, list, str]]  # includes "period"
    intents: dict[str, list[str]]
    intent_relations: list[tuple[str, str, str]]
    # Filtered intent -> the same question with its filter dropped.
    filter_drop: dict[str, str]
    # (unfiltered intent, filtered intent, slot): the filter-added near-miss.
    filter_add: tuple[str, str, str] | None
    # (excluding intent, including intent, slot): the same value, negated or not.
    negations: list[tuple[str, str, str]]
    # Extraction prompt: opening sentence and one line per non-period slot.
    # "{ids}" is replaced by the slot's ids with their canonical wordings.
    prompt_intro: str
    slot_prompts: dict[str, str]
    # Human-question sheet (README step 4a).
    human_context: str
    human_goals: dict[str, str]
    slot_labels: dict[str, str] = field(default_factory=dict)

    @property
    def slot_order(self) -> list[str]:
        return list(self.slots)


# Shared by every domain: what a writer is told each period means.
HUMAN_PERIODS = {
    "this_month": "the current month so far (Oct 1 - Oct 27, 2026)",
    "last_month": "the previous calendar month (Sep 1 - Sep 30, 2026)",
    "aug_2026": "August 2026 (Aug 1 - Aug 31)",
    "this_year": "this calendar year so far (Jan 1 - Oct 27, 2026)",
    "last_year": "the previous calendar year (all of 2025)",
    "last_12_months": "a rolling 12-month window ending today (Oct 28, 2025 - Oct 27, 2026)",
    "this_week": "the current week so far (Mon Oct 26 - Tue Oct 27, 2026)",
    "last_week": "the previous calendar week (Mon Oct 19 - Sun Oct 25, 2026)",
    "last_30_days": "a rolling 30-day window ending today (Sep 28 - Oct 27, 2026)",
    "last_3_months": "a rolling 3-month window ending today (Jul 28 - Oct 27, 2026)",
    "last_6_months": "a rolling 6-month window ending today (Apr 28 - Oct 27, 2026)",
    "q3_2026": "the third quarter of 2026 (Jul 1 - Sep 30)",
    "q2_2026": "the second quarter of 2026 (Apr 1 - Jun 30)",
}

_TOP_N = 'the number of items asked for in a "top N" question, as an integer.'

FINANCE = Domain(
    name="finance",
    slots=SLOTS,
    intents=INTENTS,
    intent_relations=INTENT_RELATIONS,
    filter_drop={i: "total_spend" for i in sorted(FILTERED_INTENTS)},
    filter_add=("total_spend", "category_spend_total", "category"),
    negations=[("category_spend_excluding", "category_spend_total", "category")],
    prompt_intro=(
        "You extract the parameters of a question about the user's personal finances, so\n"
        "that a cached SQL query can be reused with the new values."
    ),
    slot_prompts={
        "merchant": "one of {ids}. Return the id.",
        "category": "a spending category named in the question, one of {ids}. Return the id.",
        "account": "one of {ids}. Return the id.",
        "amount": "a dollar amount in the question, as an integer number of dollars.",
        "n": _TOP_N,
    },
    human_context="Your personal finances (your bank and card statements)",
    human_goals={
        "merchant_spend_total": "total amount spent at a merchant",
        "merchant_txn_count": "number of transactions at a merchant",
        "merchant_avg": "average amount per transaction at a merchant",
        "merchant_refunds": "total refunds received from a merchant",
        "category_spend_total": "total spent in one spending category",
        "category_spend_excluding": "total spending on everything EXCEPT one category",
        "account_spend_total": "total money that went out of one account",
        "total_spend": "total spending overall",
        "income_total": "total income received",
        "net_cash_flow": "income minus spending",
        "largest_purchase": "the single largest purchase",
        "top_merchants": "the top N merchants by amount spent",
        "top_categories": "the top N spending categories by amount",
        "large_transactions": "every transaction above a dollar amount",
    },
    slot_labels={
        "merchant": "merchant",
        "category": "category",
        "account": "account",
        "amount": "amount",
        "n": "N",
    },
)


def _amount(surfaces: dict, neighbors: dict) -> tuple[dict, dict, list, str]:
    return (surfaces, neighbors, list(surfaces), "[AMOUNT]")


_TOPN_SLOT = (TOPN_SURFACES, TOPN_NEIGHBORS, list(TOPN_SURFACES), "[N]")
# Healthcare has 8 departments and IT 6 teams: "top 10" of them would read oddly.
_TOPN_SMALL = {2: ["2", "two"], 3: ["3", "three"], 5: ["5", "five"]}
_TOPN_SMALL_SLOT = (_TOPN_SMALL, {2: [3], 3: [2, 5], 5: [3]}, list(_TOPN_SMALL), "[N]")
_PERIOD_SLOT = SLOTS["period"]


# ── Retail sales ─────────────────────────────────────────────────────────

_PRODUCTS = {
    "running_shoes": ["running shoes", "running sneakers"],
    "trail_shoes": ["trail shoes", "trail runners"],
    "hiking_boots": ["hiking boots"],
    "rain_jackets": ["rain jackets", "raincoats"],
    "ski_jackets": ["ski jackets"],
    "yoga_mats": ["yoga mats"],
    "water_bottles": ["water bottles"],
    "backpacks": ["backpacks", "rucksacks"],
}
_REGIONS = {
    "northeast": ["the Northeast", "the Northeast region"],
    "southeast": ["the Southeast", "the Southeast region"],
    "midwest": ["the Midwest", "the Midwest region"],
    "west": ["the West", "the West region"],
}
_CHANNELS = {
    "online": ["online", "through the website"],
    "in_store": ["in stores", "in our stores"],
    "wholesale": ["through wholesale", "via wholesale"],
}

RETAIL = Domain(
    name="retail",
    slots={
        "period": _PERIOD_SLOT,
        "product": (
            _PRODUCTS,
            {
                "running_shoes": ["trail_shoes"],
                "trail_shoes": ["running_shoes", "hiking_boots"],
                "hiking_boots": ["trail_shoes"],
                "rain_jackets": ["ski_jackets"],
                "ski_jackets": ["rain_jackets"],
                "yoga_mats": ["water_bottles"],
                "water_bottles": ["yoga_mats"],
                "backpacks": ["water_bottles"],
            },
            list(_PRODUCTS),
            "[PRODUCT]",
        ),
        "region": (
            _REGIONS,
            {
                "northeast": ["southeast"],
                "southeast": ["northeast"],
                "midwest": ["west"],
                "west": ["midwest"],
            },
            list(_REGIONS),
            "[REGION]",
        ),
        "channel": (
            _CHANNELS,
            {"online": ["in_store"], "in_store": ["online"], "wholesale": ["in_store"]},
            list(_CHANNELS),
            "[CHANNEL]",
        ),
        "amount": _amount(
            {
                50: ["$50", "50 dollars"],
                100: ["$100", "100 dollars"],
                250: ["$250", "250 dollars"],
                500: ["$500", "500 dollars"],
            },
            {50: [100], 100: [50, 250], 250: [100, 500], 500: [250]},
        ),
        "n": _TOPN_SLOT,
    },
    intents={
        "product_revenue": [
            "How much revenue did {product} bring in {period}?",
            "What were total sales of {product} {period}?",
            "Total revenue from {product} {period}",
            "What did {product} generate in sales {period}?",
            "How much did {product} sell for in total {period}?",
        ],
        "product_units": [
            "How many units of {product} did we sell {period}?",
            "Number of {product} sold {period}",
            "How many {product} were sold {period}?",
            "Unit sales of {product} {period}",
        ],
        "product_avg_price": [
            "What was the average selling price of {product} {period}?",
            "Average price paid for {product} {period}",
            "On average, how much did customers pay for {product} {period}?",
            "What did {product} sell for on average {period}?",
        ],
        "product_returns": [
            "How much did we refund on {product} {period}?",
            "Total returns of {product} {period}",
            "What was the value of {product} returned {period}?",
            "How much money went back to customers for {product} {period}?",
        ],
        "region_revenue": [
            "What were sales in {region} {period}?",
            "How much revenue came from {region} {period}?",
            "Total revenue for {region} {period}",
            "How much did we sell in {region} {period}?",
        ],
        "region_revenue_excluding": [
            "What were sales everywhere except {region} {period}?",
            "What was our total revenue {period}, not counting {region}?",
            "Total revenue from every region but {region} {period}",
            "How much did we sell {period} outside {region}?",
        ],
        "channel_orders": [
            "How many orders did we get {channel} {period}?",
            "Number of orders placed {channel} {period}",
            "How many orders were placed {channel} {period}?",
            "Order count {channel} {period}",
        ],
        "total_revenue": [
            "What was our total revenue {period}?",
            "How much did we sell in total {period}?",
            "Total sales {period}",
            "What were overall sales {period}?",
            "How much revenue did we make {period}?",
        ],
        "total_returns": [
            "How much did we refund in total {period}?",
            "Total returns {period}",
            "What was the total value of returns {period}?",
            "How much money went back to customers {period}?",
        ],
        "net_sales": [
            "What were net sales {period}?",
            "Revenue minus returns {period}",
            "How much did we make after refunds {period}?",
            "What were sales net of returns {period}?",
        ],
        "largest_order": [
            "What was our largest order {period}?",
            "Show the biggest single order {period}",
            "What was the highest-value order {period}?",
            "Largest sale {period}",
        ],
        "top_products": [
            "What were the top {n} products by revenue {period}?",
            "Which {n} products sold the most {period}?",
            "Show our {n} best-selling products {period}",
            "Top {n} products by sales {period}",
        ],
        "top_customers": [
            "Who were our top {n} customers by spending {period}?",
            "Which {n} customers spent the most {period}?",
            "Show our {n} biggest customers {period}",
            "Top {n} customers by revenue {period}",
        ],
        "large_orders": [
            "Show orders over {amount} {period}",
            "Which orders were above {amount} {period}?",
            "List every order bigger than {amount} {period}",
            "Any orders above {amount} {period}?",
        ],
    },
    intent_relations=[
        ("product_revenue", "product_units", "aggregation"),
        ("product_revenue", "product_avg_price", "aggregation"),
        ("product_units", "product_avg_price", "aggregation"),
        ("product_revenue", "product_returns", "direction"),
        ("region_revenue", "region_revenue_excluding", "negation"),
        ("total_revenue", "total_returns", "direction"),
        ("total_revenue", "net_sales", "measure"),
        ("total_returns", "net_sales", "measure"),
        ("total_revenue", "largest_order", "aggregation"),
        ("top_products", "top_customers", "grouping"),
    ],
    filter_drop={"product_revenue": "total_revenue", "region_revenue": "total_revenue"},
    filter_add=("total_revenue", "region_revenue", "region"),
    negations=[("region_revenue_excluding", "region_revenue", "region")],
    prompt_intro=(
        "You extract the parameters of a question about the user's retail business\n"
        "(online, in-store and wholesale sales), so that a cached SQL query can be\n"
        "reused with the new values."
    ),
    slot_prompts={
        "product": "a product named in the question, one of {ids}. Return the id.",
        "region": "a sales region named in the question, one of {ids}. Return the id.",
        "channel": "a sales channel named in the question, one of {ids}. Return the id.",
        "amount": "an order value in the question, as an integer number of dollars.",
        "n": _TOP_N,
    },
    human_context="Your retail business (online, in-store and wholesale sales)",
    human_goals={
        "product_revenue": "total revenue from one product",
        "product_units": "number of units sold of one product",
        "product_avg_price": "average selling price of one product",
        "product_returns": "total value refunded for returns of one product",
        "region_revenue": "total revenue in one sales region",
        "region_revenue_excluding": "total revenue from every region EXCEPT one",
        "channel_orders": "number of orders through one sales channel",
        "total_revenue": "total revenue overall",
        "total_returns": "total value of all returns",
        "net_sales": "revenue minus returns",
        "largest_order": "the single largest order",
        "top_products": "the top N products by revenue",
        "top_customers": "the top N customers by amount spent",
        "large_orders": "every order above a dollar amount",
    },
    slot_labels={
        "product": "product",
        "region": "region",
        "channel": "channel",
        "amount": "order value over",
        "n": "N",
    },
)


# ── Healthcare operations (outpatient clinics; synthetic, no patient data) ─

_DEPARTMENTS = {
    "cardiology": ["cardiology", "the cardiology department"],
    "pulmonology": ["pulmonology", "the pulmonology department"],
    "pediatrics": ["pediatrics", "the pediatrics department"],
    "family_medicine": ["family medicine", "the family medicine department"],
    "orthopedics": ["orthopedics", "the orthopedics department"],
    "physical_therapy": ["physical therapy", "the physical therapy department"],
    "dermatology": ["dermatology", "the dermatology department"],
    "radiology": ["radiology", "the radiology department"],
}
_CLINICS = {
    "downtown": ["the Downtown clinic", "the Downtown site"],
    "midtown": ["the Midtown clinic", "the Midtown site"],
    "riverside": ["the Riverside clinic", "the Riverside site"],
    "lakeside": ["the Lakeside clinic", "the Lakeside site"],
    "northgate": ["the Northgate clinic", "the Northgate site"],
    "southgate": ["the Southgate clinic", "the Southgate site"],
}
_PAYERS = {
    "medicare": ["Medicare"],
    "medicare_advantage": ["Medicare Advantage"],
    "medicaid": ["Medicaid"],
    "commercial": ["commercial insurance", "private insurance"],
}

HEALTHCARE = Domain(
    name="healthcare",
    slots={
        "period": _PERIOD_SLOT,
        "department": (
            _DEPARTMENTS,
            {
                "cardiology": ["pulmonology"],
                "pulmonology": ["cardiology"],
                "pediatrics": ["family_medicine"],
                "family_medicine": ["pediatrics"],
                "orthopedics": ["physical_therapy"],
                "physical_therapy": ["orthopedics"],
                "dermatology": ["radiology"],
                "radiology": ["dermatology"],
            },
            list(_DEPARTMENTS),
            "[DEPARTMENT]",
        ),
        "clinic": (
            _CLINICS,
            {
                "downtown": ["midtown"],
                "midtown": ["downtown"],
                "riverside": ["lakeside"],
                "lakeside": ["riverside"],
                "northgate": ["southgate"],
                "southgate": ["northgate"],
            },
            list(_CLINICS),
            "[CLINIC]",
        ),
        "payer": (
            _PAYERS,
            {
                "medicare": ["medicare_advantage", "medicaid"],
                "medicare_advantage": ["medicare"],
                "medicaid": ["medicare"],
                "commercial": ["medicare_advantage"],
            },
            list(_PAYERS),
            "[PAYER]",
        ),
        "amount": _amount(
            {
                15: ["15 minutes", "a quarter of an hour"],
                30: ["30 minutes", "half an hour"],
                45: ["45 minutes", "three quarters of an hour"],
                60: ["60 minutes", "an hour"],
            },
            {15: [30], 30: [15, 45], 45: [30, 60], 60: [45]},
        ),
        "n": _TOPN_SMALL_SLOT,
    },
    intents={
        "dept_visits": [
            "How many visits did {department} have {period}?",
            "Number of patient visits in {department} {period}",
            "How many patient visits did {department} handle {period}?",
            "Visit count for {department} {period}",
        ],
        "dept_avg_wait": [
            "What was the average wait time in {department} {period}?",
            "How long did patients wait on average in {department} {period}?",
            "Average wait for {department} {period}",
            "Mean waiting time in {department} {period}",
        ],
        "dept_charges": [
            "How much did {department} bill {period}?",
            "Total charges billed by {department} {period}",
            "What did {department} bill in total {period}?",
            "Sum of charges for {department} {period}",
        ],
        "clinic_referrals_in": [
            "How many referrals did {clinic} receive {period}?",
            "Number of incoming referrals at {clinic} {period}",
            "How many patients were referred to {clinic} {period}?",
            "Referrals into {clinic} {period}",
        ],
        "clinic_referrals_out": [
            "How many referrals did {clinic} send out {period}?",
            "Number of outgoing referrals from {clinic} {period}",
            "How many patients did {clinic} refer elsewhere {period}?",
            "Referrals out of {clinic} {period}",
        ],
        "clinic_visits": [
            "How many visits were there at {clinic} {period}?",
            "Number of patient visits at {clinic} {period}",
            "How many patient visits did {clinic} handle {period}?",
            "Visit volume at {clinic} {period}",
        ],
        "clinic_visits_excluding": [
            "How many visits were there across all clinics except {clinic} {period}?",
            "What was our visit count {period}, not counting {clinic}?",
            "Visits at every site but {clinic} {period}",
            "How many visits did we have {period} outside {clinic}?",
        ],
        "payer_visits": [
            "How many visits were billed to {payer} {period}?",
            "Number of visits covered by {payer} {period}",
            "How many {payer} visits did we have {period}?",
            "Visit count for {payer} patients {period}",
        ],
        "total_visits": [
            "How many patient visits did we have {period}?",
            "Total visits {period}",
            "What was our overall visit volume {period}?",
            "How many visits did we handle in total {period}?",
        ],
        "total_no_shows": [
            "How many no-shows did we have {period}?",
            "Total missed appointments {period}",
            "How many appointments were no-shows {period}?",
            "No-show count {period}",
        ],
        "no_show_rate": [
            "What was our no-show rate {period}?",
            "What share of appointments were missed {period}?",
            "No-shows as a percentage of appointments {period}",
            "How often did patients miss appointments {period}?",
        ],
        "avg_wait": [
            "What was the average wait time {period}?",
            "How long did patients wait on average {period}?",
            "Average patient wait {period}",
            "Mean wait time {period}",
        ],
        "longest_wait": [
            "What was the longest wait {period}?",
            "Show the single longest patient wait {period}",
            "What was the maximum wait time {period}?",
            "Longest wait recorded {period}",
        ],
        "top_departments": [
            "Which {n} departments had the most visits {period}?",
            "Top {n} departments by visit volume {period}",
            "Show our {n} busiest departments {period}",
            "What were the {n} departments with the most visits {period}?",
        ],
        "top_providers": [
            "Which {n} providers had the most visits {period}?",
            "Top {n} providers by visit count {period}",
            "Show our {n} busiest providers {period}",
            "Who were the {n} providers with the most visits {period}?",
        ],
        "long_waits": [
            "Show visits with waits over {amount} {period}",
            "Which appointments had a wait longer than {amount} {period}?",
            "List every visit where the wait exceeded {amount} {period}",
            "Any waits above {amount} {period}?",
        ],
    },
    intent_relations=[
        ("dept_visits", "dept_charges", "aggregation"),
        ("dept_visits", "dept_avg_wait", "measure"),
        ("clinic_referrals_in", "clinic_referrals_out", "direction"),
        ("clinic_visits", "clinic_visits_excluding", "negation"),
        ("total_visits", "total_no_shows", "measure"),
        ("total_no_shows", "no_show_rate", "aggregation"),
        ("avg_wait", "longest_wait", "aggregation"),
        ("top_departments", "top_providers", "grouping"),
    ],
    filter_drop={
        "dept_visits": "total_visits",
        "clinic_visits": "total_visits",
        "payer_visits": "total_visits",
    },
    filter_add=("total_visits", "clinic_visits", "clinic"),
    negations=[("clinic_visits_excluding", "clinic_visits", "clinic")],
    prompt_intro=(
        "You extract the parameters of a question about the outpatient clinic network\n"
        "the user manages, so that a cached SQL query can be reused with the new\n"
        "values."
    ),
    slot_prompts={
        "department": "a department named in the question, one of {ids}. Return the id.",
        "clinic": "a clinic named in the question, one of {ids}. Return the id.",
        "payer": "a payer named in the question, one of {ids}. Return the id.",
        "amount": "a wait-time threshold in the question, as an integer number of minutes.",
        "n": _TOP_N,
    },
    human_context="The outpatient clinic network you manage",
    human_goals={
        "dept_visits": "number of patient visits in one department",
        "dept_avg_wait": "average patient wait time in one department",
        "dept_charges": "total amount billed by one department",
        "clinic_referrals_in": "number of referrals received by one clinic",
        "clinic_referrals_out": "number of referrals sent out by one clinic",
        "clinic_visits": "number of patient visits at one clinic",
        "clinic_visits_excluding": "number of visits at every clinic EXCEPT one",
        "payer_visits": "number of visits billed to one payer",
        "total_visits": "total patient visits overall",
        "total_no_shows": "number of missed appointments (no-shows)",
        "no_show_rate": "share of appointments that were no-shows",
        "avg_wait": "average patient wait time overall",
        "longest_wait": "the single longest patient wait",
        "top_departments": "the top N departments by number of visits",
        "top_providers": "the top N providers by number of visits",
        "long_waits": "every visit with a wait longer than a threshold",
    },
    slot_labels={
        "department": "department",
        "clinic": "clinic",
        "payer": "payer",
        "amount": "wait longer than",
        "n": "N",
    },
)


# ── IT support / operations ──────────────────────────────────────────────

_TEAMS = {
    "service_desk": ["the service desk", "the help desk"],
    "desktop_support": ["desktop support", "the desktop support team"],
    "network": ["the network team", "network engineering"],
    "security": ["the security team", "information security"],
    "database": ["the database team", "the DBA team"],
    "cloud": ["the cloud team", "the cloud platform team"],
}
_PRIORITIES = {
    "p1": ["P1", "priority 1", "critical"],
    "p2": ["P2", "priority 2", "high-priority"],
    "p3": ["P3", "priority 3", "medium-priority"],
    "p4": ["P4", "priority 4", "low-priority"],
}
_SERVICES = {
    "email": ["email", "the email system"],
    "vpn": ["the VPN", "VPN access"],
    "wifi": ["Wi-Fi", "the wireless network"],
    "printing": ["printing", "printers"],
    "sso": ["single sign-on", "SSO"],
    "laptops": ["laptops", "laptop hardware"],
}

IT_SUPPORT = Domain(
    name="it_support",
    slots={
        "period": _PERIOD_SLOT,
        "team": (
            _TEAMS,
            {
                "service_desk": ["desktop_support"],
                "desktop_support": ["service_desk"],
                "network": ["security"],
                "security": ["network"],
                "database": ["cloud"],
                "cloud": ["database"],
            },
            list(_TEAMS),
            "[TEAM]",
        ),
        "priority": (
            _PRIORITIES,
            {"p1": ["p2"], "p2": ["p1", "p3"], "p3": ["p2", "p4"], "p4": ["p3"]},
            list(_PRIORITIES),
            "[PRIORITY]",
        ),
        "service": (
            _SERVICES,
            {
                "email": ["sso"],
                "sso": ["email"],
                "vpn": ["wifi"],
                "wifi": ["vpn"],
                "printing": ["laptops"],
                "laptops": ["printing"],
            },
            list(_SERVICES),
            "[SERVICE]",
        ),
        "amount": _amount(
            {
                4: ["4 hours", "four hours"],
                8: ["8 hours", "eight hours"],
                24: ["24 hours", "a day"],
                48: ["48 hours", "two days"],
            },
            {4: [8], 8: [4, 24], 24: [8, 48], 48: [24]},
        ),
        "n": _TOPN_SMALL_SLOT,
    },
    intents={
        "team_opened": [
            "How many tickets did {team} receive {period}?",
            "Number of tickets assigned to {team} {period}",
            "How many new tickets went to {team} {period}?",
            "Ticket intake for {team} {period}",
        ],
        "team_resolved": [
            "How many tickets did {team} resolve {period}?",
            "Number of tickets closed by {team} {period}",
            "How many tickets did {team} close out {period}?",
            "Resolved ticket count for {team} {period}",
        ],
        "team_avg_resolution": [
            "What was the average resolution time for {team} {period}?",
            "How long did {team} take to resolve tickets on average {period}?",
            "Average time to resolve for {team} {period}",
            "Mean resolution time for {team} {period}",
        ],
        "priority_count": [
            "How many {priority} tickets did we get {period}?",
            "Number of {priority} tickets {period}",
            "How many {priority} tickets were opened {period}?",
            "Count of {priority} tickets {period}",
        ],
        "priority_count_excluding": [
            "How many tickets were opened {period}, excluding {priority} ones?",
            "What was our ticket count {period}, not counting {priority} tickets?",
            "How many tickets of every priority except {priority} did we get {period}?",
            "Count of all tickets but {priority} ones {period}",
        ],
        "service_count": [
            "How many tickets were about {service} {period}?",
            "Number of tickets about {service} {period}",
            "How many issues with {service} were reported {period}?",
            "Ticket volume for {service} {period}",
        ],
        "total_opened": [
            "How many tickets were opened {period}?",
            "Total tickets {period}",
            "What was our overall ticket volume {period}?",
            "How many tickets came in {period}?",
        ],
        "total_resolved": [
            "How many tickets were resolved {period}?",
            "Total tickets closed {period}",
            "How many tickets did we close {period}?",
            "Resolved tickets {period}",
        ],
        "backlog_change": [
            "How much did the backlog grow {period}?",
            "Tickets opened minus tickets closed {period}",
            "What was the net change in open tickets {period}?",
            "By how many tickets did the backlog change {period}?",
        ],
        "avg_resolution": [
            "What was the average resolution time {period}?",
            "How long did tickets take to resolve on average {period}?",
            "Average time to resolve {period}",
            "Mean resolution time {period}",
        ],
        "longest_resolution": [
            "What was the longest resolution time {period}?",
            "Which ticket took longest to resolve {period}?",
            "Show the slowest-resolved ticket {period}",
            "Maximum time to resolve {period}",
        ],
        "top_teams": [
            "Which {n} teams got the most tickets {period}?",
            "Top {n} teams by ticket volume {period}",
            "Show the {n} busiest teams {period}",
            "What were the {n} teams with the most tickets {period}?",
        ],
        "top_services": [
            "Which {n} services had the most tickets {period}?",
            "Top {n} services by ticket count {period}",
            "Show the {n} most-reported services {period}",
            "What were the {n} services with the most issues {period}?",
        ],
        "slow_tickets": [
            "Show tickets that took longer than {amount} to resolve {period}",
            "Which tickets stayed open more than {amount} {period}?",
            "List every ticket resolved in over {amount} {period}",
            "Any tickets taking over {amount} to close {period}?",
        ],
    },
    intent_relations=[
        ("team_opened", "team_resolved", "direction"),
        ("team_resolved", "team_avg_resolution", "aggregation"),
        ("priority_count", "priority_count_excluding", "negation"),
        ("total_opened", "total_resolved", "direction"),
        ("total_opened", "backlog_change", "measure"),
        ("total_resolved", "backlog_change", "measure"),
        ("avg_resolution", "longest_resolution", "aggregation"),
        ("top_teams", "top_services", "grouping"),
    ],
    filter_drop={
        "team_opened": "total_opened",
        "priority_count": "total_opened",
        "service_count": "total_opened",
    },
    filter_add=("total_opened", "service_count", "service"),
    negations=[("priority_count_excluding", "priority_count", "priority")],
    prompt_intro=(
        "You extract the parameters of a question about the IT support organization\n"
        "the user runs, so that a cached SQL query can be reused with the new values."
    ),
    slot_prompts={
        "team": "a support team named in the question, one of {ids}. Return the id.",
        "priority": "a ticket priority named in the question, one of {ids}. Return the id.",
        "service": "a service named in the question, one of {ids}. Return the id.",
        "amount": "a resolution-time threshold in the question, as an integer number of hours.",
        "n": _TOP_N,
    },
    human_context="The IT support organization you lead",
    human_goals={
        "team_opened": "number of tickets assigned to one team",
        "team_resolved": "number of tickets one team resolved",
        "team_avg_resolution": "average time one team took to resolve tickets",
        "priority_count": "number of tickets of one priority",
        "priority_count_excluding": "number of tickets of every priority EXCEPT one",
        "service_count": "number of tickets about one service",
        "total_opened": "total tickets opened",
        "total_resolved": "total tickets resolved",
        "backlog_change": "tickets opened minus tickets resolved",
        "avg_resolution": "average resolution time overall",
        "longest_resolution": "the single longest resolution time",
        "top_teams": "the top N teams by number of tickets",
        "top_services": "the top N services by number of tickets",
        "slow_tickets": "every ticket that took longer than a threshold to resolve",
    },
    slot_labels={
        "team": "team",
        "priority": "priority",
        "service": "service",
        "amount": "resolution longer than",
        "n": "N",
    },
)

DOMAINS: dict[str, Domain] = {d.name: d for d in (FINANCE, RETAIL, HEALTHCARE, IT_SUPPORT)}
