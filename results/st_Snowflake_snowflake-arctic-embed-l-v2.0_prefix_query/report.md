# st:Snowflake/snowflake-arctic-embed-l-v2.0 prefix='query: '

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9102 | 0.7413 | 0.958 | 0.9906 | 0.9978 |
| **equivalent_surface (same wording=True)** | 262 | 0.9102 | 0.7413 | 0.958 | 0.9906 | 0.9978 |
| **filter_change** | 37 | 0.678 | 0.5391 | 0.6726 | 0.8279 | 0.9009 |
| **intent_near_miss** | 176 | 0.7319 | 0.5705 | 0.7582 | 0.8514 | 0.9147 |
| **intent_near_miss (same wording=False)** | 176 | 0.7319 | 0.5705 | 0.7582 | 0.8514 | 0.9147 |
| **param_near_miss** | 637 | 0.8127 | 0.6294 | 0.8258 | 0.9697 | 0.9909 |
| **param_near_miss (same wording=False)** | 228 | 0.7119 | 0.5544 | 0.724 | 0.8554 | 0.9433 |
| **param_near_miss (same wording=True)** | 409 | 0.8688 | 0.7484 | 0.8821 | 0.9785 | 0.9909 |
| **paraphrase** | 384 | 0.8042 | 0.6261 | 0.8325 | 0.9251 | 0.9775 |
| equivalent_surface/account/alias | 10 | 0.9583 | 0.949 | 0.9603 | 0.9643 | 0.9733 |
| equivalent_surface/amount/alias | 10 | 0.9774 | 0.9671 | 0.9769 | 0.9871 | 0.988 |
| equivalent_surface/category/alias | 15 | 0.9471 | 0.9012 | 0.9578 | 0.9728 | 0.983 |
| equivalent_surface/merchant/alias | 12 | 0.9688 | 0.9538 | 0.9769 | 0.9829 | 0.986 |
| equivalent_surface/n/alias | 20 | 0.9956 | 0.994 | 0.9957 | 0.9973 | 0.9978 |
| equivalent_surface/period/alias | 195 | 0.889 | 0.7265 | 0.949 | 0.9822 | 0.9942 |
| filter_change/filter_added/category_spend_total | 7 | 0.7538 | 0.6482 | 0.7252 | 0.8804 | 0.9009 |
| filter_change/filter_dropped/total_spend | 30 | 0.6603 | 0.5362 | 0.6559 | 0.8148 | 0.8476 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5754 | 0.4603 | 0.61 | 0.6834 | 0.714 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7995 | 0.6777 | 0.8018 | 0.8735 | 0.9038 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8027 | 0.7255 | 0.7937 | 0.8756 | 0.8994 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7794 | 0.7213 | 0.7621 | 0.8549 | 0.9147 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5618 | 0.4323 | 0.5279 | 0.7306 | 0.7947 |
| intent_near_miss/direction/income_total | 7 | 0.678 | 0.5816 | 0.6419 | 0.8021 | 0.8185 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.797 | 0.7564 | 0.7993 | 0.8246 | 0.8844 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.776 | 0.7498 | 0.7876 | 0.8035 | 0.813 |
| intent_near_miss/direction/total_spend | 7 | 0.6945 | 0.6128 | 0.6703 | 0.7795 | 0.8033 |
| intent_near_miss/grouping/top_categories | 10 | 0.6886 | 0.5776 | 0.7172 | 0.754 | 0.8301 |
| intent_near_miss/grouping/top_merchants | 10 | 0.6951 | 0.5782 | 0.7253 | 0.7583 | 0.7594 |
| intent_near_miss/measure/income_total | 7 | 0.6524 | 0.5587 | 0.6428 | 0.7559 | 0.7768 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6248 | 0.4992 | 0.6206 | 0.7463 | 0.7807 |
| intent_near_miss/measure/total_spend | 7 | 0.6414 | 0.5544 | 0.6319 | 0.7315 | 0.7517 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8269 | 0.7406 | 0.8339 | 0.9038 | 0.9058 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7985 | 0.764 | 0.7994 | 0.8458 | 0.8567 |
| param_near_miss/account/neighbor | 20 | 0.7518 | 0.5868 | 0.7855 | 0.8863 | 0.9268 |
| param_near_miss/amount/neighbor | 25 | 0.7396 | 0.4989 | 0.7972 | 0.9089 | 0.9457 |
| param_near_miss/category/neighbor | 45 | 0.8079 | 0.7044 | 0.8151 | 0.8965 | 0.959 |
| param_near_miss/merchant/neighbor | 87 | 0.7017 | 0.5848 | 0.7297 | 0.8009 | 0.8381 |
| param_near_miss/n/neighbor | 45 | 0.8722 | 0.7008 | 0.9283 | 0.9762 | 0.9839 |
| param_near_miss/period/adjacent | 230 | 0.8498 | 0.674 | 0.8756 | 0.9828 | 0.9909 |
| param_near_miss/period/granularity | 185 | 0.8218 | 0.6846 | 0.8466 | 0.9191 | 0.9649 |
| paraphrase/wording/template | 384 | 0.8042 | 0.6261 | 0.8325 | 0.9251 | 0.9775 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5078 | [0.4217, 0.5938] | 0.9766 | [0.9453, 1.0] |
| param_near_miss | 128 | 0.5078 | [0.4219, 0.5938] | 0.9609 | [0.9219, 0.9922] |
| period_near_miss | 128 | 0.5078 | [0.4297, 0.5938] | 0.9531 | [0.9141, 0.9844] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.04] | 0.62 | [0.53, 0.7002] |
| intent_near_miss | 118 | 0.0169 | [0.0, 0.0424] | 0.5 | [0.4153, 0.5847] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0211 | [0.0144, 0.0309] | 0.0211 | 0.0228 | 0.5317 |
| raw_oracle_entry | 0.1073 | [0.0917, 0.1426] | — | — | 0.5317 |
| split_full | 0.2236 | [0.2092, 0.271] | 0.2585 | 0.3122 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9033 | Income minus expenses during 2025 | 0.6757 |
| Total money coming in last year | Total money coming in this year | 0.9146 | Total money coming in during 2025 | 0.7062 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9766 | What did I pay Starbucks in total last year? | 0.8595 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9888 | How much did I get refunded from Spotify last year? | 0.878 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9841 | Average transaction amount at Walmart last year | 0.8809 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9768 | What was my largest purchase last year? | 0.8757 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9564 | Total expenses last year | 0.8653 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9692 | How much did I spend per transaction at Uber last year, on average? | 0.8813 |
| Total spent on gas last year | Total spent on gas this year | 0.9582 | How much did I spend on gas last year? | 0.8939 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9732 | How much did I get refunded from Shell last year? | 0.915 |
| How much did I earn this year? | How much did I earn last year? | 0.9276 | How much did I earn so far this year? | 0.8718 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9854 | What was my average purchase at Shell last year? | 0.9306 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9779 | How much more did I earn than I spent so far this year? | 0.9273 |
| Total spent on shopping this year | Total spent on shopping last year | 0.9506 | Total spent on shopping year to date | 0.9103 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9621 | How many transactions did I have at Starbucks last year? | 0.9236 |
