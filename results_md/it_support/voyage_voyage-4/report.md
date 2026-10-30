# voyage:voyage-4

Dataset sha256(pairs) `1d79815b26be9c19`, 125 cached questions, 1077 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 356 | 0.9117 | 0.7761 | 0.9554 | 0.988 | 0.9972 |
| **equivalent_surface (same wording=True)** | 356 | 0.9117 | 0.7761 | 0.9554 | 0.988 | 0.9972 |
| **filter_change** | 37 | 0.6799 | 0.4898 | 0.7045 | 0.7851 | 0.8235 |
| **intent_near_miss** | 136 | 0.7628 | 0.6429 | 0.7874 | 0.8643 | 0.925 |
| **intent_near_miss (same wording=False)** | 136 | 0.7628 | 0.6429 | 0.7874 | 0.8643 | 0.925 |
| **param_near_miss** | 609 | 0.8532 | 0.7116 | 0.884 | 0.9631 | 0.9876 |
| **param_near_miss (same wording=False)** | 215 | 0.7644 | 0.6369 | 0.7794 | 0.8746 | 0.9386 |
| **param_near_miss (same wording=True)** | 394 | 0.9017 | 0.7856 | 0.9205 | 0.973 | 0.9876 |
| **paraphrase** | 250 | 0.8412 | 0.7498 | 0.8487 | 0.9253 | 0.9852 |
| equivalent_surface/amount/alias | 10 | 0.9617 | 0.9215 | 0.9676 | 0.987 | 0.9967 |
| equivalent_surface/n/alias | 20 | 0.9928 | 0.9911 | 0.9919 | 0.9971 | 0.9972 |
| equivalent_surface/period/alias | 246 | 0.9101 | 0.7782 | 0.9588 | 0.9865 | 0.996 |
| equivalent_surface/priority/alias | 40 | 0.8308 | 0.7176 | 0.8314 | 0.9678 | 0.9769 |
| equivalent_surface/service/alias | 10 | 0.9518 | 0.9396 | 0.9555 | 0.9666 | 0.9673 |
| equivalent_surface/team/alias | 30 | 0.9479 | 0.9202 | 0.9522 | 0.9761 | 0.985 |
| filter_change/filter_added/service_count | 7 | 0.5267 | 0.4352 | 0.4591 | 0.7025 | 0.7065 |
| filter_change/filter_dropped/total_opened | 30 | 0.7156 | 0.6396 | 0.7107 | 0.7869 | 0.8235 |
| intent_near_miss/aggregation/avg_resolution | 7 | 0.8139 | 0.7657 | 0.8192 | 0.8573 | 0.863 |
| intent_near_miss/aggregation/longest_resolution | 7 | 0.7683 | 0.7386 | 0.7724 | 0.79 | 0.7955 |
| intent_near_miss/aggregation/team_avg_resolution | 10 | 0.8111 | 0.7777 | 0.8179 | 0.8373 | 0.8404 |
| intent_near_miss/aggregation/team_resolved | 10 | 0.737 | 0.6458 | 0.7603 | 0.8081 | 0.809 |
| intent_near_miss/direction/team_opened | 10 | 0.8925 | 0.8614 | 0.9023 | 0.9161 | 0.925 |
| intent_near_miss/direction/team_resolved | 10 | 0.8118 | 0.7716 | 0.8059 | 0.8589 | 0.8652 |
| intent_near_miss/direction/total_opened | 7 | 0.7622 | 0.706 | 0.7444 | 0.8353 | 0.8391 |
| intent_near_miss/direction/total_resolved | 7 | 0.7861 | 0.707 | 0.7797 | 0.8695 | 0.885 |
| intent_near_miss/grouping/top_services | 10 | 0.7034 | 0.5749 | 0.7199 | 0.8141 | 0.8277 |
| intent_near_miss/grouping/top_teams | 10 | 0.6474 | 0.4712 | 0.671 | 0.785 | 0.8054 |
| intent_near_miss/measure/backlog_change | 14 | 0.7215 | 0.6415 | 0.7121 | 0.8239 | 0.8518 |
| intent_near_miss/measure/total_opened | 7 | 0.6445 | 0.531 | 0.6768 | 0.7363 | 0.7862 |
| intent_near_miss/measure/total_resolved | 7 | 0.6893 | 0.5712 | 0.7227 | 0.7846 | 0.8246 |
| intent_near_miss/negation/priority_count | 10 | 0.8142 | 0.7875 | 0.8062 | 0.8479 | 0.8509 |
| intent_near_miss/negation/priority_count_excluding | 10 | 0.822 | 0.7501 | 0.8057 | 0.8903 | 0.898 |
| param_near_miss/amount/neighbor | 25 | 0.8671 | 0.7252 | 0.9226 | 0.9718 | 0.9834 |
| param_near_miss/n/neighbor | 48 | 0.8452 | 0.6843 | 0.9065 | 0.935 | 0.9539 |
| param_near_miss/period/adjacent | 243 | 0.8696 | 0.7356 | 0.8997 | 0.9731 | 0.984 |
| param_near_miss/period/granularity | 163 | 0.87 | 0.7515 | 0.8962 | 0.943 | 0.9814 |
| param_near_miss/priority/neighbor | 50 | 0.8855 | 0.7774 | 0.8965 | 0.978 | 0.9876 |
| param_near_miss/service/neighbor | 20 | 0.6276 | 0.4674 | 0.6756 | 0.7282 | 0.7695 |
| param_near_miss/team/neighbor | 60 | 0.7902 | 0.684 | 0.803 | 0.8829 | 0.9061 |
| paraphrase/wording/template | 250 | 0.8412 | 0.7498 | 0.8487 | 0.9253 | 0.9852 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 125 | 0.016 | [0.0, 0.04] | 1.0 | [1.0, 1.0] |
| param_near_miss | 125 | 0.016 | [0.0, 0.04] | 1.0 | [1.0, 1.0] |
| period_near_miss | 125 | 0.008 | [0.0, 0.024] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 90 | 0.0222 | [0.0, 0.0556] | 0.8 | [0.7222, 0.8778] |
| intent_near_miss | 115 | 0.0 | [0.0, 0.0] | 0.4696 | [0.3739, 0.5565] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 125 | 0.912 | [0.856, 0.96] |
| B | 125 | 0.016 | [0.0, 0.04] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0353 | [0.0257, 0.076] | 0.0353 | 0.0631 | 0.6147 |
| raw_oracle_entry | 0.1848 | [0.1819, 0.2197] | — | — | 0.6147 |
| split_full | 0.3612 | [0.3389, 0.3964] | 0.3816 | 0.48 | 0.6147 |
| split_template | 0.7289 | [0.6988, 0.7573] | 0.7289 | 0.9146 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many tickets of every priority except P3 did we get last month? | How many tickets of every priority except P2 did we get last month? | 0.9826 | How many tickets of every priority except priority 3 did we get last month? | 0.974 |
| Any tickets taking over 24 hours to close in Q3 2026? | Any tickets taking over 48 hours to close in Q3 2026? | 0.9834 | Any tickets taking over a day to close in Q3 2026? | 0.9754 |
| How many tickets were opened last year, excluding P1 ones? | How many tickets were opened last year, excluding P2 ones? | 0.9746 | How many tickets were opened in the previous year, excluding P1 ones? | 0.9761 |
| How long did tickets take to resolve on average last month? | How long did tickets take to resolve on average this month? | 0.976 | How long did tickets take to resolve on average in the previous month? | 0.978 |
| What was the longest resolution time last month? | What was the longest resolution time this month? | 0.9713 | What was the longest resolution time in the previous month? | 0.9737 |
| How many tickets of every priority except P4 did we get this year? | How many tickets of every priority except P3 did we get this year? | 0.9752 | How many tickets of every priority except P4 did we get so far this year? | 0.9785 |
| How many tickets of every priority except P2 did we get this week? | How many tickets of every priority except P1 did we get this week? | 0.9835 | How many tickets of every priority except P2 did we get so far this week? | 0.9876 |
| How many tickets of every priority except P3 did we get in the last 3 months? | How many tickets of every priority except P2 did we get in the last 3 months? | 0.9876 | How many tickets of every priority except P3 did we get over the past three months? | 0.992 |
| Ticket volume for the VPN this week | Ticket volume for the VPN last week | 0.9765 | Ticket volume for the VPN so far this week | 0.9813 |
| Ticket volume for printing this week | Ticket volume for printing last week | 0.9702 | Ticket volume for printing so far this week | 0.9756 |
| What was our overall ticket volume last month? | What was our overall ticket volume this month? | 0.9649 | What was our overall ticket volume in the previous month? | 0.9706 |
| What was our overall ticket volume this month? | What was our overall ticket volume last month? | 0.9649 | What was our overall ticket volume so far this month? | 0.9707 |
| Which tickets stayed open more than 48 hours last month? | Which tickets stayed open more than 48 hours this month? | 0.9827 | Which tickets stayed open more than 48 hours in the previous month? | 0.9897 |
| What was the net change in open tickets last month? | What was the net change in open tickets this month? | 0.971 | What was the net change in open tickets in the previous month? | 0.978 |
| Any tickets taking over 24 hours to close last month? | Any tickets taking over 24 hours to close this month? | 0.9742 | Any tickets taking over 24 hours to close in the previous month? | 0.9812 |
