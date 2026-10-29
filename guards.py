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
