# voyage:voyage-3.5

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9022 | 0.7729 | 0.9371 | 0.9813 | 0.994 |
| **equivalent_surface (same wording=True)** | 310 | 0.9022 | 0.7729 | 0.9371 | 0.9813 | 0.994 |
| **filter_change** | 27 | 0.5931 | 0.4798 | 0.5797 | 0.7179 | 0.7863 |
| **intent_near_miss** | 176 | 0.7058 | 0.5462 | 0.7234 | 0.8432 | 0.9133 |
| **intent_near_miss (same wording=False)** | 176 | 0.7058 | 0.5462 | 0.7234 | 0.8432 | 0.9133 |
| **param_near_miss** | 643 | 0.8158 | 0.6536 | 0.8291 | 0.9592 | 0.9917 |
| **param_near_miss (same wording=False)** | 228 | 0.725 | 0.5773 | 0.7333 | 0.8627 | 0.9235 |
| **param_near_miss (same wording=True)** | 415 | 0.8657 | 0.755 | 0.8726 | 0.9761 | 0.9917 |
| **paraphrase** | 256 | 0.8125 | 0.6492 | 0.8413 | 0.9185 | 0.9622 |
| equivalent_surface/amount/alias | 10 | 0.9626 | 0.9443 | 0.9788 | 0.9839 | 0.9847 |
| equivalent_surface/channel/alias | 10 | 0.9255 | 0.8421 | 0.9392 | 0.9919 | 0.9927 |
| equivalent_surface/n/alias | 20 | 0.9829 | 0.9669 | 0.9883 | 0.9934 | 0.994 |
| equivalent_surface/period/alias | 235 | 0.8864 | 0.7614 | 0.9239 | 0.9708 | 0.9884 |
| equivalent_surface/product/alias | 15 | 0.9066 | 0.8494 | 0.9149 | 0.9622 | 0.9688 |
| equivalent_surface/region/alias | 20 | 0.9622 | 0.9455 | 0.9581 | 0.9848 | 0.9865 |
| filter_change/filter_added/region_revenue | 7 | 0.5519 | 0.4593 | 0.5363 | 0.6575 | 0.7065 |
| filter_change/filter_dropped/total_revenue | 20 | 0.6075 | 0.4974 | 0.5884 | 0.7388 | 0.7863 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5254 | 0.4469 | 0.5141 | 0.6272 | 0.6331 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7498 | 0.6506 | 0.7449 | 0.8376 | 0.8482 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8142 | 0.7574 | 0.8157 | 0.8578 | 0.9133 |
| intent_near_miss/aggregation/product_units | 20 | 0.7833 | 0.7274 | 0.7622 | 0.8743 | 0.8961 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5798 | 0.4999 | 0.5668 | 0.6832 | 0.7509 |
| intent_near_miss/direction/product_returns | 10 | 0.772 | 0.7181 | 0.7691 | 0.8214 | 0.8588 |
| intent_near_miss/direction/product_revenue | 10 | 0.7635 | 0.7262 | 0.7647 | 0.8144 | 0.8146 |
| intent_near_miss/direction/total_returns | 7 | 0.5998 | 0.5048 | 0.5911 | 0.7138 | 0.7687 |
| intent_near_miss/direction/total_revenue | 7 | 0.5971 | 0.5606 | 0.5753 | 0.6455 | 0.6963 |
| intent_near_miss/grouping/top_customers | 10 | 0.664 | 0.6114 | 0.6833 | 0.7026 | 0.7622 |
| intent_near_miss/grouping/top_products | 10 | 0.6642 | 0.5926 | 0.673 | 0.7243 | 0.7797 |
| intent_near_miss/measure/net_sales | 14 | 0.6214 | 0.5235 | 0.6319 | 0.7012 | 0.8449 |
| intent_near_miss/measure/total_returns | 7 | 0.6446 | 0.6073 | 0.6495 | 0.6794 | 0.6804 |
| intent_near_miss/measure/total_revenue | 7 | 0.5596 | 0.4601 | 0.591 | 0.6375 | 0.6385 |
| intent_near_miss/negation/region_revenue | 10 | 0.7188 | 0.6472 | 0.6818 | 0.8809 | 0.8831 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8201 | 0.7931 | 0.8239 | 0.8575 | 0.8878 |
| param_near_miss/amount/neighbor | 26 | 0.822 | 0.739 | 0.8343 | 0.8833 | 0.9191 |
| param_near_miss/channel/neighbor | 20 | 0.7863 | 0.7056 | 0.7876 | 0.8645 | 0.9006 |
| param_near_miss/n/neighbor | 47 | 0.8278 | 0.6556 | 0.8726 | 0.9148 | 0.9426 |
| param_near_miss/period/adjacent | 245 | 0.8548 | 0.7073 | 0.874 | 0.9792 | 0.9917 |
| param_near_miss/period/granularity | 180 | 0.8232 | 0.719 | 0.8382 | 0.9222 | 0.9693 |
| param_near_miss/product/neighbor | 85 | 0.7331 | 0.6034 | 0.7312 | 0.8523 | 0.9179 |
| param_near_miss/region/neighbor | 40 | 0.7157 | 0.5774 | 0.7429 | 0.8632 | 0.912 |
| paraphrase/wording/template | 256 | 0.8125 | 0.6492 | 0.8413 | 0.9185 | 0.9622 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4844 | [0.3984, 0.5703] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.4844 | [0.3984, 0.5703] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.4844 | [0.3984, 0.5703] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.62 | [0.53, 0.7102] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.3889 | [0.2963, 0.4722] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9375 | [0.8906, 0.9766] |
| B | 128 | 0.6328 | [0.5469, 0.7188] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0045 | [0.0009, 0.0164] | 0.0045 | 0.0045 | 0.5373 |
| raw_oracle_entry | 0.1141 | [0.1066, 0.1581] | — | — | 0.5373 |
| split_full | 0.2929 | [0.2797, 0.3573] | 0.3558 | 0.3854 | 0.5373 |
| split_template | 0.7907 | [0.758, 0.8213] | 0.7907 | 0.92 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9445 | What was the total value of returns year to date? | 0.8535 |
| What was our total revenue this year? | What was our total revenue last year? | 0.9237 | What was our total revenue so far this year? | 0.843 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9606 | What was the total value of returns so far this week? | 0.8935 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9584 | What was the total value of returns so far this month? | 0.9095 |
| What did hiking boots sell for on average last month? | What did hiking boots sell for on average this month? | 0.9787 | What did hiking boots sell for on average in the previous month? | 0.9372 |
| Revenue minus returns in the last 3 months | Revenue minus returns in the last 6 months | 0.9212 | Revenue minus returns over the past three months | 0.8846 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9767 | What were sales net of returns in the previous month? | 0.9404 |
| On average, how much did customers pay for trail shoes this year? | On average, how much did customers pay for trail shoes last year? | 0.9782 | On average, how much did customers pay for trail shoes so far this year? | 0.9461 |
| What did trail shoes generate in sales this week? | What did trail shoes generate in sales last week? | 0.9879 | What did trail shoes generate in sales so far this week? | 0.9566 |
| How much revenue came from the Northeast last month? | How much revenue came from the Northeast this month? | 0.9793 | How much revenue came from the Northeast region last month? | 0.9484 |
| Revenue minus returns this year | Revenue minus returns last year | 0.8945 | Revenue minus returns year to date | 0.864 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9214 | Revenue minus returns so far this month | 0.8914 |
| How many units of water bottles did we sell this year? | How many units of water bottles did we sell last year? | 0.9811 | How many units of water bottles did we sell so far this year? | 0.9521 |
| What did hiking boots generate in sales last month? | What did hiking boots generate in sales this month? | 0.9837 | What did hiking boots generate in sales in the previous month? | 0.9548 |
| What was the value of yoga mats returned this year? | What was the value of yoga mats returned last year? | 0.9672 | What was the value of yoga mats returned so far this year? | 0.9395 |
