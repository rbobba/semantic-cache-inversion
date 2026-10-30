# vertex:gemini-embedding-001 holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9492 | 0.8805 | 0.9666 | 0.9913 | 0.998 |
| **equivalent_surface (same wording=True)** | 370 | 0.9492 | 0.8805 | 0.9666 | 0.9913 | 0.998 |
| **filter_change** | 37 | 0.8024 | 0.7372 | 0.8019 | 0.8936 | 0.9235 |
| **intent_near_miss** | 142 | 0.8453 | 0.7703 | 0.8451 | 0.9359 | 0.9864 |
| **intent_near_miss (same wording=False)** | 142 | 0.8453 | 0.7703 | 0.8451 | 0.9359 | 0.9864 |
| **param_near_miss** | 714 | 0.9232 | 0.8365 | 0.9417 | 0.9857 | 0.9967 |
| **param_near_miss (same wording=False)** | 255 | 0.8804 | 0.8107 | 0.8795 | 0.9489 | 0.986 |
| **param_near_miss (same wording=True)** | 459 | 0.947 | 0.8754 | 0.9657 | 0.988 | 0.9967 |
| **paraphrase** | 290 | 0.9167 | 0.8566 | 0.9264 | 0.9664 | 0.9945 |
| equivalent_surface/amount/alias | 10 | 0.9757 | 0.9639 | 0.9776 | 0.9836 | 0.9865 |
| equivalent_surface/clinic/alias | 40 | 0.9413 | 0.9082 | 0.9435 | 0.9755 | 0.9796 |
| equivalent_surface/department/alias | 30 | 0.9605 | 0.9388 | 0.9618 | 0.9793 | 0.9849 |
| equivalent_surface/n/alias | 20 | 0.9949 | 0.9907 | 0.9955 | 0.9977 | 0.998 |
| equivalent_surface/payer/alias | 2 | 0.9188 | 0.911 | 0.9188 | 0.9265 | 0.9285 |
| equivalent_surface/period/alias | 268 | 0.945 | 0.872 | 0.968 | 0.9908 | 0.9958 |
| filter_change/filter_added/clinic_visits | 7 | 0.8735 | 0.8032 | 0.8956 | 0.9157 | 0.9235 |
| filter_change/filter_dropped/total_visits | 30 | 0.7858 | 0.7304 | 0.7942 | 0.8324 | 0.86 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.8661 | 0.8222 | 0.8481 | 0.9385 | 0.9423 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.8294 | 0.7997 | 0.824 | 0.8755 | 0.884 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.8339 | 0.8018 | 0.8364 | 0.8706 | 0.8736 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8347 | 0.8181 | 0.8307 | 0.8534 | 0.8555 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8883 | 0.8755 | 0.8833 | 0.9072 | 0.9151 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.8821 | 0.8275 | 0.8543 | 0.9441 | 0.9579 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9425 | 0.8967 | 0.9473 | 0.9811 | 0.9864 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9135 | 0.8683 | 0.9203 | 0.9504 | 0.9643 |
| intent_near_miss/grouping/top_departments | 10 | 0.8075 | 0.7696 | 0.7862 | 0.8578 | 0.8682 |
| intent_near_miss/grouping/top_providers | 10 | 0.7798 | 0.7331 | 0.7622 | 0.8398 | 0.8399 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.8319 | 0.8065 | 0.8292 | 0.8608 | 0.8659 |
| intent_near_miss/measure/dept_visits | 10 | 0.8261 | 0.8081 | 0.8254 | 0.8461 | 0.8512 |
| intent_near_miss/measure/total_no_shows | 7 | 0.7674 | 0.7026 | 0.7898 | 0.8031 | 0.8085 |
| intent_near_miss/measure/total_visits | 7 | 0.7411 | 0.7097 | 0.7242 | 0.7982 | 0.7992 |
| intent_near_miss/negation/clinic_visits | 10 | 0.861 | 0.8026 | 0.8584 | 0.9243 | 0.9405 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8911 | 0.8635 | 0.8936 | 0.9084 | 0.9153 |
| param_near_miss/amount/neighbor | 27 | 0.9335 | 0.8373 | 0.9769 | 0.985 | 0.9873 |
| param_near_miss/clinic/neighbor | 80 | 0.9086 | 0.8469 | 0.915 | 0.9629 | 0.9805 |
| param_near_miss/department/neighbor | 60 | 0.8376 | 0.792 | 0.8408 | 0.8897 | 0.9178 |
| param_near_miss/n/neighbor | 47 | 0.952 | 0.8846 | 0.9713 | 0.9866 | 0.9912 |
| param_near_miss/payer/neighbor | 24 | 0.8807 | 0.8232 | 0.8856 | 0.9355 | 0.9657 |
| param_near_miss/period/adjacent | 277 | 0.9394 | 0.8575 | 0.9549 | 0.9908 | 0.9967 |
| param_near_miss/period/granularity | 199 | 0.9292 | 0.8584 | 0.9483 | 0.9739 | 0.9864 |
| paraphrase/wording/template | 290 | 0.9167 | 0.8566 | 0.9264 | 0.9664 | 0.9945 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4276 | [0.3448, 0.5103] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.4276 | [0.3448, 0.5103] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.4138 | [0.331, 0.4897] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0364 | [0.0091, 0.0727] | 0.7182 | [0.6364, 0.8] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.3185 | [0.2444, 0.4] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.931 | [0.8897, 0.9655] |
| B | 145 | 0.4966 | [0.4138, 0.5724] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0057 | [0.0, 0.0132] | 0.0057 | 0.0057 | 0.5534 |
| raw_oracle_entry | 0.2519 | [0.2301, 0.3119] | — | — | 0.5534 |
| split_full | 0.0057 | [0.0, 0.0165] | 0.0057 | 0.0057 | 0.5534 |
| split_template | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How often did patients miss appointments last month? | How often did patients miss appointments this month? | 0.9917 | How often did patients miss appointments in the previous month? | 0.9503 |
| Visit count for Medicare patients last year | Visit count for Medicare patients this year | 0.9719 | Visit count for Medicare patients in the previous year | 0.9389 |
| Longest wait recorded last month | Longest wait recorded this month | 0.967 | Longest wait recorded in the previous month | 0.937 |
| Visit count for Medicare Advantage patients last year | Visit count for Medicare Advantage patients this year | 0.9759 | Visit count for Medicare Advantage patients in the previous year | 0.9459 |
| Mean waiting time in pediatrics this week | Mean waiting time in pediatrics last week | 0.9905 | Mean waiting time in pediatrics so far this week | 0.9666 |
| How long did patients wait on average this year? | How long did patients wait on average last year? | 0.9685 | How long did patients wait on average so far this year? | 0.9464 |
| How often did patients miss appointments last year? | How often did patients miss appointments this year? | 0.9831 | How often did patients miss appointments in the previous year? | 0.9622 |
| Visits at every site but the Downtown clinic in the last 3 months | Visits at every site but the Downtown clinic in the last 6 months | 0.9796 | Visits at every site but the Downtown clinic over the past three months | 0.9591 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.98 | What was our no-show rate so far this year? | 0.961 |
| What was the average wait time in pulmonology this year? | What was the average wait time in pulmonology last year? | 0.9948 | What was the average wait time in pulmonology so far this year? | 0.9764 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9862 | How many patient visits did we have in the previous year? | 0.9699 |
| Mean waiting time in pulmonology this month | Mean waiting time in pulmonology last month | 0.9926 | Mean waiting time in pulmonology so far this month | 0.9764 |
| Visits at every site but the Southgate clinic last year | Visits at every site but the Southgate clinic this year | 0.9716 | Visits at every site but the Southgate clinic in the previous year | 0.9561 |
| Mean waiting time in radiology this month | Mean waiting time in radiology last month | 0.9923 | Mean waiting time in radiology so far this month | 0.9772 |
| Total missed appointments last year | Total missed appointments this year | 0.9764 | Total missed appointments in the previous year | 0.9621 |
