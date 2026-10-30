# st:sentence-transformers/all-MiniLM-L6-v2 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9381 | 0.8478 | 0.9636 | 0.9931 | 0.9962 |
| **equivalent_surface (same wording=True)** | 310 | 0.9381 | 0.8478 | 0.9636 | 0.9931 | 0.9962 |
| **filter_change** | 27 | 0.5797 | 0.5122 | 0.5894 | 0.6419 | 0.6772 |
| **intent_near_miss** | 176 | 0.7203 | 0.5532 | 0.729 | 0.8631 | 0.9695 |
| **intent_near_miss (same wording=False)** | 176 | 0.7203 | 0.5532 | 0.729 | 0.8631 | 0.9695 |
| **param_near_miss** | 643 | 0.8374 | 0.636 | 0.8684 | 0.9821 | 0.9963 |
| **param_near_miss (same wording=False)** | 228 | 0.7159 | 0.5319 | 0.7285 | 0.8589 | 0.9434 |
| **param_near_miss (same wording=True)** | 415 | 0.9042 | 0.8119 | 0.931 | 0.9857 | 0.9963 |
| **paraphrase** | 256 | 0.7973 | 0.6601 | 0.8237 | 0.9068 | 0.9601 |
| equivalent_surface/amount/alias | 10 | 0.9775 | 0.968 | 0.9804 | 0.9827 | 0.9839 |
| equivalent_surface/channel/alias | 10 | 0.9474 | 0.8978 | 0.9521 | 0.9916 | 0.9962 |
| equivalent_surface/n/alias | 20 | 0.9938 | 0.9904 | 0.9948 | 0.9959 | 0.9962 |
| equivalent_surface/period/alias | 235 | 0.9341 | 0.8457 | 0.9554 | 0.9908 | 0.9952 |
| equivalent_surface/product/alias | 15 | 0.8497 | 0.7053 | 0.8545 | 0.946 | 0.9496 |
| equivalent_surface/region/alias | 20 | 0.9718 | 0.9395 | 0.9739 | 0.9934 | 0.9943 |
| filter_change/filter_added/region_revenue | 7 | 0.5762 | 0.5015 | 0.5877 | 0.6432 | 0.6453 |
| filter_change/filter_dropped/total_revenue | 20 | 0.581 | 0.5219 | 0.5908 | 0.6275 | 0.6772 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5183 | 0.4785 | 0.5182 | 0.5658 | 0.5717 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7651 | 0.6654 | 0.7846 | 0.8318 | 0.8721 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8298 | 0.7746 | 0.8317 | 0.8732 | 0.9187 |
| intent_near_miss/aggregation/product_units | 20 | 0.7855 | 0.7238 | 0.8079 | 0.8433 | 0.8509 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5666 | 0.4214 | 0.5549 | 0.7417 | 0.7662 |
| intent_near_miss/direction/product_returns | 10 | 0.7845 | 0.7536 | 0.7791 | 0.8146 | 0.8572 |
| intent_near_miss/direction/product_revenue | 10 | 0.7863 | 0.7185 | 0.769 | 0.8628 | 0.8971 |
| intent_near_miss/direction/total_returns | 7 | 0.6291 | 0.5926 | 0.6186 | 0.6889 | 0.6971 |
| intent_near_miss/direction/total_revenue | 7 | 0.6732 | 0.6321 | 0.6802 | 0.7122 | 0.7221 |
| intent_near_miss/grouping/top_customers | 10 | 0.6345 | 0.5701 | 0.6481 | 0.6962 | 0.7606 |
| intent_near_miss/grouping/top_products | 10 | 0.6328 | 0.5457 | 0.6218 | 0.7205 | 0.7713 |
| intent_near_miss/measure/net_sales | 14 | 0.6104 | 0.5432 | 0.6087 | 0.6913 | 0.7659 |
| intent_near_miss/measure/total_returns | 7 | 0.6883 | 0.5582 | 0.7264 | 0.7689 | 0.7782 |
| intent_near_miss/measure/total_revenue | 7 | 0.6228 | 0.5186 | 0.6436 | 0.7151 | 0.7847 |
| intent_near_miss/negation/region_revenue | 10 | 0.7516 | 0.6637 | 0.7119 | 0.9664 | 0.9695 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8835 | 0.8651 | 0.8955 | 0.9135 | 0.9185 |
| param_near_miss/amount/neighbor | 26 | 0.8383 | 0.6749 | 0.8773 | 0.9306 | 0.9501 |
| param_near_miss/channel/neighbor | 20 | 0.7699 | 0.6706 | 0.808 | 0.8448 | 0.8663 |
| param_near_miss/n/neighbor | 47 | 0.873 | 0.7247 | 0.9327 | 0.9743 | 0.9789 |
| param_near_miss/period/adjacent | 245 | 0.8771 | 0.7066 | 0.9093 | 0.9925 | 0.9963 |
| param_near_miss/period/granularity | 180 | 0.8776 | 0.7649 | 0.9066 | 0.9725 | 0.9843 |
| param_near_miss/product/neighbor | 85 | 0.6866 | 0.4577 | 0.6965 | 0.8811 | 0.9017 |
| param_near_miss/region/neighbor | 40 | 0.7255 | 0.5749 | 0.7362 | 0.8742 | 0.8913 |
| paraphrase/wording/template | 256 | 0.7973 | 0.6601 | 0.8237 | 0.9068 | 0.9601 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4688 | [0.3906, 0.5547] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.4688 | [0.3828, 0.5547] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.4688 | [0.375, 0.5549] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.72 | [0.63, 0.81] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.463 | [0.3704, 0.5648] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9922 | [0.9766, 1.0] |
| B | 128 | 0.5859 | [0.5, 0.6719] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0146] | 0.0 | 0.0 | 0.5344 |
| raw_oracle_entry | 0.19 | [0.172, 0.2459] | — | — | 0.5344 |
| split_full | 0.0 | [0.0, 0.0797] | 0.0 | 0.0 | 0.5344 |
| split_template | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_full_extracted | 0.0 | [0.0, 0.0762] | 0.0 | 0.0 | 0.5344 |
| split_template_extracted | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_extracted_slots | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_negguard | 0.3779 | [0.3126, 0.4395] | 0.3779 | 0.9353 | 1.0 |
| split_template_guarded | 0.6075 | [0.5531, 0.6596] | 0.6075 | 0.8706 | 0.8706 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.8747 | 0.8559 [0.8189, 0.8896] | 0.0215 [0.0074, 0.0379] | 9 | 9 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9854 | 0.9854 [0.9712, 0.996] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest sale in Q3 2026 | Largest sale in Q2 2026 | 0.9379 | Largest sale in the third quarter of 2026 | 0.8308 |
| Revenue minus returns in Q3 2026 | Revenue minus returns in Q2 2026 | 0.9621 | Revenue minus returns in the third quarter of 2026 | 0.8822 |
| On average, how much did customers pay for yoga mats in Q3 2026? | On average, how much did customers pay for yoga mats in Q2 2026? | 0.9837 | On average, how much did customers pay for yoga mats in the third quarter of 2026? | 0.9356 |
| What did ski jackets sell for on average in Q3 2026? | What did ski jackets sell for on average in Q2 2026? | 0.9791 | What was the average selling price of ski jackets in Q3 2026? | 0.9313 |
| What was the total value of returns in Q3 2026? | What was the total value of returns in Q2 2026? | 0.9535 | Total returns in Q3 2026 | 0.9115 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9768 | What was the total value of returns so far this month? | 0.95 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9789 | What was the total value of returns so far this week? | 0.9602 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.981 | What was the total value of returns so far this year? | 0.9642 |
| Total revenue for the Midwest this year | Total revenue for the Midwest last year | 0.9861 | Total revenue for the Midwest so far this year | 0.9702 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9697 | Revenue minus returns so far this month | 0.9549 |
| Revenue minus returns this year | Revenue minus returns last year | 0.9684 | Revenue minus returns so far this year | 0.9554 |
| Largest sale this year | Largest sale last year | 0.9735 | Largest sale so far this year | 0.9614 |
| Total revenue from running shoes in Q3 2026 | Total revenue from running shoes in Q2 2026 | 0.9625 | How much revenue did running shoes bring in in Q3 2026? | 0.9526 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.9816 | How much revenue did we make so far this week? | 0.9722 |
| Total revenue for the Northeast this year | Total revenue for the Northeast last year | 0.9832 | Total revenue for the Northeast so far this year | 0.9743 |
