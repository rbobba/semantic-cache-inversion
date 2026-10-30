# openai:text-embedding-3-small holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9145 | 0.8218 | 0.9344 | 0.9817 | 0.9944 |
| **equivalent_surface (same wording=True)** | 356 | 0.9145 | 0.8218 | 0.9344 | 0.9817 | 0.9944 |
| **filter_change** | 37 | 0.6467 | 0.4721 | 0.6717 | 0.7449 | 0.8104 |
| **intent_near_miss** | 136 | 0.7256 | 0.5663 | 0.7446 | 0.8358 | 0.9173 |
| **intent_near_miss (same wording=False)** | 136 | 0.7256 | 0.5663 | 0.7446 | 0.8358 | 0.9173 |
| **param_near_miss** | 609 | 0.8416 | 0.6724 | 0.8834 | 0.9764 | 0.993 |
| **param_near_miss (same wording=False)** | 215 | 0.7084 | 0.5491 | 0.7258 | 0.8315 | 0.9429 |
| **param_near_miss (same wording=True)** | 394 | 0.9143 | 0.8205 | 0.9275 | 0.9811 | 0.993 |
| **paraphrase** | 250 | 0.758 | 0.6258 | 0.778 | 0.8861 | 0.9548 |
| equivalent_surface/amount/alias | 10 | 0.9482 | 0.8913 | 0.9509 | 0.9938 | 0.9944 |
| equivalent_surface/n/alias | 20 | 0.9841 | 0.9794 | 0.9826 | 0.9893 | 0.9935 |
| equivalent_surface/period/alias | 246 | 0.9211 | 0.8402 | 0.938 | 0.9786 | 0.9876 |
| equivalent_surface/priority/alias | 40 | 0.8345 | 0.7331 | 0.8223 | 0.9562 | 0.963 |
| equivalent_surface/service/alias | 10 | 0.9206 | 0.901 | 0.9236 | 0.9641 | 0.9692 |
| equivalent_surface/team/alias | 30 | 0.9079 | 0.8398 | 0.9172 | 0.9692 | 0.9759 |
| filter_change/filter_added/service_count | 7 | 0.5146 | 0.4053 | 0.4706 | 0.7102 | 0.7286 |
| filter_change/filter_dropped/total_opened | 30 | 0.6775 | 0.5733 | 0.6959 | 0.7576 | 0.8104 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.7623 | 0.6744 | 0.7721 | 0.8256 | 0.8322 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.6451 | 0.6172 | 0.6372 | 0.6776 | 0.6779 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.6623 | 0.6068 | 0.6625 | 0.736 | 0.7361 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.6317 | 0.5625 | 0.6181 | 0.7137 | 0.7193 |
| intent_near_miss/direction/team_opened | 10 | 0.8402 | 0.7879 | 0.8238 | 0.9135 | 0.9173 |
| intent_near_miss/direction/team_resolved | 10 | 0.7734 | 0.7327 | 0.7636 | 0.8126 | 0.873 |
| intent_near_miss/direction/total_opened | 7 | 0.7555 | 0.6918 | 0.7502 | 0.8387 | 0.8842 |
| intent_near_miss/direction/total_resolved | 7 | 0.8041 | 0.7024 | 0.8194 | 0.8957 | 0.9106 |
| intent_near_miss/grouping/top_services | 10 | 0.6859 | 0.5344 | 0.7402 | 0.8083 | 0.8108 |
| intent_near_miss/grouping/top_teams | 10 | 0.6428 | 0.4621 | 0.6466 | 0.8117 | 0.8316 |
| intent_near_miss/measure/backlog_change | 14 | 0.6828 | 0.5698 | 0.684 | 0.7952 | 0.8144 |
| intent_near_miss/measure/total_opened | 7 | 0.705 | 0.5955 | 0.7368 | 0.7834 | 0.8177 |
| intent_near_miss/measure/total_resolved | 7 | 0.7159 | 0.6144 | 0.7496 | 0.7906 | 0.8062 |
| intent_near_miss/negation/priority_count | 10 | 0.8137 | 0.7398 | 0.8305 | 0.8586 | 0.8599 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.7902 | 0.7478 | 0.7737 | 0.8396 | 0.8599 |
| param_near_miss/amount/neighbor | 25 | 0.8456 | 0.6739 | 0.939 | 0.9667 | 0.978 |
| param_near_miss/n/neighbor | 48 | 0.8116 | 0.5815 | 0.9059 | 0.9381 | 0.9655 |
| param_near_miss/period/adjacent | 243 | 0.8516 | 0.6728 | 0.8825 | 0.9844 | 0.991 |
| param_near_miss/period/granularity | 163 | 0.8764 | 0.7461 | 0.9062 | 0.9562 | 0.993 |
| param_near_miss/priority/neighbor | 50 | 0.8782 | 0.7549 | 0.9027 | 0.9708 | 0.9829 |
| param_near_miss/service/neighbor | 20 | 0.6363 | 0.4132 | 0.7351 | 0.7647 | 0.7842 |
| param_near_miss/team/neighbor | 60 | 0.7674 | 0.6741 | 0.7727 | 0.8696 | 0.8942 |
| paraphrase/wording/template | 250 | 0.758 | 0.6258 | 0.778 | 0.8861 | 0.9548 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.504 | [0.408, 0.592] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.504 | [0.416, 0.6] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.504 | [0.416, 0.592] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0444 | [0.0111, 0.0889] | 0.9556 | [0.9111, 0.9889] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6783 | [0.5913, 0.7652] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 1.0 | [1.0, 1.0] |
| B | 125 | 0.6 | [0.512, 0.6802] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0024 | [0.0023, 0.0382] | 0.0024 | 0.0024 | 0.6039 |
| raw_oracle_entry | 0.2101 | [0.1807, 0.264] | — | — | 0.6039 |
| split_full | 0.0097 | [0.0023, 0.0208] | 0.0097 | 0.0097 | 0.6039 |
| split_template | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Any tickets taking over 24 hours to close in Q3 2026? | Any tickets taking over 48 hours to close in Q3 2026? | 0.978 | Any tickets taking over 24 hours to close in the third quarter of 2026? | 0.9298 |
| How many tickets were opened in Q3 2026? | How many tickets were opened in Q2 2026? | 0.9665 | How many tickets came in in Q3 2026? | 0.9331 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.9687 | What was the longest resolution time in the third quarter of 2026? | 0.9366 |
| Number of tickets about single sign-on in Q3 2026 | Number of tickets about single sign-on in Q2 2026 | 0.9869 | Number of tickets about single sign-on in the third quarter of 2026 | 0.955 |
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.9524 | Average time to resolve in the third quarter of 2026 | 0.9251 |
| What was the net change in open tickets last year? | What was the net change in open tickets this year? | 0.9787 | What was the net change in open tickets in the previous year? | 0.9548 |
| Ticket intake for the service desk in Q3 2026 | Ticket intake for the service desk in Q2 2026 | 0.9791 | Ticket intake for the service desk in the third quarter of 2026 | 0.956 |
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9585 | How many tickets were opened so far this year? | 0.9355 |
| Number of P1 tickets in Q3 2026 | Number of P1 tickets in Q2 2026 | 0.9612 | Count of P1 tickets in Q3 2026 | 0.9383 |
| How many tickets were resolved in Q3 2026? | How many tickets were resolved in Q2 2026? | 0.9641 | How many tickets were resolved in the third quarter of 2026? | 0.9411 |
| How many tickets were opened last year? | How many tickets were opened this year? | 0.9585 | How many tickets were opened in the previous year? | 0.9365 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.9759 | What was our overall ticket volume in the previous month? | 0.956 |
| How many tickets of every priority except P4 did we get this year? | How many tickets of every priority except P4 did we get last year? | 0.9796 | How many tickets of every priority except P4 did we get so far this year? | 0.9603 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9819 | How much did the backlog grow so far this year? | 0.963 |
| How many tickets were resolved last month? | How many tickets were resolved this month? | 0.976 | How many tickets were resolved in the previous month? | 0.9575 |
