"""Guards for the hybrid cache (README section 15).

The guarded cache uses similarity only to shortlist cached templates. A reuse
also needs every guard below to pass, and any doubt means a miss:

  slots      the same set of extracted slots (already required by
             split_template)
  signature  the same operator signature, (operation, excludes, flow), as
             extracted by the model with the values (extract.py
             --extractor gemini-relsig:<model>)
  negation   a negation cue ("except", "excluding", "not counting", ...) must
             appear in both questions or in neither, and a question with a
             cue must have a named value extracted for it to exclude

Every rule here was written before any guarded result existed and has no
tunable part. The cue list is generic English, not any domain's wording.

GOLD_SIGNATURES is the author's reading of each intent. It is used for two
things only: reporting how often the extractor's signature agrees with it,
and an upper bound (the guarded design given perfect signatures). The guarded
design itself never sees it.
"""

from __future__ import annotations

import re

NEGATION_CUE = re.compile(
    r"\b(?:except|excluding|exclude|not counting|other than|apart from|outside)\b"
    r"|\b(?:all|every\w*|everything)\s+(?:\w+\s+)?but\b",
    re.IGNORECASE,
)

# Slots that carry a named value a question could exclude.
NON_ENTITY_SLOTS = {"period", "amount", "n"}


def has_negation_cue(text: str) -> bool:
    return bool(NEGATION_CUE.search(text))


def negation_consistent(text: str, params: dict) -> bool:
    """False when the question excludes something but nothing was extracted
    for it to exclude, which is the silent-drop failure of section 13."""
    if not has_negation_cue(text):
        return True
    return any(s not in NON_ENTITY_SLOTS for s in params)


# (operation, excludes, flow) per intent.
GOLD_SIGNATURES: dict[str, dict[str, tuple[str, bool, str]]] = {
    "finance": {
        "merchant_spend_total": ("sum", False, "outbound"),
        "merchant_txn_count": ("count", False, "outbound"),
        "merchant_avg": ("average", False, "outbound"),
        "merchant_refunds": ("sum", False, "inbound"),
        "category_spend_total": ("sum", False, "outbound"),
        "category_spend_excluding": ("sum", True, "outbound"),
        "account_spend_total": ("sum", False, "outbound"),
        "total_spend": ("sum", False, "outbound"),
        "income_total": ("sum", False, "inbound"),
        "net_cash_flow": ("difference", False, "net"),
        "largest_purchase": ("maximum", False, "outbound"),
        "top_merchants": ("rank", False, "outbound"),
        "top_categories": ("rank", False, "outbound"),
        "large_transactions": ("list", False, "outbound"),
    },
    "retail": {
        "product_revenue": ("sum", False, "inbound"),
        "product_units": ("count", False, "inbound"),
        "product_avg_price": ("average", False, "inbound"),
        "product_returns": ("sum", False, "outbound"),
        "region_revenue": ("sum", False, "inbound"),
        "region_revenue_excluding": ("sum", True, "inbound"),
        "channel_orders": ("count", False, "inbound"),
        "total_revenue": ("sum", False, "inbound"),
        "total_returns": ("sum", False, "outbound"),
        "net_sales": ("difference", False, "net"),
        "largest_order": ("maximum", False, "inbound"),
        "top_products": ("rank", False, "inbound"),
        "top_customers": ("rank", False, "inbound"),
        "large_orders": ("list", False, "inbound"),
    },
    "healthcare": {
        "dept_visits": ("count", False, "none"),
        "dept_avg_wait": ("average", False, "none"),
        "dept_charges": ("sum", False, "none"),
        "clinic_referrals_in": ("count", False, "inbound"),
        "clinic_referrals_out": ("count", False, "outbound"),
        "clinic_visits": ("count", False, "none"),
        "clinic_visits_excluding": ("count", True, "none"),
        "payer_visits": ("count", False, "none"),
        "total_visits": ("count", False, "none"),
        "total_no_shows": ("count", False, "none"),
        "no_show_rate": ("rate", False, "none"),
        "avg_wait": ("average", False, "none"),
        "longest_wait": ("maximum", False, "none"),
        "top_departments": ("rank", False, "none"),
        "top_providers": ("rank", False, "none"),
        "long_waits": ("list", False, "none"),
    },
    "it_support": {
        "team_opened": ("count", False, "inbound"),
        "team_resolved": ("count", False, "outbound"),
        "team_avg_resolution": ("average", False, "none"),
        "priority_count": ("count", False, "inbound"),
        "priority_count_excluding": ("count", True, "inbound"),
        "service_count": ("count", False, "inbound"),
        "total_opened": ("count", False, "inbound"),
        "total_resolved": ("count", False, "outbound"),
        "backlog_change": ("difference", False, "net"),
        "avg_resolution": ("average", False, "none"),
        "longest_resolution": ("maximum", False, "none"),
        "top_teams": ("rank", False, "inbound"),
        "top_services": ("rank", False, "inbound"),
        "slow_tickets": ("list", False, "none"),
    },
}


def signature_key(sig: dict | None) -> tuple | None:
    if not sig:
        return None
    return (sig.get("operation"), bool(sig.get("excludes")), sig.get("flow"))


# ── Full signature (README section 18) ──────────────────────────────────
#
# Section 15's signature left the measure (visits or referrals) and the
# grouping (teams or services) to similarity, and similarity confused them on
# held-out wording. The full signature asks the extractor for both, from each
# domain's own closed list, as a semantic layer would define them. Direction
# ("flow") is dropped: the measure carries it (spending or refunds, referrals
# received or sent).

FULL_MEASURES: dict[str, dict[str, str]] = {
    "finance": {
        "spending": "money the user spent or that went out of an account: purchases, "
        "payments, charges, transactions",
        "refunds": "money a merchant paid back to the user",
        "income": "money the user received: pay, salary, deposits",
        "net_cash_flow": "income minus spending",
    },
    "retail": {
        "revenue": "money customers paid for sales: revenue, sales, what customers spent",
        "units": "units of a product sold",
        "price": "the price a product sold for, per unit",
        "returns": "money refunded to customers for returned items",
        "orders": "orders: how many there were, or the value of single orders",
        "net_sales": "revenue minus returns",
    },
    "healthcare": {
        "visits": "patient visits or appointments that took place",
        "wait_time": "how long patients waited",
        "charges": "amounts billed for care",
        "referrals_received": "referrals a clinic received from elsewhere",
        "referrals_sent": "referrals a clinic sent out to others",
        "no_shows": "missed appointments (no-shows)",
    },
    "it_support": {
        "tickets_opened": "tickets received, opened, assigned or reported: ticket volume or intake",
        "tickets_resolved": "tickets resolved or closed",
        "resolution_time": "how long tickets took to resolve",
        "backlog": "tickets opened minus tickets resolved",
    },
}

# What a question ranks or breaks its answer down by; "none" otherwise.
FULL_GROUPINGS: dict[str, dict[str, str]] = {
    "finance": {"merchant": "merchants", "category": "spending categories"},
    "retail": {"product": "products", "customer": "customers"},
    "healthcare": {"department": "departments", "provider": "providers (clinicians)"},
    "it_support": {"team": "support teams", "service": "services or systems"},
}

# (operation, measure, group_by, excludes) per intent: the author's reading,
# used only for agreement and the upper bound, as GOLD_SIGNATURES is.
GOLD_FULL_SIGNATURES: dict[str, dict[str, tuple[str, str, str, bool]]] = {
    "finance": {
        "merchant_spend_total": ("sum", "spending", "none", False),
        "merchant_txn_count": ("count", "spending", "none", False),
        "merchant_avg": ("average", "spending", "none", False),
        "merchant_refunds": ("sum", "refunds", "none", False),
        "category_spend_total": ("sum", "spending", "none", False),
        "category_spend_excluding": ("sum", "spending", "none", True),
        "account_spend_total": ("sum", "spending", "none", False),
        "total_spend": ("sum", "spending", "none", False),
        "income_total": ("sum", "income", "none", False),
        "net_cash_flow": ("difference", "net_cash_flow", "none", False),
        "largest_purchase": ("maximum", "spending", "none", False),
        "top_merchants": ("rank", "spending", "merchant", False),
        "top_categories": ("rank", "spending", "category", False),
        "large_transactions": ("list", "spending", "none", False),
    },
    "retail": {
        "product_revenue": ("sum", "revenue", "none", False),
        "product_units": ("count", "units", "none", False),
        "product_avg_price": ("average", "price", "none", False),
        "product_returns": ("sum", "returns", "none", False),
        "region_revenue": ("sum", "revenue", "none", False),
        "region_revenue_excluding": ("sum", "revenue", "none", True),
        "channel_orders": ("count", "orders", "none", False),
        "total_revenue": ("sum", "revenue", "none", False),
        "total_returns": ("sum", "returns", "none", False),
        "net_sales": ("difference", "net_sales", "none", False),
        "largest_order": ("maximum", "orders", "none", False),
        "top_products": ("rank", "revenue", "product", False),
        "top_customers": ("rank", "revenue", "customer", False),
        "large_orders": ("list", "orders", "none", False),
    },
    "healthcare": {
        "dept_visits": ("count", "visits", "none", False),
        "dept_avg_wait": ("average", "wait_time", "none", False),
        "dept_charges": ("sum", "charges", "none", False),
        "clinic_referrals_in": ("count", "referrals_received", "none", False),
        "clinic_referrals_out": ("count", "referrals_sent", "none", False),
        "clinic_visits": ("count", "visits", "none", False),
        "clinic_visits_excluding": ("count", "visits", "none", True),
        "payer_visits": ("count", "visits", "none", False),
        "total_visits": ("count", "visits", "none", False),
        "total_no_shows": ("count", "no_shows", "none", False),
        "no_show_rate": ("rate", "no_shows", "none", False),
        "avg_wait": ("average", "wait_time", "none", False),
        "longest_wait": ("maximum", "wait_time", "none", False),
        "top_departments": ("rank", "visits", "department", False),
        "top_providers": ("rank", "visits", "provider", False),
        "long_waits": ("list", "wait_time", "none", False),
    },
    "it_support": {
        "team_opened": ("count", "tickets_opened", "none", False),
        "team_resolved": ("count", "tickets_resolved", "none", False),
        "team_avg_resolution": ("average", "resolution_time", "none", False),
        "priority_count": ("count", "tickets_opened", "none", False),
        "priority_count_excluding": ("count", "tickets_opened", "none", True),
        "service_count": ("count", "tickets_opened", "none", False),
        "total_opened": ("count", "tickets_opened", "none", False),
        "total_resolved": ("count", "tickets_resolved", "none", False),
        "backlog_change": ("difference", "backlog", "none", False),
        "avg_resolution": ("average", "resolution_time", "none", False),
        "longest_resolution": ("maximum", "resolution_time", "none", False),
        "top_teams": ("rank", "tickets_opened", "team", False),
        "top_services": ("rank", "tickets_opened", "service", False),
        "slow_tickets": ("list", "resolution_time", "none", False),
    },
}


def full_signature_key(sig: dict | None) -> tuple | None:
    if not sig or not sig.get("measure"):
        return None
    return (
        sig.get("operation"),
        sig.get("measure"),
        sig.get("group_by"),
        bool(sig.get("excludes")),
    )
