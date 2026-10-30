# vertex:gemini-embedding-001 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9454 | 0.8658 | 0.9699 | 0.9908 | 0.9975 |
| **equivalent_surface (same wording=True)** | 310 | 0.9454 | 0.8658 | 0.9699 | 0.9908 | 0.9975 |
| **filter_change** | 27 | 0.7752 | 0.7027 | 0.7731 | 0.8353 | 0.8637 |
| **intent_near_miss** | 176 | 0.8295 | 0.7508 | 0.8299 | 0.9062 | 0.9477 |
| **intent_near_miss (same wording=False)** | 176 | 0.8295 | 0.7508 | 0.8299 | 0.9062 | 0.9477 |
| **param_near_miss** | 643 | 0.9078 | 0.8159 | 0.9215 | 0.9813 | 0.9943 |
| **param_near_miss (same wording=False)** | 228 | 0.8594 | 0.7781 | 0.8639 | 0.9377 | 0.9675 |
| **param_near_miss (same wording=True)** | 415 | 0.9344 | 0.8619 | 0.9477 | 0.9875 | 0.9943 |
| **paraphrase** | 256 | 0.8994 | 0.819 | 0.9089 | 0.9602 | 0.9827 |
| equivalent_surface/amount/alias | 10 | 0.9861 | 0.984 | 0.9871 | 0.9887 | 0.9888 |
| equivalent_surface/channel/alias | 10 | 0.9378 | 0.8817 | 0.9469 | 0.9834 | 0.9925 |
| equivalent_surface/n/alias | 20 | 0.992 | 0.9851 | 0.9941 | 0.9964 | 0.9975 |
| equivalent_surface/period/alias | 235 | 0.9366 | 0.8576 | 0.9595 | 0.9879 | 0.9956 |
| equivalent_surface/product/alias | 15 | 0.9615 | 0.9492 | 0.9663 | 0.9771 | 0.9813 |
| equivalent_surface/region/alias | 20 | 0.9736 | 0.9465 | 0.9786 | 0.9864 | 0.9932 |
| filter_change/filter_added/region_revenue | 7 | 0.7418 | 0.6797 | 0.7264 | 0.8187 | 0.8637 |
| filter_change/filter_dropped/total_revenue | 20 | 0.7869 | 0.7344 | 0.8042 | 0.8329 | 0.8487 |
| intent_near_miss/aggregation/largest_order | 7 | 0.7672 | 0.7371 | 0.7721 | 0.7951 | 0.8093 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8427 | 0.7937 | 0.8546 | 0.8846 | 0.8969 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8927 | 0.8387 | 0.8943 | 0.9344 | 0.9473 |
| intent_near_miss/aggregation/product_units | 20 | 0.8903 | 0.8533 | 0.8955 | 0.9325 | 0.936 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.7867 | 0.7589 | 0.7825 | 0.8248 | 0.835 |
| intent_near_miss/direction/product_returns | 10 | 0.8589 | 0.8407 | 0.8562 | 0.8792 | 0.8992 |
| intent_near_miss/direction/product_revenue | 10 | 0.8596 | 0.8479 | 0.8593 | 0.8752 | 0.8798 |
| intent_near_miss/direction/total_returns | 7 | 0.7148 | 0.6638 | 0.7024 | 0.7724 | 0.8192 |
| intent_near_miss/direction/total_revenue | 7 | 0.7947 | 0.762 | 0.8015 | 0.8208 | 0.8227 |
| intent_near_miss/grouping/top_customers | 10 | 0.8003 | 0.7621 | 0.8038 | 0.8195 | 0.8399 |
| intent_near_miss/grouping/top_products | 10 | 0.7875 | 0.7488 | 0.779 | 0.8303 | 0.8483 |
| intent_near_miss/measure/net_sales | 14 | 0.8099 | 0.7729 | 0.8035 | 0.844 | 0.9026 |
| intent_near_miss/measure/total_returns | 7 | 0.7475 | 0.7135 | 0.7415 | 0.7846 | 0.7956 |
| intent_near_miss/measure/total_revenue | 7 | 0.7836 | 0.7336 | 0.7928 | 0.8193 | 0.8261 |
| intent_near_miss/negation/region_revenue | 10 | 0.8285 | 0.7623 | 0.816 | 0.9215 | 0.9477 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8637 | 0.8466 | 0.8625 | 0.8855 | 0.8904 |
| param_near_miss/amount/neighbor | 26 | 0.9144 | 0.8448 | 0.9357 | 0.9542 | 0.9582 |
| param_near_miss/channel/neighbor | 20 | 0.8642 | 0.8122 | 0.8577 | 0.9203 | 0.9238 |
| param_near_miss/n/neighbor | 47 | 0.9333 | 0.8624 | 0.9476 | 0.9805 | 0.9854 |
| param_near_miss/period/adjacent | 245 | 0.9232 | 0.8294 | 0.9402 | 0.9903 | 0.9943 |
| param_near_miss/period/granularity | 180 | 0.9145 | 0.8382 | 0.9339 | 0.9641 | 0.9911 |
| param_near_miss/product/neighbor | 85 | 0.8601 | 0.7806 | 0.873 | 0.9399 | 0.9536 |
| param_near_miss/region/neighbor | 40 | 0.8718 | 0.7868 | 0.8846 | 0.9592 | 0.9706 |
| paraphrase/wording/template | 256 | 0.8994 | 0.819 | 0.9089 | 0.9602 | 0.9827 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4531 | [0.3672, 0.5391] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.4531 | [0.3672, 0.5391] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.4531 | [0.3672, 0.5391] | 0.9844 | [0.9609, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.04] | 0.7 | [0.61, 0.79] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.2778 | [0.1852, 0.3611] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9297 | [0.8828, 0.9688] |
| B | 128 | 0.5859 | [0.5, 0.6719] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0271 | [0.0147, 0.0458] | 0.0271 | 0.0271 | 0.5344 |
| raw_oracle_entry | 0.2944 | [0.2752, 0.3552] | — | — | 0.5344 |
| split_full | 0.0125 | [0.0041, 0.1752] | 0.0125 | 0.1461 | 0.5344 |
| split_template | 0.0856 | [0.0576, 0.1144] | 0.0856 | 0.0856 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much revenue did we make this month? | How much revenue did we make last month? | 0.9882 | How much revenue did we make so far this month? | 0.9602 |
| Revenue minus returns this week | Revenue minus returns last week | 0.9596 | Revenue minus returns so far this week | 0.9324 |
| Order count online this year | Order count online last year | 0.9218 | Order count online so far this year | 0.8976 |
| What was our total revenue this year? | What was our total revenue last year? | 0.975 | What was our total revenue so far this year? | 0.951 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.9822 | How much revenue did we make in the previous year? | 0.9591 |
| What was the value of yoga mats returned this week? | What was the value of yoga mats returned last week? | 0.9799 | What was the value of yoga mats returned so far this week? | 0.9588 |
| How many units of hiking boots did we sell last year? | How many units of hiking boots did we sell this year? | 0.9903 | How many units of hiking boots did we sell in the previous year? | 0.9693 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9807 | What were sales net of returns in the previous year? | 0.9602 |
| Total revenue from every region but the West last year | Total revenue from every region but the West this year | 0.9794 | Total revenue from every region but the West in the previous year | 0.9598 |
| Order count in stores this week | Order count in stores last week | 0.9759 | Order count in stores so far this week | 0.9573 |
| Total revenue from every region but the Southeast last month | Total revenue from every region but the Southeast this month | 0.9855 | Total revenue from every region but the Southeast region last month | 0.9693 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9885 | What were sales everywhere except the West so far this month? | 0.9728 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9888 | What was the total value of returns in the previous month? | 0.9731 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9859 | Revenue minus returns so far this month | 0.9705 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9872 | What was the total value of returns so far this week? | 0.9724 |
