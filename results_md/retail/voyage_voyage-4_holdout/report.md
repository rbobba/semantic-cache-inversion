# voyage:voyage-4 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9147 | 0.7738 | 0.9632 | 0.9894 | 0.9958 |
| **equivalent_surface (same wording=True)** | 310 | 0.9147 | 0.7738 | 0.9632 | 0.9894 | 0.9958 |
| **filter_change** | 27 | 0.5493 | 0.436 | 0.5743 | 0.6399 | 0.6998 |
| **intent_near_miss** | 176 | 0.7249 | 0.5538 | 0.7338 | 0.8776 | 0.9371 |
| **intent_near_miss (same wording=False)** | 176 | 0.7249 | 0.5538 | 0.7338 | 0.8776 | 0.9371 |
| **param_near_miss** | 643 | 0.8205 | 0.6456 | 0.8443 | 0.9494 | 0.9854 |
| **param_near_miss (same wording=False)** | 228 | 0.7313 | 0.5374 | 0.7552 | 0.8742 | 0.9454 |
| **param_near_miss (same wording=True)** | 415 | 0.8695 | 0.7506 | 0.8951 | 0.9624 | 0.9854 |
| **paraphrase** | 256 | 0.8363 | 0.6831 | 0.8616 | 0.9469 | 0.9754 |
| equivalent_surface/amount/alias | 10 | 0.9904 | 0.9861 | 0.991 | 0.9927 | 0.9955 |
| equivalent_surface/channel/alias | 10 | 0.9448 | 0.8827 | 0.956 | 0.9903 | 0.9934 |
| equivalent_surface/n/alias | 20 | 0.9905 | 0.9856 | 0.9916 | 0.9952 | 0.9958 |
| equivalent_surface/period/alias | 235 | 0.8974 | 0.7639 | 0.9484 | 0.9833 | 0.9896 |
| equivalent_surface/product/alias | 15 | 0.9249 | 0.8931 | 0.9288 | 0.9665 | 0.9772 |
| equivalent_surface/region/alias | 20 | 0.9817 | 0.968 | 0.9798 | 0.995 | 0.9957 |
| filter_change/filter_added/region_revenue | 7 | 0.5072 | 0.3975 | 0.5421 | 0.6111 | 0.6552 |
| filter_change/filter_dropped/total_revenue | 20 | 0.5641 | 0.4912 | 0.5758 | 0.6345 | 0.6998 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5682 | 0.5035 | 0.5858 | 0.6118 | 0.6501 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7685 | 0.6926 | 0.7799 | 0.8243 | 0.8707 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8515 | 0.7766 | 0.8526 | 0.9015 | 0.9317 |
| intent_near_miss/aggregation/product_units | 20 | 0.7966 | 0.7234 | 0.812 | 0.8454 | 0.8898 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5989 | 0.491 | 0.5937 | 0.7044 | 0.716 |
| intent_near_miss/direction/product_returns | 10 | 0.809 | 0.7516 | 0.8044 | 0.867 | 0.9041 |
| intent_near_miss/direction/product_revenue | 10 | 0.7674 | 0.7268 | 0.7585 | 0.8091 | 0.8326 |
| intent_near_miss/direction/total_returns | 7 | 0.6232 | 0.5367 | 0.6154 | 0.7103 | 0.7875 |
| intent_near_miss/direction/total_revenue | 7 | 0.5633 | 0.4965 | 0.5682 | 0.6377 | 0.6702 |
| intent_near_miss/grouping/top_customers | 10 | 0.6821 | 0.5952 | 0.7107 | 0.7251 | 0.7448 |
| intent_near_miss/grouping/top_products | 10 | 0.7073 | 0.6683 | 0.7076 | 0.7584 | 0.7619 |
| intent_near_miss/measure/net_sales | 14 | 0.585 | 0.4774 | 0.6024 | 0.6776 | 0.7842 |
| intent_near_miss/measure/total_returns | 7 | 0.67 | 0.6099 | 0.6478 | 0.7513 | 0.7775 |
| intent_near_miss/measure/total_revenue | 7 | 0.5853 | 0.5057 | 0.5783 | 0.6733 | 0.6863 |
| intent_near_miss/negation/region_revenue | 10 | 0.7438 | 0.6524 | 0.6957 | 0.9316 | 0.9371 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8706 | 0.8469 | 0.8843 | 0.8962 | 0.9099 |
| param_near_miss/amount/neighbor | 26 | 0.8442 | 0.7516 | 0.8654 | 0.915 | 0.9242 |
| param_near_miss/channel/neighbor | 20 | 0.8114 | 0.7114 | 0.8272 | 0.8729 | 0.892 |
| param_near_miss/n/neighbor | 47 | 0.8595 | 0.7586 | 0.8831 | 0.9234 | 0.9365 |
| param_near_miss/period/adjacent | 245 | 0.8531 | 0.6933 | 0.8819 | 0.9749 | 0.9854 |
| param_near_miss/period/granularity | 180 | 0.8461 | 0.7245 | 0.887 | 0.9279 | 0.9539 |
| param_near_miss/product/neighbor | 85 | 0.7015 | 0.5361 | 0.7293 | 0.823 | 0.9399 |
| param_near_miss/region/neighbor | 40 | 0.7016 | 0.5185 | 0.7065 | 0.9027 | 0.9175 |
| paraphrase/wording/template | 256 | 0.8363 | 0.6831 | 0.8616 | 0.9469 | 0.9754 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.0391 | [0.0078, 0.0703] | 0.9766 | [0.9531, 1.0] |
| param_near_miss | 128 | 0.0391 | [0.0078, 0.0781] | 0.9766 | [0.9453, 1.0] |
| period_near_miss | 128 | 0.0391 | [0.0078, 0.0781] | 0.9766 | [0.9531, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.61 | [0.52, 0.7] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4074 | [0.3056, 0.5] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8359 | [0.7656, 0.8906] |
| B | 128 | 0.0625 | [0.0234, 0.1018] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0564 | [0.0361, 0.0833] | 0.0564 | 0.0626 | 0.5344 |
| raw_oracle_entry | 0.3382 | [0.3096, 0.3899] | — | — | 0.5344 |
| split_full | 0.2463 | [0.2034, 0.3369] | 0.2463 | 0.3257 | 0.5344 |
| split_template | 0.8267 | [0.784, 0.8683] | 0.8267 | 0.8267 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest sale last month | Largest sale this month | 0.9381 | Largest sale in the previous month | 0.8901 |
| How much did we refund on ski jackets last year? | How much did we refund on ski jackets this year? | 0.9741 | How much did we refund on ski jackets in the previous year? | 0.9533 |
| How much did we refund on running shoes last month? | How much did we refund on running shoes this month? | 0.9846 | How much did we refund on running sneakers last month? | 0.9772 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9809 | What were sales everywhere except the West so far this month? | 0.9757 |
| Total revenue from ski jackets last month | Total revenue from ski jackets this month | 0.9699 | Total revenue from ski jackets in the previous month | 0.9676 |
| How many units of ski jackets did we sell last month? | How many units of ski jackets did we sell this month? | 0.9626 | How many units of ski jackets did we sell in the previous month? | 0.9636 |
| What did trail shoes generate in sales this week? | What did trail shoes generate in sales last week? | 0.983 | What did trail shoes generate in sales so far this week? | 0.9846 |
| What did hiking boots sell for on average last month? | What did hiking boots sell for on average this month? | 0.9801 | What did hiking boots sell for on average in the previous month? | 0.9818 |
| What was the value of trail shoes returned last month? | What was the value of trail shoes returned this month? | 0.9832 | What was the value of trail shoes returned in the previous month? | 0.9852 |
| What was the value of yoga mats returned this week? | What was the value of yoga mats returned last week? | 0.9835 | What was the value of yoga mats returned so far this week? | 0.9855 |
| How much revenue came from the Northeast last month? | How much revenue came from the Northeast this month? | 0.981 | How much revenue came from the Northeast in the previous month? | 0.983 |
| Total revenue for the West last month | Total revenue for the West this month | 0.9685 | Total revenue for the West in the previous month | 0.9708 |
| On average, how much did customers pay for yoga mats last month? | On average, how much did customers pay for yoga mats this month? | 0.9815 | On average, how much did customers pay for yoga mats in the previous month? | 0.9843 |
| How much did we refund on ski jackets this month? | How much did we refund on ski jackets last month? | 0.9854 | How much did we refund on ski jackets so far this month? | 0.9884 |
| On average, how much did customers pay for trail shoes this year? | On average, how much did customers pay for trail shoes last year? | 0.9728 | On average, how much did customers pay for trail shoes so far this year? | 0.9759 |
