# st:Snowflake/snowflake-arctic-embed-l-v2.0 prefix='query: ' holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9048 | 0.7457 | 0.953 | 0.9908 | 0.9973 |
| **equivalent_surface (same wording=True)** | 310 | 0.9048 | 0.7457 | 0.953 | 0.9908 | 0.9973 |
| **filter_change** | 27 | 0.5472 | 0.4331 | 0.5415 | 0.6377 | 0.7748 |
| **intent_near_miss** | 176 | 0.7314 | 0.5636 | 0.7586 | 0.8725 | 0.9506 |
| **intent_near_miss (same wording=False)** | 176 | 0.7314 | 0.5636 | 0.7586 | 0.8725 | 0.9506 |
| **param_near_miss** | 643 | 0.8196 | 0.6384 | 0.8442 | 0.966 | 0.995 |
| **param_near_miss (same wording=False)** | 228 | 0.7288 | 0.5555 | 0.7271 | 0.8925 | 0.9482 |
| **param_near_miss (same wording=True)** | 415 | 0.8695 | 0.7343 | 0.8883 | 0.9814 | 0.995 |
| **paraphrase** | 256 | 0.8269 | 0.6642 | 0.8467 | 0.938 | 0.9886 |
| equivalent_surface/amount/alias | 10 | 0.9733 | 0.9606 | 0.9752 | 0.9803 | 0.9874 |
| equivalent_surface/channel/alias | 10 | 0.9469 | 0.9165 | 0.941 | 0.9879 | 0.9902 |
| equivalent_surface/n/alias | 20 | 0.9934 | 0.9892 | 0.9933 | 0.9962 | 0.9973 |
| equivalent_surface/period/alias | 235 | 0.8885 | 0.7258 | 0.9426 | 0.9861 | 0.9947 |
| equivalent_surface/product/alias | 15 | 0.8825 | 0.837 | 0.8723 | 0.9393 | 0.9426 |
| equivalent_surface/region/alias | 20 | 0.9693 | 0.9504 | 0.964 | 0.9937 | 0.9946 |
| filter_change/filter_added/region_revenue | 7 | 0.5476 | 0.4147 | 0.5586 | 0.6798 | 0.7748 |
| filter_change/filter_dropped/total_revenue | 20 | 0.5471 | 0.4593 | 0.5413 | 0.6137 | 0.7516 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5333 | 0.3993 | 0.529 | 0.6667 | 0.7107 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8084 | 0.7332 | 0.8164 | 0.8689 | 0.8771 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8545 | 0.8182 | 0.8482 | 0.9065 | 0.9506 |
| intent_near_miss/aggregation/product_units | 20 | 0.8507 | 0.7833 | 0.8643 | 0.9006 | 0.9092 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5713 | 0.4503 | 0.5088 | 0.7499 | 0.7697 |
| intent_near_miss/direction/product_returns | 10 | 0.8255 | 0.7835 | 0.8238 | 0.8536 | 0.9275 |
| intent_near_miss/direction/product_revenue | 10 | 0.7785 | 0.7517 | 0.7661 | 0.8174 | 0.819 |
| intent_near_miss/direction/total_returns | 7 | 0.5945 | 0.5125 | 0.5331 | 0.7167 | 0.8271 |
| intent_near_miss/direction/total_revenue | 7 | 0.673 | 0.622 | 0.6679 | 0.7344 | 0.7552 |
| intent_near_miss/grouping/top_customers | 10 | 0.6476 | 0.606 | 0.6328 | 0.7062 | 0.7606 |
| intent_near_miss/grouping/top_products | 10 | 0.6445 | 0.5828 | 0.6128 | 0.728 | 0.7767 |
| intent_near_miss/measure/net_sales | 14 | 0.6418 | 0.5634 | 0.6229 | 0.7642 | 0.914 |
| intent_near_miss/measure/total_returns | 7 | 0.6555 | 0.5806 | 0.6626 | 0.7142 | 0.7217 |
| intent_near_miss/measure/total_revenue | 7 | 0.5764 | 0.4247 | 0.6255 | 0.7097 | 0.7545 |
| intent_near_miss/negation/region_revenue | 10 | 0.7083 | 0.64 | 0.6875 | 0.8461 | 0.8596 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.8197 | 0.7944 | 0.8263 | 0.8445 | 0.8674 |
| param_near_miss/amount/neighbor | 26 | 0.7992 | 0.6849 | 0.8257 | 0.8834 | 0.9223 |
| param_near_miss/channel/neighbor | 20 | 0.8192 | 0.7269 | 0.8502 | 0.891 | 0.9223 |
| param_near_miss/n/neighbor | 47 | 0.8591 | 0.7003 | 0.8988 | 0.9512 | 0.9784 |
| param_near_miss/period/adjacent | 245 | 0.8581 | 0.658 | 0.8923 | 0.9897 | 0.995 |
| param_near_miss/period/granularity | 180 | 0.8348 | 0.6808 | 0.8602 | 0.9419 | 0.968 |
| param_near_miss/product/neighbor | 85 | 0.6937 | 0.5505 | 0.7059 | 0.8147 | 0.8601 |
| param_near_miss/region/neighbor | 40 | 0.7504 | 0.5562 | 0.7504 | 0.9056 | 0.9513 |
| paraphrase/wording/template | 256 | 0.8269 | 0.6642 | 0.8467 | 0.938 | 0.9886 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.3906 | [0.3125, 0.4766] | 0.9688 | [0.9375, 0.9922] |
| param_near_miss | 128 | 0.3906 | [0.3125, 0.4689] | 0.9609 | [0.9219, 0.9922] |
| period_near_miss | 128 | 0.3906 | [0.3047, 0.4844] | 0.9609 | [0.9297, 0.9922] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.58 | [0.49, 0.67] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4907 | [0.3981, 0.5833] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.875 | [0.8125, 0.9297] |
| B | 128 | 0.5703 | [0.4844, 0.6641] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0125 | [0.0041, 0.0423] | 0.0125 | 0.0125 | 0.5344 |
| raw_oracle_entry | 0.2965 | [0.2779, 0.3626] | — | — | 0.5344 |
| split_full | 0.0251 | [0.0143, 0.2138] | 0.0251 | 0.2234 | 0.5344 |
| split_template | 0.6013 | [0.5303, 0.6708] | 0.6013 | 0.6013 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our total revenue this year? | What was our total revenue last year? | 0.9542 | What was our total revenue year to date? | 0.8957 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9557 | What was the total value of returns so far this year? | 0.8972 |
| Largest sale last month | Largest sale this month | 0.9537 | Largest sale in the previous month | 0.9072 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9672 | What was the total value of returns so far this month? | 0.935 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.97 | What was the total value of returns so far this week? | 0.9413 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9727 | What were sales net of returns in the previous month? | 0.9472 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9672 | What was the total value of returns in the previous month? | 0.943 |
| How much revenue did we make this month? | How much revenue did we make last month? | 0.9527 | How much revenue did we make so far this month? | 0.9293 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.9527 | How much revenue did we make in the previous month? | 0.9294 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.9645 | How much revenue did we make so far this week? | 0.9423 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9557 | What was the total value of returns in the previous year? | 0.9335 |
| Total revenue for the West last month | Total revenue for the West this month | 0.9761 | Total revenue for the West in the previous month | 0.9554 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.956 | How much revenue did we make in the previous year? | 0.9353 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9663 | What were sales net of returns in the previous year? | 0.9458 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9847 | What were sales everywhere except the West so far this month? | 0.9653 |
