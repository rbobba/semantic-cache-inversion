# st:mixedbread-ai/mxbai-embed-large-v1 holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9297 | 0.8282 | 0.9633 | 0.9904 | 0.9978 |
| **equivalent_surface (same wording=True)** | 356 | 0.9297 | 0.8282 | 0.9633 | 0.9904 | 0.9978 |
| **filter_change** | 37 | 0.7582 | 0.6037 | 0.7726 | 0.836 | 0.8634 |
| **intent_near_miss** | 136 | 0.7945 | 0.6815 | 0.8135 | 0.8983 | 0.9394 |
| **intent_near_miss (same wording=False)** | 136 | 0.7945 | 0.6815 | 0.8135 | 0.8983 | 0.9394 |
| **param_near_miss** | 609 | 0.8802 | 0.7506 | 0.8964 | 0.988 | 0.9983 |
| **param_near_miss (same wording=False)** | 215 | 0.8004 | 0.6804 | 0.8098 | 0.8998 | 0.9722 |
| **param_near_miss (same wording=True)** | 394 | 0.9237 | 0.8446 | 0.9302 | 0.9907 | 0.9983 |
| **paraphrase** | 250 | 0.8418 | 0.727 | 0.8619 | 0.9254 | 0.9881 |
| equivalent_surface/amount/alias | 10 | 0.9629 | 0.9291 | 0.9573 | 0.9959 | 0.9975 |
| equivalent_surface/n/alias | 20 | 0.9943 | 0.9922 | 0.9939 | 0.9969 | 0.9978 |
| equivalent_surface/period/alias | 246 | 0.9281 | 0.8199 | 0.9715 | 0.9872 | 0.9938 |
| equivalent_surface/priority/alias | 40 | 0.8887 | 0.7966 | 0.9038 | 0.9505 | 0.9571 |
| equivalent_surface/service/alias | 10 | 0.9653 | 0.9475 | 0.9762 | 0.9829 | 0.9848 |
| equivalent_surface/team/alias | 30 | 0.9312 | 0.8833 | 0.936 | 0.9733 | 0.9898 |
| filter_change/filter_added/service_count | 7 | 0.6409 | 0.5594 | 0.5965 | 0.7862 | 0.812 |
| filter_change/filter_dropped/total_opened | 30 | 0.7856 | 0.7255 | 0.7795 | 0.8364 | 0.8634 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8005 | 0.74 | 0.8076 | 0.8554 | 0.8585 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7637 | 0.7174 | 0.7373 | 0.8258 | 0.8278 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.7456 | 0.7223 | 0.74 | 0.7686 | 0.7949 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7389 | 0.6552 | 0.6914 | 0.8503 | 0.8626 |
| intent_near_miss/direction/team_opened | 10 | 0.898 | 0.8671 | 0.8923 | 0.9325 | 0.9394 |
| intent_near_miss/direction/team_resolved | 10 | 0.8188 | 0.7704 | 0.8171 | 0.8618 | 0.8845 |
| intent_near_miss/direction/total_opened | 7 | 0.8189 | 0.7695 | 0.8022 | 0.8792 | 0.9034 |
| intent_near_miss/direction/total_resolved | 7 | 0.7948 | 0.7192 | 0.7882 | 0.8855 | 0.8997 |
| intent_near_miss/grouping/top_services | 10 | 0.7574 | 0.659 | 0.7877 | 0.845 | 0.8461 |
| intent_near_miss/grouping/top_teams | 10 | 0.705 | 0.5701 | 0.713 | 0.8276 | 0.8463 |
| intent_near_miss/measure/backlog_change | 14 | 0.8038 | 0.7405 | 0.8151 | 0.8526 | 0.8566 |
| intent_near_miss/measure/total_opened | 7 | 0.7582 | 0.6739 | 0.7775 | 0.8317 | 0.8624 |
| intent_near_miss/measure/total_resolved | 7 | 0.7085 | 0.6322 | 0.7058 | 0.7999 | 0.815 |
| intent_near_miss/negation/priority_count | 10 | 0.9083 | 0.8877 | 0.9032 | 0.9291 | 0.9301 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8571 | 0.8334 | 0.8385 | 0.8997 | 0.9075 |
| param_near_miss/amount/neighbor | 25 | 0.8827 | 0.7814 | 0.9214 | 0.9652 | 0.9722 |
| param_near_miss/n/neighbor | 48 | 0.8526 | 0.6657 | 0.9008 | 0.946 | 0.9605 |
| param_near_miss/period/adjacent | 243 | 0.8991 | 0.7497 | 0.9211 | 0.9936 | 0.9983 |
| param_near_miss/period/granularity | 163 | 0.894 | 0.8233 | 0.9068 | 0.9494 | 0.9667 |
| param_near_miss/priority/neighbor | 50 | 0.9025 | 0.8308 | 0.8983 | 0.9748 | 0.9879 |
| param_near_miss/service/neighbor | 20 | 0.7408 | 0.5765 | 0.7777 | 0.8242 | 0.874 |
| param_near_miss/team/neighbor | 60 | 0.815 | 0.7278 | 0.8145 | 0.8951 | 0.919 |
| paraphrase/wording/template | 250 | 0.8418 | 0.727 | 0.8619 | 0.9254 | 0.9881 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.504 | [0.416, 0.592] | 0.992 | [0.976, 1.0] |
| param_near_miss | 125 | 0.504 | [0.416, 0.592] | 0.992 | [0.976, 1.0] |
| period_near_miss | 125 | 0.504 | [0.416, 0.592] | 0.992 | [0.976, 1.0] |
| entity_near_miss | 90 | 0.0 | [0.0, 0.0] | 0.8556 | [0.7889, 0.9222] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6087 | [0.5217, 0.6957] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.928 | [0.88, 0.968] |
| B | 125 | 0.624 | [0.536, 0.712] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0097 | [0.0024, 0.0239] | 0.0097 | 0.0097 | 0.6039 |
| raw_oracle_entry | 0.2029 | [0.1774, 0.2693] | — | — | 0.6039 |
| split_full | 0.0097 | [0.0023, 0.0229] | 0.0097 | 0.0097 | 0.6039 |
| split_template | 0.0483 | [0.0229, 0.0765] | 0.0483 | 0.0483 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the longest resolution time last year? | What was the longest resolution time this year? | 0.9851 | What was the longest resolution time in the previous year? | 0.9531 |
| What was the net change in open tickets this week? | What was the net change in open tickets last week? | 0.9966 | What was the net change in open tickets so far this week? | 0.9776 |
| What was the net change in open tickets last year? | What was the net change in open tickets this year? | 0.9933 | What was the net change in open tickets in the previous year? | 0.9748 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9956 | What was the net change in open tickets so far this month? | 0.9773 |
| How many tickets were opened last year? | How many tickets were opened this year? | 0.9822 | How many tickets were opened in the previous year? | 0.9652 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9943 | What was our overall ticket volume so far this month? | 0.9772 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.9924 | How many tickets were opened so far this week? | 0.976 |
| How many tickets did the service desk resolve this week? | How many tickets did the service desk resolve last week? | 0.996 | How many tickets did the service desk resolve so far this week? | 0.9826 |
| Resolved ticket count for the database team this month | Resolved ticket count for the database team last month | 0.9935 | Resolved ticket count for the database team so far this month | 0.9801 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9887 | What was the longest resolution time in the previous month? | 0.9753 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9902 | How much did the backlog grow year to date? | 0.9774 |
| Resolved ticket count for the security team this month | Resolved ticket count for the security team last month | 0.993 | Resolved ticket count for the security team so far this month | 0.9804 |
| How many tickets were resolved last year? | How many tickets were resolved this year? | 0.9859 | How many tickets were resolved in the previous year? | 0.9737 |
| How many P3 tickets were opened last year? | How many P3 tickets were opened this year? | 0.9899 | How many P3 tickets were opened in the previous year? | 0.978 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.9956 | What was the net change in open tickets in the previous month? | 0.9839 |
