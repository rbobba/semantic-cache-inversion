# st:Snowflake/snowflake-arctic-embed-l-v2.0 prefix='query: '

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 1077 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.8945 | 0.763 | 0.9401 | 0.9885 | 0.9986 |
| **equivalent_surface (same wording=True)** | 356 | 0.8945 | 0.763 | 0.9401 | 0.9885 | 0.9986 |
| **filter_change** | 37 | 0.6153 | 0.4605 | 0.6153 | 0.7518 | 0.8116 |
| **intent_near_miss** | 136 | 0.725 | 0.5525 | 0.7535 | 0.8607 | 0.932 |
| **intent_near_miss (same wording=False)** | 136 | 0.725 | 0.5525 | 0.7535 | 0.8607 | 0.932 |
| **param_near_miss** | 609 | 0.8346 | 0.6679 | 0.8566 | 0.977 | 0.9923 |
| **param_near_miss (same wording=False)** | 215 | 0.7252 | 0.5756 | 0.7339 | 0.8821 | 0.9555 |
| **param_near_miss (same wording=True)** | 394 | 0.8943 | 0.7684 | 0.9199 | 0.9824 | 0.9923 |
| **paraphrase** | 250 | 0.7915 | 0.6506 | 0.8101 | 0.915 | 0.9936 |
| equivalent_surface/amount/alias | 10 | 0.9308 | 0.8702 | 0.9142 | 0.9962 | 0.9969 |
| equivalent_surface/n/alias | 20 | 0.9953 | 0.9929 | 0.9951 | 0.9972 | 0.9986 |
| equivalent_surface/period/alias | 246 | 0.8964 | 0.7623 | 0.9529 | 0.9847 | 0.9961 |
| equivalent_surface/priority/alias | 40 | 0.8107 | 0.6398 | 0.8457 | 0.9439 | 0.9482 |
| equivalent_surface/service/alias | 10 | 0.918 | 0.8882 | 0.915 | 0.9511 | 0.9562 |
| equivalent_surface/team/alias | 30 | 0.9034 | 0.8495 | 0.9131 | 0.9595 | 0.9783 |
| filter_change/filter_added/service_count | 7 | 0.5062 | 0.4098 | 0.4421 | 0.6888 | 0.7447 |
| filter_change/filter_dropped/total_opened | 30 | 0.6408 | 0.5643 | 0.6177 | 0.763 | 0.8116 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.7588 | 0.6493 | 0.7807 | 0.8318 | 0.8501 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.6106 | 0.5266 | 0.5879 | 0.7014 | 0.7376 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.681 | 0.646 | 0.6823 | 0.7208 | 0.7644 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.6484 | 0.5733 | 0.5941 | 0.7564 | 0.7781 |
| intent_near_miss/direction/team_opened | 10 | 0.8829 | 0.8488 | 0.8766 | 0.9239 | 0.9306 |
| intent_near_miss/direction/team_resolved | 10 | 0.7975 | 0.7649 | 0.7951 | 0.8301 | 0.8609 |
| intent_near_miss/direction/total_opened | 7 | 0.73 | 0.6486 | 0.7042 | 0.8194 | 0.8723 |
| intent_near_miss/direction/total_resolved | 7 | 0.79 | 0.7363 | 0.7733 | 0.8667 | 0.9045 |
| intent_near_miss/grouping/top_services | 10 | 0.6336 | 0.4594 | 0.6589 | 0.7853 | 0.8423 |
| intent_near_miss/grouping/top_teams | 10 | 0.6578 | 0.4713 | 0.6721 | 0.8201 | 0.8759 |
| intent_near_miss/measure/backlog_change | 14 | 0.6806 | 0.5556 | 0.6621 | 0.8111 | 0.8983 |
| intent_near_miss/measure/total_opened | 7 | 0.6743 | 0.5542 | 0.6785 | 0.7989 | 0.8605 |
| intent_near_miss/measure/total_resolved | 7 | 0.6645 | 0.5507 | 0.6789 | 0.7672 | 0.8382 |
| intent_near_miss/negation/priority_count | 10 | 0.8245 | 0.7988 | 0.8379 | 0.8478 | 0.8537 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8215 | 0.7719 | 0.8027 | 0.8995 | 0.932 |
| param_near_miss/amount/neighbor | 25 | 0.8312 | 0.6785 | 0.9059 | 0.9417 | 0.9622 |
| param_near_miss/n/neighbor | 48 | 0.8633 | 0.6421 | 0.9324 | 0.9709 | 0.9885 |
| param_near_miss/period/adjacent | 243 | 0.8551 | 0.6793 | 0.8914 | 0.9866 | 0.9923 |
| param_near_miss/period/granularity | 163 | 0.8534 | 0.7222 | 0.8894 | 0.9396 | 0.9876 |
| param_near_miss/priority/neighbor | 50 | 0.8286 | 0.7275 | 0.8143 | 0.9569 | 0.9685 |
| param_near_miss/service/neighbor | 20 | 0.6331 | 0.4657 | 0.7007 | 0.755 | 0.7643 |
| param_near_miss/team/neighbor | 60 | 0.7513 | 0.6425 | 0.774 | 0.8376 | 0.8859 |
| paraphrase/wording/template | 250 | 0.7915 | 0.6506 | 0.8101 | 0.915 | 0.9936 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.456 | [0.3678, 0.544] | 0.984 | [0.96, 1.0] |
| param_near_miss | 125 | 0.456 | [0.368, 0.536] | 0.984 | [0.96, 1.0] |
| period_near_miss | 125 | 0.456 | [0.368, 0.544] | 0.984 | [0.952, 1.0] |
| entity_near_miss | 90 | 0.0 | [0.0, 0.0] | 0.8 | [0.7111, 0.8778] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6 | [0.513, 0.687] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.912 | [0.864, 0.96] |
| B | 125 | 0.56 | [0.48, 0.648] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.026 | [0.0179, 0.0383] | 0.026 | 0.0288 | 0.6147 |
| raw_oracle_entry | 0.1077 | [0.1035, 0.1459] | — | — | 0.6147 |
| split_full | 0.338 | [0.3195, 0.3903] | 0.3788 | 0.4067 | 0.6147 |
| split_template | 0.7437 | [0.7145, 0.7716] | 0.7437 | 0.7837 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Resolved tickets this week | Resolved tickets last week | 0.9639 | Resolved tickets so far this week | 0.9385 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9802 | What was our overall ticket volume so far this month? | 0.9553 |
| How many tickets were resolved this year? | How many tickets were resolved last year? | 0.9767 | How many tickets were resolved so far this year? | 0.9519 |
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9702 | How many tickets were opened year to date? | 0.9456 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.9864 | What was the net change in open tickets in the previous month? | 0.9645 |
| How many tickets of every priority except P4 did we get this year? | How many tickets of every priority except P4 did we get last year? | 0.9877 | How many tickets of every priority except P4 did we get year to date? | 0.9669 |
| How many tickets were resolved last month? | How many tickets were resolved this month? | 0.98 | How many tickets were resolved in the previous month? | 0.9606 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.977 | How many tickets were opened so far this week? | 0.9587 |
| What was the net change in open tickets this week? | What was the net change in open tickets last week? | 0.986 | What was the net change in open tickets so far this week? | 0.9681 |
| Resolved tickets this month | Resolved tickets last month | 0.9554 | Resolved tickets so far this month | 0.9393 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9824 | What was the longest resolution time in the previous month? | 0.9666 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9864 | What was the net change in open tickets so far this month? | 0.9711 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.9802 | What was our overall ticket volume in the previous month? | 0.9659 |
| How many P3 tickets were opened this year? | How many P3 tickets were opened last year? | 0.9879 | How many P3 tickets were opened year to date? | 0.9737 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9775 | How much did the backlog grow so far this year? | 0.9643 |
