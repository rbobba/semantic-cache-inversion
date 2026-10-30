# vertex:text-embedding-004

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 1077 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9352 | 0.8644 | 0.96 | 0.9939 | 0.9983 |
| **equivalent_surface (same wording=True)** | 356 | 0.9352 | 0.8644 | 0.96 | 0.9939 | 0.9983 |
| **filter_change** | 37 | 0.6997 | 0.5563 | 0.724 | 0.8004 | 0.825 |
| **intent_near_miss** | 136 | 0.7956 | 0.6518 | 0.8231 | 0.8989 | 0.9596 |
| **intent_near_miss (same wording=False)** | 136 | 0.7956 | 0.6518 | 0.8231 | 0.8989 | 0.9596 |
| **param_near_miss** | 609 | 0.8925 | 0.7617 | 0.9249 | 0.9864 | 0.998 |
| **param_near_miss (same wording=False)** | 215 | 0.8146 | 0.6742 | 0.8243 | 0.9357 | 0.9708 |
| **param_near_miss (same wording=True)** | 394 | 0.9351 | 0.8427 | 0.9595 | 0.992 | 0.998 |
| **paraphrase** | 250 | 0.8605 | 0.7233 | 0.8803 | 0.9554 | 0.9887 |
| equivalent_surface/amount/alias | 10 | 0.9797 | 0.9588 | 0.9777 | 0.9974 | 0.9983 |
| equivalent_surface/n/alias | 20 | 0.9966 | 0.9958 | 0.9966 | 0.9974 | 0.9982 |
| equivalent_surface/period/alias | 246 | 0.9432 | 0.8707 | 0.9689 | 0.9914 | 0.9972 |
| equivalent_surface/priority/alias | 40 | 0.8625 | 0.7285 | 0.8669 | 0.9788 | 0.9809 |
| equivalent_surface/service/alias | 10 | 0.9066 | 0.8817 | 0.9123 | 0.9361 | 0.938 |
| equivalent_surface/team/alias | 30 | 0.9198 | 0.8521 | 0.9326 | 0.9707 | 0.9867 |
| filter_change/filter_added/service_count | 7 | 0.5794 | 0.4993 | 0.5405 | 0.7039 | 0.7328 |
| filter_change/filter_dropped/total_opened | 30 | 0.7278 | 0.6539 | 0.7333 | 0.8063 | 0.825 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8238 | 0.7527 | 0.8194 | 0.9086 | 0.9104 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7834 | 0.7376 | 0.772 | 0.8381 | 0.8407 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.8415 | 0.8096 | 0.8429 | 0.8787 | 0.8895 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.7988 | 0.712 | 0.8065 | 0.8831 | 0.8873 |
| intent_near_miss/direction/team_opened | 10 | 0.9333 | 0.914 | 0.935 | 0.9553 | 0.9596 |
| intent_near_miss/direction/team_resolved | 10 | 0.8619 | 0.8335 | 0.8601 | 0.8926 | 0.9314 |
| intent_near_miss/direction/total_opened | 7 | 0.7487 | 0.6863 | 0.7632 | 0.803 | 0.8221 |
| intent_near_miss/direction/total_resolved | 7 | 0.8519 | 0.8254 | 0.8539 | 0.8806 | 0.8886 |
| intent_near_miss/grouping/top_services | 10 | 0.6509 | 0.4976 | 0.6985 | 0.7573 | 0.7723 |
| intent_near_miss/grouping/top_teams | 10 | 0.6022 | 0.4842 | 0.5893 | 0.7313 | 0.7745 |
| intent_near_miss/measure/backlog_change | 14 | 0.7661 | 0.6527 | 0.7842 | 0.8682 | 0.8892 |
| intent_near_miss/measure/total_opened | 7 | 0.7721 | 0.6663 | 0.7978 | 0.8489 | 0.8952 |
| intent_near_miss/measure/total_resolved | 7 | 0.8152 | 0.6948 | 0.87 | 0.8789 | 0.8874 |
| intent_near_miss/negation/priority_count | 10 | 0.839 | 0.7981 | 0.8524 | 0.8748 | 0.878 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8637 | 0.8407 | 0.861 | 0.8992 | 0.9157 |
| param_near_miss/amount/neighbor | 25 | 0.9064 | 0.8075 | 0.9718 | 0.9863 | 0.9905 |
| param_near_miss/n/neighbor | 48 | 0.881 | 0.7172 | 0.9239 | 0.9656 | 0.9804 |
| param_near_miss/period/adjacent | 243 | 0.917 | 0.8003 | 0.9497 | 0.9952 | 0.998 |
| param_near_miss/period/granularity | 163 | 0.9177 | 0.8295 | 0.9458 | 0.9735 | 0.9969 |
| param_near_miss/priority/neighbor | 50 | 0.8842 | 0.7889 | 0.8872 | 0.9783 | 0.9832 |
| param_near_miss/service/neighbor | 20 | 0.6423 | 0.5257 | 0.6643 | 0.7402 | 0.7648 |
| param_near_miss/team/neighbor | 60 | 0.8191 | 0.7446 | 0.8304 | 0.8813 | 0.9291 |
| paraphrase/wording/template | 250 | 0.8605 | 0.7233 | 0.8803 | 0.9554 | 0.9887 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.488 | [0.408, 0.584] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.488 | [0.3998, 0.576] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.48 | [0.392, 0.568] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0444 | [0.0111, 0.0889] | 0.6444 | [0.5556, 0.7333] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4783 | [0.3911, 0.5739] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.968 | [0.936, 0.992] |
| B | 125 | 0.6 | [0.512, 0.688] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0019 | [0.0, 0.0054] | 0.0019 | 0.0019 | 0.6147 |
| raw_oracle_entry | 0.0975 | [0.0913, 0.139] | — | — | 0.6147 |
| split_full | 0.3445 | [0.3255, 0.3825] | 0.3723 | 0.4615 | 0.6147 |
| split_template | 0.7344 | [0.7095, 0.7614] | 0.7344 | 0.8273 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many new tickets went to the network team this year? | How many new tickets went to the network team last year? | 0.9863 | How many new tickets went to the network team so far this year? | 0.9695 |
| Which tickets stayed open more than 48 hours last month? | Which tickets stayed open more than 48 hours this month? | 0.9974 | Which tickets stayed open more than 48 hours in the previous month? | 0.9807 |
| How many tickets of every priority except P4 did we get this week? | How many tickets of every priority except P4 did we get last week? | 0.9965 | How many tickets of every priority except P4 did we get so far this week? | 0.9804 |
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9753 | How many tickets were opened so far this year? | 0.9594 |
| How many tickets of every priority except P3 did we get this week? | How many tickets of every priority except P3 did we get last week? | 0.9962 | How many tickets of every priority except P3 did we get so far this week? | 0.9806 |
| How many tickets of every priority except P2 did we get this week? | How many tickets of every priority except P2 did we get last week? | 0.9963 | How many tickets of every priority except P2 did we get so far this week? | 0.9809 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.9969 | What was the net change in open tickets in the previous month? | 0.9817 |
| How many tickets were opened last year? | How many tickets were opened this year? | 0.9753 | How many tickets were opened in the previous year? | 0.9604 |
| Any tickets taking over 24 hours to close last month? | Any tickets taking over 24 hours to close this month? | 0.9872 | Any tickets taking over a day to close last month? | 0.9731 |
| How many tickets were opened last month, excluding P4 ones? | How many tickets were opened this month, excluding P4 ones? | 0.9958 | How many tickets were opened in the previous month, excluding P4 ones? | 0.9819 |
| How many P2 tickets were opened last month? | How many P2 tickets were opened this month? | 0.9947 | How many P2 tickets were opened in the previous month? | 0.9814 |
| Ticket intake for the cloud team this week | Ticket intake for the cloud team last week | 0.976 | Ticket intake for the cloud platform team this week | 0.9627 |
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.995 | How many P4 tickets were opened in the previous month? | 0.9822 |
| How many P3 tickets were opened this year? | How many P3 tickets were opened last year? | 0.9866 | How many P3 tickets were opened so far this year? | 0.974 |
| How many tickets of every priority except P3 did we get last month? | How many tickets of every priority except P3 did we get this month? | 0.9961 | How many tickets of every priority except P3 did we get in the previous month? | 0.9837 |
