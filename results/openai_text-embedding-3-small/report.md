# openai:text-embedding-3-small

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9322 | 0.8421 | 0.9586 | 0.9826 | 0.9947 |
| **equivalent_surface (same wording=True)** | 262 | 0.9322 | 0.8421 | 0.9586 | 0.9826 | 0.9947 |
| **filter_change** | 37 | 0.671 | 0.5714 | 0.6648 | 0.7786 | 0.8838 |
| **intent_near_miss** | 176 | 0.7431 | 0.6235 | 0.7616 | 0.8423 | 0.9148 |
| **intent_near_miss (same wording=False)** | 176 | 0.7431 | 0.6235 | 0.7616 | 0.8423 | 0.9148 |
| **param_near_miss** | 637 | 0.833 | 0.6535 | 0.8553 | 0.972 | 0.9919 |
| **param_near_miss (same wording=False)** | 228 | 0.7167 | 0.5902 | 0.7168 | 0.8483 | 0.9313 |
| **param_near_miss (same wording=True)** | 409 | 0.8978 | 0.784 | 0.9231 | 0.9799 | 0.9919 |
| **paraphrase** | 384 | 0.792 | 0.6465 | 0.8116 | 0.8945 | 0.9736 |
| equivalent_surface/account/alias | 10 | 0.9548 | 0.9448 | 0.955 | 0.9718 | 0.9835 |
| equivalent_surface/amount/alias | 10 | 0.974 | 0.9673 | 0.9731 | 0.9805 | 0.9824 |
| equivalent_surface/category/alias | 15 | 0.9431 | 0.8907 | 0.9521 | 0.9733 | 0.9798 |
| equivalent_surface/merchant/alias | 12 | 0.9744 | 0.9644 | 0.9752 | 0.9879 | 0.9898 |
| equivalent_surface/n/alias | 20 | 0.986 | 0.9818 | 0.9869 | 0.9906 | 0.9947 |
| equivalent_surface/period/alias | 195 | 0.9199 | 0.8193 | 0.9471 | 0.9768 | 0.9926 |
| filter_change/filter_added/category_spend_total | 7 | 0.738 | 0.6513 | 0.7298 | 0.8408 | 0.8838 |
| filter_change/filter_dropped/total_spend | 30 | 0.6554 | 0.5675 | 0.6467 | 0.7593 | 0.803 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5759 | 0.4736 | 0.5829 | 0.666 | 0.7209 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7962 | 0.7367 | 0.7983 | 0.8627 | 0.8688 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8002 | 0.7371 | 0.7831 | 0.8784 | 0.9065 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7923 | 0.7326 | 0.7936 | 0.8578 | 0.9113 |
| intent_near_miss/aggregation/total_spend | 7 | 0.6191 | 0.476 | 0.6348 | 0.7459 | 0.7825 |
| intent_near_miss/direction/income_total | 7 | 0.6781 | 0.5922 | 0.6437 | 0.776 | 0.7967 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8045 | 0.7649 | 0.8078 | 0.8461 | 0.8695 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7917 | 0.7717 | 0.7958 | 0.8142 | 0.8208 |
| intent_near_miss/direction/total_spend | 7 | 0.6873 | 0.6455 | 0.6681 | 0.7533 | 0.7533 |
| intent_near_miss/grouping/top_categories | 10 | 0.7001 | 0.587 | 0.75 | 0.7654 | 0.7814 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7253 | 0.655 | 0.7514 | 0.7804 | 0.8037 |
| intent_near_miss/measure/income_total | 7 | 0.6782 | 0.604 | 0.6753 | 0.7615 | 0.8201 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6685 | 0.5766 | 0.6653 | 0.7274 | 0.8232 |
| intent_near_miss/measure/total_spend | 7 | 0.6849 | 0.6256 | 0.6695 | 0.7697 | 0.7928 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8214 | 0.7492 | 0.8126 | 0.9052 | 0.9148 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7753 | 0.7336 | 0.7732 | 0.8278 | 0.8495 |
| param_near_miss/account/neighbor | 20 | 0.7742 | 0.6607 | 0.7968 | 0.8965 | 0.9046 |
| param_near_miss/amount/neighbor | 25 | 0.8092 | 0.5904 | 0.9263 | 0.96 | 0.9697 |
| param_near_miss/category/neighbor | 45 | 0.782 | 0.663 | 0.7852 | 0.8937 | 0.9578 |
| param_near_miss/merchant/neighbor | 87 | 0.7266 | 0.6132 | 0.7353 | 0.8288 | 0.9044 |
| param_near_miss/n/neighbor | 45 | 0.8413 | 0.6845 | 0.9017 | 0.9483 | 0.9636 |
| param_near_miss/period/adjacent | 230 | 0.8649 | 0.6958 | 0.8826 | 0.9841 | 0.9919 |
| param_near_miss/period/granularity | 185 | 0.8633 | 0.7226 | 0.8923 | 0.9491 | 0.9916 |
| paraphrase/wording/template | 384 | 0.792 | 0.6465 | 0.8116 | 0.8945 | 0.9736 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5625 | [0.4766, 0.6408] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5625 | [0.4766, 0.6484] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5625 | [0.4766, 0.6484] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.04] | 0.72 | [0.63, 0.8] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.5085 | [0.4153, 0.6017] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0016 | [0.0, 0.0042] | 0.0016 | 0.0016 | 0.5317 |
| raw_oracle_entry | 0.0642 | [0.0571, 0.0905] | — | — | 0.5317 |
| split_full | 0.2138 | [0.2002, 0.227] | 0.2138 | 0.3 | 0.5317 |
| split_template | 0.9683 | [0.9549, 0.98] | 0.9683 | 0.9683 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.9103 | Total money coming in during 2025 | 0.7515 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9569 | What was my total spending last year? | 0.8419 |
| Income minus expenses last year | Income minus expenses this year | 0.9527 | Income minus expenses during 2025 | 0.8515 |
| Total spent on gas last year | Total spent on gas this year | 0.9509 | Total spent on fuel last year | 0.8498 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9782 | Average transaction amount at Uber during 2025 | 0.8858 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9845 | How much money did Spotify give back to me during 2025? | 0.9003 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9854 | What was my average purchase at Shell last year? | 0.903 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9847 | How much did I spend per transaction at Walmart during 2025, on average? | 0.9049 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9714 | Total refunds from Shell during 2025 | 0.8922 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9766 | Count my transactions at Starbucks during 2025 | 0.9006 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9639 | What was my largest purchase last year? | 0.8892 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9715 | What did I pay Starbucks in total last year? | 0.8968 |
| How much did I earn this year? | How much did I earn last year? | 0.949 | How much did I earn so far this year? | 0.8796 |
| How much income did I receive this month? | How much income did I receive last month? | 0.958 | How much income did I receive so far this month? | 0.9068 |
| Total money coming in last month | Total money coming in this month | 0.9411 | Total money coming in in the previous month | 0.9048 |
