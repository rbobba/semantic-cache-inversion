# vertex:text-embedding-004

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.952 | 0.8618 | 0.9798 | 0.995 | 0.9989 |
| **equivalent_surface (same wording=True)** | 262 | 0.952 | 0.8618 | 0.9798 | 0.995 | 0.9989 |
| **filter_change** | 37 | 0.7351 | 0.6524 | 0.7448 | 0.8321 | 0.8839 |
| **intent_near_miss** | 176 | 0.7828 | 0.669 | 0.7886 | 0.8834 | 0.932 |
| **intent_near_miss (same wording=False)** | 176 | 0.7828 | 0.669 | 0.7886 | 0.8834 | 0.932 |
| **param_near_miss** | 637 | 0.876 | 0.7334 | 0.8943 | 0.9874 | 0.998 |
| **param_near_miss (same wording=False)** | 228 | 0.7897 | 0.6688 | 0.7968 | 0.9011 | 0.9786 |
| **param_near_miss (same wording=True)** | 409 | 0.9241 | 0.8397 | 0.9425 | 0.9928 | 0.998 |
| **paraphrase** | 384 | 0.8465 | 0.7293 | 0.8651 | 0.9468 | 0.987 |
| equivalent_surface/account/alias | 10 | 0.96 | 0.9255 | 0.9645 | 0.9798 | 0.9851 |
| equivalent_surface/amount/alias | 10 | 0.9884 | 0.9861 | 0.9886 | 0.9906 | 0.9909 |
| equivalent_surface/category/alias | 15 | 0.97 | 0.9322 | 0.98 | 0.9909 | 0.9922 |
| equivalent_surface/merchant/alias | 12 | 0.9918 | 0.9846 | 0.992 | 0.9977 | 0.998 |
| equivalent_surface/n/alias | 20 | 0.9964 | 0.9935 | 0.9976 | 0.9983 | 0.9989 |
| equivalent_surface/period/alias | 195 | 0.9413 | 0.8512 | 0.9741 | 0.9926 | 0.9974 |
| filter_change/filter_added/category_spend_total | 7 | 0.7878 | 0.7298 | 0.7617 | 0.8728 | 0.8839 |
| filter_change/filter_dropped/total_spend | 30 | 0.7228 | 0.638 | 0.7081 | 0.8274 | 0.8371 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7328 | 0.6365 | 0.709 | 0.8249 | 0.8292 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8257 | 0.7334 | 0.8385 | 0.8998 | 0.927 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8322 | 0.7429 | 0.8448 | 0.8999 | 0.9166 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8086 | 0.7388 | 0.7988 | 0.8924 | 0.932 |
| intent_near_miss/aggregation/total_spend | 7 | 0.6991 | 0.6096 | 0.6679 | 0.8479 | 0.8785 |
| intent_near_miss/direction/income_total | 7 | 0.7007 | 0.6022 | 0.7236 | 0.781 | 0.7811 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7662 | 0.729 | 0.7675 | 0.8072 | 0.8353 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7822 | 0.7261 | 0.7984 | 0.8302 | 0.8409 |
| intent_near_miss/direction/total_spend | 7 | 0.7096 | 0.6431 | 0.7189 | 0.7678 | 0.7728 |
| intent_near_miss/grouping/top_categories | 10 | 0.762 | 0.6596 | 0.7742 | 0.8554 | 0.8678 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7677 | 0.701 | 0.762 | 0.8265 | 0.8279 |
| intent_near_miss/measure/income_total | 7 | 0.7359 | 0.6601 | 0.7512 | 0.8139 | 0.8222 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.734 | 0.6568 | 0.7271 | 0.7985 | 0.8505 |
| intent_near_miss/measure/total_spend | 7 | 0.746 | 0.687 | 0.7333 | 0.8277 | 0.8625 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8665 | 0.8187 | 0.8715 | 0.9099 | 0.926 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8444 | 0.7966 | 0.849 | 0.8813 | 0.8977 |
| param_near_miss/account/neighbor | 20 | 0.8025 | 0.7037 | 0.8128 | 0.9099 | 0.9241 |
| param_near_miss/amount/neighbor | 25 | 0.8541 | 0.7224 | 0.9255 | 0.959 | 0.973 |
| param_near_miss/category/neighbor | 45 | 0.8467 | 0.7346 | 0.8515 | 0.9415 | 0.9853 |
| param_near_miss/merchant/neighbor | 87 | 0.7899 | 0.6703 | 0.8054 | 0.8819 | 0.9057 |
| param_near_miss/n/neighbor | 45 | 0.8912 | 0.767 | 0.9461 | 0.9695 | 0.9809 |
| param_near_miss/period/adjacent | 230 | 0.9037 | 0.7667 | 0.9337 | 0.9945 | 0.998 |
| param_near_miss/period/granularity | 185 | 0.8964 | 0.796 | 0.9223 | 0.9632 | 0.9774 |
| paraphrase/wording/template | 384 | 0.8465 | 0.7293 | 0.8651 | 0.9468 | 0.987 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5234 | [0.4375, 0.6094] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5234 | [0.4375, 0.6172] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5234 | [0.4453, 0.6094] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.82 | [0.7498, 0.89] |
| intent_near_miss | 118 | 0.0085 | [0.0, 0.0254] | 0.4661 | [0.3814, 0.5511] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0049 | [0.0017, 0.0155] | 0.0049 | 0.0049 | 0.5317 |
| raw_oracle_entry | 0.0927 | [0.0812, 0.123] | — | — | 0.5317 |
| split_full | 0.2423 | [0.2278, 0.2731] | 0.2561 | 0.3114 | 0.5317 |
| split_template | 0.9732 | [0.9599, 0.9844] | 0.9732 | 0.9732 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9478 | Income minus expenses during 2025 | 0.7961 |
| Total money coming in last year | Total money coming in this year | 0.9238 | Total money coming in during 2025 | 0.7838 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9901 | Average transaction amount at Uber during 2025 | 0.8811 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9924 | What was the biggest single thing I bought during 2025? | 0.8836 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9815 | What was my total spending last year? | 0.8969 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9879 | On average, how much did each purchase at Shell cost in 2025? | 0.9038 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9936 | How much money did Spotify give back to me during 2025? | 0.9148 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9948 | What was my average purchase at Walmart last year? | 0.9188 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9891 | Sum of my purchases at Starbucks last year | 0.9195 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9925 | Total refunds from Shell in 2025 | 0.9242 |
| Total spent on gas last year | Total spent on gas this year | 0.9785 | Total spent on fuel last year | 0.9212 |
| What was the biggest single thing I bought last month? | What was the biggest single thing I bought this month? | 0.996 | What was the biggest single thing I bought in the previous month? | 0.9413 |
| How much did I earn this year? | How much did I earn last year? | 0.9805 | How much did I earn so far this year? | 0.937 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.988 | How many transactions did I have at Starbucks last year? | 0.9504 |
| Sum of my purchases at Home Depot last month | Sum of my purchases at Home Depot this month | 0.9939 | Sum of my purchases at Home Depot in the previous month | 0.9593 |
