# st:sentence-transformers/all-MiniLM-L6-v2

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9295 | 0.8347 | 0.9599 | 0.9913 | 0.9977 |
| **equivalent_surface (same wording=True)** | 262 | 0.9295 | 0.8347 | 0.9599 | 0.9913 | 0.9977 |
| **filter_change** | 37 | 0.6179 | 0.4509 | 0.5883 | 0.758 | 0.9282 |
| **intent_near_miss** | 176 | 0.7282 | 0.5679 | 0.7358 | 0.8723 | 0.9708 |
| **intent_near_miss (same wording=False)** | 176 | 0.7282 | 0.5679 | 0.7358 | 0.8723 | 0.9708 |
| **param_near_miss** | 637 | 0.8233 | 0.6061 | 0.8513 | 0.98 | 0.9947 |
| **param_near_miss (same wording=False)** | 228 | 0.6965 | 0.5288 | 0.7036 | 0.859 | 0.9453 |
| **param_near_miss (same wording=True)** | 409 | 0.894 | 0.7502 | 0.9252 | 0.9846 | 0.9947 |
| **paraphrase** | 384 | 0.7796 | 0.6045 | 0.8043 | 0.9069 | 0.9685 |
| equivalent_surface/account/alias | 10 | 0.8867 | 0.842 | 0.8694 | 0.9601 | 0.9656 |
| equivalent_surface/amount/alias | 10 | 0.9775 | 0.9695 | 0.9801 | 0.9836 | 0.9863 |
| equivalent_surface/category/alias | 15 | 0.9191 | 0.8753 | 0.9232 | 0.9585 | 0.9735 |
| equivalent_surface/merchant/alias | 12 | 0.9678 | 0.9309 | 0.9836 | 0.993 | 0.9949 |
| equivalent_surface/n/alias | 20 | 0.9936 | 0.9896 | 0.9938 | 0.9964 | 0.9977 |
| equivalent_surface/period/alias | 195 | 0.9211 | 0.8199 | 0.9432 | 0.9888 | 0.9939 |
| filter_change/filter_added/category_spend_total | 7 | 0.7215 | 0.6006 | 0.6911 | 0.8674 | 0.9282 |
| filter_change/filter_dropped/total_spend | 30 | 0.5937 | 0.4415 | 0.583 | 0.7542 | 0.7799 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5512 | 0.4468 | 0.5685 | 0.6366 | 0.6507 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.766 | 0.6658 | 0.7845 | 0.8676 | 0.8978 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7687 | 0.6761 | 0.7619 | 0.867 | 0.8863 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7511 | 0.6427 | 0.7575 | 0.8582 | 0.91 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5833 | 0.4671 | 0.5924 | 0.6896 | 0.769 |
| intent_near_miss/direction/income_total | 7 | 0.65 | 0.5613 | 0.6445 | 0.7339 | 0.7457 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8159 | 0.7488 | 0.8113 | 0.896 | 0.9196 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8211 | 0.7293 | 0.8303 | 0.8807 | 0.8966 |
| intent_near_miss/direction/total_spend | 7 | 0.683 | 0.6333 | 0.6835 | 0.7234 | 0.7387 |
| intent_near_miss/grouping/top_categories | 10 | 0.635 | 0.5373 | 0.6393 | 0.7744 | 0.7799 |
| intent_near_miss/grouping/top_merchants | 10 | 0.648 | 0.5542 | 0.6558 | 0.7225 | 0.7548 |
| intent_near_miss/measure/income_total | 7 | 0.7119 | 0.574 | 0.7244 | 0.8616 | 0.9325 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6612 | 0.5483 | 0.6659 | 0.7587 | 0.8393 |
| intent_near_miss/measure/total_spend | 7 | 0.674 | 0.5802 | 0.6218 | 0.8279 | 0.8447 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8746 | 0.8189 | 0.8644 | 0.9466 | 0.9708 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8266 | 0.7944 | 0.8171 | 0.8698 | 0.8742 |
| param_near_miss/account/neighbor | 20 | 0.7099 | 0.5129 | 0.7303 | 0.8801 | 0.8886 |
| param_near_miss/amount/neighbor | 25 | 0.7793 | 0.5428 | 0.89 | 0.9442 | 0.951 |
| param_near_miss/category/neighbor | 45 | 0.762 | 0.6533 | 0.7655 | 0.8598 | 0.9348 |
| param_near_miss/merchant/neighbor | 87 | 0.6682 | 0.5394 | 0.6643 | 0.793 | 0.851 |
| param_near_miss/n/neighbor | 45 | 0.8705 | 0.6833 | 0.9619 | 0.9806 | 0.9883 |
| param_near_miss/period/adjacent | 230 | 0.8645 | 0.6416 | 0.9147 | 0.9883 | 0.9947 |
| param_near_miss/period/granularity | 185 | 0.8667 | 0.7372 | 0.9009 | 0.9555 | 0.983 |
| paraphrase/wording/template | 384 | 0.7796 | 0.6045 | 0.8043 | 0.9069 | 0.9685 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4688 | [0.3828, 0.5625] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.4688 | [0.3828, 0.5547] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.4688 | [0.375, 0.5547] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.61 | [0.51, 0.7] |
| intent_near_miss | 118 | 0.0085 | [0.0, 0.0254] | 0.5424 | [0.4492, 0.6356] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9609 | [0.9295, 0.9922] |
| B | 111 | 0.5405 | [0.4505, 0.6306] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0081 | [0.0039, 0.0138] | 0.0081 | 0.0081 | 0.5317 |
| raw_oracle_entry | 0.0715 | [0.064, 0.0968] | — | — | 0.5317 |
| split_full | 0.213 | [0.1989, 0.227] | 0.213 | 0.2472 | 0.5317 |
| split_template | 0.9732 | [0.9599, 0.9844] | 0.9732 | 0.9732 | 1.0 |
| split_full_extracted | 0.1976 | [0.1837, 0.2108] | 0.1976 | 0.2138 | 0.5179 |
| split_template_extracted | 0.0203 | [0.0074, 0.067] | 0.9545 | 0.961 | 0.9878 |
| split_template_extracted_slots | 0.1659 | [0.1305, 0.4482] | 0.9577 | 0.9691 | 0.9959 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 1.0 | 0.1959 | 0.1959 [0.1828, 0.2096] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9088 | 0.9602 | 0.9537 [0.9352, 0.9691] | 0.0068 [0.0026, 0.012] | 8 | 0 | 8 | 0 |
| split_template_extracted_slots | 0.9088 | 0.9602 | 0.9569 [0.9392, 0.9715] | 0.0034 [0.0008, 0.007] | 4 | 0 | 4 | 0 |

Similarity as a detector of value errors (right-intent matches): AUC 0.6089 [0.4194, 0.708], 4 with a template value wrong vs 1192 right; median similarity 1.0 vs 1.0. 0.5 = no signal.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.957 | Total money coming in in 2025 | 0.7563 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9876 | What was the biggest single thing I bought in 2025? | 0.8174 |
| Income minus expenses last year | Income minus expenses this year | 0.9649 | Income minus expenses in 2025 | 0.7947 |
| Income minus expenses in Q3 2026 | Income minus expenses in Q2 2026 | 0.9665 | Income minus expenses in the third quarter of 2026 | 0.8368 |
| What went out of my checking account in Q3 2026? | What went out of my checking account in Q2 2026? | 0.9642 | What went out of my checking account in the third quarter of 2026? | 0.8456 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.983 | What was my total spending last year? | 0.8649 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9784 | How much did I spend per transaction at Uber last year, on average? | 0.8745 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9916 | How much did I spend at Starbucks in 2025? | 0.8896 |
| What went out of my Visa card in Q3 2026? | What went out of my Visa card in Q2 2026? | 0.9731 | What went out of my Visa card in the third quarter of 2026? | 0.8854 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9881 | How much did I get refunded from Shell last year? | 0.9079 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9941 | How much money did Spotify give back to me in 2025? | 0.914 |
| Total refunds from Dunkin' in Q3 2026 | Total refunds from Dunkin' in Q2 2026 | 0.9815 | How much did I get refunded from Dunkin' in Q3 2026? | 0.9034 |
| Total spent on gas last year | Total spent on gas this year | 0.9765 | Total spent on fuel last year | 0.907 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9851 | Count my transactions at Starbucks in 2025 | 0.9173 |
| What was my largest purchase in Q3 2026? | What was my largest purchase in Q2 2026? | 0.965 | What was the biggest single thing I bought in Q3 2026? | 0.8979 |
