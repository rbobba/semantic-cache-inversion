# vertex:text-embedding-004 task_type=SEMANTIC_SIMILARITY holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9509 | 0.8967 | 0.9676 | 0.9939 | 0.9986 |
| **equivalent_surface (same wording=True)** | 356 | 0.9509 | 0.8967 | 0.9676 | 0.9939 | 0.9986 |
| **filter_change** | 37 | 0.7796 | 0.6757 | 0.7924 | 0.849 | 0.8721 |
| **intent_near_miss** | 136 | 0.8302 | 0.7221 | 0.8436 | 0.9091 | 0.9563 |
| **intent_near_miss (same wording=False)** | 136 | 0.8302 | 0.7221 | 0.8436 | 0.9091 | 0.9563 |
| **param_near_miss** | 609 | 0.9106 | 0.8173 | 0.9293 | 0.9859 | 0.9976 |
| **param_near_miss (same wording=False)** | 215 | 0.8492 | 0.7425 | 0.8591 | 0.9418 | 0.9756 |
| **param_near_miss (same wording=True)** | 394 | 0.9441 | 0.8971 | 0.9504 | 0.9908 | 0.9976 |
| **paraphrase** | 250 | 0.8878 | 0.7895 | 0.9082 | 0.9627 | 0.9892 |
| equivalent_surface/amount/alias | 10 | 0.9733 | 0.9426 | 0.9697 | 0.9972 | 0.9986 |
| equivalent_surface/n/alias | 20 | 0.9967 | 0.9957 | 0.9965 | 0.9977 | 0.9981 |
| equivalent_surface/period/alias | 246 | 0.9539 | 0.8996 | 0.9687 | 0.9916 | 0.9982 |
| equivalent_surface/priority/alias | 40 | 0.9016 | 0.8048 | 0.9119 | 0.9856 | 0.9876 |
| equivalent_surface/service/alias | 10 | 0.9435 | 0.9226 | 0.9385 | 0.9678 | 0.9729 |
| equivalent_surface/team/alias | 30 | 0.9565 | 0.9156 | 0.9688 | 0.9846 | 0.9934 |
| filter_change/filter_added/service_count | 7 | 0.7018 | 0.6504 | 0.6768 | 0.7876 | 0.7921 |
| filter_change/filter_dropped/total_opened | 30 | 0.7977 | 0.7361 | 0.8022 | 0.8521 | 0.8721 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8498 | 0.7951 | 0.8602 | 0.9034 | 0.9092 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.8083 | 0.7701 | 0.8111 | 0.8515 | 0.859 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.8498 | 0.8301 | 0.8566 | 0.8638 | 0.8712 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7992 | 0.7398 | 0.8086 | 0.8423 | 0.8615 |
| intent_near_miss/direction/team_opened | 10 | 0.9342 | 0.9229 | 0.9314 | 0.9526 | 0.9563 |
| intent_near_miss/direction/team_resolved | 10 | 0.8671 | 0.8383 | 0.8652 | 0.9005 | 0.9218 |
| intent_near_miss/direction/total_opened | 7 | 0.8024 | 0.7617 | 0.8017 | 0.8449 | 0.8543 |
| intent_near_miss/direction/total_resolved | 7 | 0.8857 | 0.8552 | 0.8851 | 0.9132 | 0.9194 |
| intent_near_miss/grouping/top_services | 10 | 0.7655 | 0.6652 | 0.8 | 0.8403 | 0.8537 |
| intent_near_miss/grouping/top_teams | 10 | 0.7269 | 0.6361 | 0.7237 | 0.8244 | 0.8372 |
| intent_near_miss/measure/backlog_change | 14 | 0.8058 | 0.7115 | 0.8253 | 0.8778 | 0.9009 |
| intent_near_miss/measure/total_opened | 7 | 0.8119 | 0.7439 | 0.8267 | 0.8662 | 0.8935 |
| intent_near_miss/measure/total_resolved | 7 | 0.8328 | 0.7539 | 0.86 | 0.8795 | 0.8865 |
| intent_near_miss/negation/priority_count | 10 | 0.8621 | 0.8386 | 0.8704 | 0.8778 | 0.8818 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8643 | 0.8422 | 0.8592 | 0.9028 | 0.9153 |
| param_near_miss/amount/neighbor | 25 | 0.9042 | 0.813 | 0.9499 | 0.974 | 0.9849 |
| param_near_miss/n/neighbor | 48 | 0.8663 | 0.7456 | 0.8945 | 0.9339 | 0.9714 |
| param_near_miss/period/adjacent | 243 | 0.9283 | 0.8347 | 0.952 | 0.9948 | 0.9976 |
| param_near_miss/period/granularity | 163 | 0.9286 | 0.8748 | 0.941 | 0.9663 | 0.984 |
| param_near_miss/priority/neighbor | 50 | 0.9107 | 0.8375 | 0.917 | 0.9795 | 0.9903 |
| param_near_miss/service/neighbor | 20 | 0.7355 | 0.6457 | 0.762 | 0.8043 | 0.8288 |
| param_near_miss/team/neighbor | 60 | 0.8864 | 0.8179 | 0.8954 | 0.9356 | 0.9536 |
| paraphrase/wording/template | 250 | 0.8878 | 0.7895 | 0.9082 | 0.9627 | 0.9892 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.392 | [0.304, 0.48] | 0.984 | [0.96, 1.0] |
| param_near_miss | 125 | 0.392 | [0.304, 0.48] | 0.976 | [0.944, 1.0] |
| period_near_miss | 125 | 0.392 | [0.304, 0.48] | 0.976 | [0.944, 1.0] |
| entity_near_miss | 90 | 0.0 | [0.0, 0.0] | 0.7333 | [0.6444, 0.8222] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4087 | [0.3217, 0.5043] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.936 | [0.888, 0.976] |
| B | 125 | 0.512 | [0.432, 0.6] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0217 | [0.0114, 0.0576] | 0.0217 | 0.0217 | 0.6039 |
| raw_oracle_entry | 0.2899 | [0.2587, 0.3458] | — | — | 0.6039 |
| split_full | 0.2536 | [0.2076, 0.3134] | 0.2536 | 0.3164 | 0.6039 |
| split_template | 0.5966 | [0.5439, 0.6525] | 0.5966 | 0.5966 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9738 | How many tickets were opened so far this year? | 0.9492 |
| How many P3 tickets were opened this year? | How many P3 tickets were opened last year? | 0.986 | How many P3 tickets were opened so far this year? | 0.9634 |
| How many new tickets went to the network team this year? | How many new tickets went to the network team last year? | 0.9809 | How many new tickets went to the network team so far this year? | 0.9589 |
| How many new tickets went to the security team this year? | How many new tickets went to the security team last year? | 0.9841 | How many new tickets went to the security team so far this year? | 0.9686 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.995 | What was our overall ticket volume in the previous month? | 0.983 |
| How many P2 tickets were opened last month? | How many P2 tickets were opened this month? | 0.9931 | How many P2 tickets were opened in the previous month? | 0.9826 |
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.9936 | How many P4 tickets were opened in the previous month? | 0.9837 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.995 | What was our overall ticket volume so far this month? | 0.9856 |
| How many P3 tickets were opened last year? | How many P3 tickets were opened this year? | 0.986 | How many P3 tickets were opened in the previous year? | 0.9767 |
| Which tickets stayed open more than 48 hours last month? | Which tickets stayed open more than 48 hours this month? | 0.9968 | Which tickets stayed open more than 48 hours in the previous month? | 0.9878 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9965 | What was the net change in open tickets so far this month? | 0.9875 |
| How many new tickets went to the network team this week? | How many new tickets went to the network team last week? | 0.9949 | How many new tickets went to the network team so far this week? | 0.986 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.9965 | What was the net change in open tickets in the previous month? | 0.9877 |
| Ticket intake for the security team this week | Ticket intake for the security team last week | 0.97 | Ticket intake for the security team so far this week | 0.9614 |
| Number of tickets about email this week | Number of tickets about email last week | 0.9835 | Number of tickets about email so far this week | 0.976 |
