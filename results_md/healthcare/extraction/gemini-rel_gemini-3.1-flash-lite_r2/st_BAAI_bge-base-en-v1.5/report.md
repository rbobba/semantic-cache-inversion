# st:BAAI/bge-base-en-v1.5

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9454 | 0.8706 | 0.9686 | 0.9875 | 0.9981 |
| **equivalent_surface (same wording=True)** | 370 | 0.9454 | 0.8706 | 0.9686 | 0.9875 | 0.9981 |
| **filter_change** | 37 | 0.7888 | 0.6792 | 0.8036 | 0.8652 | 0.8864 |
| **intent_near_miss** | 142 | 0.8268 | 0.7603 | 0.8153 | 0.9149 | 0.9872 |
| **intent_near_miss (same wording=False)** | 142 | 0.8268 | 0.7603 | 0.8153 | 0.9149 | 0.9872 |
| **param_near_miss** | 714 | 0.9025 | 0.8171 | 0.9111 | 0.9857 | 0.9968 |
| **param_near_miss (same wording=False)** | 255 | 0.8493 | 0.7744 | 0.8511 | 0.9303 | 0.9816 |
| **param_near_miss (same wording=True)** | 459 | 0.932 | 0.8695 | 0.9362 | 0.9909 | 0.9968 |
| **paraphrase** | 290 | 0.8909 | 0.8152 | 0.8981 | 0.9563 | 0.9925 |
| equivalent_surface/amount/alias | 10 | 0.9372 | 0.9286 | 0.9365 | 0.9489 | 0.9533 |
| equivalent_surface/clinic/alias | 40 | 0.9331 | 0.9077 | 0.9357 | 0.9656 | 0.9869 |
| equivalent_surface/department/alias | 30 | 0.972 | 0.9656 | 0.9712 | 0.9784 | 0.9875 |
| equivalent_surface/n/alias | 20 | 0.9951 | 0.9927 | 0.9954 | 0.9978 | 0.9981 |
| equivalent_surface/payer/alias | 2 | 0.9162 | 0.8948 | 0.9162 | 0.9375 | 0.9429 |
| equivalent_surface/period/alias | 268 | 0.9411 | 0.8642 | 0.971 | 0.9857 | 0.9927 |
| filter_change/filter_added/clinic_visits | 7 | 0.7921 | 0.7174 | 0.8069 | 0.8462 | 0.8556 |
| filter_change/filter_dropped/total_visits | 30 | 0.7881 | 0.6895 | 0.7992 | 0.8713 | 0.8864 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.8113 | 0.7635 | 0.7889 | 0.8888 | 0.8984 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.7846 | 0.7365 | 0.79 | 0.8172 | 0.8299 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7811 | 0.7474 | 0.7722 | 0.8265 | 0.8501 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.7916 | 0.7724 | 0.7967 | 0.8074 | 0.8204 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8734 | 0.8519 | 0.8695 | 0.8981 | 0.9038 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.807 | 0.7705 | 0.7904 | 0.8591 | 0.8696 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9311 | 0.8694 | 0.9359 | 0.9854 | 0.9872 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.8968 | 0.8722 | 0.8914 | 0.925 | 0.9698 |
| intent_near_miss/grouping/top_departments | 10 | 0.8058 | 0.7221 | 0.7876 | 0.8884 | 0.893 |
| intent_near_miss/grouping/top_providers | 10 | 0.7854 | 0.7645 | 0.7769 | 0.8092 | 0.8274 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.8201 | 0.7964 | 0.8174 | 0.8498 | 0.857 |
| intent_near_miss/measure/dept_visits | 10 | 0.8216 | 0.7909 | 0.8221 | 0.8546 | 0.8593 |
| intent_near_miss/measure/total_no_shows | 7 | 0.7449 | 0.7087 | 0.7499 | 0.7732 | 0.7811 |
| intent_near_miss/measure/total_visits | 7 | 0.8004 | 0.7495 | 0.7953 | 0.8708 | 0.8835 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8968 | 0.8597 | 0.8874 | 0.9563 | 0.9601 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8374 | 0.7764 | 0.8387 | 0.8922 | 0.9035 |
| param_near_miss/amount/neighbor | 27 | 0.902 | 0.7926 | 0.9472 | 0.9622 | 0.9644 |
| param_near_miss/clinic/neighbor | 80 | 0.8629 | 0.7749 | 0.871 | 0.9448 | 0.9618 |
| param_near_miss/department/neighbor | 60 | 0.8557 | 0.8023 | 0.8609 | 0.9067 | 0.9182 |
| param_near_miss/n/neighbor | 47 | 0.9077 | 0.8247 | 0.9334 | 0.9642 | 0.9749 |
| param_near_miss/payer/neighbor | 24 | 0.9076 | 0.8592 | 0.9235 | 0.9594 | 0.9617 |
| param_near_miss/period/adjacent | 277 | 0.9248 | 0.8339 | 0.9428 | 0.993 | 0.9968 |
| param_near_miss/period/granularity | 199 | 0.8997 | 0.8411 | 0.9123 | 0.948 | 0.9599 |
| paraphrase/wording/template | 290 | 0.8909 | 0.8152 | 0.8981 | 0.9563 | 0.9925 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.6345 | [0.5586, 0.7103] | 0.9931 | [0.9793, 1.0] |
| param_near_miss | 145 | 0.6345 | [0.5517, 0.7105] | 0.9931 | [0.9793, 1.0] |
| period_near_miss | 145 | 0.6345 | [0.5517, 0.7172] | 0.9862 | [0.9655, 1.0] |
| entity_near_miss | 110 | 0.0091 | [0.0, 0.0273] | 0.7364 | [0.6545, 0.8182] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.3185 | [0.2443, 0.4] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9448 | [0.9103, 0.9793] |
| B | 145 | 0.731 | [0.6552, 0.8] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0032 | [0.0008, 0.009] | 0.0032 | 0.0032 | 0.5598 |
| raw_oracle_entry | 0.0925 | [0.0828, 0.1262] | — | — | 0.5598 |
| split_full | 0.303 | [0.2855, 0.3191] | 0.303 | 0.3812 | 0.5598 |
| split_template | 0.5949 | [0.5751, 0.6144] | 0.5949 | 0.6643 | 1.0 |
| split_full_extracted | 0.2727 | [0.2552, 0.2933] | 0.2759 | 0.3812 | 0.5486 |
| split_template_extracted | 0.5678 | [0.5472, 0.5934] | 0.575 | 0.6611 | 0.9896 |
| split_template_extracted_slots | 0.5678 | [0.5472, 0.5934] | 0.575 | 0.6611 | 0.9896 |
| split_template_negguard | 0.575 | [0.5543, 0.5965] | 0.575 | 0.701 | 0.9896 |
| split_template_guarded_goldsig | 0.9625 | [0.9512, 0.9733] | 0.9833 | 0.9833 | 0.9896 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9747 | 0.2719 | 0.2719 [0.254, 0.2899] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9911 | 0.5367 | 0.5367 [0.5141, 0.5599] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9911 | 0.5367 | 0.5367 [0.5141, 0.5599] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9911 | 0.5367 | 0.5367 [0.5141, 0.5599] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9896 | 0.9833 [0.9743, 0.9905] | 0.0064 [0.0023, 0.0118] | 8 | 8 | 0 | 0 |

Similarity as a detector of value errors (right-intent matches): AUC 0.1397 [0.0, 0.3785], 3 with a template value wrong vs 1138 right; median similarity 0.8343 vs 1.0. 0.5 = no signal.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total missed appointments last month | Total missed appointments this month | 0.9877 | Total missed appointments in the previous month | 0.9661 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9944 | What was our no-show rate so far this year? | 0.9744 |
| What was the average wait time in orthopedics this month? | What was the average wait time in orthopedics last month? | 0.9942 | What was the average wait time in orthopedics so far this month? | 0.9755 |
| Show visits with waits over 30 minutes in Q3 2026 | Show visits with waits over 30 minutes in Q2 2026 | 0.9707 | Show visits with waits over half an hour in Q3 2026 | 0.9533 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9857 | How many visits were billed to Medicare so far this month? | 0.9686 |
| Total missed appointments last year | Total missed appointments this year | 0.9911 | Total missed appointments in the previous year | 0.9746 |
| How long did patients wait on average this year? | How long did patients wait on average last year? | 0.9923 | How long did patients wait on average so far this year? | 0.976 |
| Which appointments had a wait longer than 15 minutes in Q3 2026? | Which appointments had a wait longer than 15 minutes in Q2 2026? | 0.9742 | Which appointments had a wait longer than 15 minutes in the third quarter of 2026? | 0.9586 |
| How often did patients miss appointments this month? | How often did patients miss appointments last month? | 0.9911 | How often did patients miss appointments so far this month? | 0.9757 |
| How many visits were billed to commercial insurance last month? | How many visits were billed to commercial insurance this month? | 0.9931 | How many visits were billed to commercial insurance in the previous month? | 0.9785 |
| How many patient visits did we have this month? | How many patient visits did we have last month? | 0.9827 | How many patient visits did we have so far this month? | 0.9683 |
| How long did patients wait on average last month? | How long did patients wait on average this month? | 0.9908 | How long did patients wait on average in the previous month? | 0.9767 |
| What was the longest wait in Q3 2026? | What was the longest wait in Q2 2026? | 0.9547 | What was the longest wait in the third quarter of 2026? | 0.9405 |
| What did pediatrics bill in total this year? | What did pediatrics bill in total last year? | 0.991 | What did pediatrics bill in total so far this year? | 0.9771 |
| What was the average wait time in family medicine last year? | What was the average wait time in family medicine this year? | 0.9945 | What was the average wait time in family medicine in the previous year? | 0.9807 |
