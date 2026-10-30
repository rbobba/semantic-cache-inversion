# st:intfloat/e5-base-v2 prefix='query: '

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9746 | 0.9336 | 0.9859 | 0.9969 | 0.9991 |
| **equivalent_surface (same wording=True)** | 370 | 0.9746 | 0.9336 | 0.9859 | 0.9969 | 0.9991 |
| **filter_change** | 37 | 0.882 | 0.8381 | 0.8857 | 0.9205 | 0.9366 |
| **intent_near_miss** | 142 | 0.9122 | 0.8607 | 0.9097 | 0.9528 | 0.9971 |
| **intent_near_miss (same wording=False)** | 142 | 0.9122 | 0.8607 | 0.9097 | 0.9528 | 0.9971 |
| **param_near_miss** | 714 | 0.952 | 0.9008 | 0.959 | 0.9948 | 0.999 |
| **param_near_miss (same wording=False)** | 255 | 0.9193 | 0.8735 | 0.9193 | 0.9614 | 0.9952 |
| **param_near_miss (same wording=True)** | 459 | 0.9701 | 0.9383 | 0.9725 | 0.9965 | 0.999 |
| **paraphrase** | 290 | 0.9402 | 0.8981 | 0.9427 | 0.9767 | 0.9973 |
| equivalent_surface/amount/alias | 10 | 0.9813 | 0.9762 | 0.9806 | 0.9881 | 0.9924 |
| equivalent_surface/clinic/alias | 40 | 0.9691 | 0.9571 | 0.9662 | 0.9844 | 0.9934 |
| equivalent_surface/department/alias | 30 | 0.9846 | 0.9791 | 0.9849 | 0.9902 | 0.9907 |
| equivalent_surface/n/alias | 20 | 0.9984 | 0.9976 | 0.9985 | 0.9991 | 0.9991 |
| equivalent_surface/payer/alias | 2 | 0.9618 | 0.958 | 0.9618 | 0.9655 | 0.9664 |
| equivalent_surface/period/alias | 268 | 0.9723 | 0.9302 | 0.988 | 0.9963 | 0.9987 |
| filter_change/filter_added/clinic_visits | 7 | 0.9005 | 0.869 | 0.9128 | 0.9205 | 0.9231 |
| filter_change/filter_dropped/total_visits | 30 | 0.8776 | 0.8351 | 0.8793 | 0.9186 | 0.9366 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.914 | 0.8973 | 0.9064 | 0.9414 | 0.9481 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.903 | 0.8869 | 0.8969 | 0.9262 | 0.9287 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.9046 | 0.8779 | 0.8994 | 0.9411 | 0.9419 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8997 | 0.8817 | 0.9029 | 0.9135 | 0.9191 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.9425 | 0.9277 | 0.9425 | 0.9544 | 0.9566 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.896 | 0.8448 | 0.8874 | 0.954 | 0.9602 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9639 | 0.9112 | 0.9773 | 0.997 | 0.9971 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9529 | 0.9392 | 0.9481 | 0.9691 | 0.9887 |
| intent_near_miss/grouping/top_departments | 10 | 0.8857 | 0.8362 | 0.8752 | 0.9307 | 0.931 |
| intent_near_miss/grouping/top_providers | 10 | 0.8783 | 0.8592 | 0.8712 | 0.9078 | 0.9132 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.923 | 0.9047 | 0.9265 | 0.941 | 0.9432 |
| intent_near_miss/measure/dept_visits | 10 | 0.9251 | 0.9154 | 0.9256 | 0.9329 | 0.9339 |
| intent_near_miss/measure/total_no_shows | 7 | 0.8755 | 0.8469 | 0.8862 | 0.8948 | 0.8985 |
| intent_near_miss/measure/total_visits | 7 | 0.8649 | 0.8419 | 0.8527 | 0.8997 | 0.9055 |
| intent_near_miss/negation/clinic_visits | 10 | 0.9258 | 0.8995 | 0.9032 | 0.9787 | 0.9822 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.916 | 0.8828 | 0.9164 | 0.9409 | 0.9486 |
| param_near_miss/amount/neighbor | 27 | 0.951 | 0.8872 | 0.9802 | 0.9892 | 0.9948 |
| param_near_miss/clinic/neighbor | 80 | 0.9239 | 0.8686 | 0.9341 | 0.9626 | 0.9698 |
| param_near_miss/department/neighbor | 60 | 0.9276 | 0.8934 | 0.9341 | 0.9531 | 0.9629 |
| param_near_miss/n/neighbor | 47 | 0.9662 | 0.9139 | 0.9869 | 0.9922 | 0.9949 |
| param_near_miss/payer/neighbor | 24 | 0.9454 | 0.9149 | 0.9541 | 0.9729 | 0.9756 |
| param_near_miss/period/adjacent | 277 | 0.9593 | 0.9072 | 0.97 | 0.9977 | 0.999 |
| param_near_miss/period/granularity | 199 | 0.9578 | 0.9318 | 0.9655 | 0.9804 | 0.9894 |
| paraphrase/wording/template | 290 | 0.9402 | 0.8981 | 0.9427 | 0.9767 | 0.9973 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.5517 | [0.4757, 0.6276] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.5517 | [0.469, 0.6345] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.5379 | [0.4619, 0.6207] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0182 | [0.0, 0.0455] | 0.7727 | [0.6909, 0.8455] |
| intent_near_miss | 135 | 0.0074 | [0.0, 0.0222] | 0.3926 | [0.3111, 0.4743] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.931 | [0.8897, 0.9724] |
| B | 145 | 0.5931 | [0.5103, 0.6621] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0032 | [0.0008, 0.009] | 0.0032 | 0.0032 | 0.5598 |
| raw_oracle_entry | 0.0949 | [0.0864, 0.128] | — | — | 0.5598 |
| split_full | 0.2951 | [0.2791, 0.3109] | 0.2951 | 0.3557 | 0.5598 |
| split_template | 0.5821 | [0.5647, 0.6006] | 0.5821 | 0.6132 | 1.0 |
| split_full_extracted | 0.2448 | [0.2281, 0.2765] | 0.264 | 0.3501 | 0.5534 |
| split_template_extracted | 0.5423 | [0.5197, 0.5634] | 0.5423 | 0.5933 | 0.992 |
| split_template_extracted_slots | 0.5423 | [0.5197, 0.5634] | 0.5423 | 0.5933 | 0.992 |
| split_template_negguard | 0.5423 | [0.5197, 0.5634] | 0.5423 | 0.7018 | 0.992 |
| split_template_guarded | 0.6683 | [0.6445, 0.7088] | 0.7368 | 0.9585 | 0.9912 |
| split_template_guarded_goldsig | 0.9203 | [0.9052, 0.9969] | 0.992 | 0.992 | 0.992 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 1.0 | 0.1986 | 0.1986 [0.1787, 0.2179] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 1.0 | 0.5112 | 0.5112 [0.4879, 0.5352] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 1.0 | 0.5112 | 0.5112 [0.4879, 0.5352] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 1.0 | 0.5112 | 0.5112 [0.4879, 0.5352] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.9928 | 0.9585 [0.9412, 0.9742] | 0.0345 [0.0192, 0.0505] | 43 | 42 | 0 | 1 |
| split_template_guarded_goldsig | 0.5 | 0.9928 | 0.992 [0.9847, 0.9976] | 0.0008 [0.0, 0.0025] | 1 | 0 | 0 | 1 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Which appointments had a wait longer than 15 minutes in Q3 2026? | Which appointments had a wait longer than 30 minutes in Q3 2026? | 0.9933 | Which appointments had a wait longer than a quarter of an hour in Q3 2026? | 0.9876 |
| Total missed appointments last year | Total missed appointments this year | 0.9947 | Total missed appointments in the previous year | 0.9891 |
| Average patient wait last year | Average patient wait this year | 0.9929 | Average patient wait in the previous year | 0.9877 |
| What was the average wait time in family medicine last year? | What was the average wait time in family medicine this year? | 0.9981 | What was the average wait time in family medicine in the previous year? | 0.993 |
| Total missed appointments this week | Total missed appointments last week | 0.9964 | Total missed appointments so far this week | 0.9917 |
| What did pediatrics bill in total this year? | What did pediatrics bill in total last year? | 0.9973 | What did pediatrics bill in total so far this year? | 0.9927 |
| Total missed appointments this year | Total missed appointments last year | 0.9947 | Total missed appointments so far this year | 0.9901 |
| Average patient wait this week | Average patient wait last week | 0.9958 | Average patient wait so far this week | 0.9913 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9944 | What was our no-show rate so far this year? | 0.99 |
| What was our no-show rate this week? | What was our no-show rate last week? | 0.9972 | What was our no-show rate so far this week? | 0.9928 |
| Visit volume at the Midtown clinic this year | Visit volume at the Midtown clinic last year | 0.9883 | Visit volume at the Midtown clinic so far this year | 0.9841 |
| Total missed appointments last month | Total missed appointments this month | 0.9965 | Total missed appointments in the previous month | 0.9924 |
| Visit volume at the Southgate clinic this year | Visit volume at the Southgate clinic last year | 0.9871 | Visit volume at the Southgate clinic so far this year | 0.9831 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.997 | How many visits were billed to Medicare so far this month? | 0.9933 |
| What did physical therapy bill in total this week? | What did physical therapy bill in total last week? | 0.9984 | What did physical therapy bill in total so far this week? | 0.9946 |
