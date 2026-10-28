# st:Qwen/Qwen3-Embedding-0.6B

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9501 | 0.8567 | 0.9744 | 0.9918 | 0.9972 |
| **equivalent_surface (same wording=True)** | 262 | 0.9501 | 0.8567 | 0.9744 | 0.9918 | 0.9972 |
| **filter_change** | 37 | 0.7719 | 0.6583 | 0.7809 | 0.8785 | 0.9209 |
| **intent_near_miss** | 176 | 0.7914 | 0.6981 | 0.7996 | 0.8767 | 0.9567 |
| **intent_near_miss (same wording=False)** | 176 | 0.7914 | 0.6981 | 0.7996 | 0.8767 | 0.9567 |
| **param_near_miss** | 637 | 0.8752 | 0.7226 | 0.8922 | 0.9785 | 0.9941 |
| **param_near_miss (same wording=False)** | 228 | 0.7854 | 0.6677 | 0.7995 | 0.8822 | 0.9582 |
| **param_near_miss (same wording=True)** | 409 | 0.9253 | 0.8385 | 0.9409 | 0.9841 | 0.9941 |
| **paraphrase** | 384 | 0.844 | 0.7128 | 0.8616 | 0.9316 | 0.9729 |
| equivalent_surface/account/alias | 10 | 0.9622 | 0.9404 | 0.962 | 0.9819 | 0.9869 |
| equivalent_surface/amount/alias | 10 | 0.9874 | 0.9819 | 0.9886 | 0.9919 | 0.9947 |
| equivalent_surface/category/alias | 15 | 0.9713 | 0.9441 | 0.974 | 0.9901 | 0.9918 |
| equivalent_surface/merchant/alias | 12 | 0.9708 | 0.9398 | 0.9724 | 0.9932 | 0.9949 |
| equivalent_surface/n/alias | 20 | 0.9904 | 0.9843 | 0.9912 | 0.9947 | 0.9972 |
| equivalent_surface/period/alias | 195 | 0.9406 | 0.8406 | 0.9704 | 0.989 | 0.9967 |
| filter_change/filter_added/category_spend_total | 7 | 0.8412 | 0.7834 | 0.8372 | 0.9026 | 0.9209 |
| filter_change/filter_dropped/total_spend | 30 | 0.7557 | 0.6538 | 0.7513 | 0.8638 | 0.8878 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6881 | 0.6322 | 0.6868 | 0.7446 | 0.8107 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8157 | 0.7025 | 0.835 | 0.8937 | 0.9165 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8279 | 0.7628 | 0.8337 | 0.8787 | 0.9024 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8176 | 0.6935 | 0.825 | 0.9125 | 0.9567 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7232 | 0.6598 | 0.7038 | 0.8192 | 0.8299 |
| intent_near_miss/direction/income_total | 7 | 0.7678 | 0.7177 | 0.77 | 0.8208 | 0.8491 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8407 | 0.7901 | 0.8536 | 0.8826 | 0.9002 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8127 | 0.7687 | 0.8102 | 0.8607 | 0.8732 |
| intent_near_miss/direction/total_spend | 7 | 0.7769 | 0.7308 | 0.7859 | 0.8124 | 0.8285 |
| intent_near_miss/grouping/top_categories | 10 | 0.7646 | 0.6941 | 0.8042 | 0.8198 | 0.8206 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7519 | 0.652 | 0.789 | 0.8046 | 0.8046 |
| intent_near_miss/measure/income_total | 7 | 0.759 | 0.7208 | 0.7553 | 0.8064 | 0.8236 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7384 | 0.6871 | 0.7384 | 0.7655 | 0.8541 |
| intent_near_miss/measure/total_spend | 7 | 0.7511 | 0.7 | 0.7544 | 0.8003 | 0.808 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8613 | 0.8353 | 0.8647 | 0.9137 | 0.9172 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8145 | 0.7499 | 0.8222 | 0.8779 | 0.8912 |
| param_near_miss/account/neighbor | 20 | 0.8239 | 0.7316 | 0.8335 | 0.9133 | 0.9189 |
| param_near_miss/amount/neighbor | 25 | 0.8504 | 0.6498 | 0.9475 | 0.9811 | 0.9941 |
| param_near_miss/category/neighbor | 45 | 0.873 | 0.7884 | 0.8857 | 0.9458 | 0.9778 |
| param_near_miss/merchant/neighbor | 87 | 0.7689 | 0.6748 | 0.7834 | 0.8537 | 0.874 |
| param_near_miss/n/neighbor | 45 | 0.9062 | 0.7681 | 0.9652 | 0.9849 | 0.9919 |
| param_near_miss/period/adjacent | 230 | 0.8914 | 0.7474 | 0.9168 | 0.9851 | 0.9926 |
| param_near_miss/period/granularity | 185 | 0.9069 | 0.8337 | 0.9238 | 0.9578 | 0.9782 |
| paraphrase/wording/template | 384 | 0.844 | 0.7128 | 0.8616 | 0.9316 | 0.9729 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.2188 | [0.1484, 0.2891] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.2188 | [0.1562, 0.2969] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.2109 | [0.1406, 0.2812] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.72 | [0.63, 0.81] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.4915 | [0.3983, 0.5763] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0106 | [0.0056, 0.0263] | 0.0106 | 0.0187 | 0.5317 |
| raw_oracle_entry | 0.1122 | [0.103, 0.1378] | — | — | 0.5317 |
| split_full | 0.2154 | [0.2016, 0.2295] | 0.2154 | 0.3163 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.9351 | What was my total income last year? | 0.8204 |
| Income minus expenses last year | Income minus expenses this year | 0.9431 | Income minus expenses during 2025 | 0.8385 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9847 | How much did I spend per transaction at Walmart during 2025, on average? | 0.8977 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9776 | How much money did Spotify give back to me in 2025? | 0.8963 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9646 | What was my total spending last year? | 0.8928 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9839 | Average transaction amount at Uber during 2025 | 0.9271 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9765 | What was my average purchase at Shell last year? | 0.9201 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9851 | Total refunds from Shell during 2025 | 0.9341 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9905 | Count my transactions at Starbucks in 2025 | 0.9437 |
| Total spent on gas last year | Total spent on gas this year | 0.967 | Total spent on fuel last year | 0.9265 |
| On average, how much did each purchase at Trader Joe's cost last year? | On average, how much did each purchase at Trader Joe's cost this year? | 0.9741 | On average, how much did each purchase at Trader Joes cost last year? | 0.9383 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9633 | What was my largest purchase last year? | 0.9283 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9567 | What did I pay Starbucks in total last year? | 0.93 |
| What was my total spending last month? | What was my total spending this month? | 0.9804 | What was my total spending in the previous month? | 0.9635 |
| How much money went to Whole Foods this week? | How much money went to Whole Foods last week? | 0.9793 | How much money went to Whole Foods so far this week? | 0.9731 |
