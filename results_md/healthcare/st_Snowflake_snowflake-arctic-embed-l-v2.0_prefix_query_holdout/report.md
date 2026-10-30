# st:Snowflake/snowflake-arctic-embed-l-v2.0 prefix='query: ' holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.911 | 0.786 | 0.9499 | 0.9883 | 0.9981 |
| **equivalent_surface (same wording=True)** | 370 | 0.911 | 0.786 | 0.9499 | 0.9883 | 0.9981 |
| **filter_change** | 37 | 0.6246 | 0.4937 | 0.6376 | 0.7175 | 0.8345 |
| **intent_near_miss** | 142 | 0.7459 | 0.563 | 0.7138 | 0.9325 | 0.9808 |
| **intent_near_miss (same wording=False)** | 142 | 0.7459 | 0.563 | 0.7138 | 0.9325 | 0.9808 |
| **param_near_miss** | 714 | 0.8614 | 0.7247 | 0.8814 | 0.9775 | 0.996 |
| **param_near_miss (same wording=False)** | 255 | 0.7946 | 0.6641 | 0.7964 | 0.9219 | 0.9815 |
| **param_near_miss (same wording=True)** | 459 | 0.8984 | 0.7812 | 0.9126 | 0.9841 | 0.996 |
| **paraphrase** | 290 | 0.8687 | 0.7662 | 0.891 | 0.9607 | 0.9951 |
| equivalent_surface/amount/alias | 10 | 0.8844 | 0.8665 | 0.8753 | 0.9236 | 0.9359 |
| equivalent_surface/clinic/alias | 40 | 0.8873 | 0.8651 | 0.8844 | 0.9251 | 0.9799 |
| equivalent_surface/department/alias | 30 | 0.9476 | 0.9336 | 0.9498 | 0.9594 | 0.9648 |
| equivalent_surface/n/alias | 20 | 0.9958 | 0.9938 | 0.9957 | 0.9977 | 0.9981 |
| equivalent_surface/payer/alias | 2 | 0.8424 | 0.8379 | 0.8424 | 0.8469 | 0.8481 |
| equivalent_surface/period/alias | 268 | 0.9056 | 0.7733 | 0.9558 | 0.9855 | 0.9962 |
| filter_change/filter_added/clinic_visits | 7 | 0.6063 | 0.5283 | 0.6143 | 0.6881 | 0.7216 |
| filter_change/filter_dropped/total_visits | 30 | 0.6288 | 0.4963 | 0.6412 | 0.7201 | 0.8345 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7301 | 0.6758 | 0.7008 | 0.8198 | 0.8513 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7135 | 0.6641 | 0.6941 | 0.8191 | 0.8252 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7112 | 0.6842 | 0.7131 | 0.7398 | 0.7562 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7214 | 0.6852 | 0.6949 | 0.7892 | 0.8206 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.7681 | 0.6755 | 0.7491 | 0.8833 | 0.8905 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.6947 | 0.5343 | 0.6884 | 0.8501 | 0.8745 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9514 | 0.9274 | 0.9481 | 0.9769 | 0.9808 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.941 | 0.926 | 0.9346 | 0.9631 | 0.9642 |
| intent_near_miss/grouping/top_departments | 10 | 0.6408 | 0.5063 | 0.6473 | 0.7515 | 0.7574 |
| intent_near_miss/grouping/top_providers | 10 | 0.6061 | 0.5199 | 0.6219 | 0.6857 | 0.6886 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7206 | 0.6801 | 0.706 | 0.7895 | 0.7964 |
| intent_near_miss/measure/dept_visits | 10 | 0.6941 | 0.6526 | 0.6818 | 0.7667 | 0.7696 |
| intent_near_miss/measure/total_no_shows | 7 | 0.5618 | 0.4698 | 0.5645 | 0.6432 | 0.6837 |
| intent_near_miss/measure/total_visits | 7 | 0.6035 | 0.5266 | 0.6104 | 0.6984 | 0.7335 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8747 | 0.8347 | 0.8669 | 0.927 | 0.943 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8822 | 0.8484 | 0.8748 | 0.9246 | 0.9313 |
| param_near_miss/amount/neighbor | 27 | 0.8471 | 0.6821 | 0.9135 | 0.9381 | 0.9613 |
| param_near_miss/clinic/neighbor | 80 | 0.8146 | 0.7101 | 0.8222 | 0.8988 | 0.937 |
| param_near_miss/department/neighbor | 60 | 0.7425 | 0.6646 | 0.7539 | 0.8218 | 0.8541 |
| param_near_miss/n/neighbor | 47 | 0.9036 | 0.7726 | 0.9452 | 0.9789 | 0.9873 |
| param_near_miss/payer/neighbor | 24 | 0.8201 | 0.6921 | 0.8598 | 0.9071 | 0.9194 |
| param_near_miss/period/adjacent | 277 | 0.892 | 0.7587 | 0.9242 | 0.9866 | 0.996 |
| param_near_miss/period/granularity | 199 | 0.8702 | 0.777 | 0.8871 | 0.9475 | 0.9875 |
| paraphrase/wording/template | 290 | 0.8687 | 0.7662 | 0.891 | 0.9607 | 0.9951 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4552 | [0.3791, 0.5379] | 0.9655 | [0.931, 0.9931] |
| param_near_miss | 145 | 0.4552 | [0.3724, 0.5312] | 0.9586 | [0.9241, 0.9862] |
| period_near_miss | 145 | 0.4483 | [0.3724, 0.531] | 0.9517 | [0.9171, 0.9862] |
| entity_near_miss | 110 | 0.0182 | [0.0, 0.0455] | 0.5091 | [0.4273, 0.6] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.3778 | [0.2963, 0.4593] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.8345 | [0.7724, 0.8897] |
| B | 145 | 0.5241 | [0.4483, 0.6] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0057 | [0.0, 0.015] | 0.0057 | 0.0057 | 0.5534 |
| raw_oracle_entry | 0.3569 | [0.3275, 0.4151] | — | — | 0.5534 |
| split_full | 0.0134 | [0.004, 0.0299] | 0.0134 | 0.0134 | 0.5534 |
| split_template | 0.0744 | [0.0466, 0.106] | 0.0744 | 0.0744 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Show visits with waits over 45 minutes last month | Show visits with waits over 45 minutes this month | 0.9811 | Show visits with waits over 45 minutes in the previous month | 0.8878 |
| Total missed appointments last month | Total missed appointments this month | 0.9815 | Total missed appointments in the previous month | 0.9369 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9762 | What was our overall visit volume year to date? | 0.9434 |
| How many patient visits did we have last month? | How many patient visits did we have this month? | 0.9727 | How many patient visits did we have in the previous month? | 0.9402 |
| How many patient visits did we have this week? | How many patient visits did we have last week? | 0.9734 | How many patient visits did we have so far this week? | 0.9458 |
| How many patient visits did we have this month? | How many patient visits did we have last month? | 0.9727 | How many patient visits did we have so far this month? | 0.9457 |
| Longest wait recorded last month | Longest wait recorded this month | 0.9848 | Longest wait recorded in the previous month | 0.9586 |
| How long did patients wait on average this year? | How long did patients wait on average last year? | 0.9717 | How long did patients wait on average so far this year? | 0.948 |
| Total missed appointments this year | Total missed appointments last year | 0.9736 | Total missed appointments so far this year | 0.9502 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9764 | What was our no-show rate so far this year? | 0.9531 |
| How often did patients miss appointments last month? | How often did patients miss appointments this month? | 0.9886 | How often did patients miss appointments in the previous month? | 0.9663 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.981 | How many visits were billed to Medicare in the previous month? | 0.959 |
| Total missed appointments last year | Total missed appointments this year | 0.9736 | Total missed appointments in the previous year | 0.9519 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9761 | How many patient visits did we have in the previous year? | 0.9549 |
| How many patient visits did physical therapy handle last month? | How many patient visits did physical therapy handle this month? | 0.9866 | How many patient visits did physical therapy handle in the previous month? | 0.9655 |
