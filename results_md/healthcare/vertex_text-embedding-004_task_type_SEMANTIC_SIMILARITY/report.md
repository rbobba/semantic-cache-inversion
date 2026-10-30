# vertex:text-embedding-004 task_type=SEMANTIC_SIMILARITY

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 1254 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9618 | 0.9118 | 0.9791 | 0.9936 | 0.9987 |
| **equivalent_surface (same wording=True)** | 370 | 0.9618 | 0.9118 | 0.9791 | 0.9936 | 0.9987 |
| **filter_change** | 37 | 0.8122 | 0.7563 | 0.8183 | 0.8848 | 0.9082 |
| **intent_near_miss** | 142 | 0.8417 | 0.735 | 0.8421 | 0.9395 | 0.9814 |
| **intent_near_miss (same wording=False)** | 142 | 0.8417 | 0.735 | 0.8421 | 0.9395 | 0.9814 |
| **param_near_miss** | 714 | 0.9243 | 0.8506 | 0.9368 | 0.9895 | 0.9975 |
| **param_near_miss (same wording=False)** | 255 | 0.88 | 0.8052 | 0.8865 | 0.9531 | 0.9886 |
| **param_near_miss (same wording=True)** | 459 | 0.949 | 0.8962 | 0.9552 | 0.993 | 0.9975 |
| **paraphrase** | 290 | 0.9179 | 0.8435 | 0.9307 | 0.9735 | 0.9931 |
| equivalent_surface/amount/alias | 10 | 0.964 | 0.9167 | 0.972 | 0.9841 | 0.9883 |
| equivalent_surface/clinic/alias | 40 | 0.9528 | 0.9041 | 0.9604 | 0.9817 | 0.989 |
| equivalent_surface/department/alias | 30 | 0.9789 | 0.9697 | 0.9794 | 0.9857 | 0.99 |
| equivalent_surface/n/alias | 20 | 0.9971 | 0.9959 | 0.9975 | 0.9984 | 0.9987 |
| equivalent_surface/payer/alias | 2 | 0.9425 | 0.9411 | 0.9425 | 0.9439 | 0.9442 |
| equivalent_surface/period/alias | 268 | 0.9586 | 0.9086 | 0.98 | 0.9925 | 0.998 |
| filter_change/filter_added/clinic_visits | 7 | 0.8759 | 0.843 | 0.8887 | 0.8977 | 0.9082 |
| filter_change/filter_dropped/total_visits | 30 | 0.7974 | 0.7345 | 0.8043 | 0.8402 | 0.8657 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.8554 | 0.8379 | 0.8517 | 0.8764 | 0.8786 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.8452 | 0.8246 | 0.8412 | 0.8863 | 0.8891 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.8444 | 0.8324 | 0.8448 | 0.8607 | 0.8675 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8585 | 0.844 | 0.859 | 0.8705 | 0.8762 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8871 | 0.8501 | 0.8842 | 0.9248 | 0.9312 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.8728 | 0.7997 | 0.848 | 0.961 | 0.9644 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.946 | 0.9048 | 0.9474 | 0.9812 | 0.9814 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9423 | 0.9264 | 0.9395 | 0.9563 | 0.9677 |
| intent_near_miss/grouping/top_departments | 10 | 0.7806 | 0.7182 | 0.7319 | 0.865 | 0.8813 |
| intent_near_miss/grouping/top_providers | 10 | 0.8146 | 0.7945 | 0.8091 | 0.8433 | 0.8553 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.8278 | 0.8119 | 0.8306 | 0.8456 | 0.8504 |
| intent_near_miss/measure/dept_visits | 10 | 0.8286 | 0.8172 | 0.827 | 0.843 | 0.8444 |
| intent_near_miss/measure/total_no_shows | 7 | 0.768 | 0.7165 | 0.7786 | 0.8048 | 0.8084 |
| intent_near_miss/measure/total_visits | 7 | 0.7429 | 0.7198 | 0.7326 | 0.7771 | 0.7883 |
| intent_near_miss/negation/clinic_visits | 10 | 0.7892 | 0.7222 | 0.764 | 0.8868 | 0.9142 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8446 | 0.7693 | 0.8537 | 0.9363 | 0.9369 |
| param_near_miss/amount/neighbor | 27 | 0.9206 | 0.8535 | 0.9359 | 0.9742 | 0.9783 |
| param_near_miss/clinic/neighbor | 80 | 0.9016 | 0.791 | 0.9195 | 0.9572 | 0.974 |
| param_near_miss/department/neighbor | 60 | 0.8618 | 0.8142 | 0.8615 | 0.8967 | 0.91 |
| param_near_miss/n/neighbor | 47 | 0.8938 | 0.8308 | 0.9069 | 0.9342 | 0.9564 |
| param_near_miss/payer/neighbor | 24 | 0.9173 | 0.8596 | 0.9191 | 0.9619 | 0.9666 |
| param_near_miss/period/adjacent | 277 | 0.9436 | 0.8653 | 0.9596 | 0.995 | 0.9975 |
| param_near_miss/period/granularity | 199 | 0.9341 | 0.8761 | 0.9481 | 0.9683 | 0.9828 |
| paraphrase/wording/template | 290 | 0.9179 | 0.8435 | 0.9307 | 0.9735 | 0.9931 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.4552 | [0.3791, 0.531] | 0.9931 | [0.9793, 1.0] |
| param_near_miss | 145 | 0.4552 | [0.3793, 0.5379] | 0.9931 | [0.9793, 1.0] |
| period_near_miss | 145 | 0.4483 | [0.3655, 0.531] | 0.9862 | [0.9655, 1.0] |
| entity_near_miss | 110 | 0.0273 | [0.0, 0.0636] | 0.6273 | [0.5455, 0.7182] |
| intent_near_miss | 135 | 0.0 | [0.0, 0.0] | 0.2444 | [0.1704, 0.3185] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.9034 | [0.855, 0.9517] |
| B | 145 | 0.5379 | [0.4621, 0.6138] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0088 | [0.0039, 0.0153] | 0.0088 | 0.0088 | 0.5598 |
| raw_oracle_entry | 0.1252 | [0.1117, 0.1619] | — | — | 0.5598 |
| split_full | 0.3062 | [0.2887, 0.3231] | 0.3182 | 0.4179 | 0.5598 |
| split_template | 0.6132 | [0.594, 0.633] | 0.6132 | 0.7767 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Visit volume at the Downtown clinic in Q3 2026 | Visit volume at the Downtown clinic in Q2 2026 | 0.9683 | Visit volume at the Downtown clinic in the third quarter of 2026 | 0.9274 |
| Visit volume at the Northgate clinic in Q3 2026 | Visit volume at the Northgate clinic in Q2 2026 | 0.9666 | Visit volume at the Northgate clinic in the third quarter of 2026 | 0.9466 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9859 | What was our overall visit volume year to date? | 0.967 |
| How many patient visits did we have last year? | How many patient visits did we have this year? | 0.9891 | How many patient visits did we have in the previous year? | 0.9707 |
| How many patient visits did we have this month? | How many patient visits did we have last month? | 0.9926 | How many patient visits did we have so far this month? | 0.9772 |
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9827 | What was our no-show rate so far this year? | 0.9675 |
| How many patient visits did we have last month? | How many patient visits did we have this month? | 0.9926 | How many patient visits did we have in the previous month? | 0.979 |
| What did pediatrics bill in total last year? | What did pediatrics bill in total this year? | 0.9938 | How much did pediatrics bill last year? | 0.981 |
| How many visits were billed to Medicare this month? | How many visits were billed to Medicare last month? | 0.9955 | How many visits were billed to Medicare so far this month? | 0.9834 |
| How often did patients miss appointments last year? | How often did patients miss appointments this year? | 0.9935 | How often did patients miss appointments in the previous year? | 0.9821 |
| What did pediatrics bill in total this year? | What did pediatrics bill in total last year? | 0.9938 | How much did pediatrics bill this year? | 0.9824 |
| Total charges billed by physical therapy this year | Total charges billed by physical therapy last year | 0.9931 | Total charges billed by physical therapy so far this year | 0.9822 |
| Total charges billed by radiology this year | Total charges billed by radiology last year | 0.9929 | Total charges billed by radiology so far this year | 0.9822 |
| How many visits were billed to Medicare last month? | How many visits were billed to Medicare this month? | 0.9955 | How many visits were billed to Medicare in the previous month? | 0.9849 |
| How long did patients wait on average this month? | How long did patients wait on average last month? | 0.994 | How long did patients wait on average so far this month? | 0.9848 |
