# st:BAAI/bge-base-en-v1.5

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 1077 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9409 | 0.8643 | 0.9635 | 0.9905 | 0.9981 |
| **equivalent_surface (same wording=True)** | 356 | 0.9409 | 0.8643 | 0.9635 | 0.9905 | 0.9981 |
| **filter_change** | 37 | 0.7976 | 0.6837 | 0.8101 | 0.8647 | 0.883 |
| **intent_near_miss** | 136 | 0.8236 | 0.7324 | 0.832 | 0.9057 | 0.9491 |
| **intent_near_miss (same wording=False)** | 136 | 0.8236 | 0.7324 | 0.832 | 0.9057 | 0.9491 |
| **param_near_miss** | 609 | 0.8981 | 0.7851 | 0.919 | 0.9906 | 0.9976 |
| **param_near_miss (same wording=False)** | 215 | 0.824 | 0.7241 | 0.8312 | 0.9135 | 0.9481 |
| **param_near_miss (same wording=True)** | 394 | 0.9386 | 0.874 | 0.9415 | 0.9933 | 0.9976 |
| **paraphrase** | 250 | 0.8571 | 0.7693 | 0.8685 | 0.9308 | 0.9718 |
| equivalent_surface/amount/alias | 10 | 0.9534 | 0.9075 | 0.9505 | 0.9947 | 0.9948 |
| equivalent_surface/n/alias | 20 | 0.9952 | 0.9942 | 0.9951 | 0.9966 | 0.9981 |
| equivalent_surface/period/alias | 246 | 0.942 | 0.8647 | 0.9675 | 0.9886 | 0.9944 |
| equivalent_surface/priority/alias | 40 | 0.8917 | 0.8204 | 0.9038 | 0.9549 | 0.9569 |
| equivalent_surface/service/alias | 10 | 0.9699 | 0.9531 | 0.9758 | 0.9821 | 0.9851 |
| equivalent_surface/team/alias | 30 | 0.9479 | 0.9145 | 0.9524 | 0.9817 | 0.992 |
| filter_change/filter_added/service_count | 7 | 0.7107 | 0.6165 | 0.6572 | 0.8721 | 0.883 |
| filter_change/filter_dropped/total_opened | 30 | 0.8179 | 0.7745 | 0.8183 | 0.8641 | 0.8767 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8487 | 0.8018 | 0.8362 | 0.8972 | 0.8974 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7838 | 0.751 | 0.7923 | 0.812 | 0.8203 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.7989 | 0.7696 | 0.8045 | 0.8217 | 0.8238 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7794 | 0.7151 | 0.7439 | 0.8754 | 0.8898 |
| intent_near_miss/direction/team_opened | 10 | 0.9075 | 0.8852 | 0.9013 | 0.9399 | 0.9427 |
| intent_near_miss/direction/team_resolved | 10 | 0.8575 | 0.8421 | 0.8536 | 0.8724 | 0.9006 |
| intent_near_miss/direction/total_opened | 7 | 0.8332 | 0.7734 | 0.8219 | 0.9035 | 0.9313 |
| intent_near_miss/direction/total_resolved | 7 | 0.8148 | 0.7347 | 0.7754 | 0.9269 | 0.9368 |
| intent_near_miss/grouping/top_services | 10 | 0.8055 | 0.7274 | 0.84 | 0.8656 | 0.8668 |
| intent_near_miss/grouping/top_teams | 10 | 0.7663 | 0.646 | 0.7673 | 0.8828 | 0.8891 |
| intent_near_miss/measure/backlog_change | 14 | 0.8047 | 0.7463 | 0.8077 | 0.8577 | 0.8815 |
| intent_near_miss/measure/total_opened | 7 | 0.7889 | 0.7164 | 0.8051 | 0.8465 | 0.8594 |
| intent_near_miss/measure/total_resolved | 7 | 0.7733 | 0.7138 | 0.7718 | 0.8385 | 0.848 |
| intent_near_miss/negation/priority_count | 10 | 0.9206 | 0.8925 | 0.9199 | 0.9489 | 0.9491 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.849 | 0.8068 | 0.8371 | 0.893 | 0.899 |
| param_near_miss/amount/neighbor | 25 | 0.8782 | 0.7776 | 0.9206 | 0.9496 | 0.9593 |
| param_near_miss/n/neighbor | 48 | 0.8879 | 0.7278 | 0.9324 | 0.9626 | 0.9819 |
| param_near_miss/period/adjacent | 243 | 0.9143 | 0.7953 | 0.9261 | 0.9945 | 0.9976 |
| param_near_miss/period/granularity | 163 | 0.9058 | 0.837 | 0.9238 | 0.9501 | 0.9766 |
| param_near_miss/priority/neighbor | 50 | 0.9184 | 0.8493 | 0.9199 | 0.9811 | 0.985 |
| param_near_miss/service/neighbor | 20 | 0.7903 | 0.596 | 0.8389 | 0.8872 | 0.9096 |
| param_near_miss/team/neighbor | 60 | 0.8474 | 0.7589 | 0.8478 | 0.918 | 0.9299 |
| paraphrase/wording/template | 250 | 0.8571 | 0.7693 | 0.8685 | 0.9308 | 0.9718 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.656 | [0.568, 0.744] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.656 | [0.568, 0.736] | 0.992 | [0.976, 1.0] |
| period_near_miss | 125 | 0.656 | [0.568, 0.736] | 0.992 | [0.976, 1.0] |
| entity_near_miss | 90 | 0.0 | [0.0, 0.0] | 0.8667 | [0.7997, 0.9333] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6087 | [0.5217, 0.6957] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.96 | [0.92, 0.992] |
| B | 125 | 0.824 | [0.76, 0.888] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0009 | [0.0, 0.0035] | 0.0009 | 0.0009 | 0.6147 |
| raw_oracle_entry | 0.0808 | [0.0681, 0.1126] | — | — | 0.6147 |
| split_full | 0.3343 | [0.3147, 0.3534] | 0.3343 | 0.3668 | 0.6147 |
| split_template | 0.6342 | [0.6104, 0.656] | 0.6342 | 0.6927 | 1.0 |
| split_full_extracted | 0.3138 | [0.2921, 0.3356] | 0.3138 | 0.3695 | 0.6147 |
| split_template_extracted | 0.6314 | [0.608, 0.6533] | 0.6314 | 0.7112 | 1.0 |
| split_template_extracted_slots | 0.6314 | [0.608, 0.6533] | 0.6314 | 0.7112 | 1.0 |
| split_template_negguard | 0.7289 | [0.7004, 0.7571] | 0.7289 | 0.8384 | 1.0 |
| split_template_guarded_goldsig | 0.8106 | [0.7768, 0.8427] | 0.8106 | 0.9545 | 1.0 |
| split_template_fullsig | 0.9991 | [0.9971, 1.0] | 0.9991 | 0.9991 | 0.9991 |
| split_template_fullsig_gold | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9749 | 0.3083 | 0.3083 [0.2854, 0.3307] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9749 | 0.6314 | 0.6314 [0.608, 0.6533] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9749 | 0.6314 | 0.6314 [0.608, 0.6533] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9749 | 0.6314 | 0.6314 [0.608, 0.6533] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 0.9545 [0.9301, 0.9733] | 0.0455 [0.0267, 0.0699] | 49 | 49 | 0 | 0 |
| split_template_fullsig | 0.5 | 0.9991 | 0.9991 [0.9971, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_fullsig_gold | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many tickets were opened last year? | How many tickets were opened this year? | 0.9883 | How many tickets were opened in the previous year? | 0.9651 |
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9883 | How many tickets were opened so far this year? | 0.9685 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.971 | What was the longest resolution time in the third quarter of 2026? | 0.9522 |
| How many P3 tickets were opened last year? | How many P3 tickets were opened this year? | 0.9933 | How many P3 tickets were opened in the previous year? | 0.976 |
| Resolved tickets this month | Resolved tickets last month | 0.9844 | Resolved tickets so far this month | 0.9673 |
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.9605 | Average time to resolve in the third quarter of 2026 | 0.9435 |
| Number of P4 tickets last year | Number of P4 tickets this year | 0.982 | Count of P4 tickets last year | 0.9658 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.9929 | How many tickets were opened so far this week? | 0.9768 |
| How many tickets were resolved this year? | How many tickets were resolved last year? | 0.9925 | How many tickets were resolved so far this year? | 0.9773 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9951 | What was the net change in open tickets so far this month? | 0.981 |
| Resolved tickets this week | Resolved tickets last week | 0.99 | Resolved tickets so far this week | 0.9759 |
| How many P2 tickets were opened last month? | How many P2 tickets were opened this month? | 0.9938 | How many P2 tickets were opened in the previous month? | 0.98 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9949 | How much did the backlog grow so far this year? | 0.982 |
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.9937 | How many P4 tickets were opened in the previous month? | 0.9815 |
| What was the net change in open tickets this week? | What was the net change in open tickets last week? | 0.9968 | What was the net change in open tickets so far this week? | 0.9846 |
