# st:mixedbread-ai/mxbai-embed-large-v1 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9314 | 0.8122 | 0.9713 | 0.9889 | 0.9966 |
| **equivalent_surface (same wording=True)** | 310 | 0.9314 | 0.8122 | 0.9713 | 0.9889 | 0.9966 |
| **filter_change** | 27 | 0.7119 | 0.6432 | 0.7182 | 0.7667 | 0.7868 |
| **intent_near_miss** | 176 | 0.7969 | 0.6768 | 0.8051 | 0.8998 | 0.9443 |
| **intent_near_miss (same wording=False)** | 176 | 0.7969 | 0.6768 | 0.8051 | 0.8998 | 0.9443 |
| **param_near_miss** | 643 | 0.8664 | 0.7345 | 0.885 | 0.9852 | 0.9982 |
| **param_near_miss (same wording=False)** | 228 | 0.8002 | 0.673 | 0.8166 | 0.9074 | 0.9542 |
| **param_near_miss (same wording=True)** | 415 | 0.9027 | 0.8007 | 0.9114 | 0.9896 | 0.9982 |
| **paraphrase** | 256 | 0.8694 | 0.7516 | 0.8864 | 0.94 | 0.9832 |
| equivalent_surface/amount/alias | 10 | 0.9846 | 0.98 | 0.9851 | 0.9874 | 0.9902 |
| equivalent_surface/channel/alias | 10 | 0.9703 | 0.9557 | 0.9678 | 0.9916 | 0.9919 |
| equivalent_surface/n/alias | 20 | 0.993 | 0.9875 | 0.9935 | 0.996 | 0.9966 |
| equivalent_surface/period/alias | 235 | 0.9193 | 0.7911 | 0.9675 | 0.9852 | 0.9916 |
| equivalent_surface/product/alias | 15 | 0.9261 | 0.9013 | 0.9239 | 0.9506 | 0.9665 |
| equivalent_surface/region/alias | 20 | 0.9694 | 0.9473 | 0.9734 | 0.9809 | 0.9835 |
| filter_change/filter_added/region_revenue | 7 | 0.7 | 0.6217 | 0.7289 | 0.7707 | 0.7868 |
| filter_change/filter_dropped/total_revenue | 20 | 0.7161 | 0.6769 | 0.7167 | 0.7662 | 0.7689 |
| intent_near_miss/aggregation/largest_order | 7 | 0.6633 | 0.5789 | 0.6773 | 0.7332 | 0.7359 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8498 | 0.7811 | 0.8535 | 0.8976 | 0.918 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8719 | 0.8443 | 0.8697 | 0.8979 | 0.9329 |
| intent_near_miss/aggregation/product_units | 20 | 0.8888 | 0.8334 | 0.9057 | 0.9197 | 0.9443 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.7303 | 0.6618 | 0.7244 | 0.8008 | 0.8278 |
| intent_near_miss/direction/product_returns | 10 | 0.8606 | 0.8382 | 0.8557 | 0.8817 | 0.9336 |
| intent_near_miss/direction/product_revenue | 10 | 0.7772 | 0.7542 | 0.7748 | 0.797 | 0.8108 |
| intent_near_miss/direction/total_returns | 7 | 0.7419 | 0.6511 | 0.763 | 0.8112 | 0.8382 |
| intent_near_miss/direction/total_revenue | 7 | 0.7122 | 0.6537 | 0.6905 | 0.7814 | 0.8245 |
| intent_near_miss/grouping/top_customers | 10 | 0.7949 | 0.7726 | 0.7947 | 0.8196 | 0.8207 |
| intent_near_miss/grouping/top_products | 10 | 0.7411 | 0.7082 | 0.7407 | 0.7753 | 0.8122 |
| intent_near_miss/measure/net_sales | 14 | 0.7412 | 0.6505 | 0.7511 | 0.8052 | 0.9135 |
| intent_near_miss/measure/total_returns | 7 | 0.7518 | 0.7125 | 0.7488 | 0.7875 | 0.7906 |
| intent_near_miss/measure/total_revenue | 7 | 0.6994 | 0.6259 | 0.6812 | 0.7955 | 0.8032 |
| intent_near_miss/negation/region_revenue | 10 | 0.7379 | 0.6594 | 0.704 | 0.8885 | 0.8913 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8459 | 0.8263 | 0.847 | 0.8601 | 0.8678 |
| param_near_miss/amount/neighbor | 26 | 0.8776 | 0.8076 | 0.9067 | 0.9327 | 0.9523 |
| param_near_miss/channel/neighbor | 20 | 0.8767 | 0.8272 | 0.8737 | 0.9149 | 0.9273 |
| param_near_miss/n/neighbor | 47 | 0.864 | 0.774 | 0.8685 | 0.9389 | 0.9611 |
| param_near_miss/period/adjacent | 245 | 0.9015 | 0.7544 | 0.9167 | 0.9925 | 0.9982 |
| param_near_miss/period/granularity | 180 | 0.8718 | 0.7774 | 0.8943 | 0.9326 | 0.9578 |
| param_near_miss/product/neighbor | 85 | 0.779 | 0.6117 | 0.7984 | 0.8926 | 0.9293 |
| param_near_miss/region/neighbor | 40 | 0.803 | 0.6585 | 0.8 | 0.9711 | 0.9803 |
| paraphrase/wording/template | 256 | 0.8694 | 0.7516 | 0.8864 | 0.94 | 0.9832 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5234 | [0.4453, 0.6094] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.5234 | [0.4297, 0.6096] | 0.9766 | [0.9529, 1.0] |
| period_near_miss | 128 | 0.5234 | [0.4373, 0.6094] | 0.9609 | [0.9219, 0.9922] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.68 | [0.59, 0.77] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4815 | [0.3889, 0.5741] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8594 | [0.7891, 0.9141] |
| B | 128 | 0.6406 | [0.5625, 0.7266] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0063 | [0.0, 0.04] | 0.0063 | 0.0063 | 0.5344 |
| raw_oracle_entry | 0.2777 | [0.2567, 0.3327] | — | — | 0.5344 |
| split_full | 0.071 | [0.0496, 0.1221] | 0.071 | 0.071 | 0.5344 |
| split_template | 0.2797 | [0.2233, 0.3376] | 0.2797 | 0.2797 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9909 | What was the total value of returns so far this week? | 0.9581 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9927 | What were sales everywhere except the West so far this month? | 0.9622 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9852 | What was the total value of returns in the previous year? | 0.9559 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9849 | What was the total value of returns so far this month? | 0.9557 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9852 | What was the total value of returns year to date? | 0.9608 |
| What did trail shoes generate in sales this week? | What did trail shoes generate in sales last week? | 0.9897 | What did trail shoes generate in sales so far this week? | 0.9664 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9787 | What were sales net of returns in the previous year? | 0.9558 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9898 | Revenue minus returns so far this month | 0.9701 |
| Revenue minus returns this year | Revenue minus returns last year | 0.9867 | Revenue minus returns so far this year | 0.9675 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.9822 | How much revenue did we make so far this week? | 0.964 |
| What did running shoes sell for on average this month? | What did running shoes sell for on average last month? | 0.994 | What was the average selling price of running shoes this month? | 0.9758 |
| How many running shoes were sold this month? | How many running shoes were sold last month? | 0.9897 | How many running shoes were sold so far this month? | 0.9726 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9849 | What was the total value of returns in the previous month? | 0.9679 |
| What was the value of yoga mats returned this year? | What was the value of yoga mats returned last year? | 0.9963 | What was the value of yoga mats returned so far this year? | 0.9799 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9832 | What were sales net of returns in the previous month? | 0.9672 |
