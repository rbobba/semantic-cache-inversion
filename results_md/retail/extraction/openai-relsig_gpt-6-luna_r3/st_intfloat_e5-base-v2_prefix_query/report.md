# st:intfloat/e5-base-v2 prefix='query: '

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9729 | 0.9257 | 0.988 | 0.9966 | 0.999 |
| **equivalent_surface (same wording=True)** | 310 | 0.9729 | 0.9257 | 0.988 | 0.9966 | 0.999 |
| **filter_change** | 27 | 0.8753 | 0.8357 | 0.8797 | 0.9056 | 0.9107 |
| **intent_near_miss** | 176 | 0.9151 | 0.8681 | 0.9217 | 0.9583 | 0.9831 |
| **intent_near_miss (same wording=False)** | 176 | 0.9151 | 0.8681 | 0.9217 | 0.9583 | 0.9831 |
| **param_near_miss** | 643 | 0.9449 | 0.8904 | 0.9515 | 0.9951 | 0.9989 |
| **param_near_miss (same wording=False)** | 228 | 0.9103 | 0.8596 | 0.9113 | 0.9521 | 0.9859 |
| **param_near_miss (same wording=True)** | 415 | 0.9639 | 0.9265 | 0.9673 | 0.997 | 0.9989 |
| **paraphrase** | 256 | 0.9361 | 0.897 | 0.94 | 0.9707 | 0.9889 |
| equivalent_surface/amount/alias | 10 | 0.9941 | 0.9933 | 0.9942 | 0.995 | 0.9956 |
| equivalent_surface/channel/alias | 10 | 0.9799 | 0.9687 | 0.9794 | 0.9938 | 0.9949 |
| equivalent_surface/n/alias | 20 | 0.9979 | 0.9973 | 0.9979 | 0.9985 | 0.999 |
| equivalent_surface/period/alias | 235 | 0.9689 | 0.9197 | 0.9871 | 0.996 | 0.9974 |
| equivalent_surface/product/alias | 15 | 0.9633 | 0.9439 | 0.9607 | 0.9808 | 0.9856 |
| equivalent_surface/region/alias | 20 | 0.9882 | 0.9769 | 0.9898 | 0.9964 | 0.9967 |
| filter_change/filter_added/region_revenue | 7 | 0.88 | 0.8429 | 0.9003 | 0.9072 | 0.9107 |
| filter_change/filter_dropped/total_revenue | 20 | 0.8737 | 0.8281 | 0.8788 | 0.903 | 0.9068 |
| intent_near_miss/aggregation/largest_order | 7 | 0.8648 | 0.8397 | 0.8705 | 0.8861 | 0.8939 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.9309 | 0.8914 | 0.9368 | 0.9635 | 0.9668 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.9552 | 0.9424 | 0.9554 | 0.9649 | 0.9831 |
| intent_near_miss/aggregation/product_units | 20 | 0.9343 | 0.9145 | 0.9358 | 0.9492 | 0.9661 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.8608 | 0.8308 | 0.8587 | 0.8892 | 0.8929 |
| intent_near_miss/direction/product_returns | 10 | 0.9379 | 0.9204 | 0.9335 | 0.9555 | 0.9707 |
| intent_near_miss/direction/product_revenue | 10 | 0.9375 | 0.9331 | 0.9369 | 0.943 | 0.9433 |
| intent_near_miss/direction/total_returns | 7 | 0.8914 | 0.8617 | 0.8878 | 0.9212 | 0.9382 |
| intent_near_miss/direction/total_revenue | 7 | 0.8945 | 0.8765 | 0.8986 | 0.9089 | 0.9206 |
| intent_near_miss/grouping/top_customers | 10 | 0.8893 | 0.8702 | 0.8889 | 0.9076 | 0.9194 |
| intent_near_miss/grouping/top_products | 10 | 0.8865 | 0.8648 | 0.8728 | 0.9213 | 0.9264 |
| intent_near_miss/measure/net_sales | 14 | 0.9082 | 0.8893 | 0.9058 | 0.9276 | 0.9558 |
| intent_near_miss/measure/total_returns | 7 | 0.8954 | 0.8704 | 0.9076 | 0.9134 | 0.9154 |
| intent_near_miss/measure/total_revenue | 7 | 0.8624 | 0.819 | 0.8577 | 0.916 | 0.9304 |
| intent_near_miss/negation/region_revenue | 10 | 0.9135 | 0.8831 | 0.8995 | 0.9717 | 0.9754 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.94 | 0.9288 | 0.9369 | 0.9593 | 0.9594 |
| param_near_miss/amount/neighbor | 26 | 0.9349 | 0.895 | 0.9435 | 0.9617 | 0.9689 |
| param_near_miss/channel/neighbor | 20 | 0.9331 | 0.8969 | 0.9474 | 0.9569 | 0.9702 |
| param_near_miss/n/neighbor | 47 | 0.9565 | 0.9089 | 0.9735 | 0.9848 | 0.9906 |
| param_near_miss/period/adjacent | 245 | 0.9559 | 0.9021 | 0.9597 | 0.9977 | 0.9989 |
| param_near_miss/period/granularity | 180 | 0.9535 | 0.9192 | 0.9633 | 0.9781 | 0.9881 |
| param_near_miss/product/neighbor | 85 | 0.9116 | 0.8621 | 0.9139 | 0.9571 | 0.9643 |
| param_near_miss/region/neighbor | 40 | 0.9089 | 0.8455 | 0.9113 | 0.9605 | 0.9668 |
| paraphrase/wording/template | 256 | 0.9361 | 0.897 | 0.94 | 0.9707 | 0.9889 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5859 | [0.5078, 0.6719] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5859 | [0.5, 0.6719] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5859 | [0.5, 0.6719] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.77 | [0.69, 0.85] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.6389 | [0.537, 0.7222] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9297 | [0.8828, 0.9688] |
| B | 128 | 0.6953 | [0.6172, 0.7812] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0009 | [0.0, 0.0029] | 0.0009 | 0.0009 | 0.5373 |
| raw_oracle_entry | 0.0925 | [0.085, 0.1282] | — | — | 0.5373 |
| split_full | 0.2803 | [0.2634, 0.3021] | 0.2983 | 0.3423 | 0.5373 |
| split_template | 0.6325 | [0.6125, 0.6543] | 0.6325 | 0.6478 | 1.0 |
| split_full_extracted | 0.2722 | [0.2542, 0.2949] | 0.292 | 0.3378 | 0.5364 |
| split_template_extracted | 0.6325 | [0.6122, 0.6542] | 0.6325 | 0.6478 | 0.9991 |
| split_template_extracted_slots | 0.6325 | [0.6122, 0.6542] | 0.6325 | 0.6478 | 0.9991 |
| split_template_negguard | 0.6325 | [0.6122, 0.6542] | 0.6325 | 0.655 | 0.9991 |
| split_template_guarded | 0.8194 | [0.7995, 0.8374] | 0.8194 | 0.947 | 0.947 |
| split_template_guarded_goldsig | 0.9991 | [0.9972, 1.0] | 0.9991 | 0.9991 | 0.9991 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.977 | 0.2704 | 0.2704 [0.2528, 0.2893] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9628 | 0.6325 | 0.6325 [0.6122, 0.6542] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9628 | 0.6325 | 0.6325 [0.6122, 0.6542] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9628 | 0.6325 | 0.6325 [0.6122, 0.6542] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.9569 | 0.947 [0.9329, 0.9626] | 0.0103 [0.0039, 0.0175] | 11 | 11 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.9991 | 0.9991 [0.9972, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9951 | What was the total value of returns in the previous year? | 0.9878 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9957 | What were sales net of returns in the previous year? | 0.9884 |
| Show the biggest single order last year | Show the biggest single order this year | 0.9905 | Show the biggest single order in the previous year | 0.9834 |
| How much revenue did we make last year? | How much revenue did we make this year? | 0.9955 | How much revenue did we make in the previous year? | 0.9887 |
| What was our total revenue this year? | What was our total revenue last year? | 0.9958 | What was our total revenue so far this year? | 0.9895 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9951 | What was the total value of returns so far this year? | 0.9895 |
| Order count in stores last month | Order count in stores this month | 0.9892 | Order count in stores in the previous month | 0.9836 |
| What did running shoes sell for on average this month? | What did running shoes sell for on average last month? | 0.998 | What did running shoes sell for on average so far this month? | 0.9928 |
| Order count online this month | Order count online last month | 0.9862 | Order count online so far this month | 0.981 |
| Order count in stores this week | Order count in stores last week | 0.9884 | Order count in stores so far this week | 0.9836 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9976 | What was the total value of returns so far this week? | 0.9929 |
| Revenue minus returns this week | Revenue minus returns last week | 0.9933 | Revenue minus returns so far this week | 0.9888 |
| On average, how much did customers pay for ski jackets this week? | On average, how much did customers pay for ski jackets last week? | 0.9989 | On average, how much did customers pay for ski jackets so far this week? | 0.9944 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9963 | What were sales net of returns in the previous month? | 0.992 |
| What were sales everywhere except the West this month? | What were sales everywhere except the West last month? | 0.9972 | What were sales everywhere except the West so far this month? | 0.9929 |
