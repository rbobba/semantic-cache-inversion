# st:intfloat/e5-base-v2 prefix='query: '

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 1077 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9697 | 0.9294 | 0.9817 | 0.997 | 0.999 |
| **equivalent_surface (same wording=True)** | 356 | 0.9697 | 0.9294 | 0.9817 | 0.997 | 0.999 |
| **filter_change** | 37 | 0.8904 | 0.851 | 0.8933 | 0.9217 | 0.9361 |
| **intent_near_miss** | 136 | 0.9093 | 0.8512 | 0.9153 | 0.9605 | 0.9877 |
| **intent_near_miss (same wording=False)** | 136 | 0.9093 | 0.8512 | 0.9153 | 0.9605 | 0.9877 |
| **param_near_miss** | 609 | 0.9476 | 0.8847 | 0.9572 | 0.9958 | 0.9991 |
| **param_near_miss (same wording=False)** | 215 | 0.9054 | 0.8529 | 0.9065 | 0.9517 | 0.9871 |
| **param_near_miss (same wording=True)** | 394 | 0.9706 | 0.9365 | 0.9751 | 0.9974 | 0.9991 |
| **paraphrase** | 250 | 0.9239 | 0.8733 | 0.9302 | 0.9686 | 0.9897 |
| equivalent_surface/amount/alias | 10 | 0.9824 | 0.9649 | 0.9789 | 0.9986 | 0.9986 |
| equivalent_surface/n/alias | 20 | 0.9983 | 0.9979 | 0.9983 | 0.9988 | 0.999 |
| equivalent_surface/period/alias | 246 | 0.9721 | 0.9315 | 0.9864 | 0.9964 | 0.9983 |
| equivalent_surface/priority/alias | 40 | 0.9393 | 0.9014 | 0.9398 | 0.9727 | 0.9807 |
| equivalent_surface/service/alias | 10 | 0.9787 | 0.9616 | 0.9864 | 0.9886 | 0.9898 |
| equivalent_surface/team/alias | 30 | 0.9644 | 0.9449 | 0.9637 | 0.987 | 0.9896 |
| filter_change/filter_added/service_count | 7 | 0.8626 | 0.8197 | 0.8463 | 0.9269 | 0.9361 |
| filter_change/filter_dropped/total_opened | 30 | 0.8969 | 0.8658 | 0.8989 | 0.9212 | 0.936 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.9244 | 0.8931 | 0.9341 | 0.9549 | 0.9572 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.8748 | 0.8393 | 0.886 | 0.899 | 0.9013 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.9018 | 0.8924 | 0.9036 | 0.9128 | 0.9182 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.8962 | 0.8451 | 0.8864 | 0.9444 | 0.9467 |
| intent_near_miss/direction/team_opened | 10 | 0.9608 | 0.9362 | 0.9654 | 0.9858 | 0.9877 |
| intent_near_miss/direction/team_resolved | 10 | 0.9366 | 0.9233 | 0.936 | 0.945 | 0.9768 |
| intent_near_miss/direction/total_opened | 7 | 0.9114 | 0.8759 | 0.9137 | 0.9521 | 0.9639 |
| intent_near_miss/direction/total_resolved | 7 | 0.8998 | 0.8538 | 0.8734 | 0.9567 | 0.9628 |
| intent_near_miss/grouping/top_services | 10 | 0.8843 | 0.838 | 0.8955 | 0.9245 | 0.9318 |
| intent_near_miss/grouping/top_teams | 10 | 0.8855 | 0.8304 | 0.8882 | 0.9385 | 0.9436 |
| intent_near_miss/measure/backlog_change | 14 | 0.8896 | 0.8575 | 0.8879 | 0.9315 | 0.9409 |
| intent_near_miss/measure/total_opened | 7 | 0.8941 | 0.8658 | 0.901 | 0.9224 | 0.9266 |
| intent_near_miss/measure/total_resolved | 7 | 0.8867 | 0.8615 | 0.8881 | 0.9167 | 0.92 |
| intent_near_miss/negation/priority_count | 10 | 0.9513 | 0.9311 | 0.9603 | 0.9672 | 0.9675 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.9301 | 0.9178 | 0.9245 | 0.9521 | 0.9602 |
| param_near_miss/amount/neighbor | 25 | 0.9381 | 0.8768 | 0.9675 | 0.9855 | 0.9897 |
| param_near_miss/n/neighbor | 48 | 0.9551 | 0.8867 | 0.9817 | 0.9915 | 0.9937 |
| param_near_miss/period/adjacent | 243 | 0.9542 | 0.8949 | 0.9624 | 0.9981 | 0.9991 |
| param_near_miss/period/granularity | 163 | 0.9562 | 0.9271 | 0.965 | 0.9791 | 0.9912 |
| param_near_miss/priority/neighbor | 50 | 0.9497 | 0.9032 | 0.9545 | 0.9862 | 0.9913 |
| param_near_miss/service/neighbor | 20 | 0.8903 | 0.8033 | 0.9114 | 0.9364 | 0.946 |
| param_near_miss/team/neighbor | 60 | 0.9124 | 0.8617 | 0.9203 | 0.9474 | 0.9593 |
| paraphrase/wording/template | 250 | 0.9239 | 0.8733 | 0.9302 | 0.9686 | 0.9897 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.56 | [0.472, 0.648] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.56 | [0.464, 0.64] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.552 | [0.464, 0.64] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0111 | [0.0, 0.0333] | 0.8667 | [0.7889, 0.9225] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.6522 | [0.5652, 0.7391] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.968 | [0.936, 1.0] |
| B | 125 | 0.688 | [0.608, 0.768] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0046] | 0.0 | 0.0 | 0.6147 |
| raw_oracle_entry | 0.0826 | [0.0721, 0.1131] | — | — | 0.6147 |
| split_full | 0.3305 | [0.3117, 0.3495] | 0.3305 | 0.3733 | 0.6147 |
| split_template | 0.6156 | [0.5943, 0.6364] | 0.6156 | 0.7716 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the longest resolution time last year? | What was the longest resolution time this year? | 0.9945 | What was the longest resolution time in the previous year? | 0.9871 |
| Number of P3 tickets this month | Number of P3 tickets last month | 0.9959 | Number of P3 tickets so far this month | 0.9895 |
| Resolved tickets this week | Resolved tickets last week | 0.9899 | Resolved tickets so far this week | 0.9849 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9974 | What was our overall ticket volume so far this month? | 0.9925 |
| Resolved tickets this month | Resolved tickets last month | 0.9899 | Resolved tickets so far this month | 0.985 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.9974 | How many tickets were opened so far this week? | 0.9927 |
| Number of P1 tickets this week | Number of P1 tickets last week | 0.9954 | Number of P1 tickets so far this week | 0.9909 |
| What was the net change in open tickets last year? | What was the net change in open tickets this year? | 0.9968 | What was the net change in open tickets in the previous year? | 0.9926 |
| How many tickets of every priority except P2 did we get this week? | How many tickets of every priority except P2 did we get last week? | 0.9985 | How many tickets of every priority except P2 did we get so far this week? | 0.9944 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9965 | What was the longest resolution time in the previous month? | 0.9924 |
| How many tickets of every priority except P3 did we get this week? | How many tickets of every priority except P3 did we get last week? | 0.9985 | How many tickets of every priority except P3 did we get so far this week? | 0.9946 |
| How many tickets of every priority except P4 did we get this week? | How many tickets of every priority except P4 did we get last week? | 0.9986 | How many tickets of every priority except P4 did we get so far this week? | 0.9948 |
| How many tickets were opened this week, excluding P1 ones? | How many tickets were opened last week, excluding P1 ones? | 0.9986 | How many tickets were opened so far this week, excluding P1 ones? | 0.9951 |
| Average time to resolve this week | Average time to resolve last week | 0.9932 | Average time to resolve so far this week | 0.9897 |
| How many tickets were resolved this year? | How many tickets were resolved last year? | 0.9963 | How many tickets were resolved so far this year? | 0.9928 |
