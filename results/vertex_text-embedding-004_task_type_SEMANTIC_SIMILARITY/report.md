# vertex:text-embedding-004 task_type=SEMANTIC_SIMILARITY

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9656 | 0.9061 | 0.9851 | 0.996 | 0.999 |
| **equivalent_surface (same wording=True)** | 262 | 0.9656 | 0.9061 | 0.9851 | 0.996 | 0.999 |
| **filter_change** | 37 | 0.8212 | 0.7641 | 0.8235 | 0.8794 | 0.9193 |
| **intent_near_miss** | 176 | 0.8347 | 0.7548 | 0.8456 | 0.8932 | 0.9417 |
| **intent_near_miss (same wording=False)** | 176 | 0.8347 | 0.7548 | 0.8456 | 0.8932 | 0.9417 |
| **param_near_miss** | 637 | 0.9034 | 0.7983 | 0.9171 | 0.9889 | 0.998 |
| **param_near_miss (same wording=False)** | 228 | 0.84 | 0.7541 | 0.8436 | 0.9187 | 0.9774 |
| **param_near_miss (same wording=True)** | 409 | 0.9387 | 0.8891 | 0.9412 | 0.9929 | 0.998 |
| **paraphrase** | 384 | 0.8866 | 0.7938 | 0.8988 | 0.9589 | 0.9889 |
| equivalent_surface/account/alias | 10 | 0.9738 | 0.9537 | 0.9756 | 0.9891 | 0.9913 |
| equivalent_surface/amount/alias | 10 | 0.9928 | 0.9909 | 0.9933 | 0.9948 | 0.9948 |
| equivalent_surface/category/alias | 15 | 0.982 | 0.9657 | 0.9892 | 0.9929 | 0.9932 |
| equivalent_surface/merchant/alias | 12 | 0.9945 | 0.9893 | 0.995 | 0.9984 | 0.9986 |
| equivalent_surface/n/alias | 20 | 0.9971 | 0.9948 | 0.998 | 0.9986 | 0.999 |
| equivalent_surface/period/alias | 195 | 0.9575 | 0.894 | 0.9811 | 0.9942 | 0.9981 |
| filter_change/filter_added/category_spend_total | 7 | 0.8558 | 0.8039 | 0.8485 | 0.912 | 0.9193 |
| filter_change/filter_dropped/total_spend | 30 | 0.8131 | 0.7631 | 0.8075 | 0.8787 | 0.8944 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7857 | 0.724 | 0.7696 | 0.8495 | 0.864 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8598 | 0.7771 | 0.8706 | 0.9063 | 0.9417 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8674 | 0.8148 | 0.8724 | 0.9157 | 0.932 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8505 | 0.7966 | 0.8466 | 0.9067 | 0.9337 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7649 | 0.7029 | 0.7553 | 0.8438 | 0.8724 |
| intent_near_miss/direction/income_total | 7 | 0.804 | 0.7239 | 0.8318 | 0.87 | 0.8736 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8312 | 0.7896 | 0.8442 | 0.8841 | 0.8902 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8335 | 0.762 | 0.8385 | 0.8795 | 0.8921 |
| intent_near_miss/direction/total_spend | 7 | 0.8116 | 0.7671 | 0.8282 | 0.8467 | 0.8473 |
| intent_near_miss/grouping/top_categories | 10 | 0.8358 | 0.7577 | 0.8556 | 0.8893 | 0.8994 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8446 | 0.8065 | 0.8418 | 0.8837 | 0.8904 |
| intent_near_miss/measure/income_total | 7 | 0.7978 | 0.7351 | 0.7861 | 0.8699 | 0.8797 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.8046 | 0.7357 | 0.8108 | 0.8696 | 0.8741 |
| intent_near_miss/measure/total_spend | 7 | 0.7983 | 0.7421 | 0.8114 | 0.8401 | 0.8741 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8709 | 0.8402 | 0.8724 | 0.9111 | 0.9332 |
| intent_near_miss/negation/category_spend_total | 10 | 0.859 | 0.8347 | 0.8591 | 0.8786 | 0.8906 |
| param_near_miss/account/neighbor | 20 | 0.8612 | 0.7842 | 0.8682 | 0.9424 | 0.9492 |
| param_near_miss/amount/neighbor | 25 | 0.8662 | 0.7678 | 0.9136 | 0.9468 | 0.9673 |
| param_near_miss/category/neighbor | 45 | 0.8868 | 0.8093 | 0.8914 | 0.9597 | 0.9901 |
| param_near_miss/merchant/neighbor | 87 | 0.8504 | 0.7657 | 0.8639 | 0.9206 | 0.9357 |
| param_near_miss/n/neighbor | 45 | 0.8914 | 0.8225 | 0.9129 | 0.9509 | 0.9638 |
| param_near_miss/period/adjacent | 230 | 0.926 | 0.8224 | 0.9478 | 0.9949 | 0.998 |
| param_near_miss/period/granularity | 185 | 0.9167 | 0.8509 | 0.9324 | 0.9623 | 0.9771 |
| paraphrase/wording/template | 384 | 0.8866 | 0.7938 | 0.8988 | 0.9589 | 0.9889 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4844 | [0.3984, 0.5781] | 0.9766 | [0.9453, 1.0] |
| param_near_miss | 128 | 0.4844 | [0.3984, 0.5781] | 0.9766 | [0.9531, 1.0] |
| period_near_miss | 128 | 0.4844 | [0.3984, 0.5703] | 0.9766 | [0.9453, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.88 | [0.82, 0.94] |
| intent_near_miss | 118 | 0.0085 | [0.0, 0.0254] | 0.3983 | [0.3136, 0.4915] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0114 | [0.0057, 0.0194] | 0.0114 | 0.0114 | 0.5317 |
| raw_oracle_entry | 0.1098 | [0.0949, 0.142] | — | — | 0.5317 |
| split_full | 0.2732 | [0.256, 0.291] | 0.2732 | 0.3081 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9625 | Income minus expenses during 2025 | 0.8331 |
| Total money coming in last year | Total money coming in this year | 0.9268 | Total money coming in during 2025 | 0.8235 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9928 | Average transaction amount at Uber during 2025 | 0.9291 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9933 | Total refunds from Shell in 2025 | 0.9367 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9917 | How much money did Spotify give back to me during 2025? | 0.9385 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9923 | On average, how much did each purchase at Shell cost during 2025? | 0.9396 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9831 | What was my total spending last year? | 0.9388 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9954 | How much did I spend per transaction at Walmart during 2025, on average? | 0.9514 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9848 | What did I pay Starbucks in total last year? | 0.9411 |
| Total spent on gas last year | Total spent on gas this year | 0.9843 | How much money went to gas last year? | 0.9444 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9865 | How many transactions did I have at Starbucks last year? | 0.9489 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9909 | What was my largest purchase last year? | 0.9655 |
| How much did I earn this year? | How much did I earn last year? | 0.9801 | How much income did I receive this year? | 0.9588 |
| How much income did I receive this month? | How much income did I receive last month? | 0.9889 | How much income did I receive so far this month? | 0.9702 |
| Total spent on everything but entertainment this year | Total spent on everything but entertainment last year | 0.9843 | Total spent on everything but entertainment so far this year | 0.9676 |
