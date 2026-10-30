# voyage:voyage-3-large holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9226 | 0.8169 | 0.9535 | 0.9831 | 0.9957 |
| **equivalent_surface (same wording=True)** | 310 | 0.9226 | 0.8169 | 0.9535 | 0.9831 | 0.9957 |
| **filter_change** | 27 | 0.7121 | 0.6092 | 0.7109 | 0.8219 | 0.8594 |
| **intent_near_miss** | 176 | 0.7668 | 0.6846 | 0.7641 | 0.8611 | 0.9147 |
| **intent_near_miss (same wording=False)** | 176 | 0.7668 | 0.6846 | 0.7641 | 0.8611 | 0.9147 |
| **param_near_miss** | 643 | 0.8596 | 0.7575 | 0.8779 | 0.9585 | 0.9886 |
| **param_near_miss (same wording=False)** | 228 | 0.8043 | 0.6911 | 0.8201 | 0.9036 | 0.9395 |
| **param_near_miss (same wording=True)** | 415 | 0.89 | 0.7984 | 0.897 | 0.9705 | 0.9886 |
| **paraphrase** | 256 | 0.8791 | 0.782 | 0.8967 | 0.948 | 0.9757 |
| equivalent_surface/amount/alias | 10 | 0.981 | 0.9777 | 0.9813 | 0.9838 | 0.9842 |
| equivalent_surface/channel/alias | 10 | 0.9448 | 0.8966 | 0.9528 | 0.9835 | 0.9872 |
| equivalent_surface/n/alias | 20 | 0.9897 | 0.9848 | 0.9909 | 0.9932 | 0.9957 |
| equivalent_surface/period/alias | 235 | 0.909 | 0.8054 | 0.9406 | 0.9739 | 0.9916 |
| equivalent_surface/product/alias | 15 | 0.9336 | 0.8905 | 0.9477 | 0.9603 | 0.9609 |
| equivalent_surface/region/alias | 20 | 0.9668 | 0.9505 | 0.9674 | 0.9814 | 0.9863 |
| filter_change/filter_added/region_revenue | 7 | 0.6923 | 0.6105 | 0.7091 | 0.7486 | 0.7511 |
| filter_change/filter_dropped/total_revenue | 20 | 0.719 | 0.61 | 0.7133 | 0.8506 | 0.8594 |
| intent_near_miss/aggregation/largest_order | 7 | 0.6528 | 0.6274 | 0.6519 | 0.6772 | 0.6927 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7694 | 0.7353 | 0.7614 | 0.8154 | 0.8277 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.837 | 0.7713 | 0.8391 | 0.9055 | 0.9106 |
| intent_near_miss/aggregation/product_units | 20 | 0.8026 | 0.7453 | 0.7899 | 0.8686 | 0.9147 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.6531 | 0.579 | 0.6231 | 0.7394 | 0.7397 |
| intent_near_miss/direction/product_returns | 10 | 0.7948 | 0.765 | 0.7821 | 0.8401 | 0.8956 |
| intent_near_miss/direction/product_revenue | 10 | 0.8121 | 0.7929 | 0.8148 | 0.8308 | 0.8555 |
| intent_near_miss/direction/total_returns | 7 | 0.7026 | 0.6192 | 0.7142 | 0.7645 | 0.7757 |
| intent_near_miss/direction/total_revenue | 7 | 0.7382 | 0.7036 | 0.7522 | 0.7677 | 0.7684 |
| intent_near_miss/grouping/top_customers | 10 | 0.7343 | 0.6913 | 0.749 | 0.7544 | 0.7556 |
| intent_near_miss/grouping/top_products | 10 | 0.7311 | 0.7033 | 0.7342 | 0.7611 | 0.7651 |
| intent_near_miss/measure/net_sales | 14 | 0.7258 | 0.6452 | 0.7173 | 0.7937 | 0.8406 |
| intent_near_miss/measure/total_returns | 7 | 0.7346 | 0.666 | 0.7728 | 0.7786 | 0.7799 |
| intent_near_miss/measure/total_revenue | 7 | 0.7274 | 0.6752 | 0.7396 | 0.7652 | 0.787 |
| intent_near_miss/negation/region_revenue | 10 | 0.778 | 0.7285 | 0.7479 | 0.8968 | 0.9056 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8658 | 0.8339 | 0.8639 | 0.9042 | 0.9051 |
| param_near_miss/amount/neighbor | 26 | 0.8759 | 0.8138 | 0.8985 | 0.9187 | 0.9228 |
| param_near_miss/channel/neighbor | 20 | 0.8307 | 0.7756 | 0.8357 | 0.8829 | 0.8844 |
| param_near_miss/n/neighbor | 47 | 0.8681 | 0.7834 | 0.886 | 0.9292 | 0.9482 |
| param_near_miss/period/adjacent | 245 | 0.8914 | 0.7747 | 0.9124 | 0.9767 | 0.9886 |
| param_near_miss/period/granularity | 180 | 0.8489 | 0.7613 | 0.8703 | 0.9132 | 0.9481 |
| param_near_miss/product/neighbor | 85 | 0.8146 | 0.6975 | 0.8268 | 0.9158 | 0.9446 |
| param_near_miss/region/neighbor | 40 | 0.8018 | 0.6758 | 0.8057 | 0.9352 | 0.9446 |
| paraphrase/wording/template | 256 | 0.8791 | 0.782 | 0.8967 | 0.948 | 0.9757 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.3828 | [0.3047, 0.4688] | 0.9375 | [0.8984, 0.9766] |
| param_near_miss | 128 | 0.3828 | [0.3047, 0.4688] | 0.9375 | [0.8906, 0.9766] |
| period_near_miss | 128 | 0.3828 | [0.3047, 0.4688] | 0.9297 | [0.875, 0.9688] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.66 | [0.57, 0.75] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.3981 | [0.3056, 0.5] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8438 | [0.7812, 0.9062] |
| B | 128 | 0.5469 | [0.4609, 0.6328] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0397 | [0.0255, 0.11] | 0.0397 | 0.0856 | 0.5344 |
| raw_oracle_entry | 0.3883 | [0.3619, 0.4388] | — | — | 0.5344 |
| split_full | 0.2317 | [0.1992, 0.3914] | 0.3612 | 0.3612 | 0.5344 |
| split_template | 0.952 | [0.9243, 0.9751] | 0.952 | 0.9708 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What did trail shoes generate in sales this week? | What did trail shoes generate in sales last week? | 0.9879 | What did trail shoes generate in sales so far this week? | 0.9575 |
| Total revenue from every region but the Southeast last month | Total revenue from every region but the Southeast this month | 0.9794 | Total revenue from every region but the Southeast region last month | 0.9523 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9886 | What were sales everywhere except the West region this month? | 0.9632 |
| Revenue minus returns this year | Revenue minus returns last year | 0.9444 | Revenue minus returns so far this year | 0.919 |
| Total revenue from every region but the West last year | Total revenue from every region but the West this year | 0.966 | Total revenue from every region but the West region last year | 0.9409 |
| Total revenue from every region but the Midwest last month | Total revenue from every region but the Midwest this month | 0.9756 | Total revenue from every region but the Midwest region last month | 0.9506 |
| Total revenue from ski jackets last month | Total revenue from ski jackets this month | 0.9619 | How much revenue did ski jackets bring in last month? | 0.9378 |
| How much did we refund on ski jackets this month? | How much did we refund on ski jackets last month? | 0.9845 | How much did we refund on ski jackets so far this month? | 0.9606 |
| What was the total value of returns in Q3 2026? | What was the total value of returns in Q2 2026? | 0.9468 | What was the total value of returns in the third quarter of 2026? | 0.9232 |
| Revenue minus returns this week | Revenue minus returns last week | 0.9433 | Revenue minus returns so far this week | 0.9219 |
| Largest sale in Q3 2026 | Largest sale in Q2 2026 | 0.9599 | Largest sale in the third quarter of 2026 | 0.9401 |
| On average, how much did customers pay for ski jackets this week? | On average, how much did customers pay for ski jackets last week? | 0.9871 | On average, how much did customers pay for ski jackets so far this week? | 0.9676 |
| What did hiking boots generate in sales last month? | What did hiking boots generate in sales this month? | 0.9777 | What did hiking boots generate in sales in the previous month? | 0.9586 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.973 | What was the total value of returns so far this week? | 0.9539 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.958 | How much revenue did we make so far this week? | 0.9391 |
