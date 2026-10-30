# vertex:gemini-embedding-001 holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9364 | 0.8643 | 0.9557 | 0.992 | 0.9975 |
| **equivalent_surface (same wording=True)** | 356 | 0.9364 | 0.8643 | 0.9557 | 0.992 | 0.9975 |
| **filter_change** | 37 | 0.7997 | 0.7148 | 0.8061 | 0.8668 | 0.8926 |
| **intent_near_miss** | 136 | 0.8477 | 0.777 | 0.8582 | 0.9125 | 0.9508 |
| **intent_near_miss (same wording=False)** | 136 | 0.8477 | 0.777 | 0.8582 | 0.9125 | 0.9508 |
| **param_near_miss** | 609 | 0.9141 | 0.831 | 0.9272 | 0.9862 | 0.996 |
| **param_near_miss (same wording=False)** | 215 | 0.8615 | 0.7715 | 0.8718 | 0.9318 | 0.9727 |
| **param_near_miss (same wording=True)** | 394 | 0.9428 | 0.8761 | 0.958 | 0.9895 | 0.996 |
| **paraphrase** | 250 | 0.8927 | 0.8184 | 0.9043 | 0.9534 | 0.9814 |
| equivalent_surface/amount/alias | 10 | 0.9733 | 0.9504 | 0.9737 | 0.9938 | 0.9943 |
| equivalent_surface/n/alias | 20 | 0.9945 | 0.9911 | 0.995 | 0.9968 | 0.9975 |
| equivalent_surface/period/alias | 246 | 0.9385 | 0.8706 | 0.9592 | 0.9905 | 0.9953 |
| equivalent_surface/priority/alias | 40 | 0.8767 | 0.7855 | 0.8841 | 0.9715 | 0.9795 |
| equivalent_surface/service/alias | 10 | 0.9344 | 0.9122 | 0.9394 | 0.9572 | 0.9575 |
| equivalent_surface/team/alias | 30 | 0.9486 | 0.9008 | 0.9557 | 0.9805 | 0.9889 |
| filter_change/filter_added/service_count | 7 | 0.7575 | 0.7053 | 0.718 | 0.855 | 0.88 |
| filter_change/filter_dropped/total_opened | 30 | 0.8096 | 0.7501 | 0.8122 | 0.8648 | 0.8926 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8488 | 0.7993 | 0.8268 | 0.9195 | 0.9355 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.8221 | 0.787 | 0.8198 | 0.8656 | 0.8656 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.8736 | 0.836 | 0.8828 | 0.9038 | 0.9106 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.8598 | 0.836 | 0.8571 | 0.8888 | 0.8906 |
| intent_near_miss/direction/team_opened | 10 | 0.9218 | 0.9044 | 0.919 | 0.9479 | 0.9508 |
| intent_near_miss/direction/team_resolved | 10 | 0.8914 | 0.865 | 0.8953 | 0.9125 | 0.9435 |
| intent_near_miss/direction/total_opened | 7 | 0.8395 | 0.7846 | 0.8499 | 0.8892 | 0.9035 |
| intent_near_miss/direction/total_resolved | 7 | 0.8946 | 0.8488 | 0.9095 | 0.9308 | 0.9462 |
| intent_near_miss/grouping/top_services | 10 | 0.7723 | 0.6728 | 0.7893 | 0.8339 | 0.8825 |
| intent_near_miss/grouping/top_teams | 10 | 0.7704 | 0.6481 | 0.7824 | 0.8731 | 0.8938 |
| intent_near_miss/measure/backlog_change | 14 | 0.8176 | 0.7782 | 0.8055 | 0.87 | 0.898 |
| intent_near_miss/measure/total_opened | 7 | 0.8033 | 0.7399 | 0.8062 | 0.8645 | 0.897 |
| intent_near_miss/measure/total_resolved | 7 | 0.8362 | 0.7808 | 0.8507 | 0.8808 | 0.8968 |
| intent_near_miss/negation/priority_count | 10 | 0.8756 | 0.8262 | 0.8832 | 0.9019 | 0.9142 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8885 | 0.8514 | 0.8849 | 0.9224 | 0.9248 |
| param_near_miss/amount/neighbor | 25 | 0.9296 | 0.8497 | 0.9631 | 0.9843 | 0.9916 |
| param_near_miss/n/neighbor | 48 | 0.9253 | 0.8209 | 0.9591 | 0.9843 | 0.9889 |
| param_near_miss/period/adjacent | 243 | 0.9277 | 0.8492 | 0.9444 | 0.9916 | 0.996 |
| param_near_miss/period/granularity | 163 | 0.9195 | 0.846 | 0.9357 | 0.9717 | 0.9836 |
| param_near_miss/priority/neighbor | 50 | 0.9102 | 0.8391 | 0.9133 | 0.9821 | 0.9902 |
| param_near_miss/service/neighbor | 20 | 0.7661 | 0.6859 | 0.7974 | 0.8361 | 0.8458 |
| param_near_miss/team/neighbor | 60 | 0.8813 | 0.835 | 0.8783 | 0.9455 | 0.9608 |
| paraphrase/wording/template | 250 | 0.8927 | 0.8184 | 0.9043 | 0.9534 | 0.9814 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.512 | [0.424, 0.6] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.512 | [0.4318, 0.6] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.504 | [0.408, 0.592] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0556 | [0.0111, 0.1111] | 0.8222 | [0.7444, 0.8892] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4783 | [0.3826, 0.5652] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.984 | [0.96, 1.0] |
| B | 125 | 0.584 | [0.496, 0.672] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0097 | [0.0024, 0.026] | 0.0097 | 0.0097 | 0.6039 |
| raw_oracle_entry | 0.2778 | [0.2469, 0.3358] | — | — | 0.6039 |
| split_full | 0.0894 | [0.0622, 0.1238] | 0.0894 | 0.0894 | 0.6039 |
| split_template | 0.256 | [0.1875, 0.3208] | 0.256 | 0.256 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Maximum time to resolve this month | Maximum time to resolve last month | 0.9436 | Maximum time to resolve so far this month | 0.9095 |
| Maximum time to resolve this year | Maximum time to resolve last year | 0.9297 | Maximum time to resolve year to date | 0.8957 |
| Ticket volume for laptops last year | Ticket volume for laptops this year | 0.9747 | Ticket volume for laptops in the previous year | 0.9524 |
| How many tickets of every priority except P3 did we get last month? | How many tickets of every priority except P3 did we get this month? | 0.9906 | How many tickets of every priority except P3 did we get in the previous month? | 0.9725 |
| What was the net change in open tickets last year? | What was the net change in open tickets this year? | 0.9798 | What was the net change in open tickets in the previous year? | 0.9641 |
| How many tickets of every priority except P3 did we get this week? | How many tickets of every priority except P3 did we get last week? | 0.9918 | How many tickets of every priority except P3 did we get so far this week? | 0.9785 |
| How many new tickets went to the security team this year? | How many new tickets went to the security team last year? | 0.9792 | How many new tickets went to the security team so far this year? | 0.9667 |
| How many tickets were resolved last year? | How many tickets were resolved this year? | 0.9867 | How many tickets were resolved in the previous year? | 0.9742 |
| How many P4 tickets were opened last month? | How many P4 tickets were opened this month? | 0.9931 | How many P4 tickets were opened in the previous month? | 0.9809 |
| How many tickets of every priority except P2 did we get this week? | How many tickets of every priority except P2 did we get last week? | 0.9922 | How many tickets of every priority except P2 did we get so far this week? | 0.98 |
| Average time to resolve this month | Average time to resolve last month | 0.969 | Average time to resolve so far this month | 0.9573 |
| How many tickets did the security team resolve last year? | How many tickets did the security team resolve this year? | 0.9908 | How many tickets did the security team resolve in the previous year? | 0.9791 |
| Ticket volume for printing this year | Ticket volume for printing last year | 0.9433 | Ticket volume for printing so far this year | 0.9319 |
| How many tickets of every priority except P4 did we get this year? | How many tickets of every priority except P4 did we get last year? | 0.9865 | How many tickets of every priority except priority 4 did we get this year? | 0.9756 |
| How long did tickets take to resolve on average last year? | How long did tickets take to resolve on average this year? | 0.9863 | How long did tickets take to resolve on average in the previous year? | 0.9757 |
