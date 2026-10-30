# st:sentence-transformers/all-MiniLM-L6-v2 holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9368 | 0.8604 | 0.9492 | 0.9917 | 0.9976 |
| **equivalent_surface (same wording=True)** | 370 | 0.9368 | 0.8604 | 0.9492 | 0.9917 | 0.9976 |
| **filter_change** | 37 | 0.5918 | 0.44 | 0.6153 | 0.7418 | 0.8176 |
| **intent_near_miss** | 142 | 0.7061 | 0.5019 | 0.7116 | 0.904 | 0.9935 |
| **intent_near_miss (same wording=False)** | 142 | 0.7061 | 0.5019 | 0.7116 | 0.904 | 0.9935 |
| **param_near_miss** | 714 | 0.8621 | 0.685 | 0.8968 | 0.9866 | 0.9965 |
| **param_near_miss (same wording=False)** | 255 | 0.7462 | 0.5837 | 0.7619 | 0.9017 | 0.9785 |
| **param_near_miss (same wording=True)** | 459 | 0.9265 | 0.8209 | 0.9571 | 0.989 | 0.9965 |
| **paraphrase** | 290 | 0.7964 | 0.6263 | 0.8268 | 0.9321 | 0.9892 |
| equivalent_surface/amount/alias | 10 | 0.9416 | 0.932 | 0.9415 | 0.9527 | 0.962 |
| equivalent_surface/clinic/alias | 40 | 0.8689 | 0.7613 | 0.8895 | 0.948 | 0.9777 |
| equivalent_surface/department/alias | 30 | 0.9629 | 0.9446 | 0.9651 | 0.9811 | 0.9856 |
| equivalent_surface/n/alias | 20 | 0.9952 | 0.9921 | 0.9961 | 0.9974 | 0.9976 |
| equivalent_surface/payer/alias | 2 | 0.9105 | 0.8853 | 0.9105 | 0.9357 | 0.942 |
| equivalent_surface/period/alias | 268 | 0.9397 | 0.8677 | 0.9488 | 0.9911 | 0.9961 |
| filter_change/filter_added/clinic_visits | 7 | 0.7074 | 0.5864 | 0.7297 | 0.8095 | 0.8176 |
| filter_change/filter_dropped/total_visits | 30 | 0.5648 | 0.4241 | 0.6066 | 0.6789 | 0.7599 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7159 | 0.6197 | 0.6651 | 0.8773 | 0.8896 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.6598 | 0.6205 | 0.665 | 0.7036 | 0.7088 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.6489 | 0.5856 | 0.6303 | 0.7758 | 0.7765 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.6637 | 0.6037 | 0.6572 | 0.72 | 0.7269 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.7939 | 0.7201 | 0.7813 | 0.8833 | 0.8863 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.5063 | 0.3403 | 0.3727 | 0.7307 | 0.7314 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9057 | 0.8259 | 0.9036 | 0.9898 | 0.9935 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8953 | 0.8052 | 0.9043 | 0.9494 | 0.9744 |
| intent_near_miss/grouping/top_departments | 10 | 0.5996 | 0.4348 | 0.5559 | 0.792 | 0.794 |
| intent_near_miss/grouping/top_providers | 10 | 0.6134 | 0.5481 | 0.6053 | 0.6835 | 0.7268 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7146 | 0.6545 | 0.7047 | 0.8184 | 0.8265 |
| intent_near_miss/measure/dept_visits | 10 | 0.7116 | 0.6712 | 0.7262 | 0.7458 | 0.7518 |
| intent_near_miss/measure/total_no_shows | 7 | 0.4656 | 0.4162 | 0.4771 | 0.5022 | 0.5028 |
| intent_near_miss/measure/total_visits | 7 | 0.5712 | 0.5014 | 0.5529 | 0.66 | 0.6689 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8818 | 0.8348 | 0.879 | 0.9314 | 0.9462 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.7949 | 0.7305 | 0.7993 | 0.9018 | 0.909 |
| param_near_miss/amount/neighbor | 27 | 0.8583 | 0.6158 | 0.9541 | 0.9704 | 0.974 |
| param_near_miss/clinic/neighbor | 80 | 0.787 | 0.6604 | 0.7902 | 0.8892 | 0.9604 |
| param_near_miss/department/neighbor | 60 | 0.7241 | 0.5684 | 0.7456 | 0.8227 | 0.8597 |
| param_near_miss/n/neighbor | 47 | 0.9005 | 0.7056 | 0.977 | 0.989 | 0.9918 |
| param_near_miss/payer/neighbor | 24 | 0.8419 | 0.7337 | 0.868 | 0.9355 | 0.9444 |
| param_near_miss/period/adjacent | 277 | 0.882 | 0.6889 | 0.9249 | 0.99 | 0.9965 |
| param_near_miss/period/granularity | 199 | 0.9 | 0.8116 | 0.9276 | 0.9816 | 0.9947 |
| paraphrase/wording/template | 290 | 0.7964 | 0.6263 | 0.8268 | 0.9321 | 0.9892 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4759 | [0.4, 0.5586] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.4759 | [0.3931, 0.5586] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.4759 | [0.3862, 0.5588] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0545 | [0.0182, 0.1] | 0.6455 | [0.5545, 0.7364] |
| intent_near_miss | 135 | 0.0222 | [0.0, 0.0444] | 0.437 | [0.3554, 0.5185] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9862 | [0.9655, 1.0] |
| B | 145 | 0.5172 | [0.4414, 0.6] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.5534 |
| raw_oracle_entry | 0.1622 | [0.1398, 0.2089] | — | — | 0.5534 |
| split_full | 0.0057 | [0.0, 0.0127] | 0.0057 | 0.0057 | 0.5534 |
| split_template | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |
| split_full_extracted | 0.0057 | [0.0, 0.0127] | 0.0057 | 0.0057 | 0.5534 |
| split_template_extracted | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |
| split_template_extracted_slots | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |
| split_template_negguard | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |
| split_template_guarded | 0.9962 | [0.9903, 1.0] | 0.9962 | 0.9962 | 0.9962 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9853 | 0.0057 | 0.0057 [0.0, 0.0127] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9853 | 0.0267 | 0.0267 [0.0097, 0.0474] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9853 | 0.0267 | 0.0267 [0.0097, 0.0474] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9853 | 0.0267 | 0.0267 [0.0097, 0.0474] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.9656 | 0.9656 [0.9457, 0.9817] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Average patient wait in Q3 2026 | Average patient wait in Q2 2026 | 0.9759 | Average patient wait in the third quarter of 2026 | 0.8813 |
| Total missed appointments in Q3 2026 | Total missed appointments in Q2 2026 | 0.9743 | Total missed appointments in the third quarter of 2026 | 0.8864 |
| Visit volume at the Downtown clinic in Q3 2026 | Visit volume at the Downtown clinic in Q2 2026 | 0.9734 | Visit volume at the Downtown clinic in the third quarter of 2026 | 0.8961 |
| Visit volume at the Northgate clinic in Q3 2026 | Visit volume at the Northgate clinic in Q2 2026 | 0.9817 | Visit volume at the Northgate clinic in the third quarter of 2026 | 0.9066 |
| How often did patients miss appointments in Q3 2026? | How often did patients miss appointments in Q2 2026? | 0.9808 | How often did patients miss appointments in the third quarter of 2026? | 0.9192 |
| How many patient visits did we have in Q3 2026? | How many patient visits did we have in Q2 2026? | 0.9637 | How many patient visits did we have in the third quarter of 2026? | 0.9028 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.974 | What was the maximum wait time in Q3 2026? | 0.9205 |
| How many referrals did the Riverside clinic send out in Q3 2026? | How many referrals did the Riverside clinic send out in Q2 2026? | 0.976 | How many referrals did the Riverside clinic send out in the third quarter of 2026? | 0.9235 |
| How many referrals did the Northgate clinic send out in Q3 2026? | How many referrals did the Northgate clinic send out in Q2 2026? | 0.9753 | How many referrals did the Northgate clinic send out in the third quarter of 2026? | 0.9253 |
| How many patients were referred to the Northgate clinic in Q3 2026? | How many patients were referred to the Northgate clinic in Q2 2026? | 0.9808 | How many referrals did the Northgate clinic receive in Q3 2026? | 0.932 |
| Visit count for Medicare patients in Q3 2026 | Visit count for Medicare patients in Q2 2026 | 0.9736 | Visit count for Medicare patients in the third quarter of 2026 | 0.9263 |
| Visit count for Medicare Advantage patients in Q3 2026 | Visit count for Medicare Advantage patients in Q2 2026 | 0.9818 | Visit count for Medicare Advantage patients in the third quarter of 2026 | 0.9392 |
| Number of incoming referrals at the Lakeside clinic in Q3 2026 | Number of incoming referrals at the Lakeside clinic in Q2 2026 | 0.9775 | Referrals into the Lakeside clinic in Q3 2026 | 0.9368 |
| How many patients did the Midtown clinic refer elsewhere in Q3 2026? | How many patients did the Midtown clinic refer elsewhere in Q2 2026? | 0.9792 | How many patients did the Midtown clinic refer elsewhere in the third quarter of 2026? | 0.9406 |
| What was the average wait time in pulmonology in Q3 2026? | What was the average wait time in pulmonology in Q2 2026? | 0.9872 | What was the average wait time in the pulmonology department in Q3 2026? | 0.9504 |
