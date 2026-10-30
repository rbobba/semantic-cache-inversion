# st:Qwen/Qwen3-Embedding-0.6B

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9458 | 0.8742 | 0.9661 | 0.9898 | 0.9936 |
| **equivalent_surface (same wording=True)** | 370 | 0.9458 | 0.8742 | 0.9661 | 0.9898 | 0.9936 |
| **filter_change** | 37 | 0.7066 | 0.616 | 0.7037 | 0.7921 | 0.8247 |
| **intent_near_miss** | 142 | 0.7903 | 0.6814 | 0.7971 | 0.8953 | 0.9852 |
| **intent_near_miss (same wording=False)** | 142 | 0.7903 | 0.6814 | 0.7971 | 0.8953 | 0.9852 |
| **param_near_miss** | 714 | 0.8917 | 0.7737 | 0.9091 | 0.9827 | 0.9952 |
| **param_near_miss (same wording=False)** | 255 | 0.8121 | 0.7218 | 0.8207 | 0.8979 | 0.9666 |
| **param_near_miss (same wording=True)** | 459 | 0.936 | 0.8614 | 0.9511 | 0.9854 | 0.9952 |
| **paraphrase** | 290 | 0.8565 | 0.7647 | 0.8677 | 0.9344 | 0.9891 |
| equivalent_surface/amount/alias | 10 | 0.9731 | 0.9672 | 0.9746 | 0.9778 | 0.9799 |
| equivalent_surface/clinic/alias | 40 | 0.9244 | 0.9019 | 0.9224 | 0.9512 | 0.9788 |
| equivalent_surface/department/alias | 30 | 0.9562 | 0.9345 | 0.9605 | 0.9689 | 0.9779 |
| equivalent_surface/n/alias | 20 | 0.9855 | 0.975 | 0.9877 | 0.992 | 0.9923 |
| equivalent_surface/payer/alias | 2 | 0.9261 | 0.9165 | 0.9261 | 0.9358 | 0.9382 |
| equivalent_surface/period/alias | 268 | 0.9441 | 0.8649 | 0.9732 | 0.9901 | 0.9936 |
| filter_change/filter_added/clinic_visits | 7 | 0.7563 | 0.6712 | 0.7824 | 0.816 | 0.8247 |
| filter_change/filter_dropped/total_visits | 30 | 0.6951 | 0.6177 | 0.6894 | 0.7803 | 0.8048 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.8476 | 0.8096 | 0.8343 | 0.9 | 0.9022 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7937 | 0.7526 | 0.7892 | 0.833 | 0.8433 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7704 | 0.7084 | 0.7651 | 0.8292 | 0.8575 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8282 | 0.7817 | 0.8332 | 0.8638 | 0.8834 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8117 | 0.7688 | 0.8177 | 0.8439 | 0.8556 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.7671 | 0.6484 | 0.7191 | 0.8931 | 0.9161 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.8938 | 0.8289 | 0.8962 | 0.9767 | 0.9852 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8646 | 0.806 | 0.8523 | 0.9195 | 0.9698 |
| intent_near_miss/grouping/top_departments | 10 | 0.7023 | 0.6066 | 0.6486 | 0.8271 | 0.8359 |
| intent_near_miss/grouping/top_providers | 10 | 0.7326 | 0.6783 | 0.735 | 0.7747 | 0.8 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7867 | 0.7332 | 0.7966 | 0.8259 | 0.8261 |
| intent_near_miss/measure/dept_visits | 10 | 0.779 | 0.7379 | 0.7777 | 0.8249 | 0.8255 |
| intent_near_miss/measure/total_no_shows | 7 | 0.7064 | 0.6157 | 0.7415 | 0.7546 | 0.7559 |
| intent_near_miss/measure/total_visits | 7 | 0.6969 | 0.6668 | 0.6918 | 0.7299 | 0.7629 |
| intent_near_miss/negation/clinic_visits | 10 | 0.831 | 0.7785 | 0.8038 | 0.9211 | 0.9411 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8078 | 0.7849 | 0.7947 | 0.8457 | 0.8514 |
| param_near_miss/amount/neighbor | 27 | 0.9105 | 0.7197 | 0.9828 | 0.9897 | 0.9908 |
| param_near_miss/clinic/neighbor | 80 | 0.8489 | 0.7438 | 0.8505 | 0.9573 | 0.9708 |
| param_near_miss/department/neighbor | 60 | 0.8106 | 0.7353 | 0.8203 | 0.8702 | 0.8921 |
| param_near_miss/n/neighbor | 47 | 0.9097 | 0.8147 | 0.9476 | 0.9792 | 0.9913 |
| param_near_miss/payer/neighbor | 24 | 0.8716 | 0.7914 | 0.8903 | 0.9576 | 0.9633 |
| param_near_miss/period/adjacent | 277 | 0.9037 | 0.7821 | 0.9297 | 0.986 | 0.9952 |
| param_near_miss/period/granularity | 199 | 0.9124 | 0.8443 | 0.9286 | 0.9634 | 0.9889 |
| paraphrase/wording/template | 290 | 0.8565 | 0.7647 | 0.8677 | 0.9344 | 0.9891 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.2828 | [0.2069, 0.3586] | 1.0 | [1.0, 1.0] |
| param_near_miss | 145 | 0.2759 | [0.2069, 0.345] | 1.0 | [1.0, 1.0] |
| period_near_miss | 145 | 0.2621 | [0.1931, 0.331] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 110 | 0.0273 | [0.0, 0.0636] | 0.7455 | [0.6636, 0.8273] |
| intent_near_miss | 135 | 0.0074 | [0.0, 0.0222] | 0.3259 | [0.2444, 0.4074] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9655 | [0.9378, 0.9931] |
| B | 145 | 0.2759 | [0.2069, 0.3517] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.5598 |
| raw_oracle_entry | 0.118 | [0.1098, 0.1449] | — | — | 0.5598 |
| split_full | 0.303 | [0.2855, 0.3191] | 0.303 | 0.4043 | 0.5598 |
| split_template | 0.5949 | [0.5751, 0.6144] | 0.5949 | 0.6938 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Show visits with waits over 30 minutes in Q3 2026 | Show visits with waits over 30 minutes in Q2 2026 | 0.9938 | Show visits with waits over half an hour in Q3 2026 | 0.9776 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.9722 | What was the longest wait in the third quarter of 2026? | 0.9567 |
| What did pediatrics bill in total last year? | What did pediatrics bill in total this year? | 0.9731 | How much did pediatrics bill last year? | 0.9622 |
| Visit count for cardiology last month | Visit count for cardiology this month | 0.9837 | Visit count for cardiology in the previous month | 0.9731 |
| Which appointments had a wait longer than 15 minutes in Q3 2026? | Which appointments had a wait longer than 30 minutes in Q3 2026? | 0.9852 | Which appointments had a wait longer than 15 minutes in the third quarter of 2026? | 0.975 |
| How many patient visits did we have last month? | How many patient visits did we have this month? | 0.9729 | How many patient visits did we have in the previous month? | 0.9636 |
| How many visits were billed to commercial insurance last month? | How many visits were billed to commercial insurance this month? | 0.9841 | How many visits were billed to commercial insurance in the previous month? | 0.9752 |
| Visits at every site but the Southgate clinic in the last 3 months | Visits at every site but the Southgate clinic in the last 6 months | 0.9874 | Visits at every site but the Southgate clinic over the past three months | 0.9796 |
| Top 2 departments by visit volume in Q3 2026 | Top 3 departments by visit volume in Q3 2026 | 0.9913 | Top two departments by visit volume in Q3 2026 | 0.9835 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9612 | How many patient visits did we have in the previous year? | 0.9543 |
| Visit volume at the Northgate clinic in Q3 2026 | Visit volume at the Northgate clinic in Q2 2026 | 0.995 | Visit volume at the Northgate clinic in the third quarter of 2026 | 0.9882 |
| Number of incoming referrals at the Lakeside clinic this week | Number of incoming referrals at the Lakeside clinic last week | 0.9952 | Number of incoming referrals at the Lakeside clinic so far this week | 0.9902 |
| Visit volume at the Downtown clinic in Q3 2026 | Visit volume at the Downtown clinic in Q2 2026 | 0.9921 | Visit volume at the Downtown clinic in the third quarter of 2026 | 0.9873 |
| Which appointments had a wait longer than 30 minutes last month? | Which appointments had a wait longer than 30 minutes this month? | 0.9895 | Which appointments had a wait longer than 30 minutes in the previous month? | 0.9849 |
| How many visits were billed to Medicaid this week? | How many visits were billed to Medicaid last week? | 0.9798 | How many visits were billed to Medicaid so far this week? | 0.9755 |
