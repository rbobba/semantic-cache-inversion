# st:sentence-transformers/all-mpnet-base-v2

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9377 | 0.8449 | 0.9657 | 0.993 | 0.9979 |
| **equivalent_surface (same wording=True)** | 370 | 0.9377 | 0.8449 | 0.9657 | 0.993 | 0.9979 |
| **filter_change** | 37 | 0.6475 | 0.5365 | 0.6402 | 0.8244 | 0.8812 |
| **intent_near_miss** | 142 | 0.7332 | 0.5676 | 0.7295 | 0.9313 | 0.9874 |
| **intent_near_miss (same wording=False)** | 142 | 0.7332 | 0.5676 | 0.7295 | 0.9313 | 0.9874 |
| **param_near_miss** | 714 | 0.8924 | 0.7447 | 0.9245 | 0.9894 | 0.9971 |
| **param_near_miss (same wording=False)** | 255 | 0.801 | 0.655 | 0.8218 | 0.9125 | 0.9777 |
| **param_near_miss (same wording=True)** | 459 | 0.9431 | 0.8649 | 0.9619 | 0.9928 | 0.9971 |
| **paraphrase** | 290 | 0.833 | 0.6881 | 0.8644 | 0.9374 | 0.9841 |
| equivalent_surface/amount/alias | 10 | 0.9561 | 0.9325 | 0.9595 | 0.9764 | 0.9774 |
| equivalent_surface/clinic/alias | 40 | 0.8317 | 0.6939 | 0.8219 | 0.951 | 0.9819 |
| equivalent_surface/department/alias | 30 | 0.965 | 0.945 | 0.9688 | 0.978 | 0.9814 |
| equivalent_surface/n/alias | 20 | 0.9963 | 0.9948 | 0.9965 | 0.9978 | 0.9979 |
| equivalent_surface/payer/alias | 2 | 0.9464 | 0.9412 | 0.9464 | 0.9516 | 0.9529 |
| equivalent_surface/period/alias | 268 | 0.9453 | 0.8658 | 0.969 | 0.9908 | 0.9979 |
| filter_change/filter_added/clinic_visits | 7 | 0.8113 | 0.7373 | 0.8386 | 0.8645 | 0.8812 |
| filter_change/filter_dropped/total_visits | 30 | 0.6093 | 0.5277 | 0.6151 | 0.6878 | 0.7195 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7038 | 0.635 | 0.6754 | 0.8159 | 0.8309 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.6165 | 0.5129 | 0.635 | 0.6688 | 0.7039 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.6956 | 0.6255 | 0.7001 | 0.7632 | 0.7671 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7223 | 0.6804 | 0.7185 | 0.7616 | 0.7759 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8213 | 0.7518 | 0.7952 | 0.8925 | 0.8954 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.6829 | 0.5497 | 0.6389 | 0.8383 | 0.8545 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9107 | 0.8249 | 0.9342 | 0.9854 | 0.9874 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.93 | 0.8894 | 0.9362 | 0.9522 | 0.9773 |
| intent_near_miss/grouping/top_departments | 10 | 0.6374 | 0.5303 | 0.6026 | 0.7536 | 0.792 |
| intent_near_miss/grouping/top_providers | 10 | 0.6499 | 0.58 | 0.6475 | 0.7503 | 0.8203 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.6931 | 0.6468 | 0.6789 | 0.7718 | 0.7866 |
| intent_near_miss/measure/dept_visits | 10 | 0.7346 | 0.6955 | 0.7307 | 0.7868 | 0.8005 |
| intent_near_miss/measure/total_no_shows | 7 | 0.6108 | 0.5457 | 0.6408 | 0.6644 | 0.6649 |
| intent_near_miss/measure/total_visits | 7 | 0.5151 | 0.4653 | 0.5264 | 0.5556 | 0.567 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8475 | 0.7686 | 0.8366 | 0.9514 | 0.9677 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8563 | 0.8172 | 0.8404 | 0.9056 | 0.9076 |
| param_near_miss/amount/neighbor | 27 | 0.8798 | 0.6564 | 0.9563 | 0.983 | 0.9844 |
| param_near_miss/clinic/neighbor | 80 | 0.8739 | 0.7822 | 0.8731 | 0.9581 | 0.9791 |
| param_near_miss/department/neighbor | 60 | 0.7726 | 0.6525 | 0.7788 | 0.8661 | 0.906 |
| param_near_miss/n/neighbor | 47 | 0.9046 | 0.7484 | 0.957 | 0.9824 | 0.9851 |
| param_near_miss/payer/neighbor | 24 | 0.8736 | 0.7833 | 0.8922 | 0.9585 | 0.9628 |
| param_near_miss/period/adjacent | 277 | 0.9038 | 0.745 | 0.9389 | 0.9941 | 0.9971 |
| param_near_miss/period/granularity | 199 | 0.921 | 0.8242 | 0.9432 | 0.9805 | 0.9968 |
| paraphrase/wording/template | 290 | 0.833 | 0.6881 | 0.8644 | 0.9374 | 0.9841 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.6828 | [0.6069, 0.7517] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.6828 | [0.6069, 0.7586] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.6828 | [0.6069, 0.7586] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0727 | [0.0273, 0.1273] | 0.7364 | [0.6545, 0.8182] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.4148 | [0.3333, 0.5037] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 1.0 | [1.0, 1.0] |
| B | 145 | 0.7724 | [0.7034, 0.8414] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0064 | [0.0024, 0.0136] | 0.0064 | 0.0064 | 0.5598 |
| raw_oracle_entry | 0.0558 | [0.0505, 0.0809] | — | — | 0.5598 |
| split_full | 0.2974 | [0.2809, 0.3132] | 0.2974 | 0.3389 | 0.5598 |
| split_template | 0.5949 | [0.5751, 0.6144] | 0.5949 | 0.5949 | 1.0 |
| split_full_extracted | 0.2472 | [0.2288, 0.2724] | 0.256 | 0.3477 | 0.559 |
| split_template_extracted | 0.5758 | [0.5542, 0.5954] | 0.5758 | 0.5861 | 0.9992 |
| split_template_extracted_slots | 0.5758 | [0.5542, 0.5954] | 0.5758 | 0.5861 | 0.9992 |
| split_template_negguard | 0.5758 | [0.5542, 0.5954] | 0.5758 | 0.7855 | 0.9992 |
| split_template_guarded_goldsig | 0.949 | [0.9328, 0.9644] | 0.9928 | 0.9928 | 0.9992 |
| split_template_fullsig | 0.9027 | [0.8807, 0.9977] | 0.9944 | 0.9944 | 0.9944 |
| split_template_fullsig_gold | 0.9992 | [0.9975, 1.0] | 0.9992 | 0.9992 | 0.9992 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9847 | 0.2472 | 0.2472 [0.2287, 0.2666] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9847 | 0.5758 | 0.5758 [0.5542, 0.5954] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9847 | 0.5758 | 0.5758 [0.5542, 0.5954] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9847 | 0.5758 | 0.5758 [0.5542, 0.5954] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9992 | 0.9928 [0.9876, 0.9969] | 0.0064 [0.0023, 0.0116] | 8 | 8 | 0 | 0 |
| split_template_fullsig | 0.5 | 0.9952 | 0.9944 [0.9901, 0.9984] | 0.0008 [0.0, 0.0025] | 1 | 1 | 0 | 0 |
| split_template_fullsig_gold | 0.5 | 0.9992 | 0.9992 [0.9975, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Number of patient visits at the Downtown clinic last year | Number of patient visits at the Downtown clinic this year | 0.989 | Number of patient visits at the Downtown clinic in the previous year | 0.9367 |
| Number of patient visits at the Lakeside clinic last year | Number of patient visits at the Lakeside clinic this year | 0.9889 | Number of patient visits at the Lakeside clinic in the previous year | 0.9402 |
| Average patient wait last year | Average patient wait this year | 0.9568 | Average patient wait in the previous year | 0.9098 |
| Visit count for Medicare patients last year | Visit count for Medicare patients this year | 0.9573 | Visit count for Medicare patients in the previous year | 0.9138 |
| Visit count for Medicare Advantage patients last year | Visit count for Medicare Advantage patients this year | 0.9552 | Visit count for Medicare Advantage patients in the previous year | 0.9276 |
| Show visits with waits over 30 minutes in Q3 2026 | Show visits with waits over 30 minutes in Q2 2026 | 0.9804 | Show visits with waits over half an hour in Q3 2026 | 0.9549 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.9686 | What was the longest wait in the third quarter of 2026? | 0.9436 |
| Total missed appointments last month | Total missed appointments this month | 0.9781 | Total missed appointments in the previous month | 0.9541 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9912 | How many visits were billed to Medicare in the previous month? | 0.9675 |
| Show visits with waits over 30 minutes this month | Show visits with waits over 30 minutes last month | 0.9806 | Show visits with waits over 30 minutes so far this month | 0.9575 |
| Total missed appointments last year | Total missed appointments this year | 0.9722 | Total missed appointments in the previous year | 0.9498 |
| How often did patients miss appointments last year? | How often did patients miss appointments this year? | 0.9929 | How often did patients miss appointments in the previous year? | 0.9722 |
| How many visits were billed to commercial insurance last month? | How many visits were billed to commercial insurance this month? | 0.9952 | How many visits were billed to commercial insurance in the previous month? | 0.9761 |
| Total missed appointments in Q3 2026 | Total missed appointments in Q2 2026 | 0.981 | Total missed appointments in the third quarter of 2026 | 0.9635 |
| Show visits with waits over 15 minutes this week | Show visits with waits over 15 minutes last week | 0.9712 | Show visits with waits over 15 minutes so far this week | 0.954 |
