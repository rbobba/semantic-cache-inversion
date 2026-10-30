# openai:text-embedding-3-small

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9337 | 0.8577 | 0.95 | 0.9833 | 0.9945 |
| **equivalent_surface (same wording=True)** | 370 | 0.9337 | 0.8577 | 0.95 | 0.9833 | 0.9945 |
| **filter_change** | 37 | 0.5546 | 0.4214 | 0.5467 | 0.6805 | 0.7696 |
| **intent_near_miss** | 142 | 0.7282 | 0.5757 | 0.7226 | 0.8888 | 0.9726 |
| **intent_near_miss (same wording=False)** | 142 | 0.7282 | 0.5757 | 0.7226 | 0.8888 | 0.9726 |
| **param_near_miss** | 714 | 0.8616 | 0.7088 | 0.8891 | 0.9793 | 0.9946 |
| **param_near_miss (same wording=False)** | 255 | 0.7594 | 0.6416 | 0.7545 | 0.8881 | 0.9589 |
| **param_near_miss (same wording=True)** | 459 | 0.9184 | 0.8128 | 0.9354 | 0.9847 | 0.9946 |
| **paraphrase** | 290 | 0.817 | 0.7087 | 0.8277 | 0.9201 | 0.9686 |
| equivalent_surface/amount/alias | 10 | 0.9537 | 0.9306 | 0.958 | 0.9709 | 0.976 |
| equivalent_surface/clinic/alias | 40 | 0.9199 | 0.8729 | 0.9214 | 0.9543 | 0.9858 |
| equivalent_surface/department/alias | 30 | 0.9504 | 0.9262 | 0.9541 | 0.9709 | 0.9771 |
| equivalent_surface/n/alias | 20 | 0.9889 | 0.9844 | 0.9886 | 0.9925 | 0.9945 |
| equivalent_surface/payer/alias | 2 | 0.878 | 0.8597 | 0.878 | 0.8963 | 0.9009 |
| equivalent_surface/period/alias | 268 | 0.9294 | 0.8524 | 0.9509 | 0.9816 | 0.994 |
| filter_change/filter_added/clinic_visits | 7 | 0.6855 | 0.609 | 0.6997 | 0.7592 | 0.7696 |
| filter_change/filter_dropped/total_visits | 30 | 0.5241 | 0.4161 | 0.5383 | 0.613 | 0.6478 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7353 | 0.6599 | 0.7101 | 0.847 | 0.8751 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7029 | 0.6647 | 0.6875 | 0.7712 | 0.7737 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7276 | 0.7018 | 0.7226 | 0.7686 | 0.78 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.745 | 0.7159 | 0.7424 | 0.7808 | 0.7825 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.7563 | 0.7237 | 0.7575 | 0.7838 | 0.788 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.6748 | 0.5416 | 0.6149 | 0.8333 | 0.8466 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.8937 | 0.8374 | 0.9063 | 0.9701 | 0.9726 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8968 | 0.8723 | 0.8906 | 0.9275 | 0.966 |
| intent_near_miss/grouping/top_departments | 10 | 0.6005 | 0.514 | 0.5575 | 0.7162 | 0.7216 |
| intent_near_miss/grouping/top_providers | 10 | 0.6217 | 0.5667 | 0.6126 | 0.7066 | 0.7108 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7178 | 0.6829 | 0.7137 | 0.7645 | 0.7694 |
| intent_near_miss/measure/dept_visits | 10 | 0.73 | 0.7085 | 0.7251 | 0.7541 | 0.7894 |
| intent_near_miss/measure/total_no_shows | 7 | 0.5844 | 0.5136 | 0.6164 | 0.633 | 0.6441 |
| intent_near_miss/measure/total_visits | 7 | 0.5864 | 0.5224 | 0.5903 | 0.6512 | 0.6797 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8158 | 0.7324 | 0.7894 | 0.9411 | 0.9529 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.7764 | 0.703 | 0.7755 | 0.842 | 0.8474 |
| param_near_miss/amount/neighbor | 27 | 0.8821 | 0.7013 | 0.9691 | 0.976 | 0.986 |
| param_near_miss/clinic/neighbor | 80 | 0.8266 | 0.7081 | 0.8276 | 0.9409 | 0.9573 |
| param_near_miss/department/neighbor | 60 | 0.7404 | 0.6364 | 0.7658 | 0.8219 | 0.8627 |
| param_near_miss/n/neighbor | 47 | 0.8563 | 0.7183 | 0.8993 | 0.9392 | 0.957 |
| param_near_miss/payer/neighbor | 24 | 0.7907 | 0.6606 | 0.8078 | 0.9167 | 0.9236 |
| param_near_miss/period/adjacent | 277 | 0.882 | 0.7228 | 0.91 | 0.9869 | 0.9946 |
| param_near_miss/period/granularity | 199 | 0.8908 | 0.7865 | 0.9147 | 0.9648 | 0.9895 |
| paraphrase/wording/template | 290 | 0.817 | 0.7087 | 0.8277 | 0.9201 | 0.9686 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.669 | [0.5862, 0.7379] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.669 | [0.5862, 0.7517] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.669 | [0.5862, 0.7448] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0182 | [0.0, 0.0455] | 0.7 | [0.6182, 0.7818] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.2593 | [0.1926, 0.3407] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 1.0 | [1.0, 1.0] |
| B | 145 | 0.731 | [0.6552, 0.8] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0033] | 0.0 | 0.0 | 0.5598 |
| raw_oracle_entry | 0.0758 | [0.0695, 0.1081] | — | — | 0.5598 |
| split_full | 0.2951 | [0.2791, 0.3106] | 0.2951 | 0.3636 | 0.5598 |
| split_template | 0.5821 | [0.5647, 0.6006] | 0.5821 | 0.5949 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9752 | How many visits were billed to Medicare in the previous month? | 0.918 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.976 | What was our no-show rate so far this year? | 0.931 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.9456 | What was the maximum wait time in Q3 2026? | 0.9051 |
| Average patient wait in Q3 2026 | Average patient wait in Q2 2026 | 0.967 | Average patient wait in the third quarter of 2026 | 0.9316 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9698 | What was our overall visit volume so far this year? | 0.9362 |
| Total missed appointments last month | Total missed appointments this month | 0.9703 | Total missed appointments in the previous month | 0.9375 |
| How many patient visits did we have last month? | How many patient visits did we have this month? | 0.9604 | How many patient visits did we have in the previous month? | 0.9295 |
| Visit count for dermatology in Q3 2026 | Visit count for dermatology in Q2 2026 | 0.9806 | Visit count for dermatology in the third quarter of 2026 | 0.9511 |
| How many visits were billed to commercial insurance last month? | How many visits were billed to commercial insurance this month? | 0.9857 | How many visits were billed to commercial insurance in the previous month? | 0.9568 |
| Visit volume at the Southgate clinic this year | Visit volume at the Southgate clinic last year | 0.9558 | Visit volume at the Southgate clinic so far this year | 0.9298 |
| Number of patient visits at the Lakeside clinic in Q3 2026 | Number of patient visits at the Lakeside clinic in Q2 2026 | 0.9883 | Number of patient visits at the Lakeside clinic in the third quarter of 2026 | 0.963 |
| Visit count for physical therapy in Q3 2026 | Visit count for physical therapy in Q2 2026 | 0.9803 | Visit count for physical therapy in the third quarter of 2026 | 0.9567 |
| Visit volume at the Northgate clinic in Q3 2026 | Visit volume at the Northgate clinic in Q2 2026 | 0.9834 | Visit volume at the Northgate clinic in the third quarter of 2026 | 0.9608 |
| Number of incoming referrals at the Lakeside clinic in Q3 2026 | Number of incoming referrals at the Lakeside clinic in Q2 2026 | 0.9931 | Number of incoming referrals at the Lakeside clinic in the third quarter of 2026 | 0.9706 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9505 | How many patient visits did we have in the previous year? | 0.9289 |
