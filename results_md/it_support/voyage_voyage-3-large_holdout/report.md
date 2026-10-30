# voyage:voyage-3-large holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9239 | 0.8285 | 0.9503 | 0.9849 | 0.9971 |
| **equivalent_surface (same wording=True)** | 356 | 0.9239 | 0.8285 | 0.9503 | 0.9849 | 0.9971 |
| **filter_change** | 37 | 0.7448 | 0.6186 | 0.7515 | 0.8373 | 0.8718 |
| **intent_near_miss** | 136 | 0.7954 | 0.7044 | 0.8018 | 0.8883 | 0.9529 |
| **intent_near_miss (same wording=False)** | 136 | 0.7954 | 0.7044 | 0.8018 | 0.8883 | 0.9529 |
| **param_near_miss** | 609 | 0.8743 | 0.7758 | 0.8868 | 0.969 | 0.993 |
| **param_near_miss (same wording=False)** | 215 | 0.8169 | 0.7146 | 0.833 | 0.9027 | 0.9483 |
| **param_near_miss (same wording=True)** | 394 | 0.9057 | 0.8243 | 0.9103 | 0.9731 | 0.993 |
| **paraphrase** | 250 | 0.877 | 0.8035 | 0.887 | 0.9457 | 0.9808 |
| equivalent_surface/amount/alias | 10 | 0.972 | 0.9504 | 0.9684 | 0.9919 | 0.9936 |
| equivalent_surface/n/alias | 20 | 0.9906 | 0.9832 | 0.9914 | 0.9952 | 0.9971 |
| equivalent_surface/period/alias | 246 | 0.9186 | 0.8241 | 0.9496 | 0.9822 | 0.9927 |
| equivalent_surface/priority/alias | 40 | 0.8864 | 0.7727 | 0.9167 | 0.9777 | 0.9836 |
| equivalent_surface/service/alias | 10 | 0.9361 | 0.916 | 0.9371 | 0.9564 | 0.9589 |
| equivalent_surface/team/alias | 30 | 0.9527 | 0.9331 | 0.9535 | 0.9731 | 0.9867 |
| filter_change/filter_added/service_count | 7 | 0.6733 | 0.6084 | 0.6264 | 0.8099 | 0.8112 |
| filter_change/filter_dropped/total_opened | 30 | 0.7615 | 0.6834 | 0.765 | 0.8477 | 0.8718 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8402 | 0.8051 | 0.8454 | 0.8757 | 0.8835 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7681 | 0.7492 | 0.7734 | 0.7819 | 0.7841 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.7824 | 0.7553 | 0.7871 | 0.8119 | 0.817 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7157 | 0.6681 | 0.7137 | 0.7522 | 0.7644 |
| intent_near_miss/direction/team_opened | 10 | 0.892 | 0.8736 | 0.8944 | 0.9124 | 0.9186 |
| intent_near_miss/direction/team_resolved | 10 | 0.8356 | 0.8018 | 0.8342 | 0.8739 | 0.8873 |
| intent_near_miss/direction/total_opened | 7 | 0.8183 | 0.7503 | 0.8021 | 0.8897 | 0.9093 |
| intent_near_miss/direction/total_resolved | 7 | 0.8516 | 0.8051 | 0.8495 | 0.9107 | 0.9108 |
| intent_near_miss/grouping/top_services | 10 | 0.7375 | 0.6501 | 0.7604 | 0.8104 | 0.8146 |
| intent_near_miss/grouping/top_teams | 10 | 0.759 | 0.6707 | 0.7717 | 0.8398 | 0.8638 |
| intent_near_miss/measure/backlog_change | 14 | 0.7612 | 0.7076 | 0.7577 | 0.8362 | 0.8655 |
| intent_near_miss/measure/total_opened | 7 | 0.7141 | 0.6308 | 0.718 | 0.7937 | 0.8097 |
| intent_near_miss/measure/total_resolved | 7 | 0.7439 | 0.6679 | 0.7616 | 0.8106 | 0.8302 |
| intent_near_miss/negation/priority_count | 10 | 0.8307 | 0.8047 | 0.8251 | 0.8657 | 0.8894 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8838 | 0.8429 | 0.8877 | 0.9101 | 0.9529 |
| param_near_miss/amount/neighbor | 25 | 0.9012 | 0.8345 | 0.9199 | 0.967 | 0.9757 |
| param_near_miss/n/neighbor | 48 | 0.8761 | 0.7676 | 0.9087 | 0.9509 | 0.9717 |
| param_near_miss/period/adjacent | 243 | 0.8985 | 0.8017 | 0.9166 | 0.9776 | 0.993 |
| param_near_miss/period/granularity | 163 | 0.8676 | 0.7903 | 0.8834 | 0.9229 | 0.9566 |
| param_near_miss/priority/neighbor | 50 | 0.8928 | 0.81 | 0.892 | 0.9732 | 0.9775 |
| param_near_miss/service/neighbor | 20 | 0.663 | 0.5244 | 0.6923 | 0.7463 | 0.779 |
| param_near_miss/team/neighbor | 60 | 0.8371 | 0.7697 | 0.8469 | 0.9021 | 0.9378 |
| paraphrase/wording/template | 250 | 0.877 | 0.8035 | 0.887 | 0.9457 | 0.9808 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.272 | [0.2, 0.352] | 0.992 | [0.976, 1.0] |
| param_near_miss | 125 | 0.272 | [0.2, 0.344] | 0.984 | [0.96, 1.0] |
| period_near_miss | 125 | 0.264 | [0.184, 0.344] | 0.968 | [0.936, 0.992] |
| entity_near_miss | 90 | 0.0222 | [0.0, 0.0556] | 0.8444 | [0.7667, 0.9222] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4087 | [0.3304, 0.4957] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.864 | [0.8, 0.92] |
| B | 125 | 0.416 | [0.3358, 0.504] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.029 | [0.0167, 0.067] | 0.029 | 0.029 | 0.6039 |
| raw_oracle_entry | 0.3768 | [0.3417, 0.4264] | — | — | 0.6039 |
| split_full | 0.1498 | [0.108, 0.1959] | 0.1498 | 0.1691 | 0.6039 |
| split_template | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.9797 | Average time to resolve in the third quarter of 2026 | 0.9425 |
| What was the net change in open tickets in Q3 2026? | What was the net change in open tickets in Q2 2026? | 0.9619 | What was the net change in open tickets in the third quarter of 2026? | 0.9271 |
| What was the net change in open tickets this week? | What was the net change in open tickets last week? | 0.99 | What was the net change in open tickets so far this week? | 0.9625 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9754 | What was our overall ticket volume so far this month? | 0.9491 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9829 | What was the net change in open tickets so far this month? | 0.961 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9592 | How much did the backlog grow so far this year? | 0.9445 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.9754 | What was our overall ticket volume in the previous month? | 0.9611 |
| Ticket intake for the service desk in Q3 2026 | Ticket intake for the service desk in Q2 2026 | 0.9623 | Ticket intake for the service desk in the third quarter of 2026 | 0.9482 |
| What was the longest resolution time last year? | What was the longest resolution time this year? | 0.9697 | What was the longest resolution time in the previous year? | 0.9563 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9792 | What was the longest resolution time in the previous month? | 0.9679 |
| Ticket volume for the VPN this week | Ticket volume for the VPN last week | 0.9771 | Ticket volume for the VPN so far this week | 0.9662 |
| How many tickets were opened last year, excluding P1 ones? | How many tickets were opened last year, excluding P2 ones? | 0.9653 | How many tickets were opened in the previous year, excluding P1 ones? | 0.9546 |
| How many tickets were opened last year? | How many tickets were opened this year? | 0.9436 | How many tickets were opened in the previous year? | 0.9331 |
| Average time to resolve for the network team last month | Average time to resolve for the network team this month | 0.9782 | Average time to resolve for the network team in the previous month | 0.9684 |
| Average time to resolve for the security team last month | Average time to resolve for the security team this month | 0.9757 | Average time to resolve for the security team in the previous month | 0.9669 |
