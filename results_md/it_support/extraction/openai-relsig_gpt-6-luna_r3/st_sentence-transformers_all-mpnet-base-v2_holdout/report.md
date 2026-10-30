# st:sentence-transformers/all-mpnet-base-v2 holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.928 | 0.8346 | 0.9522 | 0.9921 | 0.9986 |
| **equivalent_surface (same wording=True)** | 356 | 0.928 | 0.8346 | 0.9522 | 0.9921 | 0.9986 |
| **filter_change** | 37 | 0.6494 | 0.4237 | 0.6666 | 0.8103 | 0.8333 |
| **intent_near_miss** | 136 | 0.7042 | 0.5171 | 0.7244 | 0.8775 | 0.9682 |
| **intent_near_miss (same wording=False)** | 136 | 0.7042 | 0.5171 | 0.7244 | 0.8775 | 0.9682 |
| **param_near_miss** | 609 | 0.8523 | 0.6321 | 0.9123 | 0.9886 | 0.9975 |
| **param_near_miss (same wording=False)** | 215 | 0.7121 | 0.5358 | 0.7394 | 0.8639 | 0.9493 |
| **param_near_miss (same wording=True)** | 394 | 0.9288 | 0.8207 | 0.9528 | 0.9927 | 0.9975 |
| **paraphrase** | 250 | 0.7488 | 0.551 | 0.797 | 0.8982 | 0.975 |
| equivalent_surface/amount/alias | 10 | 0.9798 | 0.9659 | 0.9738 | 0.9986 | 0.9986 |
| equivalent_surface/n/alias | 20 | 0.9964 | 0.9944 | 0.9968 | 0.998 | 0.9986 |
| equivalent_surface/period/alias | 246 | 0.9335 | 0.85 | 0.9615 | 0.9892 | 0.9973 |
| equivalent_surface/priority/alias | 40 | 0.8614 | 0.7472 | 0.8813 | 0.9563 | 0.965 |
| equivalent_surface/service/alias | 10 | 0.9246 | 0.8866 | 0.937 | 0.958 | 0.9584 |
| equivalent_surface/team/alias | 30 | 0.9102 | 0.8524 | 0.9169 | 0.9625 | 0.9823 |
| filter_change/filter_added/service_count | 7 | 0.4663 | 0.3607 | 0.3873 | 0.6613 | 0.6806 |
| filter_change/filter_dropped/total_opened | 30 | 0.6922 | 0.5744 | 0.6811 | 0.813 | 0.8333 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.704 | 0.5433 | 0.7239 | 0.8679 | 0.8752 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.5378 | 0.5122 | 0.5341 | 0.5711 | 0.5763 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.6466 | 0.5624 | 0.6588 | 0.7009 | 0.7009 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.6086 | 0.5054 | 0.5452 | 0.7555 | 0.7598 |
| intent_near_miss/direction/team_opened | 10 | 0.8843 | 0.8249 | 0.8849 | 0.9584 | 0.9682 |
| intent_near_miss/direction/team_resolved | 10 | 0.791 | 0.7242 | 0.7835 | 0.8584 | 0.9227 |
| intent_near_miss/direction/total_opened | 7 | 0.7105 | 0.6152 | 0.6693 | 0.8304 | 0.8571 |
| intent_near_miss/direction/total_resolved | 7 | 0.7477 | 0.6527 | 0.6956 | 0.8895 | 0.9041 |
| intent_near_miss/grouping/top_services | 10 | 0.6354 | 0.4739 | 0.6895 | 0.7614 | 0.7711 |
| intent_near_miss/grouping/top_teams | 10 | 0.5515 | 0.347 | 0.5558 | 0.7359 | 0.7894 |
| intent_near_miss/measure/backlog_change | 14 | 0.6774 | 0.5319 | 0.6908 | 0.7855 | 0.8217 |
| intent_near_miss/measure/total_opened | 7 | 0.6559 | 0.5557 | 0.6728 | 0.7481 | 0.7533 |
| intent_near_miss/measure/total_resolved | 7 | 0.671 | 0.5941 | 0.697 | 0.7462 | 0.7482 |
| intent_near_miss/negation/priority_count | 10 | 0.858 | 0.8192 | 0.8624 | 0.8898 | 0.8906 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8345 | 0.779 | 0.8281 | 0.9162 | 0.9197 |
| param_near_miss/amount/neighbor | 25 | 0.8457 | 0.5992 | 0.9723 | 0.9925 | 0.9944 |
| param_near_miss/n/neighbor | 48 | 0.8498 | 0.5583 | 0.9559 | 0.9885 | 0.9928 |
| param_near_miss/period/adjacent | 243 | 0.8606 | 0.6297 | 0.9083 | 0.9945 | 0.9975 |
| param_near_miss/period/granularity | 163 | 0.9053 | 0.7946 | 0.936 | 0.9721 | 0.9933 |
| param_near_miss/priority/neighbor | 50 | 0.8917 | 0.7986 | 0.9292 | 0.9721 | 0.9835 |
| param_near_miss/service/neighbor | 20 | 0.6127 | 0.4566 | 0.6593 | 0.7374 | 0.7786 |
| param_near_miss/team/neighbor | 60 | 0.7263 | 0.6076 | 0.7348 | 0.8348 | 0.8616 |
| paraphrase/wording/template | 250 | 0.7488 | 0.551 | 0.797 | 0.8982 | 0.975 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.552 | [0.464, 0.648] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.552 | [0.464, 0.6402] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.528 | [0.44, 0.6162] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0667 | [0.0222, 0.1222] | 0.8 | [0.7111, 0.8778] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6087 | [0.5217, 0.7043] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.976 | [0.9518, 1.0] |
| B | 125 | 0.64 | [0.5598, 0.728] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0072 | [0.0, 0.0206] | 0.0072 | 0.0072 | 0.6039 |
| raw_oracle_entry | 0.1135 | [0.0981, 0.1695] | — | — | 0.6039 |
| split_full | 0.0097 | [0.0023, 0.0236] | 0.0097 | 0.0097 | 0.6039 |
| split_template | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |
| split_full_extracted | 0.0097 | [0.0023, 0.0234] | 0.0097 | 0.0097 | 0.6039 |
| split_template_extracted | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |
| split_template_extracted_slots | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |
| split_template_negguard | 0.1691 | [0.1175, 0.2237] | 0.1691 | 0.1691 | 1.0 |
| split_template_guarded | 0.314 | [0.2607, 0.9141] | 0.8865 | 0.8865 | 0.8889 |
| split_template_guarded_goldsig | 0.4251 | [0.3542, 1.0] | 0.9976 | 0.9976 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9529 | 0.0097 | 0.0097 [0.0023, 0.0208] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9529 | 0.0483 | 0.0483 [0.0229, 0.0765] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9529 | 0.0483 | 0.0483 [0.0229, 0.0765] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9529 | 0.0483 | 0.0483 [0.0229, 0.0765] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.872 | 0.8696 [0.8317, 0.9066] | 0.0028 [0.0, 0.0089] | 1 | 1 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9831 | 0.9807 [0.9662, 0.9931] | 0.0025 [0.0, 0.0078] | 1 | 1 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.966 | Average time to resolve in the third quarter of 2026 | 0.9098 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9914 | What was the longest resolution time in the previous month? | 0.951 |
| Resolved tickets this month | Resolved tickets last month | 0.9628 | Resolved tickets so far this month | 0.9257 |
| Maximum time to resolve this month | Maximum time to resolve last month | 0.9499 | Maximum time to resolve so far this month | 0.9144 |
| What was the longest resolution time last year? | What was the longest resolution time this year? | 0.9904 | What was the longest resolution time in the previous year? | 0.9634 |
| Ticket intake for the service desk in Q3 2026 | Ticket intake for the service desk in Q2 2026 | 0.9903 | Ticket intake for the service desk in the third quarter of 2026 | 0.9635 |
| Which tickets stayed open more than 48 hours last month? | Which tickets stayed open more than 48 hours this month? | 0.9946 | Which tickets stayed open more than 48 hours in the previous month? | 0.9703 |
| Average time to resolve this month | Average time to resolve last month | 0.9705 | Average time to resolve so far this month | 0.9469 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.9668 | What was the longest resolution time in the third quarter of 2026? | 0.9444 |
| Maximum time to resolve this year | Maximum time to resolve last year | 0.9325 | Maximum time to resolve so far this year | 0.9104 |
| Any tickets taking over 48 hours to close this month? | Any tickets taking over 24 hours to close this month? | 0.9919 | Any tickets taking over two days to close this month? | 0.9707 |
| Resolved tickets this week | Resolved tickets last week | 0.966 | Resolved tickets so far this week | 0.9449 |
| Average time to resolve for the service desk last year | Average time to resolve for the service desk this year | 0.9817 | Average time to resolve for the service desk in the previous year | 0.9611 |
| How many tickets were resolved last month? | How many tickets were resolved this month? | 0.9921 | How many tickets were resolved in the previous month? | 0.9724 |
| How many tickets were resolved in Q3 2026? | How many tickets were resolved in Q2 2026? | 0.9751 | How many tickets were resolved in the third quarter of 2026? | 0.9555 |
