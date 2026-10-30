# st:Qwen/Qwen3-Embedding-0.6B

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.934 | 0.8463 | 0.9671 | 0.9874 | 0.9968 |
| **equivalent_surface (same wording=True)** | 310 | 0.934 | 0.8463 | 0.9671 | 0.9874 | 0.9968 |
| **filter_change** | 27 | 0.6736 | 0.5964 | 0.6765 | 0.737 | 0.7783 |
| **intent_near_miss** | 176 | 0.7798 | 0.6741 | 0.7938 | 0.8775 | 0.9367 |
| **intent_near_miss (same wording=False)** | 176 | 0.7798 | 0.6741 | 0.7938 | 0.8775 | 0.9367 |
| **param_near_miss** | 643 | 0.8636 | 0.7233 | 0.8848 | 0.9726 | 0.9921 |
| **param_near_miss (same wording=False)** | 228 | 0.7764 | 0.6595 | 0.7808 | 0.8785 | 0.9495 |
| **param_near_miss (same wording=True)** | 415 | 0.9114 | 0.8362 | 0.9273 | 0.9801 | 0.9921 |
| **paraphrase** | 256 | 0.84 | 0.7318 | 0.859 | 0.9223 | 0.9636 |
| equivalent_surface/amount/alias | 10 | 0.9813 | 0.9761 | 0.981 | 0.9858 | 0.9869 |
| equivalent_surface/channel/alias | 10 | 0.9605 | 0.9326 | 0.9573 | 0.9937 | 0.9943 |
| equivalent_surface/n/alias | 20 | 0.9821 | 0.9719 | 0.9824 | 0.9914 | 0.996 |
| equivalent_surface/period/alias | 235 | 0.9246 | 0.8248 | 0.9592 | 0.9866 | 0.9952 |
| equivalent_surface/product/alias | 15 | 0.9041 | 0.8685 | 0.9045 | 0.9392 | 0.946 |
| equivalent_surface/region/alias | 20 | 0.9826 | 0.9702 | 0.9803 | 0.9965 | 0.9968 |
| filter_change/filter_added/region_revenue | 7 | 0.6454 | 0.5831 | 0.6514 | 0.7024 | 0.7293 |
| filter_change/filter_dropped/total_revenue | 20 | 0.6835 | 0.6231 | 0.6843 | 0.7428 | 0.7783 |
| intent_near_miss/aggregation/largest_order | 7 | 0.6567 | 0.6139 | 0.6516 | 0.7025 | 0.7114 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8038 | 0.7376 | 0.8158 | 0.8498 | 0.8763 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8597 | 0.814 | 0.8593 | 0.8946 | 0.9259 |
| intent_near_miss/aggregation/product_units | 20 | 0.8474 | 0.7827 | 0.8598 | 0.911 | 0.9213 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.6632 | 0.5442 | 0.6825 | 0.7981 | 0.8022 |
| intent_near_miss/direction/product_returns | 10 | 0.8591 | 0.8139 | 0.8517 | 0.9288 | 0.9367 |
| intent_near_miss/direction/product_revenue | 10 | 0.8134 | 0.788 | 0.8065 | 0.85 | 0.855 |
| intent_near_miss/direction/total_returns | 7 | 0.7171 | 0.6605 | 0.7016 | 0.7809 | 0.855 |
| intent_near_miss/direction/total_revenue | 7 | 0.7153 | 0.6859 | 0.7131 | 0.7434 | 0.7534 |
| intent_near_miss/grouping/top_customers | 10 | 0.6918 | 0.6416 | 0.691 | 0.7501 | 0.7727 |
| intent_near_miss/grouping/top_products | 10 | 0.7296 | 0.6981 | 0.7248 | 0.7829 | 0.7892 |
| intent_near_miss/measure/net_sales | 14 | 0.7565 | 0.6979 | 0.7535 | 0.8148 | 0.8178 |
| intent_near_miss/measure/total_returns | 7 | 0.7928 | 0.7245 | 0.7831 | 0.8635 | 0.8673 |
| intent_near_miss/measure/total_revenue | 7 | 0.6778 | 0.5789 | 0.6792 | 0.7559 | 0.7974 |
| intent_near_miss/negation/region_revenue | 10 | 0.7516 | 0.6613 | 0.7269 | 0.9097 | 0.915 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8421 | 0.7943 | 0.8486 | 0.8903 | 0.9135 |
| param_near_miss/amount/neighbor | 26 | 0.9066 | 0.7761 | 0.9576 | 0.9819 | 0.9843 |
| param_near_miss/channel/neighbor | 20 | 0.8204 | 0.6972 | 0.8403 | 0.8973 | 0.9006 |
| param_near_miss/n/neighbor | 47 | 0.8919 | 0.7891 | 0.9168 | 0.9621 | 0.9823 |
| param_near_miss/period/adjacent | 245 | 0.8836 | 0.741 | 0.895 | 0.9825 | 0.9921 |
| param_near_miss/period/granularity | 180 | 0.8826 | 0.7752 | 0.9066 | 0.9447 | 0.9871 |
| param_near_miss/product/neighbor | 85 | 0.7749 | 0.6405 | 0.7813 | 0.885 | 0.9221 |
| param_near_miss/region/neighbor | 40 | 0.8039 | 0.626 | 0.8275 | 0.9569 | 0.9781 |
| paraphrase/wording/template | 256 | 0.84 | 0.7318 | 0.859 | 0.9223 | 0.9636 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.2422 | [0.1719, 0.3203] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.2422 | [0.1719, 0.3125] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.2188 | [0.1484, 0.2891] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.03 | [0.0, 0.07] | 0.78 | [0.7, 0.86] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4907 | [0.3889, 0.5833] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9531 | [0.9141, 0.9844] |
| B | 128 | 0.2891 | [0.2109, 0.3672] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0081 | [0.0036, 0.0245] | 0.0081 | 0.0081 | 0.5373 |
| raw_oracle_entry | 0.1321 | [0.1229, 0.1647] | — | — | 0.5373 |
| split_full | 0.2812 | [0.2645, 0.3176] | 0.3073 | 0.3819 | 0.5373 |
| split_template | 0.7889 | [0.7544, 0.8219] | 0.7889 | 0.9119 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Order count online in the last 3 months | Order count online in the last 6 months | 0.9871 | Order count through the website in the last 3 months | 0.9565 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.9622 | How much revenue did we make in the previous month? | 0.9455 |
| How much did rain jackets sell for in total last month? | How much did rain jackets sell for in total this month? | 0.9846 | How much did rain jackets sell for in total in the previous month? | 0.9714 |
| How many units of ski jackets did we sell last month? | How many units of ski jackets did we sell this month? | 0.9802 | How many units of ski jackets did we sell in the previous month? | 0.9679 |
| Total revenue for the West last month | Total revenue for the West this month | 0.9821 | Total revenue for the West in the previous month | 0.9705 |
| Total revenue for the Midwest last month | Total revenue for the Midwest this month | 0.987 | Total revenue for the Midwest region last month | 0.9764 |
| How much did yoga mats sell for in total last year? | How much did yoga mats sell for in total this year? | 0.9789 | How much did yoga mats sell for in total in the previous year? | 0.9683 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.9403 | How much revenue did we make in the previous year? | 0.933 |
| What was the value of yoga mats returned last year? | What was the value of yoga mats returned this year? | 0.9825 | What was the value of yoga mats returned in the previous year? | 0.9757 |
| What was the value of trail shoes returned last month? | What was the value of trail shoes returned this month? | 0.9782 | What was the value of trail shoes returned in the previous month? | 0.9716 |
| Any orders above $500 last month? | Any orders above $250 last month? | 0.9814 | Any orders above 500 dollars last month? | 0.9766 |
| Show orders over $250 last year | Show orders over $500 last year | 0.9841 | Show orders over 250 dollars last year | 0.9797 |
| Total revenue from ski jackets last month | Total revenue from ski jackets this month | 0.9782 | Total revenue from ski jackets in the previous month | 0.9744 |
| How much did we refund on ski jackets this month? | How much did we refund on ski jackets last month? | 0.9904 | How much did we refund on ski jackets so far this month? | 0.9869 |
| What did running shoes generate in sales last month? | What did running shoes generate in sales this month? | 0.9836 | What did running shoes generate in sales in the previous month? | 0.9802 |
