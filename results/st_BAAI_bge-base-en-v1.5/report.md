# st:BAAI/bge-base-en-v1.5

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.952 | 0.857 | 0.9756 | 0.993 | 0.9976 |
| **equivalent_surface (same wording=True)** | 262 | 0.952 | 0.857 | 0.9756 | 0.993 | 0.9976 |
| **filter_change** | 37 | 0.8166 | 0.7618 | 0.8206 | 0.8787 | 0.9364 |
| **intent_near_miss** | 176 | 0.8454 | 0.767 | 0.8498 | 0.9085 | 0.9594 |
| **intent_near_miss (same wording=False)** | 176 | 0.8454 | 0.767 | 0.8498 | 0.9085 | 0.9594 |
| **param_near_miss** | 637 | 0.8934 | 0.7923 | 0.9037 | 0.9874 | 0.996 |
| **param_near_miss (same wording=False)** | 228 | 0.8323 | 0.7521 | 0.8353 | 0.9097 | 0.9808 |
| **param_near_miss (same wording=True)** | 409 | 0.9275 | 0.8692 | 0.9266 | 0.9912 | 0.996 |
| **paraphrase** | 384 | 0.8791 | 0.8015 | 0.889 | 0.9405 | 0.9828 |
| equivalent_surface/account/alias | 10 | 0.9688 | 0.953 | 0.9745 | 0.9833 | 0.9862 |
| equivalent_surface/amount/alias | 10 | 0.9886 | 0.9854 | 0.9882 | 0.9931 | 0.9937 |
| equivalent_surface/category/alias | 15 | 0.974 | 0.9603 | 0.9756 | 0.9857 | 0.9875 |
| equivalent_surface/merchant/alias | 12 | 0.9881 | 0.9754 | 0.9912 | 0.996 | 0.9963 |
| equivalent_surface/n/alias | 20 | 0.9954 | 0.9941 | 0.9953 | 0.997 | 0.9976 |
| equivalent_surface/period/alias | 195 | 0.941 | 0.8541 | 0.9702 | 0.9881 | 0.9946 |
| filter_change/filter_added/category_spend_total | 7 | 0.8617 | 0.8155 | 0.8532 | 0.9201 | 0.9364 |
| filter_change/filter_dropped/total_spend | 30 | 0.8061 | 0.758 | 0.812 | 0.8718 | 0.9038 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.762 | 0.7079 | 0.7665 | 0.8182 | 0.833 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8499 | 0.7652 | 0.8548 | 0.9005 | 0.9377 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8614 | 0.8198 | 0.8513 | 0.9091 | 0.9365 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8353 | 0.7528 | 0.8515 | 0.9048 | 0.9141 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7801 | 0.7336 | 0.7638 | 0.8535 | 0.8631 |
| intent_near_miss/direction/income_total | 7 | 0.8319 | 0.7927 | 0.8178 | 0.8811 | 0.8849 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8795 | 0.8359 | 0.8793 | 0.9113 | 0.9148 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8819 | 0.8568 | 0.8895 | 0.9016 | 0.9173 |
| intent_near_miss/direction/total_spend | 7 | 0.8441 | 0.833 | 0.8394 | 0.857 | 0.8648 |
| intent_near_miss/grouping/top_categories | 10 | 0.8437 | 0.7985 | 0.8538 | 0.8846 | 0.8868 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8339 | 0.7639 | 0.846 | 0.8722 | 0.9083 |
| intent_near_miss/measure/income_total | 7 | 0.8331 | 0.7783 | 0.8209 | 0.9023 | 0.9262 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.8227 | 0.7797 | 0.8246 | 0.8844 | 0.896 |
| intent_near_miss/measure/total_spend | 7 | 0.817 | 0.7646 | 0.8013 | 0.8841 | 0.889 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.9136 | 0.8797 | 0.9044 | 0.9581 | 0.9594 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8743 | 0.8406 | 0.8797 | 0.916 | 0.9206 |
| param_near_miss/account/neighbor | 20 | 0.8728 | 0.7896 | 0.8938 | 0.9425 | 0.9541 |
| param_near_miss/amount/neighbor | 25 | 0.8499 | 0.731 | 0.8783 | 0.9384 | 0.9652 |
| param_near_miss/category/neighbor | 45 | 0.8786 | 0.805 | 0.8871 | 0.9356 | 0.9624 |
| param_near_miss/merchant/neighbor | 87 | 0.8461 | 0.7714 | 0.8545 | 0.9158 | 0.9398 |
| param_near_miss/n/neighbor | 45 | 0.9052 | 0.813 | 0.9471 | 0.9692 | 0.9751 |
| param_near_miss/period/adjacent | 230 | 0.9209 | 0.8173 | 0.9268 | 0.9935 | 0.996 |
| param_near_miss/period/granularity | 185 | 0.8902 | 0.8074 | 0.9097 | 0.9381 | 0.9695 |
| paraphrase/wording/template | 384 | 0.8791 | 0.8015 | 0.889 | 0.9405 | 0.9828 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5625 | [0.4766, 0.6484] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.5625 | [0.4766, 0.6484] | 0.9766 | [0.9453, 1.0] |
| period_near_miss | 128 | 0.5625 | [0.4844, 0.6484] | 0.9766 | [0.9453, 1.0] |
| entity_near_miss | 100 | 0.02 | [0.0, 0.05] | 0.86 | [0.79, 0.93] |
| intent_near_miss | 118 | 0.0085 | [0.0, 0.0254] | 0.6017 | [0.5169, 0.6864] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0049 | [0.0016, 0.0098] | 0.0049 | 0.0049 | 0.5317 |
| raw_oracle_entry | 0.0813 | [0.071, 0.1106] | — | — | 0.5317 |
| split_full | 0.2179 | [0.2034, 0.2317] | 0.2195 | 0.2496 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9837 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.981 | Income minus expenses during 2025 | 0.8471 |
| Total money coming in last year | Total money coming in this year | 0.9761 | Total money coming in during 2025 | 0.8502 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9954 | Average transaction amount at Walmart last year | 0.9061 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9869 | What was my largest purchase last year? | 0.9007 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.991 | How much money went to Starbucks last year? | 0.9051 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9942 | How much did I get refunded from Spotify last year? | 0.9237 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9879 | How much did I get refunded from Shell last year? | 0.9177 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9952 | What was my average purchase at Shell last year? | 0.9277 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9893 | What was my total spending last year? | 0.922 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.99 | How much did I spend per transaction at Uber last year, on average? | 0.9245 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9826 | How many transactions did I have at Starbucks last year? | 0.9207 |
| Total spent on gas last year | Total spent on gas this year | 0.9857 | Total spent on fuel last year | 0.9489 |
| What went out of my Visa card this year? | What went out of my Visa card last year? | 0.9957 | What went out of my Visa card so far this year? | 0.9702 |
| How much did I earn this year? | How much did I earn last year? | 0.9809 | How much did I earn so far this year? | 0.9572 |
| How much money did Home Depot give back to me this month? | How much money did Home Depot give back to me last month? | 0.9931 | How much money did Home Depot give back to me so far this month? | 0.9724 |
