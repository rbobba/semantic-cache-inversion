# st:sentence-transformers/all-mpnet-base-v2 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.941 | 0.8361 | 0.9727 | 0.9945 | 0.9987 |
| **equivalent_surface (same wording=True)** | 310 | 0.941 | 0.8361 | 0.9727 | 0.9945 | 0.9987 |
| **filter_change** | 27 | 0.6066 | 0.5264 | 0.6147 | 0.6959 | 0.7377 |
| **intent_near_miss** | 176 | 0.7253 | 0.5674 | 0.7363 | 0.8591 | 0.9451 |
| **intent_near_miss (same wording=False)** | 176 | 0.7253 | 0.5674 | 0.7363 | 0.8591 | 0.9451 |
| **param_near_miss** | 643 | 0.8573 | 0.6745 | 0.8976 | 0.9849 | 0.997 |
| **param_near_miss (same wording=False)** | 228 | 0.7475 | 0.5831 | 0.7603 | 0.8822 | 0.9286 |
| **param_near_miss (same wording=True)** | 415 | 0.9177 | 0.8102 | 0.9423 | 0.9893 | 0.997 |
| **paraphrase** | 256 | 0.8081 | 0.6577 | 0.8338 | 0.9166 | 0.9651 |
| equivalent_surface/amount/alias | 10 | 0.9833 | 0.9759 | 0.9848 | 0.9868 | 0.9873 |
| equivalent_surface/channel/alias | 10 | 0.9449 | 0.8959 | 0.9485 | 0.9886 | 0.9937 |
| equivalent_surface/n/alias | 20 | 0.9962 | 0.9944 | 0.9964 | 0.9985 | 0.9987 |
| equivalent_surface/period/alias | 235 | 0.9327 | 0.8097 | 0.9668 | 0.991 | 0.9972 |
| equivalent_surface/product/alias | 15 | 0.914 | 0.8398 | 0.9063 | 0.9761 | 0.982 |
| equivalent_surface/region/alias | 20 | 0.9805 | 0.9616 | 0.9817 | 0.995 | 0.9953 |
| filter_change/filter_added/region_revenue | 7 | 0.6623 | 0.6079 | 0.6347 | 0.7323 | 0.7377 |
| filter_change/filter_dropped/total_revenue | 20 | 0.5871 | 0.5223 | 0.5928 | 0.6623 | 0.6922 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5591 | 0.465 | 0.5683 | 0.6424 | 0.6507 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.767 | 0.6624 | 0.7884 | 0.843 | 0.8592 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8532 | 0.8026 | 0.8547 | 0.8897 | 0.9432 |
| intent_near_miss/aggregation/product_units | 20 | 0.8113 | 0.7811 | 0.8034 | 0.8521 | 0.9098 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5527 | 0.4566 | 0.5423 | 0.6747 | 0.6797 |
| intent_near_miss/direction/product_returns | 10 | 0.7757 | 0.7247 | 0.7688 | 0.8389 | 0.859 |
| intent_near_miss/direction/product_revenue | 10 | 0.7537 | 0.6822 | 0.7602 | 0.8345 | 0.8372 |
| intent_near_miss/direction/total_returns | 7 | 0.6537 | 0.5753 | 0.6675 | 0.7083 | 0.7098 |
| intent_near_miss/direction/total_revenue | 7 | 0.6603 | 0.6206 | 0.6603 | 0.7093 | 0.735 |
| intent_near_miss/grouping/top_customers | 10 | 0.6709 | 0.6265 | 0.6767 | 0.7274 | 0.7376 |
| intent_near_miss/grouping/top_products | 10 | 0.6218 | 0.5565 | 0.6122 | 0.6636 | 0.7098 |
| intent_near_miss/measure/net_sales | 14 | 0.7089 | 0.6218 | 0.7077 | 0.7764 | 0.8501 |
| intent_near_miss/measure/total_returns | 7 | 0.6332 | 0.5435 | 0.6341 | 0.6996 | 0.7117 |
| intent_near_miss/measure/total_revenue | 7 | 0.5832 | 0.4827 | 0.5495 | 0.7123 | 0.7495 |
| intent_near_miss/negation/region_revenue | 10 | 0.7023 | 0.5662 | 0.659 | 0.931 | 0.9451 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.836 | 0.8045 | 0.8278 | 0.889 | 0.8908 |
| param_near_miss/amount/neighbor | 26 | 0.8483 | 0.6729 | 0.9139 | 0.9445 | 0.9552 |
| param_near_miss/channel/neighbor | 20 | 0.8315 | 0.7555 | 0.8458 | 0.8992 | 0.9298 |
| param_near_miss/n/neighbor | 47 | 0.8844 | 0.7379 | 0.9365 | 0.974 | 0.9768 |
| param_near_miss/period/adjacent | 245 | 0.883 | 0.7079 | 0.9111 | 0.9933 | 0.997 |
| param_near_miss/period/granularity | 180 | 0.9012 | 0.7949 | 0.9331 | 0.9705 | 0.9891 |
| param_near_miss/product/neighbor | 85 | 0.7267 | 0.5067 | 0.7575 | 0.9092 | 0.9294 |
| param_near_miss/region/neighbor | 40 | 0.7676 | 0.5656 | 0.7625 | 0.9307 | 0.9422 |
| paraphrase/wording/template | 256 | 0.8081 | 0.6577 | 0.8338 | 0.9166 | 0.9651 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5 | [0.4141, 0.5859] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5 | [0.4141, 0.5781] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5 | [0.4141, 0.5859] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.76 | [0.68, 0.8402] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4167 | [0.3148, 0.5093] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9922 | [0.9766, 1.0] |
| B | 128 | 0.6719 | [0.5859, 0.7578] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0125 | [0.004, 0.0241] | 0.0125 | 0.0125 | 0.5344 |
| raw_oracle_entry | 0.1879 | [0.166, 0.2371] | — | — | 0.5344 |
| split_full | 0.0 | [0.0, 0.0105] | 0.0 | 0.0 | 0.5344 |
| split_template | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_full_extracted | 0.0 | [0.0, 0.0132] | 0.0 | 0.0 | 0.5344 |
| split_template_extracted | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_extracted_slots | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_negguard | 0.0856 | [0.0576, 0.1144] | 0.0856 | 0.0856 | 1.0 |
| split_template_guarded | 0.5741 | [0.5157, 0.6317] | 0.5741 | 0.8685 | 0.8685 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.8914 | 0.8685 [0.8264, 0.9059] | 0.0258 [0.0091, 0.0484] | 11 | 11 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest sale last month | Largest sale this month | 0.9813 | Largest sale in the previous month | 0.9483 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9855 | What was the total value of returns in the previous year? | 0.9558 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9797 | Revenue minus returns so far this month | 0.9511 |
| On average, how much did customers pay for backpacks last month? | On average, how much did customers pay for backpacks this month? | 0.9908 | On average, how much did customers pay for backpacks in the previous month? | 0.9633 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.985 | How much revenue did we make in the previous year? | 0.9598 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9845 | What was the total value of returns in the previous month? | 0.9615 |
| On average, how much did customers pay for yoga mats last month? | On average, how much did customers pay for yoga mats this month? | 0.9936 | On average, how much did customers pay for yoga mats in the previous month? | 0.9747 |
| Revenue minus returns this week | Revenue minus returns last week | 0.9793 | Revenue minus returns so far this week | 0.9619 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.989 | How much revenue did we make in the previous month? | 0.9718 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9894 | What was the total value of returns so far this week? | 0.9732 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9855 | What was the total value of returns so far this year? | 0.9696 |
| What was the total value of returns in Q3 2026? | What was the total value of returns in Q2 2026? | 0.9687 | What was the total value of returns in the third quarter of 2026? | 0.9529 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9925 | What were sales net of returns in the previous month? | 0.9778 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9944 | What were sales everywhere except the West region this month? | 0.9803 |
| On average, how much did customers pay for yoga mats in Q3 2026? | On average, how much did customers pay for yoga mats in Q2 2026? | 0.9968 | On average, how much did customers pay for yoga mats in the third quarter of 2026? | 0.9839 |
