# vertex:text-embedding-004

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9429 | 0.8549 | 0.9723 | 0.9923 | 0.9982 |
| **equivalent_surface (same wording=True)** | 310 | 0.9429 | 0.8549 | 0.9723 | 0.9923 | 0.9982 |
| **filter_change** | 27 | 0.6539 | 0.5789 | 0.6599 | 0.7231 | 0.8013 |
| **intent_near_miss** | 176 | 0.7913 | 0.6472 | 0.7889 | 0.9133 | 0.9746 |
| **intent_near_miss (same wording=False)** | 176 | 0.7913 | 0.6472 | 0.7889 | 0.9133 | 0.9746 |
| **param_near_miss** | 643 | 0.8841 | 0.75 | 0.9103 | 0.988 | 0.9977 |
| **param_near_miss (same wording=False)** | 228 | 0.8145 | 0.6981 | 0.8165 | 0.9357 | 0.9745 |
| **param_near_miss (same wording=True)** | 415 | 0.9223 | 0.8306 | 0.9432 | 0.9927 | 0.9977 |
| **paraphrase** | 256 | 0.8741 | 0.7679 | 0.878 | 0.965 | 0.9831 |
| equivalent_surface/amount/alias | 10 | 0.9875 | 0.9862 | 0.9875 | 0.9892 | 0.991 |
| equivalent_surface/channel/alias | 10 | 0.9465 | 0.9103 | 0.9377 | 0.994 | 0.9945 |
| equivalent_surface/n/alias | 20 | 0.9949 | 0.992 | 0.9952 | 0.997 | 0.9982 |
| equivalent_surface/period/alias | 235 | 0.9333 | 0.8481 | 0.9643 | 0.9898 | 0.9944 |
| equivalent_surface/product/alias | 15 | 0.9449 | 0.8875 | 0.9581 | 0.9835 | 0.9883 |
| equivalent_surface/region/alias | 20 | 0.9781 | 0.9658 | 0.9803 | 0.9862 | 0.9877 |
| filter_change/filter_added/region_revenue | 7 | 0.6522 | 0.5789 | 0.6726 | 0.728 | 0.8013 |
| filter_change/filter_dropped/total_revenue | 20 | 0.6545 | 0.5966 | 0.655 | 0.7191 | 0.7369 |
| intent_near_miss/aggregation/largest_order | 7 | 0.6705 | 0.6344 | 0.6597 | 0.7226 | 0.7621 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8501 | 0.748 | 0.8809 | 0.9191 | 0.9358 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8851 | 0.8385 | 0.8783 | 0.9382 | 0.9746 |
| intent_near_miss/aggregation/product_units | 20 | 0.9091 | 0.872 | 0.9073 | 0.9611 | 0.964 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.7229 | 0.6518 | 0.7083 | 0.8043 | 0.8228 |
| intent_near_miss/direction/product_returns | 10 | 0.8346 | 0.7737 | 0.8502 | 0.8676 | 0.8701 |
| intent_near_miss/direction/product_revenue | 10 | 0.7842 | 0.7678 | 0.7818 | 0.8137 | 0.8156 |
| intent_near_miss/direction/total_returns | 7 | 0.65 | 0.6204 | 0.6346 | 0.6956 | 0.7688 |
| intent_near_miss/direction/total_revenue | 7 | 0.6795 | 0.652 | 0.6674 | 0.7155 | 0.7358 |
| intent_near_miss/grouping/top_customers | 10 | 0.693 | 0.6458 | 0.6935 | 0.7383 | 0.7747 |
| intent_near_miss/grouping/top_products | 10 | 0.7295 | 0.7107 | 0.7256 | 0.7729 | 0.8053 |
| intent_near_miss/measure/net_sales | 14 | 0.7416 | 0.6386 | 0.7581 | 0.8071 | 0.9331 |
| intent_near_miss/measure/total_returns | 7 | 0.7302 | 0.6733 | 0.7238 | 0.7805 | 0.7949 |
| intent_near_miss/measure/total_revenue | 7 | 0.7107 | 0.6154 | 0.7062 | 0.8009 | 0.819 |
| intent_near_miss/negation/region_revenue | 10 | 0.7944 | 0.7406 | 0.7542 | 0.9283 | 0.932 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8504 | 0.8156 | 0.8509 | 0.8859 | 0.9004 |
| param_near_miss/amount/neighbor | 26 | 0.8934 | 0.806 | 0.9194 | 0.9463 | 0.9718 |
| param_near_miss/channel/neighbor | 20 | 0.8493 | 0.8027 | 0.8476 | 0.895 | 0.9188 |
| param_near_miss/n/neighbor | 47 | 0.9021 | 0.7947 | 0.9317 | 0.9593 | 0.9786 |
| param_near_miss/period/adjacent | 245 | 0.9145 | 0.7816 | 0.9423 | 0.9948 | 0.9977 |
| param_near_miss/period/granularity | 180 | 0.903 | 0.7915 | 0.9329 | 0.9652 | 0.9799 |
| param_near_miss/product/neighbor | 85 | 0.7887 | 0.6703 | 0.7948 | 0.8986 | 0.938 |
| param_near_miss/region/neighbor | 40 | 0.8056 | 0.6588 | 0.8004 | 0.9472 | 0.9637 |
| paraphrase/wording/template | 256 | 0.8741 | 0.7679 | 0.878 | 0.965 | 0.9831 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.6094 | [0.5234, 0.6953] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.6094 | [0.5234, 0.6875] | 0.9844 | [0.9609, 1.0] |
| period_near_miss | 128 | 0.6094 | [0.5234, 0.6953] | 0.9844 | [0.9609, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.6 | [0.51, 0.6902] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.3981 | [0.3056, 0.4907] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9219 | [0.8748, 0.9688] |
| B | 128 | 0.7031 | [0.625, 0.7812] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0009 | [0.0, 0.0053] | 0.0009 | 0.0009 | 0.5373 |
| raw_oracle_entry | 0.0961 | [0.0901, 0.1386] | — | — | 0.5373 |
| split_full | 0.3288 | [0.312, 0.3751] | 0.3648 | 0.4259 | 0.5373 |
| split_template | 0.7942 | [0.7654, 0.8212] | 0.7942 | 0.9596 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our total revenue this year? | What was our total revenue last year? | 0.9852 | What was our total revenue so far this year? | 0.9414 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9812 | What was the total value of returns in the previous year? | 0.9471 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9812 | What was the total value of returns so far this year? | 0.9476 |
| How much did we refund on ski jackets last year? | How much did we refund on ski jackets this year? | 0.9897 | How much did we refund on ski jackets in the previous year? | 0.9611 |
| Total revenue from ski jackets last month | Total revenue from ski jackets this month | 0.993 | How much revenue did ski jackets bring in last month? | 0.9644 |
| What was the value of yoga mats returned last year? | What was the value of yoga mats returned this year? | 0.9913 | What was the value of yoga mats returned in the previous year? | 0.9689 |
| How much did rain jackets sell for in total last month? | How much did rain jackets sell for in total this month? | 0.996 | How much did raincoats sell for in total last month? | 0.9745 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9946 | What was the total value of returns in the previous month? | 0.9731 |
| Largest sale last month | Largest sale this month | 0.9565 | Largest sale in the previous month | 0.935 |
| Show the biggest single order last year | Show the biggest single order this year | 0.9787 | Show the biggest single order in the previous year | 0.9589 |
| What did hiking boots generate in sales last month? | What did hiking boots generate in sales this month? | 0.9965 | What did hiking boots generate in sales in the previous month? | 0.9772 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9848 | What were sales net of returns in the previous year? | 0.9655 |
| Order count online this month | Order count online last month | 0.9819 | Order count online so far this month | 0.9632 |
| On average, how much did customers pay for backpacks last month? | On average, how much did customers pay for backpacks this month? | 0.9946 | On average, how much did customers pay for backpacks in the previous month? | 0.9759 |
| What was the value of trail shoes returned last month? | What was the value of trail shoes returned this month? | 0.9946 | What was the value of trail shoes returned in the previous month? | 0.976 |
