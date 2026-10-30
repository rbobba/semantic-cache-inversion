# st:mixedbread-ai/mxbai-embed-large-v1 holdout

Dataset sha256(pairs) `c73b22d8e8a8dc27`, 145 cached questions, 524 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 370 | 0.9347 | 0.8369 | 0.9687 | 0.9881 | 0.9973 |
| **equivalent_surface (same wording=True)** | 370 | 0.9347 | 0.8369 | 0.9687 | 0.9881 | 0.9973 |
| **filter_change** | 37 | 0.7536 | 0.6857 | 0.7563 | 0.8235 | 0.8428 |
| **intent_near_miss** | 142 | 0.8145 | 0.7099 | 0.8017 | 0.9433 | 0.9899 |
| **intent_near_miss (same wording=False)** | 142 | 0.8145 | 0.7099 | 0.8017 | 0.9433 | 0.9899 |
| **param_near_miss** | 714 | 0.8892 | 0.786 | 0.8976 | 0.9854 | 0.9971 |
| **param_near_miss (same wording=False)** | 255 | 0.8389 | 0.7558 | 0.8281 | 0.9291 | 0.9864 |
| **param_near_miss (same wording=True)** | 459 | 0.9172 | 0.8431 | 0.9186 | 0.9897 | 0.9971 |
| **paraphrase** | 290 | 0.8911 | 0.7958 | 0.9091 | 0.9621 | 0.9946 |
| equivalent_surface/amount/alias | 10 | 0.9478 | 0.9419 | 0.9469 | 0.955 | 0.9653 |
| equivalent_surface/clinic/alias | 40 | 0.918 | 0.8493 | 0.926 | 0.9626 | 0.9837 |
| equivalent_surface/department/alias | 30 | 0.9689 | 0.9599 | 0.9691 | 0.9791 | 0.9819 |
| equivalent_surface/n/alias | 20 | 0.9944 | 0.9921 | 0.9945 | 0.9966 | 0.9973 |
| equivalent_surface/payer/alias | 2 | 0.9028 | 0.8834 | 0.9028 | 0.9222 | 0.9271 |
| equivalent_surface/period/alias | 268 | 0.9287 | 0.8121 | 0.9722 | 0.9863 | 0.9937 |
| filter_change/filter_added/clinic_visits | 7 | 0.7732 | 0.712 | 0.7988 | 0.809 | 0.8173 |
| filter_change/filter_dropped/total_visits | 30 | 0.7491 | 0.6865 | 0.7423 | 0.8329 | 0.8428 |
| intent_near_miss/aggregation/avg_wait | 7 | 0.801 | 0.7547 | 0.7877 | 0.8642 | 0.8651 |
| intent_near_miss/aggregation/dept_charges | 10 | 0.813 | 0.7806 | 0.7998 | 0.8601 | 0.8701 |
| intent_near_miss/aggregation/dept_visits | 10 | 0.7849 | 0.7455 | 0.791 | 0.8257 | 0.8519 |
| intent_near_miss/aggregation/longest_wait | 7 | 0.8003 | 0.7717 | 0.801 | 0.8242 | 0.8344 |
| intent_near_miss/aggregation/no_show_rate | 7 | 0.8653 | 0.8238 | 0.8429 | 0.9259 | 0.9299 |
| intent_near_miss/aggregation/total_no_shows | 7 | 0.7907 | 0.7383 | 0.7645 | 0.8549 | 0.8897 |
| intent_near_miss/direction/clinic_referrals_in | 10 | 0.9441 | 0.8991 | 0.9441 | 0.9884 | 0.9899 |
| intent_near_miss/direction/clinic_referrals_out | 10 | 0.9479 | 0.9201 | 0.9508 | 0.9717 | 0.9801 |
| intent_near_miss/grouping/top_departments | 10 | 0.7439 | 0.6807 | 0.7311 | 0.8157 | 0.817 |
| intent_near_miss/grouping/top_providers | 10 | 0.7432 | 0.7088 | 0.7337 | 0.7848 | 0.7901 |
| intent_near_miss/measure/dept_avg_wait | 10 | 0.8034 | 0.7791 | 0.8034 | 0.8315 | 0.8406 |
| intent_near_miss/measure/dept_visits | 10 | 0.7862 | 0.7449 | 0.7934 | 0.819 | 0.8255 |
| intent_near_miss/measure/total_no_shows | 7 | 0.6867 | 0.6437 | 0.6974 | 0.7212 | 0.7386 |
| intent_near_miss/measure/total_visits | 7 | 0.7225 | 0.6726 | 0.7125 | 0.7921 | 0.793 |
| intent_near_miss/negation/clinic_visits | 10 | 0.8504 | 0.779 | 0.8322 | 0.9627 | 0.9662 |
| intent_near_miss/negation/clinic_visits_excluding | 10 | 0.8828 | 0.8565 | 0.875 | 0.9245 | 0.9305 |
| param_near_miss/amount/neighbor | 27 | 0.9051 | 0.7624 | 0.9437 | 0.976 | 0.9824 |
| param_near_miss/clinic/neighbor | 80 | 0.8503 | 0.7835 | 0.852 | 0.9145 | 0.9481 |
| param_near_miss/department/neighbor | 60 | 0.8217 | 0.7634 | 0.8252 | 0.8583 | 0.8812 |
| param_near_miss/n/neighbor | 47 | 0.8683 | 0.7875 | 0.8856 | 0.944 | 0.956 |
| param_near_miss/payer/neighbor | 24 | 0.8811 | 0.7935 | 0.8897 | 0.9492 | 0.9525 |
| param_near_miss/period/adjacent | 277 | 0.9191 | 0.7921 | 0.9482 | 0.992 | 0.9971 |
| param_near_miss/period/granularity | 199 | 0.8874 | 0.8194 | 0.8997 | 0.9392 | 0.9666 |
| paraphrase/wording/template | 290 | 0.8911 | 0.7958 | 0.9091 | 0.9621 | 0.9946 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 145 | 0.5379 | [0.4552, 0.6207] | 0.9586 | [0.9241, 0.9862] |
| param_near_miss | 145 | 0.531 | [0.4414, 0.6138] | 0.9586 | [0.9241, 0.9862] |
| period_near_miss | 145 | 0.531 | [0.4483, 0.6069] | 0.9586 | [0.9241, 0.9862] |
| entity_near_miss | 110 | 0.0091 | [0.0, 0.0273] | 0.5636 | [0.4636, 0.6545] |
| intent_near_miss | 135 | 0.0074 | [0.0, 0.0222] | 0.3704 | [0.2889, 0.4444] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 145 | 0.8897 | [0.8414, 0.9379] |
| B | 145 | 0.6069 | [0.5241, 0.6828] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0057 | [0.0, 0.0127] | 0.0057 | 0.0057 | 0.5534 |
| raw_oracle_entry | 0.2519 | [0.2284, 0.3113] | — | — | 0.5534 |
| split_full | 0.0057 | [0.0, 0.0127] | 0.0057 | 0.0057 | 0.5534 |
| split_template | 0.0305 | [0.011, 0.0542] | 0.0305 | 0.0305 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our no-show rate this year? | What was our no-show rate last year? | 0.9854 | What was our no-show rate so far this year? | 0.954 |
| What was our no-show rate this week? | What was our no-show rate last week? | 0.9881 | What was our no-show rate so far this week? | 0.9594 |
| How many patient visits did we have this week? | How many patient visits did we have last week? | 0.9865 | How many patient visits did we have so far this week? | 0.9636 |
| How long did patients wait on average this year? | How long did patients wait on average last year? | 0.9836 | How long did patients wait on average so far this year? | 0.9615 |
| How many patient visits did we have this month? | How many patient visits did we have last month? | 0.985 | How many patient visits did we have so far this month? | 0.9639 |
| How often did patients miss appointments this month? | How often did patients miss appointments last month? | 0.9938 | How often did patients miss appointments so far this month? | 0.9731 |
| What did physical therapy bill in total this week? | What did physical therapy bill in total last week? | 0.9947 | What did physical therapy bill in total so far this week? | 0.9754 |
| What did pediatrics bill in total this year? | What did pediatrics bill in total last year? | 0.9894 | What did pediatrics bill in total year to date? | 0.9712 |
| What did pediatrics bill in total last year? | What did pediatrics bill in total this year? | 0.9894 | What did pediatrics bill in total in the previous year? | 0.9714 |
| What was our overall visit volume this year? | What was our overall visit volume last year? | 0.9881 | What was our overall visit volume so far this year? | 0.9701 |
| How often did patients miss appointments last year? | How often did patients miss appointments this year? | 0.9905 | How often did patients miss appointments in the previous year? | 0.9725 |
| Show visits with waits over 30 minutes in Q3 2026 | Show visits with waits over 30 minutes in Q2 2026 | 0.983 | Show visits with waits over half an hour in Q3 2026 | 0.9653 |
| Total missed appointments last year | Total missed appointments this year | 0.9891 | Total missed appointments in the previous year | 0.9725 |
| How many patient visits did physical therapy handle this month? | How many patient visits did physical therapy handle last month? | 0.9926 | How many patient visits did physical therapy handle so far this month? | 0.9766 |
| How many patients did the Downtown clinic refer elsewhere this month? | How many patients did the Downtown clinic refer elsewhere last month? | 0.994 | How many patients did the Downtown clinic refer elsewhere so far this month? | 0.9782 |
