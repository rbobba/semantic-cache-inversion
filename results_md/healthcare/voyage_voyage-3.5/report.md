# voyage:voyage-3.5

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9087 | 0.8135 | 0.9369 | 0.9737 | 0.997 |
| **equivalent_surface (same wording=True)** | 370 | 0.9087 | 0.8135 | 0.9369 | 0.9737 | 0.997 |
| **filter_change** | 37 | 0.6844 | 0.5874 | 0.6799 | 0.7755 | 0.8466 |
| **intent_near_miss** | 142 | 0.7412 | 0.6256 | 0.7268 | 0.8858 | 0.9593 |
| **intent_near_miss (same wording=False)** | 142 | 0.7412 | 0.6256 | 0.7268 | 0.8858 | 0.9593 |
| **param_near_miss** | 714 | 0.8553 | 0.7336 | 0.866 | 0.968 | 0.9906 |
| **param_near_miss (same wording=False)** | 255 | 0.7898 | 0.6751 | 0.7979 | 0.9049 | 0.9643 |
| **param_near_miss (same wording=True)** | 459 | 0.8917 | 0.8007 | 0.8985 | 0.9755 | 0.9906 |
| **paraphrase** | 290 | 0.8567 | 0.7324 | 0.8779 | 0.9372 | 0.9807 |
| equivalent_surface/amount/alias | 10 | 0.8641 | 0.8023 | 0.8734 | 0.943 | 0.9459 |
| equivalent_surface/clinic/alias | 40 | 0.9092 | 0.8565 | 0.9109 | 0.9656 | 0.9868 |
| equivalent_surface/department/alias | 30 | 0.9464 | 0.9212 | 0.9494 | 0.9655 | 0.9723 |
| equivalent_surface/n/alias | 20 | 0.9899 | 0.9756 | 0.9916 | 0.9954 | 0.997 |
| equivalent_surface/payer/alias | 2 | 0.8628 | 0.8257 | 0.8628 | 0.9 | 0.9093 |
| equivalent_surface/period/alias | 268 | 0.9003 | 0.8053 | 0.9347 | 0.9704 | 0.9886 |
| filter_change/filter_added/clinic_visits | 7 | 0.6943 | 0.6168 | 0.6935 | 0.7725 | 0.8466 |
| filter_change/filter_dropped/total_visits | 30 | 0.6821 | 0.5952 | 0.6798 | 0.7738 | 0.8117 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7464 | 0.6958 | 0.722 | 0.8287 | 0.8637 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7299 | 0.6911 | 0.7233 | 0.7995 | 0.8058 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7181 | 0.6892 | 0.71 | 0.759 | 0.7978 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7079 | 0.6709 | 0.6897 | 0.7522 | 0.7567 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.755 | 0.6749 | 0.7752 | 0.8124 | 0.815 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.7458 | 0.616 | 0.7112 | 0.8811 | 0.9036 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.887 | 0.8256 | 0.9016 | 0.9526 | 0.9593 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8787 | 0.8521 | 0.8837 | 0.9054 | 0.908 |
| intent_near_miss/grouping/top_departments | 10 | 0.6655 | 0.5712 | 0.6373 | 0.7704 | 0.7762 |
| intent_near_miss/grouping/top_providers | 10 | 0.6599 | 0.6112 | 0.655 | 0.721 | 0.7448 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7188 | 0.6833 | 0.7007 | 0.8028 | 0.805 |
| intent_near_miss/measure/dept_visits | 10 | 0.7562 | 0.7006 | 0.7469 | 0.8313 | 0.8423 |
| intent_near_miss/measure/total_no_shows | 7 | 0.6062 | 0.5037 | 0.6477 | 0.673 | 0.6814 |
| intent_near_miss/measure/total_visits | 7 | 0.6378 | 0.5787 | 0.6236 | 0.7061 | 0.7219 |
| intent_near_miss/negation/clinic_visits | 10 | 0.7543 | 0.6621 | 0.7377 | 0.8676 | 0.9125 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.817 | 0.7694 | 0.8072 | 0.8881 | 0.8973 |
| param_near_miss/amount/neighbor | 27 | 0.8281 | 0.7249 | 0.8502 | 0.9235 | 0.9568 |
| param_near_miss/clinic/neighbor | 80 | 0.8147 | 0.6732 | 0.8143 | 0.9399 | 0.9493 |
| param_near_miss/department/neighbor | 60 | 0.7698 | 0.7028 | 0.7737 | 0.8483 | 0.888 |
| param_near_miss/n/neighbor | 47 | 0.8565 | 0.7511 | 0.876 | 0.932 | 0.9436 |
| param_near_miss/payer/neighbor | 24 | 0.8451 | 0.7613 | 0.8625 | 0.9342 | 0.9685 |
| param_near_miss/period/adjacent | 277 | 0.8867 | 0.767 | 0.9115 | 0.9784 | 0.9906 |
| param_near_miss/period/granularity | 199 | 0.8584 | 0.786 | 0.8695 | 0.9292 | 0.9759 |
| paraphrase/wording/template | 290 | 0.8567 | 0.7324 | 0.8779 | 0.9372 | 0.9807 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4897 | [0.4069, 0.5655] | 0.9862 | [0.9655, 1.0] |
| param_near_miss | 145 | 0.4897 | [0.4069, 0.5724] | 0.9862 | [0.9655, 1.0] |
| period_near_miss | 145 | 0.4897 | [0.4069, 0.5793] | 0.9862 | [0.9655, 1.0] |
| entity_near_miss | 110 | 0.0273 | [0.0, 0.0636] | 0.5818 | [0.4909, 0.6727] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.2296 | [0.1556, 0.3037] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9103 | [0.8621, 0.9517] |
| B | 145 | 0.6138 | [0.531, 0.6828] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0104 | [0.0055, 0.0187] | 0.0104 | 0.0104 | 0.5598 |
| raw_oracle_entry | 0.1292 | [0.1175, 0.1668] | — | — | 0.5598 |
| split_full | 0.303 | [0.2855, 0.3281] | 0.3469 | 0.4506 | 0.5598 |
| split_template | 0.5949 | [0.5751, 0.6144] | 0.5949 | 0.8365 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Visits at every site but the Downtown clinic in the last 3 months | Visits at every site but the Downtown clinic in the last 6 months | 0.9727 | Visits at every site but the Downtown clinic over the past three months | 0.8933 |
| Visit count for Medicare Advantage patients last year | Visit count for Medicare patients last year | 0.9208 | Number of visits covered by Medicare Advantage last year | 0.8529 |
| Visit count for Medicare patients last year | Visit count for Medicare Advantage patients last year | 0.9208 | Visit count for Medicare patients in the previous year | 0.8558 |
| Visits at every site but the Riverside clinic last month | Visits at every site but the Riverside clinic this month | 0.9713 | Visits at every site but the Riverside clinic in the previous month | 0.9148 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9533 | What was our overall visit volume so far this year? | 0.8979 |
| Number of incoming referrals at the Southgate clinic last month | Number of incoming referrals at the Southgate clinic this month | 0.9783 | Referrals into the Southgate clinic last month | 0.9244 |
| Which appointments had a wait longer than 60 minutes this year? | Which appointments had a wait longer than 60 minutes last year? | 0.9803 | Which appointments had a wait longer than 60 minutes year to date? | 0.9278 |
| How long did patients wait on average this year? | How long did patients wait on average last year? | 0.9569 | How long did patients wait on average so far this year? | 0.908 |
| What was our no-show rate this week? | What was our no-show rate last week? | 0.9839 | What was our no-show rate so far this week? | 0.9377 |
| How many patients did the Northgate clinic refer elsewhere this year? | How many patients did the Northgate clinic refer elsewhere last year? | 0.9827 | How many patients did the Northgate clinic refer elsewhere year to date? | 0.9366 |
| How many appointments were no-shows this month? | How many appointments were no-shows last month? | 0.9728 | How many appointments were no-shows so far this month? | 0.9279 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9676 | What was our no-show rate so far this year? | 0.9263 |
| How many visits were billed to Medicaid this week? | How many visits were billed to Medicaid last week? | 0.9854 | How many visits were billed to Medicaid so far this week? | 0.9453 |
| Average patient wait last year | Average patient wait this year | 0.921 | Average patient wait in the previous year | 0.8813 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9824 | How many visits were billed to Medicare so far this month? | 0.943 |
