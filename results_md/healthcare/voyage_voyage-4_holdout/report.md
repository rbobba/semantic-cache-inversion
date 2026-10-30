# voyage:voyage-4 holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9249 | 0.8181 | 0.9612 | 0.9883 | 0.9976 |
| **equivalent_surface (same wording=True)** | 370 | 0.9249 | 0.8181 | 0.9612 | 0.9883 | 0.9976 |
| **filter_change** | 37 | 0.6729 | 0.587 | 0.6699 | 0.7563 | 0.8023 |
| **intent_near_miss** | 142 | 0.7577 | 0.6084 | 0.7512 | 0.8977 | 0.9767 |
| **intent_near_miss (same wording=False)** | 142 | 0.7577 | 0.6084 | 0.7512 | 0.8977 | 0.9767 |
| **param_near_miss** | 714 | 0.8609 | 0.7309 | 0.8763 | 0.964 | 0.9885 |
| **param_near_miss (same wording=False)** | 255 | 0.7897 | 0.6881 | 0.7968 | 0.8887 | 0.9671 |
| **param_near_miss (same wording=True)** | 459 | 0.9005 | 0.8059 | 0.9178 | 0.9718 | 0.9885 |
| **paraphrase** | 290 | 0.8701 | 0.7982 | 0.8743 | 0.9476 | 0.9955 |
| equivalent_surface/amount/alias | 10 | 0.9293 | 0.8933 | 0.9366 | 0.9555 | 0.9557 |
| equivalent_surface/clinic/alias | 40 | 0.9147 | 0.8706 | 0.9137 | 0.9603 | 0.9874 |
| equivalent_surface/department/alias | 30 | 0.9688 | 0.955 | 0.9699 | 0.9809 | 0.9831 |
| equivalent_surface/n/alias | 20 | 0.9931 | 0.9892 | 0.9933 | 0.9971 | 0.9976 |
| equivalent_surface/payer/alias | 2 | 0.8659 | 0.8244 | 0.8659 | 0.9075 | 0.9179 |
| equivalent_surface/period/alias | 268 | 0.9167 | 0.7951 | 0.9628 | 0.9878 | 0.9928 |
| filter_change/filter_added/clinic_visits | 7 | 0.6767 | 0.5665 | 0.712 | 0.7484 | 0.7913 |
| filter_change/filter_dropped/total_visits | 30 | 0.672 | 0.6028 | 0.6636 | 0.7557 | 0.8023 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.7624 | 0.7166 | 0.7424 | 0.8241 | 0.8369 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7378 | 0.7144 | 0.7397 | 0.7639 | 0.7798 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7316 | 0.6769 | 0.738 | 0.793 | 0.8011 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7382 | 0.68 | 0.7281 | 0.7941 | 0.8128 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8473 | 0.8277 | 0.8337 | 0.8848 | 0.887 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.7942 | 0.7201 | 0.7592 | 0.8936 | 0.8981 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9147 | 0.8565 | 0.9372 | 0.9759 | 0.9767 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9104 | 0.8738 | 0.919 | 0.9423 | 0.9441 |
| intent_near_miss/grouping/top_departments | 10 | 0.6187 | 0.5369 | 0.5827 | 0.729 | 0.7297 |
| intent_near_miss/grouping/top_providers | 10 | 0.6512 | 0.612 | 0.6346 | 0.7679 | 0.773 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.7139 | 0.6876 | 0.7155 | 0.7311 | 0.7455 |
| intent_near_miss/measure/dept_visits | 10 | 0.7301 | 0.6794 | 0.7242 | 0.7787 | 0.7961 |
| intent_near_miss/measure/total_no_shows | 7 | 0.5817 | 0.4999 | 0.6074 | 0.653 | 0.6612 |
| intent_near_miss/measure/total_visits | 7 | 0.6311 | 0.5428 | 0.5712 | 0.7486 | 0.7546 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8358 | 0.7703 | 0.8034 | 0.9455 | 0.9523 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8667 | 0.8361 | 0.8721 | 0.8856 | 0.8923 |
| param_near_miss/amount/neighbor | 27 | 0.8491 | 0.7587 | 0.8814 | 0.9091 | 0.9154 |
| param_near_miss/clinic/neighbor | 80 | 0.808 | 0.7074 | 0.8116 | 0.9077 | 0.9614 |
| param_near_miss/department/neighbor | 60 | 0.7541 | 0.6723 | 0.7589 | 0.8182 | 0.8645 |
| param_near_miss/n/neighbor | 47 | 0.8787 | 0.7819 | 0.9038 | 0.9552 | 0.9647 |
| param_near_miss/payer/neighbor | 24 | 0.8456 | 0.737 | 0.8535 | 0.9396 | 0.9604 |
| param_near_miss/period/adjacent | 277 | 0.8844 | 0.7637 | 0.9062 | 0.9777 | 0.9885 |
| param_near_miss/period/granularity | 199 | 0.881 | 0.7865 | 0.907 | 0.9471 | 0.9656 |
| paraphrase/wording/template | 290 | 0.8701 | 0.7982 | 0.8743 | 0.9476 | 0.9955 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.0828 | [0.0414, 0.131] | 0.9931 | [0.9793, 1.0] |
| param_near_miss | 145 | 0.0828 | [0.0414, 0.131] | 0.9862 | [0.9655, 1.0] |
| period_near_miss | 145 | 0.0828 | [0.0414, 0.131] | 0.9862 | [0.9655, 1.0] |
| entity_near_miss | 110 | 0.0 | [0.0, 0.0] | 0.5727 | [0.4818, 0.6636] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.3333 | [0.2591, 0.4148] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.7931 | [0.731, 0.8552] |
| B | 145 | 0.0897 | [0.0483, 0.1379] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0057 | [0.0, 0.0157] | 0.0057 | 0.0057 | 0.5534 |
| raw_oracle_entry | 0.3225 | [0.2941, 0.3729] | — | — | 0.5534 |
| split_full | 0.0134 | [0.004, 0.0299] | 0.0134 | 0.0134 | 0.5534 |
| split_template | 0.0744 | [0.0466, 0.106] | 0.0744 | 0.0744 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Visits at every site but the Riverside clinic last month | Visits at every site but the Riverside clinic this month | 0.9815 | Visits at every site but the Riverside clinic in the previous month | 0.9459 |
| Visits at every site but the Southgate clinic last year | Visits at every site but the Southgate clinic this year | 0.9701 | Visits at every site but the Southgate clinic in the previous year | 0.9386 |
| Longest wait recorded last month | Longest wait recorded this month | 0.9729 | Longest wait recorded in the previous month | 0.9414 |
| How long did patients wait on average this month? | How long did patients wait on average last month? | 0.968 | How long did patients wait on average so far this month? | 0.9515 |
| Average patient wait this week | Average patient wait last week | 0.9721 | Average patient wait so far this week | 0.9666 |
| How long did patients wait on average last month? | How long did patients wait on average this month? | 0.968 | How long did patients wait on average in the previous month? | 0.964 |
| Visits at every site but the Southgate clinic in the last 3 months | Visits at every site but the Southgate clinic in the last 6 months | 0.9641 | Visits at every site but the Southgate clinic over the past three months | 0.9616 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9709 | How many visits were billed to Medicare so far this month? | 0.9693 |
| Total missed appointments last month | Total missed appointments this month | 0.9733 | Total missed appointments in the previous month | 0.9723 |
| How often did patients miss appointments this month? | How often did patients miss appointments last month? | 0.9728 | How often did patients miss appointments so far this month? | 0.9718 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9709 | How many visits were billed to Medicare in the previous month? | 0.9705 |
| Number of incoming referrals at the Lakeside clinic this week | Number of incoming referrals at the Lakeside clinic last week | 0.9872 | Number of incoming referrals at the Lakeside clinic so far this week | 0.9871 |
| How many referrals did the Lakeside clinic send out this month? | How many referrals did the Lakeside clinic send out last month? | 0.9874 | How many referrals did the Lakeside clinic send out so far this month? | 0.9881 |
| How often did patients miss appointments last month? | How often did patients miss appointments this month? | 0.9728 | How often did patients miss appointments in the previous month? | 0.9737 |
| How many visits were there across all clinics except the Southgate clinic last month? | How many visits were there across all clinics except the Southgate clinic this month? | 0.9848 | How many visits were there across all clinics except the Southgate clinic in the previous month? | 0.986 |
