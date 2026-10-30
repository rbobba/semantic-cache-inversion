# st:Snowflake/snowflake-arctic-embed-l-v2.0 prefix='query: ' holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.91 | 0.7492 | 0.9566 | 0.9891 | 0.9981 |
| **equivalent_surface (same wording=True)** | 290 | 0.91 | 0.7492 | 0.9566 | 0.9891 | 0.9981 |
| **filter_change** | 37 | 0.6752 | 0.5024 | 0.7185 | 0.8092 | 0.865 |
| **intent_near_miss** | 176 | 0.7383 | 0.5752 | 0.7516 | 0.8533 | 0.9006 |
| **intent_near_miss (same wording=False)** | 176 | 0.7383 | 0.5752 | 0.7516 | 0.8533 | 0.9006 |
| **param_near_miss** | 637 | 0.8107 | 0.6253 | 0.8301 | 0.9687 | 0.9901 |
| **param_near_miss (same wording=False)** | 228 | 0.7145 | 0.5578 | 0.7142 | 0.8713 | 0.9469 |
| **param_near_miss (same wording=True)** | 409 | 0.8644 | 0.7403 | 0.8723 | 0.9779 | 0.9901 |
| **paraphrase** | 266 | 0.8184 | 0.6496 | 0.8563 | 0.93 | 0.9737 |
| equivalent_surface/account/alias | 10 | 0.9592 | 0.9487 | 0.9592 | 0.9702 | 0.9704 |
| equivalent_surface/amount/alias | 10 | 0.9745 | 0.9666 | 0.9755 | 0.9807 | 0.9877 |
| equivalent_surface/category/alias | 14 | 0.9531 | 0.9179 | 0.959 | 0.9728 | 0.9862 |
| equivalent_surface/merchant/alias | 20 | 0.9619 | 0.9387 | 0.9611 | 0.982 | 0.9835 |
| equivalent_surface/n/alias | 20 | 0.9961 | 0.9945 | 0.9963 | 0.9974 | 0.9981 |
| equivalent_surface/period/alias | 216 | 0.8892 | 0.7219 | 0.9443 | 0.9823 | 0.9946 |
| filter_change/filter_added/category_spend_total | 7 | 0.7711 | 0.6783 | 0.7746 | 0.8635 | 0.865 |
| filter_change/filter_dropped/total_spend | 30 | 0.6528 | 0.4846 | 0.6882 | 0.7868 | 0.8223 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5745 | 0.5388 | 0.5473 | 0.6335 | 0.7188 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8103 | 0.7648 | 0.8101 | 0.8566 | 0.8822 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8185 | 0.7506 | 0.8308 | 0.8761 | 0.882 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7752 | 0.7135 | 0.7713 | 0.8377 | 0.8576 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5597 | 0.4397 | 0.5471 | 0.6884 | 0.6891 |
| intent_near_miss/direction/income_total | 7 | 0.7491 | 0.6858 | 0.7523 | 0.8086 | 0.8529 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8049 | 0.7384 | 0.8123 | 0.8643 | 0.8863 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7309 | 0.695 | 0.7348 | 0.7759 | 0.7805 |
| intent_near_miss/direction/total_spend | 7 | 0.6657 | 0.5989 | 0.6458 | 0.7488 | 0.7871 |
| intent_near_miss/grouping/top_categories | 10 | 0.712 | 0.5936 | 0.7276 | 0.8111 | 0.8376 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7196 | 0.6875 | 0.7174 | 0.7649 | 0.8073 |
| intent_near_miss/measure/income_total | 7 | 0.6974 | 0.6298 | 0.6783 | 0.798 | 0.8107 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6162 | 0.5183 | 0.6358 | 0.6948 | 0.7221 |
| intent_near_miss/measure/total_spend | 7 | 0.5904 | 0.5217 | 0.5793 | 0.6705 | 0.6939 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8382 | 0.7796 | 0.8494 | 0.8725 | 0.88 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8318 | 0.7821 | 0.8183 | 0.8951 | 0.9006 |
| param_near_miss/account/neighbor | 20 | 0.7553 | 0.5995 | 0.8066 | 0.8972 | 0.9268 |
| param_near_miss/amount/neighbor | 24 | 0.7337 | 0.5371 | 0.7929 | 0.877 | 0.9088 |
| param_near_miss/category/neighbor | 47 | 0.8119 | 0.6859 | 0.8278 | 0.9128 | 0.9582 |
| param_near_miss/merchant/neighbor | 86 | 0.7002 | 0.5863 | 0.7175 | 0.8024 | 0.8484 |
| param_near_miss/n/neighbor | 46 | 0.8787 | 0.712 | 0.9357 | 0.9764 | 0.9829 |
| param_near_miss/period/adjacent | 225 | 0.8479 | 0.6331 | 0.8743 | 0.9829 | 0.9901 |
| param_near_miss/period/granularity | 189 | 0.8156 | 0.6774 | 0.8378 | 0.9199 | 0.9635 |
| paraphrase/wording/template | 266 | 0.8184 | 0.6496 | 0.8563 | 0.93 | 0.9737 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4688 | [0.3828, 0.5547] | 0.9297 | [0.8828, 0.9688] |
| param_near_miss | 128 | 0.4688 | [0.3828, 0.5547] | 0.9219 | [0.8748, 0.9688] |
| period_near_miss | 128 | 0.4688 | [0.3828, 0.5547] | 0.8984 | [0.8516, 0.9531] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.6 | [0.51, 0.69] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.4237 | [0.3305, 0.5085] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8125 | [0.7422, 0.875] |
| B | 128 | 0.5547 | [0.4688, 0.6406] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0247 | [0.0136, 0.0432] | 0.0247 | 0.0247 | 0.5047 |
| raw_oracle_entry | 0.2903 | [0.2631, 0.3232] | — | — | 0.5047 |
| split_full | 0.0797 | [0.0563, 0.1825] | 0.0797 | 0.2049 | 0.5047 |
| split_template | 0.5389 | [0.4804, 0.6046] | 0.5389 | 0.5389 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9779 | How much more did I earn than I spent so far this year? | 0.9273 |
| Total spent on shopping this year | Total spent on shopping last year | 0.9506 | Total spent on shopping year to date | 0.9103 |
| What was my largest purchase this year? | What was my largest purchase last year? | 0.9684 | What was my largest purchase so far this year? | 0.9302 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9716 | How much more did I earn than I spent so far this month? | 0.9409 |
| What was my largest purchase this month? | What was my largest purchase last month? | 0.9779 | What was my largest purchase so far this month? | 0.9487 |
| How much more did I earn than I spent this week? | How much more did I earn than I spent last week? | 0.9786 | How much more did I earn than I spent so far this week? | 0.9515 |
| How much income did I receive last month? | How much income did I receive this month? | 0.94 | How much income did I receive in the previous month? | 0.9143 |
| Total spent at Amazon this year | Total spent at Amazon last year | 0.9621 | Total spent at Amazon year to date | 0.9373 |
| How much income did I receive this week? | How much income did I receive last week? | 0.955 | How much income did I receive so far this week? | 0.9312 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9569 | What were my overall expenses so far this month? | 0.9332 |
| What was my largest purchase this week? | What was my largest purchase last week? | 0.978 | What was my largest purchase so far this week? | 0.9568 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9638 | What did travel cost me so far this week? | 0.9428 |
| What did I pay Amazon in total last month? | What did I pay Amazon in total this month? | 0.972 | What did I pay Amazon in total in the previous month? | 0.9515 |
| What were my overall expenses this week? | What were my overall expenses last week? | 0.9598 | What were my overall expenses so far this week? | 0.9394 |
| Which purchases were above $100 this year? | Which purchases were above $100 last year? | 0.9804 | Which purchases were above 100 dollars this year? | 0.9618 |
