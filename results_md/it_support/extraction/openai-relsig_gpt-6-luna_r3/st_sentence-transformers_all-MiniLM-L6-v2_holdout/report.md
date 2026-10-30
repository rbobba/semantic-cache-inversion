# st:sentence-transformers/all-MiniLM-L6-v2 holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9266 | 0.8362 | 0.9364 | 0.992 | 0.9988 |
| **equivalent_surface (same wording=True)** | 356 | 0.9266 | 0.8362 | 0.9364 | 0.992 | 0.9988 |
| **filter_change** | 37 | 0.6446 | 0.3801 | 0.659 | 0.8189 | 0.8389 |
| **intent_near_miss** | 136 | 0.7035 | 0.4828 | 0.7393 | 0.8863 | 0.955 |
| **intent_near_miss (same wording=False)** | 136 | 0.7035 | 0.4828 | 0.7393 | 0.8863 | 0.955 |
| **param_near_miss** | 609 | 0.844 | 0.6167 | 0.9076 | 0.9858 | 0.9975 |
| **param_near_miss (same wording=False)** | 215 | 0.6952 | 0.5217 | 0.7108 | 0.8499 | 0.9597 |
| **param_near_miss (same wording=True)** | 394 | 0.9252 | 0.8047 | 0.9537 | 0.9894 | 0.9975 |
| **paraphrase** | 250 | 0.7451 | 0.5583 | 0.7783 | 0.8975 | 0.9599 |
| equivalent_surface/amount/alias | 10 | 0.9744 | 0.9462 | 0.9687 | 0.9986 | 0.9988 |
| equivalent_surface/n/alias | 20 | 0.9953 | 0.9932 | 0.9955 | 0.9975 | 0.9976 |
| equivalent_surface/period/alias | 246 | 0.938 | 0.863 | 0.9496 | 0.9906 | 0.9967 |
| equivalent_surface/priority/alias | 40 | 0.8389 | 0.7322 | 0.8533 | 0.9272 | 0.9371 |
| equivalent_surface/service/alias | 10 | 0.926 | 0.877 | 0.9428 | 0.9707 | 0.9711 |
| equivalent_surface/team/alias | 30 | 0.8881 | 0.8198 | 0.869 | 0.9576 | 0.963 |
| filter_change/filter_added/service_count | 7 | 0.4507 | 0.2963 | 0.356 | 0.7328 | 0.7667 |
| filter_change/filter_dropped/total_opened | 30 | 0.6899 | 0.5615 | 0.6826 | 0.822 | 0.8389 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.7426 | 0.6205 | 0.7491 | 0.8849 | 0.8874 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.5693 | 0.4857 | 0.5365 | 0.6876 | 0.6909 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.6154 | 0.5489 | 0.6149 | 0.6892 | 0.7347 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.601 | 0.4783 | 0.5629 | 0.7427 | 0.7655 |
| intent_near_miss/direction/team_opened | 10 | 0.8715 | 0.811 | 0.8439 | 0.9515 | 0.955 |
| intent_near_miss/direction/team_resolved | 10 | 0.7876 | 0.7437 | 0.7846 | 0.8259 | 0.9154 |
| intent_near_miss/direction/total_opened | 7 | 0.7745 | 0.664 | 0.7857 | 0.8651 | 0.9006 |
| intent_near_miss/direction/total_resolved | 7 | 0.7783 | 0.6977 | 0.7535 | 0.8963 | 0.913 |
| intent_near_miss/grouping/top_services | 10 | 0.6054 | 0.4306 | 0.6589 | 0.7449 | 0.75 |
| intent_near_miss/grouping/top_teams | 10 | 0.57 | 0.3323 | 0.5774 | 0.807 | 0.8112 |
| intent_near_miss/measure/backlog_change | 14 | 0.6752 | 0.5277 | 0.7198 | 0.7584 | 0.8258 |
| intent_near_miss/measure/total_opened | 7 | 0.626 | 0.5137 | 0.6591 | 0.7115 | 0.7407 |
| intent_near_miss/measure/total_resolved | 7 | 0.6338 | 0.5402 | 0.6661 | 0.7053 | 0.7349 |
| intent_near_miss/negation/priority_count | 10 | 0.8506 | 0.7749 | 0.8721 | 0.8967 | 0.8994 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8344 | 0.7966 | 0.819 | 0.9069 | 0.9105 |
| param_near_miss/amount/neighbor | 25 | 0.841 | 0.6297 | 0.9678 | 0.9804 | 0.9883 |
| param_near_miss/n/neighbor | 48 | 0.8552 | 0.5717 | 0.9684 | 0.9848 | 0.9921 |
| param_near_miss/period/adjacent | 243 | 0.8622 | 0.6473 | 0.9229 | 0.9911 | 0.9975 |
| param_near_miss/period/granularity | 163 | 0.8929 | 0.797 | 0.9276 | 0.9698 | 0.9873 |
| param_near_miss/priority/neighbor | 50 | 0.8702 | 0.7395 | 0.9101 | 0.9681 | 0.9846 |
| param_near_miss/service/neighbor | 20 | 0.573 | 0.2738 | 0.6647 | 0.7285 | 0.7502 |
| param_near_miss/team/neighbor | 60 | 0.6984 | 0.5767 | 0.7199 | 0.8053 | 0.8548 |
| paraphrase/wording/template | 250 | 0.7451 | 0.5583 | 0.7783 | 0.8975 | 0.9599 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.504 | [0.416, 0.592] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.504 | [0.416, 0.592] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.496 | [0.408, 0.584] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0111 | [0.0, 0.0333] | 0.7667 | [0.6778, 0.8556] |
| intent_near_miss | 115 | 0.0087 | [0.0, 0.0261] | 0.6348 | [0.5478, 0.7217] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 1.0 | [1.0, 1.0] |
| B | 125 | 0.552 | [0.464, 0.64] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0024 | [0.0, 0.0186] | 0.0024 | 0.0024 | 0.6039 |
| raw_oracle_entry | 0.1087 | [0.0888, 0.1644] | — | — | 0.6039 |
| split_full | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.6039 |
| split_template | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_full_extracted | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.6039 |
| split_template_extracted | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_extracted_slots | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_template_negguard | 0.2029 | [0.1485, 0.2638] | 0.2029 | 0.2029 | 1.0 |
| split_template_guarded | 0.215 | [0.1625, 0.5244] | 0.4565 | 0.4565 | 0.8889 |
| split_template_guarded_goldsig | 0.2464 | [0.1898, 0.639] | 0.5676 | 0.5676 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.8696 | 0.7874 [0.7345, 0.8352] | 0.0944 [0.0497, 0.1491] | 34 | 34 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9807 | 0.8986 [0.8478, 0.9378] | 0.0837 [0.0443, 0.1342] | 34 | 34 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.9621 | Average time to resolve in the third quarter of 2026 | 0.8382 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.9745 | What was the longest resolution time in the third quarter of 2026? | 0.851 |
| Ticket intake for the service desk in Q3 2026 | Ticket intake for the service desk in Q2 2026 | 0.9655 | Ticket intake for the help desk in Q3 2026 | 0.8558 |
| How many tickets were resolved in Q3 2026? | How many tickets were resolved in Q2 2026? | 0.9569 | How many tickets were resolved in the third quarter of 2026? | 0.8658 |
| What was the net change in open tickets in Q3 2026? | What was the net change in open tickets in Q2 2026? | 0.9748 | What was the net change in open tickets in the third quarter of 2026? | 0.8874 |
| Number of tickets about single sign-on in Q3 2026 | Number of tickets about single sign-on in Q2 2026 | 0.9711 | How many tickets were about single sign-on in Q3 2026? | 0.9416 |
| Any tickets taking over 24 hours to close in Q3 2026? | Any tickets taking over 48 hours to close in Q3 2026? | 0.9883 | Any tickets taking over a day to close in Q3 2026? | 0.97 |
| Resolved ticket count for the cloud team in Q3 2026 | Resolved ticket count for the cloud team in Q2 2026 | 0.9725 | Resolved ticket count for the cloud platform team in Q3 2026 | 0.9599 |
| Number of P1 tickets in Q3 2026 | Number of P1 tickets in Q2 2026 | 0.9671 | Count of P1 tickets in Q3 2026 | 0.9548 |
| Average time to resolve this year | Average time to resolve last year | 0.9661 | Average time to resolve so far this year | 0.9568 |
| Average time to resolve this month | Average time to resolve last month | 0.9618 | Average time to resolve so far this month | 0.9545 |
| Maximum time to resolve this month | Maximum time to resolve last month | 0.9626 | Maximum time to resolve so far this month | 0.9553 |
| Average time to resolve for the security team last month | Average time to resolve for the security team this month | 0.9876 | Average time to resolve for the security team in the previous month | 0.9805 |
| Average time to resolve for the service desk last year | Average time to resolve for the service desk this year | 0.9861 | Average time to resolve for the service desk in the previous year | 0.9791 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9865 | What was the longest resolution time in the previous month? | 0.9796 |
