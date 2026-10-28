# st:intfloat/e5-base-v2 prefix='query: '

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9757 | 0.9288 | 0.9901 | 0.9973 | 0.9993 |
| **equivalent_surface (same wording=True)** | 262 | 0.9757 | 0.9288 | 0.9901 | 0.9973 | 0.9993 |
| **filter_change** | 37 | 0.899 | 0.8679 | 0.8922 | 0.9336 | 0.9632 |
| **intent_near_miss** | 176 | 0.9222 | 0.873 | 0.9263 | 0.9605 | 0.9747 |
| **intent_near_miss (same wording=False)** | 176 | 0.9222 | 0.873 | 0.9263 | 0.9605 | 0.9747 |
| **param_near_miss** | 637 | 0.9463 | 0.888 | 0.9529 | 0.9953 | 0.9985 |
| **param_near_miss (same wording=False)** | 228 | 0.9101 | 0.8629 | 0.9142 | 0.949 | 0.9868 |
| **param_near_miss (same wording=True)** | 409 | 0.9666 | 0.9359 | 0.969 | 0.997 | 0.9985 |
| **paraphrase** | 384 | 0.933 | 0.8817 | 0.9381 | 0.9726 | 0.9942 |
| equivalent_surface/account/alias | 10 | 0.9835 | 0.978 | 0.9841 | 0.9931 | 0.9931 |
| equivalent_surface/amount/alias | 10 | 0.9951 | 0.9938 | 0.995 | 0.9965 | 0.9967 |
| equivalent_surface/category/alias | 15 | 0.9846 | 0.9754 | 0.9881 | 0.9925 | 0.9939 |
| equivalent_surface/merchant/alias | 12 | 0.9934 | 0.9903 | 0.9946 | 0.9988 | 0.9991 |
| equivalent_surface/n/alias | 20 | 0.9983 | 0.9968 | 0.9984 | 0.999 | 0.9993 |
| equivalent_surface/period/alias | 195 | 0.9702 | 0.9225 | 0.9881 | 0.9959 | 0.9982 |
| filter_change/filter_added/category_spend_total | 7 | 0.9122 | 0.8727 | 0.9206 | 0.9492 | 0.9632 |
| filter_change/filter_dropped/total_spend | 30 | 0.8959 | 0.868 | 0.8915 | 0.9234 | 0.9495 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.878 | 0.829 | 0.8909 | 0.9146 | 0.9313 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.9368 | 0.9051 | 0.9365 | 0.9654 | 0.9712 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.9329 | 0.9127 | 0.9344 | 0.954 | 0.9661 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.9323 | 0.9011 | 0.9321 | 0.9577 | 0.9743 |
| intent_near_miss/aggregation/total_spend | 7 | 0.8931 | 0.8396 | 0.9011 | 0.9366 | 0.9434 |
| intent_near_miss/direction/income_total | 7 | 0.9142 | 0.8679 | 0.9324 | 0.9532 | 0.9585 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.9436 | 0.9175 | 0.9531 | 0.9657 | 0.9676 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.9471 | 0.9141 | 0.9543 | 0.9653 | 0.9665 |
| intent_near_miss/direction/total_spend | 7 | 0.9246 | 0.8916 | 0.9299 | 0.9508 | 0.9531 |
| intent_near_miss/grouping/top_categories | 10 | 0.9011 | 0.8696 | 0.9124 | 0.9225 | 0.9276 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8999 | 0.8512 | 0.9086 | 0.9252 | 0.9437 |
| intent_near_miss/measure/income_total | 7 | 0.9106 | 0.8756 | 0.9005 | 0.9545 | 0.9658 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.9087 | 0.8604 | 0.9146 | 0.9544 | 0.961 |
| intent_near_miss/measure/total_spend | 7 | 0.9006 | 0.8684 | 0.8885 | 0.9387 | 0.9573 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.938 | 0.912 | 0.9306 | 0.969 | 0.9747 |
| intent_near_miss/negation/category_spend_total | 10 | 0.9298 | 0.9111 | 0.9303 | 0.9521 | 0.9532 |
| param_near_miss/account/neighbor | 20 | 0.9449 | 0.8986 | 0.9565 | 0.9758 | 0.9784 |
| param_near_miss/amount/neighbor | 25 | 0.9251 | 0.8479 | 0.9577 | 0.9698 | 0.9772 |
| param_near_miss/category/neighbor | 45 | 0.9318 | 0.8885 | 0.9374 | 0.9681 | 0.9869 |
| param_near_miss/merchant/neighbor | 87 | 0.9194 | 0.8743 | 0.9291 | 0.953 | 0.969 |
| param_near_miss/n/neighbor | 45 | 0.9554 | 0.8976 | 0.9818 | 0.9906 | 0.993 |
| param_near_miss/period/adjacent | 230 | 0.9561 | 0.9033 | 0.9648 | 0.9977 | 0.9985 |
| param_near_miss/period/granularity | 185 | 0.9513 | 0.9096 | 0.9604 | 0.9766 | 0.9879 |
| paraphrase/wording/template | 384 | 0.933 | 0.8817 | 0.9381 | 0.9726 | 0.9942 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5469 | [0.4609, 0.6328] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5469 | [0.4609, 0.6406] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5469 | [0.4686, 0.6328] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.88 | [0.82, 0.94] |
| intent_near_miss | 118 | 0.0169 | [0.0, 0.0426] | 0.6525 | [0.5678, 0.7373] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0089 | [0.0047, 0.0148] | 0.0089 | 0.0089 | 0.5317 |
| raw_oracle_entry | 0.0813 | [0.0692, 0.1096] | — | — | 0.5317 |
| split_full | 0.2138 | [0.2, 0.2298] | 0.2138 | 0.2382 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.9888 | Total money coming in in 2025 | 0.9038 |
| Income minus expenses last year | Income minus expenses this year | 0.9922 | Income minus expenses in 2025 | 0.9182 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9966 | How much did I spend per transaction at Uber last year, on average? | 0.9475 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9928 | How much did I get refunded from Shell last year? | 0.9491 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9974 | What was my average purchase at Shell last year? | 0.956 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9976 | How much did I get refunded from Spotify last year? | 0.9616 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9985 | What was my average purchase at Walmart last year? | 0.964 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9959 | What was my largest purchase last year? | 0.9616 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9911 | How many transactions did I have at Starbucks last year? | 0.9581 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9974 | What did I pay Starbucks in total last year? | 0.9681 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9952 | What was my total spending last year? | 0.9674 |
| Total spent on gas last year | Total spent on gas this year | 0.9942 | Total spent on fuel last year | 0.9723 |
| How much did I earn this year? | How much did I earn last year? | 0.9931 | How much did I earn so far this year? | 0.9865 |
| Total expenses this month | Total expenses last month | 0.9921 | Total expenses so far this month | 0.9858 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9967 | How much income did I receive so far this week? | 0.9907 |
