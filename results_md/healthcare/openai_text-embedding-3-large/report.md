# openai:text-embedding-3-large

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.934 | 0.8523 | 0.9508 | 0.9817 | 0.9956 |
| **equivalent_surface (same wording=True)** | 370 | 0.934 | 0.8523 | 0.9508 | 0.9817 | 0.9956 |
| **filter_change** | 37 | 0.6299 | 0.5419 | 0.6074 | 0.7618 | 0.8078 |
| **intent_near_miss** | 142 | 0.7171 | 0.5644 | 0.7097 | 0.8816 | 0.9782 |
| **intent_near_miss (same wording=False)** | 142 | 0.7171 | 0.5644 | 0.7097 | 0.8816 | 0.9782 |
| **param_near_miss** | 714 | 0.8654 | 0.7174 | 0.8974 | 0.9726 | 0.9909 |
| **param_near_miss (same wording=False)** | 255 | 0.7681 | 0.6605 | 0.7645 | 0.8837 | 0.9638 |
| **param_near_miss (same wording=True)** | 459 | 0.9194 | 0.8303 | 0.9332 | 0.9783 | 0.9909 |
| **paraphrase** | 290 | 0.8298 | 0.7278 | 0.845 | 0.9218 | 0.9797 |
| equivalent_surface/amount/alias | 10 | 0.9542 | 0.9237 | 0.9613 | 0.9688 | 0.9779 |
| equivalent_surface/clinic/alias | 40 | 0.9296 | 0.8895 | 0.9341 | 0.954 | 0.9833 |
| equivalent_surface/department/alias | 30 | 0.9459 | 0.9292 | 0.9504 | 0.9645 | 0.9734 |
| equivalent_surface/n/alias | 20 | 0.9888 | 0.9838 | 0.9889 | 0.9935 | 0.9956 |
| equivalent_surface/payer/alias | 2 | 0.9143 | 0.9061 | 0.9143 | 0.9225 | 0.9245 |
| equivalent_surface/period/alias | 268 | 0.9286 | 0.8478 | 0.9514 | 0.9799 | 0.9853 |
| filter_change/filter_added/clinic_visits | 7 | 0.7531 | 0.6782 | 0.7688 | 0.8077 | 0.8078 |
| filter_change/filter_dropped/total_visits | 30 | 0.6012 | 0.5297 | 0.5925 | 0.6864 | 0.7237 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7543 | 0.7127 | 0.7473 | 0.8132 | 0.8338 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.6716 | 0.63 | 0.6544 | 0.7483 | 0.7598 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7001 | 0.6788 | 0.6922 | 0.7286 | 0.7707 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7438 | 0.7002 | 0.7529 | 0.7773 | 0.7777 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.7935 | 0.7533 | 0.8135 | 0.8241 | 0.8318 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.7045 | 0.5674 | 0.671 | 0.8793 | 0.8819 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9025 | 0.8529 | 0.9025 | 0.9736 | 0.9782 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8876 | 0.8635 | 0.882 | 0.9189 | 0.9424 |
| intent_near_miss/grouping/top_departments | 10 | 0.5964 | 0.5212 | 0.5456 | 0.7097 | 0.7161 |
| intent_near_miss/grouping/top_providers | 10 | 0.6243 | 0.5638 | 0.6193 | 0.7252 | 0.7264 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.6682 | 0.6315 | 0.6697 | 0.7028 | 0.7164 |
| intent_near_miss/measure/dept_visits | 10 | 0.6887 | 0.6653 | 0.6935 | 0.7089 | 0.7207 |
| intent_near_miss/measure/total_no_shows | 7 | 0.5484 | 0.4828 | 0.5752 | 0.594 | 0.6168 |
| intent_near_miss/measure/total_visits | 7 | 0.5678 | 0.5025 | 0.5643 | 0.6424 | 0.7034 |
| intent_near_miss/negation/clinic_visits | 10 | 0.7898 | 0.7106 | 0.7572 | 0.9064 | 0.9467 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.7752 | 0.7277 | 0.7804 | 0.8075 | 0.8186 |
| param_near_miss/amount/neighbor | 27 | 0.8788 | 0.7021 | 0.9451 | 0.9582 | 0.9685 |
| param_near_miss/clinic/neighbor | 80 | 0.8297 | 0.7032 | 0.8404 | 0.9138 | 0.9475 |
| param_near_miss/department/neighbor | 60 | 0.7403 | 0.644 | 0.7496 | 0.8095 | 0.8446 |
| param_near_miss/n/neighbor | 47 | 0.8388 | 0.6874 | 0.8908 | 0.9121 | 0.9355 |
| param_near_miss/payer/neighbor | 24 | 0.8285 | 0.7128 | 0.8481 | 0.9353 | 0.9501 |
| param_near_miss/period/adjacent | 277 | 0.885 | 0.7344 | 0.9175 | 0.9802 | 0.9883 |
| param_near_miss/period/granularity | 199 | 0.899 | 0.7981 | 0.9228 | 0.967 | 0.9909 |
| paraphrase/wording/template | 290 | 0.8298 | 0.7278 | 0.845 | 0.9218 | 0.9797 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.469 | [0.3931, 0.5448] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.469 | [0.3793, 0.5517] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.469 | [0.3931, 0.5517] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0182 | [0.0, 0.0455] | 0.6545 | [0.5725, 0.7455] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.2815 | [0.2074, 0.3556] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9724 | [0.9448, 0.9931] |
| B | 145 | 0.5655 | [0.4828, 0.6414] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0056 | [0.0025, 0.0118] | 0.0056 | 0.0056 | 0.5598 |
| raw_oracle_entry | 0.0957 | [0.0904, 0.1279] | — | — | 0.5598 |
| split_full | 0.2974 | [0.2809, 0.3133] | 0.2974 | 0.4011 | 0.5598 |
| split_template | 0.5949 | [0.5751, 0.6144] | 0.5949 | 0.866 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Visit count for Medicare patients last year | Visit count for Medicare patients this year | 0.9475 | Visit count for Medicare patients in the previous year | 0.8965 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9791 | How many visits were billed to Medicare in the previous month? | 0.9413 |
| Total missed appointments last month | Total missed appointments this month | 0.969 | Total missed appointments in the previous month | 0.9327 |
| Visit count for Medicare Advantage patients last year | Visit count for Medicare Advantage patients this year | 0.959 | Visit count for Medicare Advantage patients in the previous year | 0.9233 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9791 | How many visits were billed to Medicare so far this month? | 0.9447 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.9207 | What was the maximum wait time in Q3 2026? | 0.8887 |
| What did pediatrics bill in total this year? | What did pediatrics bill in total last year? | 0.9818 | What did pediatrics bill in total so far this year? | 0.9514 |
| Longest wait recorded last month | Longest wait recorded this month | 0.974 | Longest wait recorded in the previous month | 0.9491 |
| How long did patients wait on average last month? | How long did patients wait on average this month? | 0.9739 | How long did patients wait on average in the previous month? | 0.9512 |
| Total missed appointments last year | Total missed appointments this year | 0.9563 | Total missed appointments in the previous year | 0.9348 |
| Which appointments had a wait longer than 30 minutes last month? | Which appointments had a wait longer than 30 minutes this month? | 0.9866 | Which appointments had a wait longer than 30 minutes in the previous month? | 0.969 |
| Visits at every site but the Riverside clinic last month | Visits at every site but the Riverside clinic this month | 0.9682 | Visits at every site but the Riverside clinic in the previous month | 0.951 |
| Number of incoming referrals at the Southgate clinic last month | Number of incoming referrals at the Southgate clinic this month | 0.9805 | Number of incoming referrals at the Southgate clinic in the previous month | 0.9633 |
| How often did patients miss appointments last year? | How often did patients miss appointments this year? | 0.9673 | How often did patients miss appointments in the previous year? | 0.9503 |
| How many patient visits did we have this month? | How many patient visits did we have last month? | 0.9723 | How many patient visits did we have so far this month? | 0.957 |
