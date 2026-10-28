# tfidf

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.6637 | 0.518 | 0.6779 | 0.7711 | 0.8304 |
| **equivalent_surface (same wording=True)** | 262 | 0.6637 | 0.518 | 0.6779 | 0.7711 | 0.8304 |
| **filter_change** | 37 | 0.2401 | 0.1227 | 0.2116 | 0.3922 | 0.6107 |
| **intent_near_miss** | 176 | 0.3232 | 0.1168 | 0.3202 | 0.5305 | 0.7287 |
| **intent_near_miss (same wording=False)** | 176 | 0.3232 | 0.1168 | 0.3202 | 0.5305 | 0.7287 |
| **param_near_miss** | 637 | 0.5433 | 0.1152 | 0.6509 | 0.8472 | 0.9539 |
| **param_near_miss (same wording=False)** | 228 | 0.1973 | 0.0768 | 0.1718 | 0.3601 | 0.5904 |
| **param_near_miss (same wording=True)** | 409 | 0.7362 | 0.5781 | 0.744 | 0.8676 | 0.9539 |
| **paraphrase** | 384 | 0.3486 | 0.1436 | 0.3237 | 0.5805 | 0.7614 |
| equivalent_surface/account/alias | 10 | 0.6891 | 0.5679 | 0.7286 | 0.7823 | 0.7884 |
| equivalent_surface/amount/alias | 10 | 0.5047 | 0.4347 | 0.5001 | 0.6153 | 0.6402 |
| equivalent_surface/category/alias | 15 | 0.5222 | 0.4276 | 0.5168 | 0.6412 | 0.6419 |
| equivalent_surface/merchant/alias | 12 | 0.6877 | 0.6013 | 0.7138 | 0.7539 | 0.8153 |
| equivalent_surface/n/alias | 20 | 0.6535 | 0.5971 | 0.6468 | 0.7205 | 0.7425 |
| equivalent_surface/period/alias | 195 | 0.681 | 0.5628 | 0.6917 | 0.7753 | 0.8304 |
| filter_change/filter_added/category_spend_total | 7 | 0.278 | 0.1294 | 0.175 | 0.4649 | 0.5788 |
| filter_change/filter_dropped/total_spend | 30 | 0.2313 | 0.115 | 0.2133 | 0.3754 | 0.6107 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.2216 | 0.1288 | 0.2016 | 0.3272 | 0.3649 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.3898 | 0.2504 | 0.4123 | 0.5047 | 0.6582 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.4231 | 0.191 | 0.4333 | 0.5795 | 0.662 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.4102 | 0.2778 | 0.3963 | 0.5609 | 0.7029 |
| intent_near_miss/aggregation/total_spend | 7 | 0.177 | 0.095 | 0.117 | 0.3395 | 0.4397 |
| intent_near_miss/direction/income_total | 7 | 0.2527 | 0.1078 | 0.1738 | 0.4466 | 0.5208 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.4008 | 0.3262 | 0.4154 | 0.4851 | 0.5068 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.3189 | 0.1524 | 0.3573 | 0.4152 | 0.4685 |
| intent_near_miss/direction/total_spend | 7 | 0.2387 | 0.1116 | 0.1792 | 0.3958 | 0.4451 |
| intent_near_miss/grouping/top_categories | 10 | 0.2726 | 0.134 | 0.1993 | 0.5897 | 0.6416 |
| intent_near_miss/grouping/top_merchants | 10 | 0.3001 | 0.1265 | 0.2424 | 0.5686 | 0.5737 |
| intent_near_miss/measure/income_total | 7 | 0.2021 | 0.0871 | 0.224 | 0.3268 | 0.4314 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.1783 | 0.0823 | 0.1558 | 0.3028 | 0.3139 |
| intent_near_miss/measure/total_spend | 7 | 0.2276 | 0.1135 | 0.1955 | 0.3793 | 0.4962 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.4202 | 0.2878 | 0.3695 | 0.6884 | 0.7287 |
| intent_near_miss/negation/category_spend_total | 10 | 0.3558 | 0.1949 | 0.3824 | 0.4303 | 0.4561 |
| param_near_miss/account/neighbor | 20 | 0.5454 | 0.3199 | 0.5532 | 0.7455 | 0.7615 |
| param_near_miss/amount/neighbor | 25 | 0.3992 | 0.0793 | 0.5219 | 0.6317 | 0.7358 |
| param_near_miss/category/neighbor | 45 | 0.412 | 0.1084 | 0.474 | 0.6499 | 0.7995 |
| param_near_miss/merchant/neighbor | 87 | 0.4263 | 0.1047 | 0.5241 | 0.7207 | 0.7677 |
| param_near_miss/n/neighbor | 45 | 0.4821 | 0.1211 | 0.675 | 0.7591 | 0.8055 |
| param_near_miss/period/adjacent | 230 | 0.5085 | 0.1036 | 0.6529 | 0.8293 | 0.8793 |
| param_near_miss/period/granularity | 185 | 0.7077 | 0.4338 | 0.7539 | 0.9273 | 0.9539 |
| paraphrase/wording/template | 384 | 0.3486 | 0.1436 | 0.3237 | 0.5805 | 0.7614 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.9922 | [0.9766, 1.0] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.9922 | [0.9766, 1.0] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.9922 | [0.9766, 1.0] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.23 | [0.15, 0.31] | 1.0 | [1.0, 1.0] |
| intent_near_miss | 118 | 0.0169 | [0.0, 0.0424] | 0.7627 | [0.6864, 0.839] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.5317 |
| raw_oracle_entry | 0.0024 | [0.0008, 0.0106] | — | — | 0.5317 |
| split_full | 0.2252 | [0.2101, 0.2422] | 0.2309 | 0.2374 | 0.5317 |
| split_template | 0.952 | [0.9373, 0.965] | 0.952 | 0.9569 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much did I earn in the last 3 months? | How much did I earn in the last 6 months? | 0.7503 | How much income did I receive in the last 3 months? | 0.4043 |
| Largest charge this week | Largest charge this month | 0.8838 | Largest charge so far this week | 0.5573 |
| Total expenses this month | Total expenses this week | 0.8444 | Total expenses so far this month | 0.5251 |
| What was my largest purchase in the last 3 months? | What was my largest purchase in the last 6 months? | 0.8029 | What was my largest purchase over the past three months? | 0.4991 |
| What was my total spending in the last 3 months? | What was my total spending in the last 6 months? | 0.7261 | Total expenses in the last 3 months | 0.4446 |
| How much money went to Lyft in the last 3 months? | How much money went to Lyft in the last 6 months? | 0.8175 | How much did I spend at Lyft in the last 3 months? | 0.5536 |
| How much money went to Target in the last 3 months? | How much money went to Target in the last 6 months? | 0.8045 | How much did I spend at Target in the last 3 months? | 0.5445 |
| How much money went to shopping in the last 3 months? | How much money went to shopping in the last 6 months? | 0.8076 | How much did I spend on shopping in the last 3 months? | 0.5536 |
| How much did I spend in the last 3 months excluding travel? | How much did I spend in the last 6 months excluding travel? | 0.822 | How much did I spend over the past three months excluding travel? | 0.5709 |
| What did I pay Spotify in total in the last 3 months? | What did I pay Spotify in total in the last 6 months? | 0.8372 | What did I pay Spotify in total over the past three months? | 0.5873 |
| Total spent at Target this week | Total spent at Target this month | 0.8917 | Total spent at Target so far this week | 0.6525 |
| How much did I spend on groceries this month? | How much did I spend on groceries this week? | 0.9009 | How much did I spend on groceries so far this month? | 0.6635 |
| What was my total spending this week? | What was my total spending this month? | 0.8654 | What was my total spending so far this week? | 0.6336 |
| Show my 10 biggest merchants this month | Show my 10 biggest merchants this week | 0.921 | Show my 10 biggest merchants so far this month | 0.6902 |
| Any spending above $200 this month? | Any spending above $200 this week? | 0.9115 | Any spending above $200 so far this month? | 0.6853 |
