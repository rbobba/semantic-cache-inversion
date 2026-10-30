# voyage:voyage-3-large holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9335 | 0.8468 | 0.9582 | 0.9843 | 0.9965 |
| **equivalent_surface (same wording=True)** | 370 | 0.9335 | 0.8468 | 0.9582 | 0.9843 | 0.9965 |
| **filter_change** | 37 | 0.7653 | 0.6681 | 0.7688 | 0.8355 | 0.8791 |
| **intent_near_miss** | 142 | 0.7839 | 0.7048 | 0.76 | 0.9006 | 0.9723 |
| **intent_near_miss (same wording=False)** | 142 | 0.7839 | 0.7048 | 0.76 | 0.9006 | 0.9723 |
| **param_near_miss** | 714 | 0.8862 | 0.7952 | 0.8937 | 0.9684 | 0.9911 |
| **param_near_miss (same wording=False)** | 255 | 0.8437 | 0.7625 | 0.8476 | 0.9262 | 0.9719 |
| **param_near_miss (same wording=True)** | 459 | 0.9099 | 0.8342 | 0.918 | 0.9754 | 0.9911 |
| **paraphrase** | 290 | 0.903 | 0.8306 | 0.9143 | 0.9582 | 0.9924 |
| equivalent_surface/amount/alias | 10 | 0.9498 | 0.9118 | 0.9569 | 0.9719 | 0.974 |
| equivalent_surface/clinic/alias | 40 | 0.9357 | 0.883 | 0.9411 | 0.9597 | 0.9874 |
| equivalent_surface/department/alias | 30 | 0.9658 | 0.9541 | 0.966 | 0.9784 | 0.9809 |
| equivalent_surface/n/alias | 20 | 0.9917 | 0.9869 | 0.9925 | 0.9951 | 0.9965 |
| equivalent_surface/payer/alias | 2 | 0.8917 | 0.8763 | 0.8917 | 0.9071 | 0.911 |
| equivalent_surface/period/alias | 268 | 0.9249 | 0.8399 | 0.9564 | 0.9808 | 0.9925 |
| filter_change/filter_added/clinic_visits | 7 | 0.8233 | 0.7744 | 0.8317 | 0.8621 | 0.8791 |
| filter_change/filter_dropped/total_visits | 30 | 0.7518 | 0.6598 | 0.7672 | 0.8112 | 0.8411 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7719 | 0.7208 | 0.7609 | 0.8436 | 0.8695 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7422 | 0.7198 | 0.7424 | 0.7634 | 0.778 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7546 | 0.7282 | 0.7528 | 0.7758 | 0.8139 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7645 | 0.7348 | 0.7599 | 0.7929 | 0.8026 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8189 | 0.7823 | 0.8156 | 0.8629 | 0.8639 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.8189 | 0.7571 | 0.8107 | 0.885 | 0.8942 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9002 | 0.8155 | 0.901 | 0.9654 | 0.9723 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9171 | 0.8928 | 0.9201 | 0.9448 | 0.9471 |
| intent_near_miss/grouping/top_departments | 10 | 0.7476 | 0.6742 | 0.7193 | 0.8298 | 0.8314 |
| intent_near_miss/grouping/top_providers | 10 | 0.7421 | 0.7071 | 0.7257 | 0.8068 | 0.8108 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7296 | 0.7096 | 0.729 | 0.7547 | 0.7591 |
| intent_near_miss/measure/dept_visits | 10 | 0.7324 | 0.6958 | 0.733 | 0.7565 | 0.7854 |
| intent_near_miss/measure/total_no_shows | 7 | 0.6841 | 0.5883 | 0.7114 | 0.7599 | 0.7735 |
| intent_near_miss/measure/total_visits | 7 | 0.7002 | 0.6591 | 0.6755 | 0.7581 | 0.7884 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8147 | 0.7496 | 0.7895 | 0.916 | 0.9465 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8594 | 0.8152 | 0.8758 | 0.89 | 0.8996 |
| param_near_miss/amount/neighbor | 27 | 0.905 | 0.8235 | 0.9292 | 0.9573 | 0.9645 |
| param_near_miss/clinic/neighbor | 80 | 0.8436 | 0.744 | 0.8477 | 0.9208 | 0.9406 |
| param_near_miss/department/neighbor | 60 | 0.8246 | 0.7756 | 0.8312 | 0.876 | 0.9002 |
| param_near_miss/n/neighbor | 47 | 0.8957 | 0.8421 | 0.9042 | 0.949 | 0.9627 |
| param_near_miss/payer/neighbor | 24 | 0.8788 | 0.8296 | 0.891 | 0.9285 | 0.9301 |
| param_near_miss/period/adjacent | 277 | 0.9172 | 0.8204 | 0.9367 | 0.9806 | 0.9911 |
| param_near_miss/period/granularity | 199 | 0.875 | 0.7847 | 0.8891 | 0.9299 | 0.9528 |
| paraphrase/wording/template | 290 | 0.903 | 0.8306 | 0.9143 | 0.9582 | 0.9924 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4552 | [0.3724, 0.531] | 0.9586 | [0.9241, 0.9862] |
| param_near_miss | 145 | 0.4552 | [0.3793, 0.5379] | 0.9448 | [0.9103, 0.9793] |
| period_near_miss | 145 | 0.4552 | [0.3793, 0.5379] | 0.9379 | [0.8966, 0.9724] |
| entity_near_miss | 110 | 0.0 | [0.0, 0.0] | 0.6545 | [0.5636, 0.7364] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.2519 | [0.1778, 0.3259] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.8345 | [0.7724, 0.8898] |
| B | 145 | 0.5793 | [0.5034, 0.6621] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0076 | [0.0018, 0.0281] | 0.0076 | 0.0076 | 0.5534 |
| raw_oracle_entry | 0.3416 | [0.3117, 0.3949] | — | — | 0.5534 |
| split_full | 0.1584 | [0.1265, 0.1971] | 0.1584 | 0.3473 | 0.5534 |
| split_template | 0.5172 | [0.4635, 0.5769] | 0.5172 | 0.9637 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9666 | What was our overall visit volume so far this year? | 0.9356 |
| Average patient wait in Q3 2026 | Average patient wait in Q2 2026 | 0.974 | Average patient wait in the third quarter of 2026 | 0.9484 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9709 | What was our no-show rate so far this year? | 0.9481 |
| Visit count for cardiology last month | Visit count for cardiology this month | 0.9735 | Visit count for cardiology in the previous month | 0.9509 |
| Total missed appointments last month | Total missed appointments this month | 0.9716 | Total missed appointments in the previous month | 0.9517 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9806 | How many visits were billed to Medicare so far this month? | 0.9617 |
| Visit volume at the Downtown clinic in Q3 2026 | Visit volume at the Downtown clinic in Q2 2026 | 0.9843 | Visit volume at the Downtown clinic in the third quarter of 2026 | 0.9662 |
| Visit volume at the Northgate clinic in Q3 2026 | Visit volume at the Northgate clinic in Q2 2026 | 0.9843 | Visit volume at the Northgate clinic in the third quarter of 2026 | 0.9664 |
| What was our no-show rate this week? | What was our no-show rate last week? | 0.9818 | What was our no-show rate so far this week? | 0.9653 |
| Visit count for Medicare Advantage patients in Q3 2026 | Visit count for Medicare Advantage patients in Q2 2026 | 0.969 | Visit count for Medicare Advantage patients in the third quarter of 2026 | 0.9535 |
| Longest wait recorded last month | Longest wait recorded this month | 0.9614 | Longest wait recorded in the previous month | 0.9462 |
| How many visits were billed to commercial insurance last month? | How many visits were billed to commercial insurance this month? | 0.9831 | How many visits were billed to commercial insurance in the previous month? | 0.9683 |
| How many visits were billed to Medicaid this week? | How many visits were billed to Medicaid last week? | 0.9851 | How many visits were billed to Medicaid so far this week? | 0.9708 |
| Visit count for Medicare Advantage patients last year | Visit count for Medicare Advantage patients this year | 0.9535 | Visit count for Medicare Advantage patients in the previous year | 0.94 |
| How often did patients miss appointments this month? | How often did patients miss appointments last month? | 0.9801 | How often did patients miss appointments so far this month? | 0.9668 |
