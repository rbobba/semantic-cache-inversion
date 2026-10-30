# vertex:text-embedding-004 holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9477 | 0.8801 | 0.9659 | 0.9932 | 0.9987 |
| **equivalent_surface (same wording=True)** | 370 | 0.9477 | 0.8801 | 0.9659 | 0.9932 | 0.9987 |
| **filter_change** | 37 | 0.7145 | 0.6383 | 0.7302 | 0.7818 | 0.8344 |
| **intent_near_miss** | 142 | 0.8224 | 0.6961 | 0.8294 | 0.9461 | 0.9857 |
| **intent_near_miss (same wording=False)** | 142 | 0.8224 | 0.6961 | 0.8294 | 0.9461 | 0.9857 |
| **param_near_miss** | 714 | 0.9112 | 0.8021 | 0.9315 | 0.9903 | 0.9983 |
| **param_near_miss (same wording=False)** | 255 | 0.8584 | 0.7622 | 0.8607 | 0.953 | 0.9793 |
| **param_near_miss (same wording=True)** | 459 | 0.9405 | 0.8568 | 0.9604 | 0.9936 | 0.9983 |
| **paraphrase** | 290 | 0.9043 | 0.8109 | 0.9212 | 0.9742 | 0.991 |
| equivalent_surface/amount/alias | 10 | 0.9651 | 0.9269 | 0.9762 | 0.9865 | 0.9887 |
| equivalent_surface/clinic/alias | 40 | 0.9231 | 0.8597 | 0.937 | 0.965 | 0.984 |
| equivalent_surface/department/alias | 30 | 0.9466 | 0.9283 | 0.9454 | 0.9661 | 0.9795 |
| equivalent_surface/n/alias | 20 | 0.9965 | 0.9945 | 0.997 | 0.9982 | 0.9987 |
| equivalent_surface/payer/alias | 2 | 0.9036 | 0.8988 | 0.9036 | 0.9083 | 0.9095 |
| equivalent_surface/period/alias | 268 | 0.9476 | 0.8802 | 0.9722 | 0.9928 | 0.9972 |
| filter_change/filter_added/clinic_visits | 7 | 0.7591 | 0.7086 | 0.7617 | 0.8077 | 0.8344 |
| filter_change/filter_dropped/total_visits | 30 | 0.704 | 0.6292 | 0.7091 | 0.7697 | 0.8128 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.842 | 0.8168 | 0.8496 | 0.8612 | 0.8762 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.838 | 0.8125 | 0.8266 | 0.8884 | 0.8984 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.8203 | 0.8098 | 0.8186 | 0.835 | 0.8448 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8325 | 0.8099 | 0.8414 | 0.8529 | 0.8604 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.888 | 0.8466 | 0.8799 | 0.9311 | 0.9412 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.8389 | 0.7412 | 0.7878 | 0.9599 | 0.9607 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9533 | 0.9318 | 0.9553 | 0.9828 | 0.9857 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9499 | 0.9333 | 0.9477 | 0.9665 | 0.9668 |
| intent_near_miss/grouping/top_departments | 10 | 0.6634 | 0.5726 | 0.6294 | 0.765 | 0.787 |
| intent_near_miss/grouping/top_providers | 10 | 0.7283 | 0.6974 | 0.7229 | 0.7658 | 0.7804 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.8277 | 0.8036 | 0.8303 | 0.8505 | 0.8668 |
| intent_near_miss/measure/dept_visits | 10 | 0.824 | 0.7996 | 0.8224 | 0.849 | 0.8518 |
| intent_near_miss/measure/total_no_shows | 7 | 0.7026 | 0.6638 | 0.7188 | 0.7328 | 0.7422 |
| intent_near_miss/measure/total_visits | 7 | 0.6605 | 0.628 | 0.662 | 0.691 | 0.7019 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8659 | 0.8269 | 0.8513 | 0.9281 | 0.9445 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8717 | 0.7967 | 0.8908 | 0.9271 | 0.9325 |
| param_near_miss/amount/neighbor | 27 | 0.9242 | 0.8341 | 0.9535 | 0.9824 | 0.9872 |
| param_near_miss/clinic/neighbor | 80 | 0.8706 | 0.7996 | 0.8788 | 0.9266 | 0.9659 |
| param_near_miss/department/neighbor | 60 | 0.801 | 0.7528 | 0.8043 | 0.8563 | 0.8785 |
| param_near_miss/n/neighbor | 47 | 0.9136 | 0.831 | 0.9455 | 0.9713 | 0.9822 |
| param_near_miss/payer/neighbor | 24 | 0.867 | 0.7935 | 0.8798 | 0.9293 | 0.9413 |
| param_near_miss/period/adjacent | 277 | 0.9365 | 0.8429 | 0.9615 | 0.9952 | 0.9983 |
| param_near_miss/period/granularity | 199 | 0.9283 | 0.8392 | 0.9522 | 0.9763 | 0.9878 |
| paraphrase/wording/template | 290 | 0.9043 | 0.8109 | 0.9212 | 0.9742 | 0.991 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.531 | [0.4552, 0.6138] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.531 | [0.4483, 0.6138] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.5172 | [0.4345, 0.6002] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0182 | [0.0, 0.0455] | 0.5 | [0.4091, 0.6] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.3259 | [0.2444, 0.4] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9379 | [0.8966, 0.9724] |
| B | 145 | 0.5793 | [0.5034, 0.6552] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0038 | [0.0, 0.0199] | 0.0038 | 0.0038 | 0.5534 |
| raw_oracle_entry | 0.2634 | [0.2357, 0.3139] | — | — | 0.5534 |
| split_full | 0.0134 | [0.004, 0.0274] | 0.0134 | 0.0134 | 0.5534 |
| split_template | 0.0744 | [0.0466, 0.106] | 0.0744 | 0.0744 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Visit count for Medicare patients last year | Visit count for Medicare patients this year | 0.981 | Visit count for Medicare patients in the previous year | 0.948 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9952 | How many visits were billed to Medicare in the previous month? | 0.9655 |
| How often did patients miss appointments last month? | How often did patients miss appointments this month? | 0.9958 | How often did patients miss appointments in the previous month? | 0.968 |
| Visits at every site but the Riverside clinic last month | Visits at every site but the Riverside clinic this month | 0.9847 | Visits at every site but the Riverside clinic in the previous month | 0.9591 |
| Visit count for cardiology last month | Visit count for cardiology this month | 0.9916 | Number of patient visits in cardiology last month | 0.9674 |
| Total missed appointments last month | Total missed appointments this month | 0.9926 | Total missed appointments in the previous month | 0.9691 |
| How many patient visits did we have last month? | How many patient visits did we have this month? | 0.9936 | How many patient visits did we have in the previous month? | 0.9721 |
| How many patient visits did physical therapy handle last month? | How many patient visits did physical therapy handle this month? | 0.9959 | How many patient visits did the physical therapy department handle last month? | 0.9748 |
| How many patient visits did family medicine handle last month? | How many patient visits did family medicine handle this month? | 0.9965 | How many patient visits did family medicine handle in the previous month? | 0.9759 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9878 | How many patient visits did we have in the previous year? | 0.9675 |
| Total missed appointments last year | Total missed appointments this year | 0.9883 | Total missed appointments in the previous year | 0.9687 |
| How many patient visits did pulmonology handle last year? | How many patient visits did pulmonology handle this year? | 0.9936 | How many patient visits did pulmonology handle in the previous year? | 0.9744 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9869 | What was our overall visit volume year to date? | 0.9687 |
| Number of incoming referrals at the Southgate clinic last month | Number of incoming referrals at the Southgate clinic this month | 0.9947 | Number of incoming referrals at the Southgate clinic in the previous month | 0.9773 |
| How long did patients wait on average last month? | How long did patients wait on average this month? | 0.9944 | How long did patients wait on average in the previous month? | 0.9772 |
