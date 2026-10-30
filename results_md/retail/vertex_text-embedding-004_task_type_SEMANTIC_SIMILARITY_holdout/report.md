# vertex:text-embedding-004 task_type=SEMANTIC_SIMILARITY holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9581 | 0.9027 | 0.9786 | 0.9943 | 0.9983 |
| **equivalent_surface (same wording=True)** | 310 | 0.9581 | 0.9027 | 0.9786 | 0.9943 | 0.9983 |
| **filter_change** | 27 | 0.7773 | 0.7109 | 0.7883 | 0.8193 | 0.842 |
| **intent_near_miss** | 176 | 0.8331 | 0.7505 | 0.8344 | 0.911 | 0.9674 |
| **intent_near_miss (same wording=False)** | 176 | 0.8331 | 0.7505 | 0.8344 | 0.911 | 0.9674 |
| **param_near_miss** | 643 | 0.9051 | 0.8033 | 0.9179 | 0.9883 | 0.9971 |
| **param_near_miss (same wording=False)** | 228 | 0.8513 | 0.7573 | 0.8547 | 0.9433 | 0.9676 |
| **param_near_miss (same wording=True)** | 415 | 0.9346 | 0.8796 | 0.9414 | 0.9921 | 0.9971 |
| **paraphrase** | 256 | 0.9015 | 0.8171 | 0.9159 | 0.9666 | 0.9855 |
| equivalent_surface/amount/alias | 10 | 0.9921 | 0.9906 | 0.9923 | 0.9932 | 0.9932 |
| equivalent_surface/channel/alias | 10 | 0.964 | 0.9298 | 0.9671 | 0.9951 | 0.9955 |
| equivalent_surface/n/alias | 20 | 0.9965 | 0.9946 | 0.9969 | 0.9979 | 0.9983 |
| equivalent_surface/period/alias | 235 | 0.9501 | 0.8911 | 0.9673 | 0.9911 | 0.9965 |
| equivalent_surface/product/alias | 15 | 0.9643 | 0.937 | 0.9695 | 0.9885 | 0.9909 |
| equivalent_surface/region/alias | 20 | 0.9892 | 0.9799 | 0.9908 | 0.9938 | 0.9943 |
| filter_change/filter_added/region_revenue | 7 | 0.7733 | 0.7078 | 0.8138 | 0.8261 | 0.842 |
| filter_change/filter_dropped/total_revenue | 20 | 0.7787 | 0.7295 | 0.7868 | 0.8181 | 0.8289 |
| intent_near_miss/aggregation/largest_order | 7 | 0.7508 | 0.7147 | 0.7518 | 0.7878 | 0.7912 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8603 | 0.8123 | 0.8737 | 0.8991 | 0.9135 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.9053 | 0.8693 | 0.9078 | 0.9397 | 0.9674 |
| intent_near_miss/aggregation/product_units | 20 | 0.9 | 0.8617 | 0.8912 | 0.9504 | 0.9567 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.7612 | 0.7196 | 0.7288 | 0.8254 | 0.8319 |
| intent_near_miss/direction/product_returns | 10 | 0.8598 | 0.8373 | 0.8593 | 0.8832 | 0.8896 |
| intent_near_miss/direction/product_revenue | 10 | 0.8342 | 0.8219 | 0.8335 | 0.8476 | 0.8527 |
| intent_near_miss/direction/total_returns | 7 | 0.7572 | 0.7342 | 0.7422 | 0.7906 | 0.8443 |
| intent_near_miss/direction/total_revenue | 7 | 0.7948 | 0.782 | 0.7886 | 0.8141 | 0.8159 |
| intent_near_miss/grouping/top_customers | 10 | 0.801 | 0.7844 | 0.8023 | 0.8189 | 0.8337 |
| intent_near_miss/grouping/top_products | 10 | 0.8026 | 0.7769 | 0.7909 | 0.8507 | 0.8644 |
| intent_near_miss/measure/net_sales | 14 | 0.826 | 0.7749 | 0.8087 | 0.8749 | 0.9424 |
| intent_near_miss/measure/total_returns | 7 | 0.7916 | 0.7609 | 0.7984 | 0.8172 | 0.8351 |
| intent_near_miss/measure/total_revenue | 7 | 0.7671 | 0.6865 | 0.7727 | 0.8511 | 0.8674 |
| intent_near_miss/negation/region_revenue | 10 | 0.7951 | 0.7539 | 0.7705 | 0.904 | 0.9085 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.846 | 0.8177 | 0.8434 | 0.8731 | 0.8823 |
| param_near_miss/amount/neighbor | 26 | 0.8874 | 0.8139 | 0.9079 | 0.9391 | 0.9573 |
| param_near_miss/channel/neighbor | 20 | 0.8814 | 0.8342 | 0.8797 | 0.9205 | 0.9272 |
| param_near_miss/n/neighbor | 47 | 0.8823 | 0.8032 | 0.9054 | 0.9228 | 0.949 |
| param_near_miss/period/adjacent | 245 | 0.9306 | 0.8421 | 0.9465 | 0.9952 | 0.9971 |
| param_near_miss/period/granularity | 180 | 0.9189 | 0.8646 | 0.9365 | 0.9611 | 0.9716 |
| param_near_miss/product/neighbor | 85 | 0.8499 | 0.7608 | 0.8533 | 0.9358 | 0.9569 |
| param_near_miss/region/neighbor | 40 | 0.8538 | 0.7483 | 0.8459 | 0.9682 | 0.9706 |
| paraphrase/wording/template | 256 | 0.9015 | 0.8171 | 0.9159 | 0.9666 | 0.9855 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4922 | [0.4141, 0.5781] | 0.9609 | [0.9219, 0.9922] |
| param_near_miss | 128 | 0.4922 | [0.4062, 0.5781] | 0.9609 | [0.9219, 0.9922] |
| period_near_miss | 128 | 0.4922 | [0.3984, 0.5781] | 0.9609 | [0.9219, 0.9922] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.62 | [0.53, 0.72] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.213 | [0.1389, 0.2963] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8906 | [0.8359, 0.9453] |
| B | 128 | 0.6719 | [0.5938, 0.75] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0146 | [0.0061, 0.0645] | 0.0146 | 0.0146 | 0.5344 |
| raw_oracle_entry | 0.309 | [0.2925, 0.3626] | — | — | 0.5344 |
| split_full | 0.096 | [0.0729, 0.2537] | 0.096 | 0.2672 | 0.5344 |
| split_template | 0.8518 | [0.803, 0.8955] | 0.8518 | 0.8685 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our total revenue this year? | What was our total revenue last year? | 0.9846 | What was our total revenue year to date? | 0.9545 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9838 | What was the total value of returns year to date? | 0.956 |
| How many units of water bottles did we sell this year? | How many units of water bottles did we sell last year? | 0.9887 | How many units of water bottles did we sell year to date? | 0.9671 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9838 | What was the total value of returns in the previous year? | 0.9641 |
| How many units of hiking boots did we sell this year? | How many units of hiking boots did we sell last year? | 0.9903 | How many units of hiking boots did we sell year to date? | 0.9711 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.993 | What was the total value of returns so far this month? | 0.9744 |
| How much revenue did we make this month? | How much revenue did we make last month? | 0.9919 | How much revenue did we make so far this month? | 0.9748 |
| How much did yoga mats sell for in total last year? | How much did yoga mats sell for in total this year? | 0.9923 | How much did yoga mats sell for in total in the previous year? | 0.9758 |
| What was the value of yoga mats returned this year? | What was the value of yoga mats returned last year? | 0.9911 | What was the value of yoga mats returned so far this year? | 0.9747 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9963 | What were sales everywhere except the West region this month? | 0.9801 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.993 | What was the total value of returns in the previous month? | 0.9771 |
| How many units of ski jackets did we sell this month? | How many units of ski jackets did we sell last month? | 0.9954 | How many units of ski jackets did we sell so far this month? | 0.9802 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.9919 | How much revenue did we make in the previous month? | 0.977 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.9814 | How much revenue did we make in the previous year? | 0.9668 |
| How many units of trail shoes did we sell this week? | How many units of trail shoes did we sell last week? | 0.9957 | How many units of trail shoes did we sell so far this week? | 0.9844 |
