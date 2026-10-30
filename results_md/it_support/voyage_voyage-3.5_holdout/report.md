# voyage:voyage-3.5 holdout

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 414 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.8994 | 0.7783 | 0.923 | 0.9798 | 0.9937 |
| **equivalent_surface (same wording=True)** | 356 | 0.8994 | 0.7783 | 0.923 | 0.9798 | 0.9937 |
| **filter_change** | 37 | 0.6624 | 0.5701 | 0.6689 | 0.7533 | 0.8179 |
| **intent_near_miss** | 136 | 0.74 | 0.6025 | 0.7575 | 0.8454 | 0.9356 |
| **intent_near_miss (same wording=False)** | 136 | 0.74 | 0.6025 | 0.7575 | 0.8454 | 0.9356 |
| **param_near_miss** | 609 | 0.8349 | 0.6958 | 0.8496 | 0.9683 | 0.9923 |
| **param_near_miss (same wording=False)** | 215 | 0.7502 | 0.628 | 0.7546 | 0.8701 | 0.9374 |
| **param_near_miss (same wording=True)** | 394 | 0.8812 | 0.7798 | 0.885 | 0.9753 | 0.9923 |
| **paraphrase** | 250 | 0.8181 | 0.6951 | 0.8396 | 0.9171 | 0.978 |
| equivalent_surface/amount/alias | 10 | 0.9227 | 0.8639 | 0.9082 | 0.9828 | 0.9937 |
| equivalent_surface/n/alias | 20 | 0.9841 | 0.976 | 0.9865 | 0.9917 | 0.9932 |
| equivalent_surface/period/alias | 246 | 0.894 | 0.7764 | 0.9237 | 0.9755 | 0.991 |
| equivalent_surface/priority/alias | 40 | 0.8605 | 0.6999 | 0.8905 | 0.9662 | 0.9736 |
| equivalent_surface/service/alias | 10 | 0.9087 | 0.8806 | 0.9146 | 0.9285 | 0.9441 |
| equivalent_surface/team/alias | 30 | 0.9286 | 0.8891 | 0.9228 | 0.9735 | 0.9857 |
| filter_change/filter_added/service_count | 7 | 0.5964 | 0.5301 | 0.5574 | 0.705 | 0.7563 |
| filter_change/filter_dropped/total_opened | 30 | 0.6778 | 0.5964 | 0.6721 | 0.7526 | 0.8179 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.7421 | 0.669 | 0.7422 | 0.8133 | 0.8285 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7011 | 0.6423 | 0.7197 | 0.7464 | 0.7511 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.7696 | 0.7444 | 0.7676 | 0.7865 | 0.8168 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.6864 | 0.6329 | 0.6866 | 0.7422 | 0.7605 |
| intent_near_miss/direction/team_opened | 10 | 0.8849 | 0.8344 | 0.8796 | 0.9323 | 0.9356 |
| intent_near_miss/direction/team_resolved | 10 | 0.8051 | 0.7719 | 0.807 | 0.8255 | 0.8388 |
| intent_near_miss/direction/total_opened | 7 | 0.7223 | 0.6095 | 0.7083 | 0.8272 | 0.8709 |
| intent_near_miss/direction/total_resolved | 7 | 0.8035 | 0.7259 | 0.7995 | 0.8847 | 0.9052 |
| intent_near_miss/grouping/top_services | 10 | 0.6893 | 0.5763 | 0.7189 | 0.7931 | 0.8369 |
| intent_near_miss/grouping/top_teams | 10 | 0.6963 | 0.5803 | 0.7025 | 0.8077 | 0.8111 |
| intent_near_miss/measure/backlog_change | 14 | 0.684 | 0.5851 | 0.6657 | 0.7828 | 0.807 |
| intent_near_miss/measure/total_opened | 7 | 0.6399 | 0.5379 | 0.6551 | 0.738 | 0.7868 |
| intent_near_miss/measure/total_resolved | 7 | 0.6746 | 0.566 | 0.7076 | 0.7531 | 0.7855 |
| intent_near_miss/negation/priority_count | 10 | 0.7676 | 0.7325 | 0.7573 | 0.8291 | 0.8521 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.8081 | 0.7673 | 0.8076 | 0.8617 | 0.8702 |
| param_near_miss/amount/neighbor | 25 | 0.8288 | 0.6625 | 0.9005 | 0.9304 | 0.9376 |
| param_near_miss/n/neighbor | 48 | 0.8141 | 0.6585 | 0.8542 | 0.9255 | 0.9458 |
| param_near_miss/period/adjacent | 243 | 0.8661 | 0.7105 | 0.8861 | 0.9793 | 0.9923 |
| param_near_miss/period/granularity | 163 | 0.8357 | 0.7334 | 0.8477 | 0.9148 | 0.9758 |
| param_near_miss/priority/neighbor | 50 | 0.8542 | 0.7498 | 0.8356 | 0.9732 | 0.9777 |
| param_near_miss/service/neighbor | 20 | 0.6204 | 0.5236 | 0.6445 | 0.7121 | 0.7456 |
| param_near_miss/team/neighbor | 60 | 0.7814 | 0.68 | 0.789 | 0.8692 | 0.9002 |
| paraphrase/wording/template | 250 | 0.8181 | 0.6951 | 0.8396 | 0.9171 | 0.978 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.424 | [0.336, 0.512] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.424 | [0.336, 0.504] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.424 | [0.336, 0.5122] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0111 | [0.0, 0.0444] | 0.7333 | [0.6444, 0.8222] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.487 | [0.3913, 0.5826] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.912 | [0.856, 0.96] |
| B | 125 | 0.552 | [0.464, 0.64] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0242 | [0.0104, 0.0435] | 0.0242 | 0.0242 | 0.6039 |
| raw_oracle_entry | 0.2923 | [0.2667, 0.3629] | — | — | 0.6039 |
| split_full | 0.0845 | [0.0549, 0.1155] | 0.0845 | 0.0845 | 0.6039 |
| split_template | 0.244 | [0.1908, 0.3028] | 0.244 | 0.244 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many tickets were opened this year? | How many tickets were opened last year? | 0.9515 | How many tickets were opened so far this year? | 0.8689 |
| How many P3 tickets were opened this year? | How many P3 tickets were opened last year? | 0.968 | How many P3 tickets were opened so far this year? | 0.9105 |
| Maximum time to resolve this month | Maximum time to resolve last month | 0.913 | Maximum time to resolve so far this month | 0.8591 |
| How many tickets were resolved this year? | How many tickets were resolved last year? | 0.9682 | How many tickets were resolved so far this year? | 0.9241 |
| How many tickets were opened this week? | How many tickets were opened last week? | 0.959 | How many tickets were opened so far this week? | 0.9188 |
| Average time to resolve this year | Average time to resolve last year | 0.9218 | Average time to resolve so far this year | 0.8856 |
| What was the net change in open tickets this month? | What was the net change in open tickets last month? | 0.9793 | What was the net change in open tickets so far this month? | 0.945 |
| What was the longest resolution time last year? | What was the longest resolution time this year? | 0.9577 | What was the longest resolution time in the previous year? | 0.9259 |
| How much did the backlog grow this year? | How much did the backlog grow last year? | 0.9214 | How much did the backlog grow so far this year? | 0.8902 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9761 | What was the longest resolution time in the previous month? | 0.9463 |
| Which tickets stayed open more than 48 hours this week? | Which tickets stayed open more than 48 hours last week? | 0.9806 | Which tickets stayed open more than 48 hours so far this week? | 0.9508 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9807 | What was our overall ticket volume so far this month? | 0.9531 |
| What was the net change in open tickets this week? | What was the net change in open tickets last week? | 0.9762 | What was the net change in open tickets so far this week? | 0.9507 |
| How many new tickets went to the network team this week? | How many new tickets went to the network team last week? | 0.9867 | How many new tickets went to the network team so far this week? | 0.963 |
| Average time to resolve this month | Average time to resolve last month | 0.9461 | Average time to resolve so far this month | 0.9226 |
