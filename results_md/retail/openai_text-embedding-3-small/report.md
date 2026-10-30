# openai:text-embedding-3-small

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9218 | 0.8275 | 0.9472 | 0.9811 | 0.9949 |
| **equivalent_surface (same wording=True)** | 310 | 0.9218 | 0.8275 | 0.9472 | 0.9811 | 0.9949 |
| **filter_change** | 27 | 0.5644 | 0.4783 | 0.5773 | 0.6362 | 0.6977 |
| **intent_near_miss** | 176 | 0.7269 | 0.5791 | 0.7429 | 0.8537 | 0.9049 |
| **intent_near_miss (same wording=False)** | 176 | 0.7269 | 0.5791 | 0.7429 | 0.8537 | 0.9049 |
| **param_near_miss** | 643 | 0.8264 | 0.6326 | 0.8582 | 0.9687 | 0.9905 |
| **param_near_miss (same wording=False)** | 228 | 0.714 | 0.5553 | 0.7272 | 0.8579 | 0.9171 |
| **param_near_miss (same wording=True)** | 415 | 0.8881 | 0.7779 | 0.9119 | 0.981 | 0.9905 |
| **paraphrase** | 256 | 0.7957 | 0.6504 | 0.8157 | 0.8949 | 0.9476 |
| equivalent_surface/amount/alias | 10 | 0.959 | 0.955 | 0.9593 | 0.9664 | 0.9683 |
| equivalent_surface/channel/alias | 10 | 0.93 | 0.882 | 0.9352 | 0.9777 | 0.9824 |
| equivalent_surface/n/alias | 20 | 0.9848 | 0.9729 | 0.987 | 0.9941 | 0.9949 |
| equivalent_surface/period/alias | 235 | 0.9112 | 0.8049 | 0.937 | 0.9769 | 0.9856 |
| equivalent_surface/product/alias | 15 | 0.9084 | 0.8641 | 0.9143 | 0.9453 | 0.9477 |
| equivalent_surface/region/alias | 20 | 0.9708 | 0.9507 | 0.975 | 0.9881 | 0.9921 |
| filter_change/filter_added/region_revenue | 7 | 0.5813 | 0.515 | 0.5544 | 0.6674 | 0.6977 |
| filter_change/filter_dropped/total_revenue | 20 | 0.5585 | 0.4617 | 0.5794 | 0.6242 | 0.6432 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5553 | 0.4926 | 0.5559 | 0.6118 | 0.6305 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7795 | 0.6967 | 0.7772 | 0.8583 | 0.875 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8228 | 0.7776 | 0.8262 | 0.8562 | 0.9033 |
| intent_near_miss/aggregation/product_units | 20 | 0.8083 | 0.7445 | 0.8177 | 0.8623 | 0.8636 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5636 | 0.4566 | 0.5559 | 0.6788 | 0.692 |
| intent_near_miss/direction/product_returns | 10 | 0.8053 | 0.7601 | 0.8 | 0.86 | 0.8819 |
| intent_near_miss/direction/product_revenue | 10 | 0.7799 | 0.745 | 0.783 | 0.8118 | 0.8158 |
| intent_near_miss/direction/total_returns | 7 | 0.6267 | 0.5502 | 0.623 | 0.7082 | 0.749 |
| intent_near_miss/direction/total_revenue | 7 | 0.6045 | 0.5505 | 0.6077 | 0.6517 | 0.6615 |
| intent_near_miss/grouping/top_customers | 10 | 0.6719 | 0.6216 | 0.6811 | 0.7153 | 0.7295 |
| intent_near_miss/grouping/top_products | 10 | 0.6863 | 0.6313 | 0.6664 | 0.7704 | 0.7792 |
| intent_near_miss/measure/net_sales | 14 | 0.6622 | 0.585 | 0.6667 | 0.7311 | 0.827 |
| intent_near_miss/measure/total_returns | 7 | 0.6623 | 0.5901 | 0.645 | 0.7391 | 0.7561 |
| intent_near_miss/measure/total_revenue | 7 | 0.5863 | 0.4756 | 0.5927 | 0.6952 | 0.7424 |
| intent_near_miss/negation/region_revenue | 10 | 0.7341 | 0.6714 | 0.6881 | 0.8986 | 0.9049 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8485 | 0.8328 | 0.8496 | 0.8751 | 0.8757 |
| param_near_miss/amount/neighbor | 26 | 0.8706 | 0.7449 | 0.9251 | 0.9544 | 0.9677 |
| param_near_miss/channel/neighbor | 20 | 0.7561 | 0.6469 | 0.8012 | 0.852 | 0.8613 |
| param_near_miss/n/neighbor | 47 | 0.8285 | 0.6769 | 0.8767 | 0.9255 | 0.9421 |
| param_near_miss/period/adjacent | 245 | 0.8616 | 0.6857 | 0.8829 | 0.9837 | 0.9905 |
| param_near_miss/period/granularity | 180 | 0.8686 | 0.7609 | 0.8941 | 0.955 | 0.9869 |
| param_near_miss/product/neighbor | 85 | 0.6767 | 0.4745 | 0.7021 | 0.8354 | 0.8852 |
| param_near_miss/region/neighbor | 40 | 0.7426 | 0.5854 | 0.7253 | 0.9166 | 0.942 |
| paraphrase/wording/template | 256 | 0.7957 | 0.6504 | 0.8157 | 0.8949 | 0.9476 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5391 | [0.4531, 0.625] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5391 | [0.4529, 0.625] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5391 | [0.4531, 0.6328] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.56 | [0.47, 0.66] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4352 | [0.3426, 0.5278] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 1.0 | [1.0, 1.0] |
| B | 128 | 0.7422 | [0.6641, 0.8203] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0063 | [0.0019, 0.0113] | 0.0063 | 0.0063 | 0.5373 |
| raw_oracle_entry | 0.0863 | [0.0813, 0.1212] | — | — | 0.5373 |
| split_full | 0.2812 | [0.2645, 0.3023] | 0.2902 | 0.3531 | 0.5373 |
| split_template | 0.6541 | [0.6324, 0.6777] | 0.6541 | 0.6541 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the total value of returns this year? | What was the total value of returns last year? | 0.965 | What was the total value of returns so far this year? | 0.9063 |
| How much revenue did we make this month? | How much revenue did we make last month? | 0.9531 | How much revenue did we make so far this month? | 0.8997 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.965 | What was the total value of returns in the previous year? | 0.9175 |
| What was our total revenue this year? | What was our total revenue last year? | 0.9513 | What was our total revenue so far this year? | 0.9071 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.9488 | How much revenue did we make in the previous year? | 0.9081 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9687 | What were sales net of returns in the previous year? | 0.9283 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.9531 | How much revenue did we make in the previous month? | 0.917 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.951 | How much revenue did we make so far this week? | 0.9161 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9713 | What were sales net of returns in the previous month? | 0.937 |
| How many units of water bottles did we sell this year? | How many units of water bottles did we sell last year? | 0.9774 | How many units of water bottles did we sell so far this year? | 0.9479 |
| Total revenue for the West last month | Total revenue for the West this month | 0.9581 | Total revenue for the West region last month | 0.9305 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9603 | What was the total value of returns in the previous month? | 0.9357 |
| What was the value of yoga mats returned this year? | What was the value of yoga mats returned last year? | 0.9836 | What was the value of yoga mats returned so far this year? | 0.9594 |
| How many units of hiking boots did we sell this year? | How many units of hiking boots did we sell last year? | 0.9848 | How many units of hiking boots did we sell so far this year? | 0.961 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9603 | What was the total value of returns so far this month? | 0.9364 |
