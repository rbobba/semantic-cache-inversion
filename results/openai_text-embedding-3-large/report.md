# openai:text-embedding-3-large

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9272 | 0.8328 | 0.9564 | 0.984 | 0.9957 |
| **equivalent_surface (same wording=True)** | 262 | 0.9272 | 0.8328 | 0.9564 | 0.984 | 0.9957 |
| **filter_change** | 37 | 0.6635 | 0.591 | 0.6475 | 0.7566 | 0.8818 |
| **intent_near_miss** | 176 | 0.7113 | 0.5751 | 0.7231 | 0.8101 | 0.912 |
| **intent_near_miss (same wording=False)** | 176 | 0.7113 | 0.5751 | 0.7231 | 0.8101 | 0.912 |
| **param_near_miss** | 637 | 0.8285 | 0.6521 | 0.8552 | 0.9658 | 0.9871 |
| **param_near_miss (same wording=False)** | 228 | 0.7101 | 0.5863 | 0.7156 | 0.8322 | 0.9351 |
| **param_near_miss (same wording=True)** | 409 | 0.8945 | 0.7913 | 0.9086 | 0.9739 | 0.9871 |
| **paraphrase** | 384 | 0.7826 | 0.6463 | 0.8047 | 0.9005 | 0.9664 |
| equivalent_surface/account/alias | 10 | 0.967 | 0.9487 | 0.9671 | 0.9831 | 0.9842 |
| equivalent_surface/amount/alias | 10 | 0.9704 | 0.9594 | 0.9744 | 0.9773 | 0.978 |
| equivalent_surface/category/alias | 15 | 0.9498 | 0.9133 | 0.9636 | 0.975 | 0.9787 |
| equivalent_surface/merchant/alias | 12 | 0.9828 | 0.9812 | 0.9835 | 0.9867 | 0.9882 |
| equivalent_surface/n/alias | 20 | 0.9891 | 0.9846 | 0.9892 | 0.9932 | 0.9957 |
| equivalent_surface/period/alias | 195 | 0.9115 | 0.8115 | 0.9453 | 0.975 | 0.9867 |
| filter_change/filter_added/category_spend_total | 7 | 0.7145 | 0.5983 | 0.6992 | 0.8234 | 0.8818 |
| filter_change/filter_dropped/total_spend | 30 | 0.6516 | 0.5923 | 0.6421 | 0.75 | 0.7967 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5689 | 0.4757 | 0.5785 | 0.6487 | 0.6859 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7544 | 0.6592 | 0.7589 | 0.824 | 0.8609 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7657 | 0.668 | 0.7645 | 0.8504 | 0.8716 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7556 | 0.684 | 0.757 | 0.8269 | 0.8863 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5828 | 0.4713 | 0.5785 | 0.6868 | 0.7855 |
| intent_near_miss/direction/income_total | 7 | 0.6627 | 0.549 | 0.654 | 0.7805 | 0.7988 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7784 | 0.7162 | 0.7929 | 0.8172 | 0.8532 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7603 | 0.6969 | 0.7765 | 0.7915 | 0.8029 |
| intent_near_miss/direction/total_spend | 7 | 0.6574 | 0.5844 | 0.6641 | 0.7213 | 0.7333 |
| intent_near_miss/grouping/top_categories | 10 | 0.6856 | 0.5501 | 0.7154 | 0.7653 | 0.7996 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7022 | 0.6152 | 0.7071 | 0.7917 | 0.8006 |
| intent_near_miss/measure/income_total | 7 | 0.6392 | 0.5344 | 0.6599 | 0.7149 | 0.7609 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6422 | 0.5459 | 0.6643 | 0.7149 | 0.7996 |
| intent_near_miss/measure/total_spend | 7 | 0.6435 | 0.5633 | 0.6228 | 0.7392 | 0.7426 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.7803 | 0.7015 | 0.777 | 0.8774 | 0.912 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7337 | 0.6998 | 0.7331 | 0.7812 | 0.8034 |
| param_near_miss/account/neighbor | 20 | 0.7833 | 0.656 | 0.7997 | 0.8971 | 0.9175 |
| param_near_miss/amount/neighbor | 25 | 0.803 | 0.5932 | 0.9014 | 0.9367 | 0.9509 |
| param_near_miss/category/neighbor | 45 | 0.7755 | 0.6503 | 0.7869 | 0.8768 | 0.9339 |
| param_near_miss/merchant/neighbor | 87 | 0.7481 | 0.614 | 0.7629 | 0.8657 | 0.8937 |
| param_near_miss/n/neighbor | 45 | 0.8125 | 0.6349 | 0.8846 | 0.946 | 0.9543 |
| param_near_miss/period/adjacent | 230 | 0.8539 | 0.6573 | 0.8858 | 0.9772 | 0.9871 |
| param_near_miss/period/granularity | 185 | 0.8598 | 0.727 | 0.894 | 0.9454 | 0.9778 |
| paraphrase/wording/template | 384 | 0.7826 | 0.6463 | 0.8047 | 0.9005 | 0.9664 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4141 | [0.3281, 0.5] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.4141 | [0.3281, 0.5078] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.4141 | [0.3359, 0.5] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.85 | [0.78, 0.92] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.4915 | [0.4068, 0.5765] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0122 | [0.0072, 0.0208] | 0.0122 | 0.0122 | 0.5317 |
| raw_oracle_entry | 0.0976 | [0.087, 0.1256] | — | — | 0.5317 |
| split_full | 0.2252 | [0.2104, 0.24] | 0.2252 | 0.3041 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.8877 | Total money coming in during 2025 | 0.6862 |
| Income minus expenses last year | Income minus expenses this year | 0.9336 | Income minus expenses during 2025 | 0.7608 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9515 | What was my total spending last year? | 0.845 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9557 | Total refunds from Shell during 2025 | 0.8569 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9608 | What was my largest purchase last year? | 0.8648 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9829 | How much money did Spotify give back to me during 2025? | 0.8942 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9545 | Average transaction amount at Uber during 2025 | 0.8686 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.987 | How much did I spend per transaction at Walmart during 2025, on average? | 0.9013 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9725 | How many transactions did I have at Starbucks last year? | 0.8912 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9781 | What was my average purchase at Shell last year? | 0.9075 |
| How much income did I receive this month? | How much income did I receive last month? | 0.9632 | How much income did I receive so far this month? | 0.8945 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9767 | What did I pay Starbucks in total last year? | 0.9093 |
| How much did I earn this year? | How much did I earn last year? | 0.923 | How much did I earn so far this year? | 0.8659 |
| Total expenses this month | Total expenses last month | 0.9115 | Total expenses so far this month | 0.8654 |
| Sum of my purchases at Home Depot last month | Sum of my purchases at Home Depot this month | 0.9769 | Sum of my purchases at Home Depot in the previous month | 0.9316 |
