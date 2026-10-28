# st:mixedbread-ai/mxbai-embed-large-v1

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.94 | 0.8181 | 0.9761 | 0.992 | 0.9975 |
| **equivalent_surface (same wording=True)** | 262 | 0.94 | 0.8181 | 0.9761 | 0.992 | 0.9975 |
| **filter_change** | 37 | 0.7828 | 0.7133 | 0.7767 | 0.8562 | 0.9169 |
| **intent_near_miss** | 176 | 0.8284 | 0.7488 | 0.8424 | 0.8952 | 0.9403 |
| **intent_near_miss (same wording=False)** | 176 | 0.8284 | 0.7488 | 0.8424 | 0.8952 | 0.9403 |
| **param_near_miss** | 637 | 0.8722 | 0.7516 | 0.8845 | 0.9867 | 0.9962 |
| **param_near_miss (same wording=False)** | 228 | 0.8041 | 0.7117 | 0.8092 | 0.8986 | 0.9742 |
| **param_near_miss (same wording=True)** | 409 | 0.9101 | 0.8296 | 0.915 | 0.9892 | 0.9962 |
| **paraphrase** | 384 | 0.8649 | 0.7664 | 0.8807 | 0.9405 | 0.9811 |
| equivalent_surface/account/alias | 10 | 0.9656 | 0.9406 | 0.9754 | 0.98 | 0.9822 |
| equivalent_surface/amount/alias | 10 | 0.9843 | 0.9747 | 0.9866 | 0.9919 | 0.9936 |
| equivalent_surface/category/alias | 15 | 0.965 | 0.9434 | 0.9709 | 0.9816 | 0.9872 |
| equivalent_surface/merchant/alias | 12 | 0.9853 | 0.9725 | 0.99 | 0.9948 | 0.9957 |
| equivalent_surface/n/alias | 20 | 0.9951 | 0.9924 | 0.9958 | 0.997 | 0.9975 |
| equivalent_surface/period/alias | 195 | 0.926 | 0.8066 | 0.974 | 0.9861 | 0.9924 |
| filter_change/filter_added/category_spend_total | 7 | 0.818 | 0.7567 | 0.7944 | 0.8996 | 0.9169 |
| filter_change/filter_dropped/total_spend | 30 | 0.7746 | 0.7019 | 0.7764 | 0.8319 | 0.874 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7538 | 0.6815 | 0.7419 | 0.818 | 0.8304 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8543 | 0.8001 | 0.8591 | 0.9084 | 0.9403 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8638 | 0.8157 | 0.8579 | 0.9119 | 0.9377 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8314 | 0.7622 | 0.8484 | 0.8936 | 0.9021 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7579 | 0.6803 | 0.7617 | 0.8384 | 0.8506 |
| intent_near_miss/direction/income_total | 7 | 0.799 | 0.7462 | 0.7986 | 0.8494 | 0.8499 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8578 | 0.7911 | 0.864 | 0.9091 | 0.9141 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8524 | 0.807 | 0.858 | 0.8869 | 0.8969 |
| intent_near_miss/direction/total_spend | 7 | 0.8143 | 0.7823 | 0.8255 | 0.8355 | 0.8405 |
| intent_near_miss/grouping/top_categories | 10 | 0.8231 | 0.7737 | 0.847 | 0.8598 | 0.879 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8157 | 0.7366 | 0.8464 | 0.8551 | 0.8734 |
| intent_near_miss/measure/income_total | 7 | 0.8169 | 0.7642 | 0.8318 | 0.8736 | 0.9011 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7859 | 0.7384 | 0.7864 | 0.851 | 0.8624 |
| intent_near_miss/measure/total_spend | 7 | 0.7914 | 0.7532 | 0.7674 | 0.86 | 0.8723 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8806 | 0.8497 | 0.8793 | 0.9173 | 0.9363 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8375 | 0.801 | 0.8516 | 0.8777 | 0.8902 |
| param_near_miss/account/neighbor | 20 | 0.8532 | 0.7714 | 0.8625 | 0.9291 | 0.9406 |
| param_near_miss/amount/neighbor | 25 | 0.8222 | 0.6867 | 0.8336 | 0.9415 | 0.974 |
| param_near_miss/category/neighbor | 45 | 0.8517 | 0.759 | 0.8607 | 0.938 | 0.9808 |
| param_near_miss/merchant/neighbor | 87 | 0.8105 | 0.7271 | 0.8238 | 0.8933 | 0.9419 |
| param_near_miss/n/neighbor | 45 | 0.876 | 0.7528 | 0.9072 | 0.9642 | 0.9693 |
| param_near_miss/period/adjacent | 230 | 0.9059 | 0.7828 | 0.9288 | 0.9917 | 0.9962 |
| param_near_miss/period/granularity | 185 | 0.872 | 0.7808 | 0.892 | 0.9372 | 0.9614 |
| paraphrase/wording/template | 384 | 0.8649 | 0.7664 | 0.8807 | 0.9405 | 0.9811 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5078 | [0.4219, 0.5938] | 0.9688 | [0.9375, 0.9922] |
| param_near_miss | 128 | 0.5078 | [0.4219, 0.5938] | 0.9688 | [0.9375, 0.9922] |
| period_near_miss | 128 | 0.5078 | [0.4297, 0.5859] | 0.9609 | [0.9297, 0.9922] |
| entity_near_miss | 100 | 0.02 | [0.0, 0.05] | 0.75 | [0.66, 0.83] |
| intent_near_miss | 118 | 0.0169 | [0.0, 0.0426] | 0.661 | [0.5678, 0.7458] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0057 | [0.0023, 0.0113] | 0.0057 | 0.0057 | 0.5317 |
| raw_oracle_entry | 0.1057 | [0.0907, 0.1418] | — | — | 0.5317 |
| split_full | 0.226 | [0.2125, 0.2416] | 0.2293 | 0.3081 | 0.5317 |
| split_template | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.9638 | What was my total income last year? | 0.824 |
| Income minus expenses last year | Income minus expenses this year | 0.9845 | Income minus expenses during 2025 | 0.8581 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9917 | How much did I get refunded from Spotify last year? | 0.8897 |
| Total spent on gas last year | Total spent on gas this year | 0.9873 | How much money went to gas last year? | 0.9076 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.988 | How many transactions did I have at Starbucks last year? | 0.9109 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9918 | Average transaction amount at Walmart last year | 0.9183 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9873 | Total expenses last year | 0.9138 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.982 | What did I pay Starbucks in total last year? | 0.9156 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9896 | How much did I spend per transaction at Uber last year, on average? | 0.9269 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9876 | How much did I get refunded from Shell last year? | 0.9255 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9879 | What was my largest purchase last year? | 0.9261 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9931 | What was my average purchase at Shell last year? | 0.9441 |
| What was my net cash flow this week? | What was my net cash flow last week? | 0.9928 | What was my net cash flow so far this week? | 0.9664 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9824 | How much more did I earn than I spent so far this month? | 0.9606 |
| What was my total spending this year? | What was my total spending last year? | 0.9856 | What was my total spending year to date? | 0.9657 |
