# openai:text-embedding-3-large holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9173 | 0.834 | 0.935 | 0.9816 | 0.9928 |
| **equivalent_surface (same wording=True)** | 356 | 0.9173 | 0.834 | 0.935 | 0.9816 | 0.9928 |
| **filter_change** | 37 | 0.6694 | 0.5827 | 0.6784 | 0.7611 | 0.8021 |
| **intent_near_miss** | 136 | 0.715 | 0.575 | 0.7265 | 0.8356 | 0.9433 |
| **intent_near_miss (same wording=False)** | 136 | 0.715 | 0.575 | 0.7265 | 0.8356 | 0.9433 |
| **param_near_miss** | 609 | 0.8481 | 0.6793 | 0.8833 | 0.9734 | 0.9912 |
| **param_near_miss (same wording=False)** | 215 | 0.7259 | 0.6075 | 0.7271 | 0.8512 | 0.9199 |
| **param_near_miss (same wording=True)** | 394 | 0.9148 | 0.8343 | 0.9301 | 0.9761 | 0.9912 |
| **paraphrase** | 250 | 0.7853 | 0.689 | 0.7898 | 0.8945 | 0.9583 |
| equivalent_surface/amount/alias | 10 | 0.9635 | 0.9348 | 0.9632 | 0.9892 | 0.9901 |
| equivalent_surface/n/alias | 20 | 0.9873 | 0.9843 | 0.9871 | 0.9908 | 0.9928 |
| equivalent_surface/period/alias | 246 | 0.9206 | 0.8389 | 0.9416 | 0.9796 | 0.9846 |
| equivalent_surface/priority/alias | 40 | 0.8475 | 0.735 | 0.8563 | 0.9552 | 0.9597 |
| equivalent_surface/service/alias | 10 | 0.9224 | 0.9054 | 0.9266 | 0.9496 | 0.9628 |
| equivalent_surface/team/alias | 30 | 0.9198 | 0.8704 | 0.9201 | 0.9696 | 0.9773 |
| filter_change/filter_added/service_count | 7 | 0.5873 | 0.4912 | 0.5877 | 0.6798 | 0.7189 |
| filter_change/filter_dropped/total_opened | 30 | 0.6886 | 0.6098 | 0.6941 | 0.7671 | 0.8021 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.7879 | 0.7384 | 0.7691 | 0.8418 | 0.8535 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.6204 | 0.5754 | 0.6135 | 0.6634 | 0.6897 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.6956 | 0.6325 | 0.6917 | 0.7709 | 0.7889 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.6735 | 0.5858 | 0.6558 | 0.774 | 0.7862 |
| intent_near_miss/direction/team_opened | 10 | 0.8291 | 0.7398 | 0.8151 | 0.9377 | 0.9433 |
| intent_near_miss/direction/team_resolved | 10 | 0.7594 | 0.7191 | 0.748 | 0.7924 | 0.8961 |
| intent_near_miss/direction/total_opened | 7 | 0.7438 | 0.698 | 0.7129 | 0.8134 | 0.8376 |
| intent_near_miss/direction/total_resolved | 7 | 0.8171 | 0.7518 | 0.8213 | 0.8795 | 0.9064 |
| intent_near_miss/grouping/top_services | 10 | 0.6343 | 0.5035 | 0.6758 | 0.7473 | 0.7519 |
| intent_near_miss/grouping/top_teams | 10 | 0.6147 | 0.4658 | 0.6172 | 0.7364 | 0.7515 |
| intent_near_miss/measure/backlog_change | 14 | 0.6521 | 0.5803 | 0.6558 | 0.7061 | 0.7482 |
| intent_near_miss/measure/total_opened | 7 | 0.6737 | 0.571 | 0.6969 | 0.7542 | 0.806 |
| intent_near_miss/measure/total_resolved | 7 | 0.7316 | 0.6512 | 0.7567 | 0.7882 | 0.8177 |
| intent_near_miss/negation/priority_count | 10 | 0.7719 | 0.7182 | 0.7452 | 0.8373 | 0.8398 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.7706 | 0.7243 | 0.7393 | 0.8518 | 0.8793 |
| param_near_miss/amount/neighbor | 25 | 0.8502 | 0.681 | 0.9334 | 0.9656 | 0.9776 |
| param_near_miss/n/neighbor | 48 | 0.8078 | 0.6168 | 0.8785 | 0.9123 | 0.9469 |
| param_near_miss/period/adjacent | 243 | 0.8643 | 0.6981 | 0.9035 | 0.9797 | 0.9911 |
| param_near_miss/period/granularity | 163 | 0.8856 | 0.7659 | 0.9222 | 0.9569 | 0.9912 |
| param_near_miss/priority/neighbor | 50 | 0.8522 | 0.6848 | 0.8799 | 0.9649 | 0.9749 |
| param_near_miss/service/neighbor | 20 | 0.66 | 0.5125 | 0.7208 | 0.7636 | 0.7787 |
| param_near_miss/team/neighbor | 60 | 0.7716 | 0.6558 | 0.7865 | 0.8615 | 0.8846 |
| paraphrase/wording/template | 250 | 0.7853 | 0.689 | 0.7898 | 0.8945 | 0.9583 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.464 | [0.376, 0.552] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.464 | [0.376, 0.5442] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.456 | [0.368, 0.552] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0444 | [0.0111, 0.0889] | 0.8556 | [0.7778, 0.9222] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4261 | [0.3391, 0.5217] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.992 | [0.9758, 1.0] |
| B | 125 | 0.584 | [0.504, 0.672] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0024 | [0.0, 0.032] | 0.0024 | 0.0024 | 0.6039 |
| raw_oracle_entry | 0.256 | [0.2302, 0.3172] | — | — | 0.6039 |
| split_full | 0.0242 | [0.0099, 0.0455] | 0.0242 | 0.0242 | 0.6039 |
| split_template | 0.0942 | [0.0633, 0.1297] | 0.0942 | 0.0942 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.9843 | How many P4 tickets were opened in the previous month? | 0.9625 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.9808 | What was the net change in open tickets in the previous month? | 0.9593 |
| Maximum time to resolve this year | Maximum time to resolve last year | 0.9089 | Maximum time to resolve so far this year | 0.8879 |
| How many P2 tickets were opened last month? | How many P2 tickets were opened this month? | 0.9839 | How many P2 tickets were opened in the previous month? | 0.9632 |
| How many tickets of every priority except P2 did we get this week? | How many tickets of every priority except P2 did we get last week? | 0.9837 | How many tickets of every priority except P2 did we get so far this week? | 0.9636 |
| How many tickets of every priority except P4 did we get this week? | How many tickets of every priority except P4 did we get last week? | 0.9833 | How many tickets of every priority except P4 did we get so far this week? | 0.9634 |
| Any tickets taking over 24 hours to close last month? | Any tickets taking over 24 hours to close this month? | 0.9761 | Any tickets taking over 24 hours to close in the previous month? | 0.9569 |
| How many tickets of every priority except P3 did we get this week? | How many tickets of every priority except P3 did we get last week? | 0.9825 | How many tickets of every priority except P3 did we get so far this week? | 0.9636 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.9731 | How many tickets were opened so far this week? | 0.9546 |
| How many tickets were opened this week, excluding P1 ones? | How many tickets were opened last week, excluding P1 ones? | 0.9811 | How many tickets were opened so far this week, excluding P1 ones? | 0.9632 |
| How many tickets were resolved last month? | How many tickets were resolved this month? | 0.9721 | How many tickets were resolved in the previous month? | 0.9551 |
| How many tickets of every priority except P4 did we get this year? | How many tickets of every priority except P4 did we get last year? | 0.9744 | How many tickets of every priority except P4 did we get so far this year? | 0.958 |
| How many tickets were opened last month, excluding P4 ones? | How many tickets were opened this month, excluding P4 ones? | 0.9805 | How many tickets were opened in the previous month, excluding P4 ones? | 0.9654 |
| Maximum time to resolve this month | Maximum time to resolve last month | 0.9254 | Maximum time to resolve so far this month | 0.9103 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.9352 | What was the longest resolution time in the third quarter of 2026? | 0.9203 |
