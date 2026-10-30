# st:Qwen/Qwen3-Embedding-0.6B holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9321 | 0.8225 | 0.9594 | 0.9904 | 0.9967 |
| **equivalent_surface (same wording=True)** | 356 | 0.9321 | 0.8225 | 0.9594 | 0.9904 | 0.9967 |
| **filter_change** | 37 | 0.7215 | 0.5546 | 0.7455 | 0.8208 | 0.8452 |
| **intent_near_miss** | 136 | 0.779 | 0.6771 | 0.7763 | 0.8713 | 0.9461 |
| **intent_near_miss (same wording=False)** | 136 | 0.779 | 0.6771 | 0.7763 | 0.8713 | 0.9461 |
| **param_near_miss** | 609 | 0.8725 | 0.7261 | 0.9004 | 0.9804 | 0.994 |
| **param_near_miss (same wording=False)** | 215 | 0.7653 | 0.6562 | 0.7761 | 0.8669 | 0.9488 |
| **param_near_miss (same wording=True)** | 394 | 0.9311 | 0.8461 | 0.9467 | 0.9848 | 0.994 |
| **paraphrase** | 250 | 0.8099 | 0.7022 | 0.8132 | 0.9161 | 0.9847 |
| equivalent_surface/amount/alias | 10 | 0.971 | 0.9439 | 0.9654 | 0.9926 | 0.9927 |
| equivalent_surface/n/alias | 20 | 0.9832 | 0.9695 | 0.9838 | 0.9921 | 0.9967 |
| equivalent_surface/period/alias | 246 | 0.9351 | 0.8272 | 0.9615 | 0.9903 | 0.9954 |
| equivalent_surface/priority/alias | 40 | 0.8706 | 0.785 | 0.8698 | 0.9815 | 0.9872 |
| equivalent_surface/service/alias | 10 | 0.9541 | 0.9203 | 0.9617 | 0.9909 | 0.9912 |
| equivalent_surface/team/alias | 30 | 0.9347 | 0.8742 | 0.9506 | 0.9873 | 0.9919 |
| filter_change/filter_added/service_count | 7 | 0.6008 | 0.5139 | 0.5488 | 0.7702 | 0.7852 |
| filter_change/filter_dropped/total_opened | 30 | 0.7497 | 0.6904 | 0.7464 | 0.826 | 0.8452 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8244 | 0.7873 | 0.8083 | 0.8829 | 0.9116 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.737 | 0.7062 | 0.7373 | 0.7674 | 0.7841 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.7508 | 0.7139 | 0.7556 | 0.7834 | 0.797 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7022 | 0.6329 | 0.7274 | 0.7574 | 0.7578 |
| intent_near_miss/direction/team_opened | 10 | 0.8729 | 0.7892 | 0.8854 | 0.9391 | 0.9461 |
| intent_near_miss/direction/team_resolved | 10 | 0.8012 | 0.7662 | 0.7985 | 0.8476 | 0.8572 |
| intent_near_miss/direction/total_opened | 7 | 0.791 | 0.7295 | 0.7756 | 0.881 | 0.8903 |
| intent_near_miss/direction/total_resolved | 7 | 0.8137 | 0.7592 | 0.7716 | 0.9116 | 0.9142 |
| intent_near_miss/grouping/top_services | 10 | 0.7645 | 0.6763 | 0.7747 | 0.841 | 0.8512 |
| intent_near_miss/grouping/top_teams | 10 | 0.7118 | 0.5793 | 0.7058 | 0.8534 | 0.8617 |
| intent_near_miss/measure/backlog_change | 14 | 0.7858 | 0.7473 | 0.793 | 0.8477 | 0.8598 |
| intent_near_miss/measure/total_opened | 7 | 0.7321 | 0.6378 | 0.748 | 0.8159 | 0.8661 |
| intent_near_miss/measure/total_resolved | 7 | 0.7655 | 0.6637 | 0.7942 | 0.8504 | 0.8678 |
| intent_near_miss/negation/priority_count | 10 | 0.8062 | 0.7637 | 0.8169 | 0.8517 | 0.8614 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8197 | 0.7537 | 0.7822 | 0.9157 | 0.9298 |
| param_near_miss/amount/neighbor | 25 | 0.8874 | 0.7197 | 0.9684 | 0.9908 | 0.9936 |
| param_near_miss/n/neighbor | 48 | 0.8704 | 0.6766 | 0.9473 | 0.9768 | 0.9866 |
| param_near_miss/period/adjacent | 243 | 0.877 | 0.7254 | 0.9066 | 0.9855 | 0.994 |
| param_near_miss/period/granularity | 163 | 0.9003 | 0.8317 | 0.9191 | 0.9631 | 0.9932 |
| param_near_miss/priority/neighbor | 50 | 0.8815 | 0.744 | 0.9029 | 0.9803 | 0.9898 |
| param_near_miss/service/neighbor | 20 | 0.7247 | 0.549 | 0.7621 | 0.8627 | 0.8889 |
| param_near_miss/team/neighbor | 60 | 0.8164 | 0.7267 | 0.8184 | 0.9083 | 0.9326 |
| paraphrase/wording/template | 250 | 0.8099 | 0.7022 | 0.8132 | 0.9161 | 0.9847 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.232 | [0.16, 0.304] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.232 | [0.16, 0.312] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.192 | [0.128, 0.264] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.1 | [0.0444, 0.1667] | 0.9556 | [0.9111, 0.9889] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6522 | [0.5652, 0.7391] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.96 | [0.92, 0.992] |
| B | 125 | 0.216 | [0.144, 0.288] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0097 | [0.0023, 0.0208] | 0.0097 | 0.0097 | 0.6039 |
| raw_oracle_entry | 0.1812 | [0.1552, 0.2316] | — | — | 0.6039 |
| split_full | 0.0097 | [0.0024, 0.0226] | 0.0097 | 0.0097 | 0.6039 |
| split_template | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many tickets were opened in the last 3 months, excluding P2 ones? | How many tickets were opened in the last 3 months, excluding P3 ones? | 0.9853 | How many tickets were opened over the past three months, excluding P2 ones? | 0.9652 |
| How many tickets were opened last year, excluding P1 ones? | How many tickets were opened last year, excluding P2 ones? | 0.9787 | How many tickets were opened in the previous year, excluding P1 ones? | 0.9589 |
| What was the longest resolution time in Q3 2026? | What was the longest resolution time in Q2 2026? | 0.9771 | What was the longest resolution time in the third quarter of 2026? | 0.9633 |
| Any tickets taking over 24 hours to close in Q3 2026? | Any tickets taking over 48 hours to close in Q3 2026? | 0.9923 | Any tickets taking over 24 hours to close in the third quarter of 2026? | 0.9791 |
| How many tickets were opened last month, excluding P4 ones? | How many tickets were opened last month, excluding P3 ones? | 0.9694 | How many tickets were opened in the previous month, excluding P4 ones? | 0.9569 |
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.9661 | How many P4 tickets were opened in the previous month? | 0.9544 |
| How many P2 tickets were opened last month? | How many P2 tickets were opened this month? | 0.9671 | How many P2 tickets were opened in the previous month? | 0.9559 |
| How many tickets did the database team resolve last month? | How many tickets did the database team resolve this month? | 0.9857 | How many tickets did the database team resolve in the previous month? | 0.9765 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.9676 | What was our overall ticket volume in the previous month? | 0.9595 |
| How many tickets were resolved last month? | How many tickets were resolved this month? | 0.969 | How many tickets were resolved in the previous month? | 0.9613 |
| Top 2 teams by ticket volume in Q3 2026 | Top 3 teams by ticket volume in Q3 2026 | 0.9866 | Top two teams by ticket volume in Q3 2026 | 0.9796 |
| Which tickets stayed open more than 48 hours last month? | Which tickets stayed open more than 24 hours last month? | 0.9875 | Which tickets stayed open more than 48 hours in the previous month? | 0.981 |
| Average time to resolve in Q3 2026 | Average time to resolve in Q2 2026 | 0.9721 | Average time to resolve in the third quarter of 2026 | 0.9692 |
| Ticket intake for the cloud team last month | Ticket intake for the cloud team this month | 0.9898 | Ticket intake for the cloud platform team last month | 0.9872 |
| How many tickets of every priority except P3 did we get in the last 3 months? | How many tickets of every priority except P2 did we get in the last 3 months? | 0.9898 | How many tickets of every priority except priority 3 did we get in the last 3 months? | 0.9872 |
