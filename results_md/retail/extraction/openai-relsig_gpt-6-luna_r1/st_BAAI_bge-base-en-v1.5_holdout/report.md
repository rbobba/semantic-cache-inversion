# st:BAAI/bge-base-en-v1.5 holdout

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 479 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.945 | 0.8618 | 0.9739 | 0.9907 | 0.9969 |
| **equivalent_surface (same wording=True)** | 310 | 0.945 | 0.8618 | 0.9739 | 0.9907 | 0.9969 |
| **filter_change** | 27 | 0.7642 | 0.7043 | 0.7757 | 0.8112 | 0.823 |
| **intent_near_miss** | 176 | 0.83 | 0.7568 | 0.8321 | 0.9054 | 0.9464 |
| **intent_near_miss (same wording=False)** | 176 | 0.83 | 0.7568 | 0.8321 | 0.9054 | 0.9464 |
| **param_near_miss** | 643 | 0.8903 | 0.7813 | 0.9065 | 0.9867 | 0.9976 |
| **param_near_miss (same wording=False)** | 228 | 0.8302 | 0.7221 | 0.8392 | 0.9218 | 0.9628 |
| **param_near_miss (same wording=True)** | 415 | 0.9233 | 0.8544 | 0.9284 | 0.9914 | 0.9976 |
| **paraphrase** | 256 | 0.8826 | 0.7906 | 0.8941 | 0.9507 | 0.9801 |
| equivalent_surface/amount/alias | 10 | 0.9857 | 0.9847 | 0.9853 | 0.9871 | 0.9883 |
| equivalent_surface/channel/alias | 10 | 0.9508 | 0.9092 | 0.9527 | 0.9884 | 0.9922 |
| equivalent_surface/n/alias | 20 | 0.9946 | 0.9933 | 0.9943 | 0.9962 | 0.9969 |
| equivalent_surface/period/alias | 235 | 0.9362 | 0.852 | 0.9719 | 0.9882 | 0.9944 |
| equivalent_surface/product/alias | 15 | 0.94 | 0.9125 | 0.9402 | 0.964 | 0.9651 |
| equivalent_surface/region/alias | 20 | 0.9794 | 0.9691 | 0.9793 | 0.9895 | 0.9914 |
| filter_change/filter_added/region_revenue | 7 | 0.7483 | 0.6593 | 0.8011 | 0.8158 | 0.823 |
| filter_change/filter_dropped/total_revenue | 20 | 0.7698 | 0.7252 | 0.7727 | 0.8077 | 0.8183 |
| intent_near_miss/aggregation/largest_order | 7 | 0.7066 | 0.6591 | 0.7133 | 0.7601 | 0.7791 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.8578 | 0.8177 | 0.8647 | 0.9031 | 0.9126 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8734 | 0.8413 | 0.8665 | 0.9126 | 0.9187 |
| intent_near_miss/aggregation/product_units | 20 | 0.8701 | 0.8181 | 0.886 | 0.9057 | 0.9187 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.7494 | 0.6983 | 0.7238 | 0.8137 | 0.8322 |
| intent_near_miss/direction/product_returns | 10 | 0.8662 | 0.8442 | 0.855 | 0.9165 | 0.9407 |
| intent_near_miss/direction/product_revenue | 10 | 0.8339 | 0.8121 | 0.8408 | 0.8504 | 0.8547 |
| intent_near_miss/direction/total_returns | 7 | 0.8046 | 0.7635 | 0.7971 | 0.8536 | 0.8863 |
| intent_near_miss/direction/total_revenue | 7 | 0.8021 | 0.7569 | 0.7849 | 0.864 | 0.8902 |
| intent_near_miss/grouping/top_customers | 10 | 0.8172 | 0.7918 | 0.8213 | 0.8401 | 0.8534 |
| intent_near_miss/grouping/top_products | 10 | 0.8054 | 0.7731 | 0.7988 | 0.8517 | 0.855 |
| intent_near_miss/measure/net_sales | 14 | 0.8011 | 0.7706 | 0.7952 | 0.8288 | 0.9216 |
| intent_near_miss/measure/total_returns | 7 | 0.821 | 0.7864 | 0.8262 | 0.8505 | 0.8576 |
| intent_near_miss/measure/total_revenue | 7 | 0.7483 | 0.6782 | 0.7269 | 0.8379 | 0.8563 |
| intent_near_miss/negation/region_revenue | 10 | 0.8149 | 0.7648 | 0.782 | 0.9424 | 0.9464 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.9031 | 0.8893 | 0.9071 | 0.9129 | 0.9238 |
| param_near_miss/amount/neighbor | 26 | 0.9022 | 0.8442 | 0.921 | 0.9413 | 0.9493 |
| param_near_miss/channel/neighbor | 20 | 0.8818 | 0.8188 | 0.8895 | 0.9247 | 0.937 |
| param_near_miss/n/neighbor | 47 | 0.8955 | 0.8191 | 0.9066 | 0.9528 | 0.965 |
| param_near_miss/period/adjacent | 245 | 0.9186 | 0.8039 | 0.9329 | 0.9941 | 0.9976 |
| param_near_miss/period/granularity | 180 | 0.894 | 0.8085 | 0.9147 | 0.9448 | 0.9708 |
| param_near_miss/product/neighbor | 85 | 0.8275 | 0.7167 | 0.8312 | 0.9244 | 0.9368 |
| param_near_miss/region/neighbor | 40 | 0.8239 | 0.6979 | 0.8335 | 0.9268 | 0.9435 |
| paraphrase/wording/template | 256 | 0.8826 | 0.7906 | 0.8941 | 0.9507 | 0.9801 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5547 | [0.4764, 0.6406] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.5547 | [0.4688, 0.6406] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.5547 | [0.4688, 0.6484] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.72 | [0.64, 0.81] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.4722 | [0.3796, 0.5648] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9219 | [0.875, 0.9688] |
| B | 128 | 0.6875 | [0.6094, 0.7656] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0104 | [0.0021, 0.0309] | 0.0104 | 0.0104 | 0.5344 |
| raw_oracle_entry | 0.2401 | [0.2214, 0.2943] | — | — | 0.5344 |
| split_full | 0.0292 | [0.0147, 0.1042] | 0.0292 | 0.0292 | 0.5344 |
| split_template | 0.1232 | [0.0889, 0.1566] | 0.1232 | 0.1232 | 1.0 |
| split_full_extracted | 0.0292 | [0.0147, 0.1042] | 0.0292 | 0.0292 | 0.5344 |
| split_template_extracted | 0.1232 | [0.0889, 0.1566] | 0.1232 | 0.1232 | 1.0 |
| split_template_extracted_slots | 0.1232 | [0.0889, 0.1566] | 0.1232 | 0.1232 | 1.0 |
| split_template_negguard | 0.3445 | [0.2802, 0.4064] | 0.3445 | 0.3445 | 1.0 |
| split_template_guarded | 0.6514 | [0.5933, 0.7064] | 0.6514 | 0.8706 | 0.8706 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9489 | 0.0292 | 0.0292 [0.0144, 0.0461] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9489 | 0.1211 | 0.1211 [0.0869, 0.1532] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9489 | 0.1211 | 0.1211 [0.0869, 0.1532] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9489 | 0.1211 | 0.1211 [0.0869, 0.1532] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.8894 | 0.8706 [0.8347, 0.9037] | 0.0211 [0.0072, 0.037] | 9 | 9 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9875 | What was the total value of returns so far this year? | 0.9608 |
| What was our total revenue this year? | What was our total revenue last year? | 0.9919 | What was our total revenue so far this year? | 0.9709 |
| Revenue minus returns this year | Revenue minus returns last year | 0.9858 | Revenue minus returns so far this year | 0.9652 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9875 | What was the total value of returns in the previous year? | 0.9685 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9822 | What was the total value of returns so far this month? | 0.9637 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9902 | What was the total value of returns so far this week? | 0.9719 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9894 | What were sales net of returns in the previous year? | 0.9719 |
| What were sales net of returns last month? | What were sales net of returns this month? | 0.9867 | What were sales net of returns in the previous month? | 0.9695 |
| How many rain jackets were sold last year? | How many rain jackets were sold this year? | 0.9914 | How many rain jackets were sold in the previous year? | 0.9748 |
| Largest sale this year | Largest sale last year | 0.9903 | Largest sale so far this year | 0.974 |
| How many running shoes were sold this month? | How many running shoes were sold last month? | 0.9934 | How many running shoes were sold so far this month? | 0.9778 |
| Revenue minus returns this month | Revenue minus returns last month | 0.9833 | Revenue minus returns so far this month | 0.9677 |
| How much revenue did we make this week? | How much revenue did we make last week? | 0.9914 | How much revenue did we make so far this week? | 0.9759 |
| What was the value of yoga mats returned this week? | What was the value of yoga mats returned last week? | 0.9963 | What was the value of yoga mats returned so far this week? | 0.9819 |
| Show the biggest single order last year | Show the biggest single order this year | 0.9797 | Show the biggest single order in the previous year | 0.9655 |
