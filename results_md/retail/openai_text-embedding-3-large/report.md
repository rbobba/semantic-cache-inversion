# openai:text-embedding-3-large

Dataset sha256(pairs) `531c4757e5d6dadc`, 128 cached questions, 1113 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 310 | 0.9219 | 0.8094 | 0.9496 | 0.9811 | 0.994 |
| **equivalent_surface (same wording=True)** | 310 | 0.9219 | 0.8094 | 0.9496 | 0.9811 | 0.994 |
| **filter_change** | 27 | 0.566 | 0.4765 | 0.5791 | 0.6403 | 0.6888 |
| **intent_near_miss** | 176 | 0.7079 | 0.5593 | 0.7245 | 0.83 | 0.911 |
| **intent_near_miss (same wording=False)** | 176 | 0.7079 | 0.5593 | 0.7245 | 0.83 | 0.911 |
| **param_near_miss** | 643 | 0.8315 | 0.6472 | 0.8659 | 0.9662 | 0.9915 |
| **param_near_miss (same wording=False)** | 228 | 0.7202 | 0.5678 | 0.7346 | 0.8573 | 0.9192 |
| **param_near_miss (same wording=True)** | 415 | 0.8927 | 0.7988 | 0.9051 | 0.9744 | 0.9915 |
| **paraphrase** | 256 | 0.7968 | 0.6648 | 0.817 | 0.8996 | 0.9638 |
| equivalent_surface/amount/alias | 10 | 0.9634 | 0.9576 | 0.9631 | 0.9685 | 0.9743 |
| equivalent_surface/channel/alias | 10 | 0.939 | 0.8896 | 0.9481 | 0.9825 | 0.9886 |
| equivalent_surface/n/alias | 20 | 0.9829 | 0.9759 | 0.9824 | 0.9928 | 0.994 |
| equivalent_surface/period/alias | 235 | 0.9091 | 0.7908 | 0.941 | 0.9764 | 0.9867 |
| equivalent_surface/product/alias | 15 | 0.9283 | 0.8965 | 0.9381 | 0.9583 | 0.9669 |
| equivalent_surface/region/alias | 20 | 0.9768 | 0.9618 | 0.9801 | 0.9879 | 0.9906 |
| filter_change/filter_added/region_revenue | 7 | 0.5502 | 0.458 | 0.5659 | 0.6512 | 0.6888 |
| filter_change/filter_dropped/total_revenue | 20 | 0.5715 | 0.4928 | 0.5813 | 0.6375 | 0.6486 |
| intent_near_miss/aggregation/largest_order | 7 | 0.5601 | 0.5089 | 0.5554 | 0.6172 | 0.6567 |
| intent_near_miss/aggregation/product_avg_price | 20 | 0.7395 | 0.6527 | 0.7473 | 0.8006 | 0.823 |
| intent_near_miss/aggregation/product_revenue | 20 | 0.8013 | 0.7338 | 0.8075 | 0.8674 | 0.911 |
| intent_near_miss/aggregation/product_units | 20 | 0.7857 | 0.7159 | 0.8147 | 0.8509 | 0.8792 |
| intent_near_miss/aggregation/total_revenue | 7 | 0.5842 | 0.5023 | 0.5724 | 0.6693 | 0.6986 |
| intent_near_miss/direction/product_returns | 10 | 0.7764 | 0.7297 | 0.7823 | 0.814 | 0.8697 |
| intent_near_miss/direction/product_revenue | 10 | 0.7831 | 0.7379 | 0.7543 | 0.8478 | 0.856 |
| intent_near_miss/direction/total_returns | 7 | 0.5914 | 0.5323 | 0.5502 | 0.6851 | 0.7528 |
| intent_near_miss/direction/total_revenue | 7 | 0.6761 | 0.6303 | 0.6547 | 0.7275 | 0.7642 |
| intent_near_miss/grouping/top_customers | 10 | 0.6517 | 0.5664 | 0.6717 | 0.7081 | 0.7622 |
| intent_near_miss/grouping/top_products | 10 | 0.6168 | 0.5645 | 0.6073 | 0.6726 | 0.7238 |
| intent_near_miss/measure/net_sales | 14 | 0.671 | 0.626 | 0.6635 | 0.7272 | 0.808 |
| intent_near_miss/measure/total_returns | 7 | 0.6502 | 0.5481 | 0.6195 | 0.7595 | 0.7629 |
| intent_near_miss/measure/total_revenue | 7 | 0.5774 | 0.5014 | 0.5564 | 0.6735 | 0.7036 |
| intent_near_miss/negation/region_revenue | 10 | 0.7198 | 0.6514 | 0.688 | 0.8798 | 0.9067 |
| intent_near_miss/negation/region_revenue_excluding | 10 | 0.7719 | 0.7362 | 0.7616 | 0.8278 | 0.8365 |
| param_near_miss/amount/neighbor | 26 | 0.836 | 0.7245 | 0.8713 | 0.9034 | 0.9199 |
| param_near_miss/channel/neighbor | 20 | 0.7898 | 0.6721 | 0.8333 | 0.8747 | 0.8847 |
| param_near_miss/n/neighbor | 47 | 0.8161 | 0.6659 | 0.8674 | 0.9076 | 0.9256 |
| param_near_miss/period/adjacent | 245 | 0.8595 | 0.6824 | 0.8942 | 0.9804 | 0.9915 |
| param_near_miss/period/granularity | 180 | 0.8704 | 0.7448 | 0.8975 | 0.9565 | 0.977 |
| param_near_miss/product/neighbor | 85 | 0.7273 | 0.5543 | 0.7481 | 0.8787 | 0.9098 |
| param_near_miss/region/neighbor | 40 | 0.7429 | 0.5859 | 0.7523 | 0.9047 | 0.9269 |
| paraphrase/wording/template | 256 | 0.7968 | 0.6648 | 0.817 | 0.8996 | 0.9638 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4609 | [0.375, 0.5469] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.4609 | [0.3828, 0.5391] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.4609 | [0.3672, 0.5547] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.71 | [0.62, 0.7902] |
| intent_near_miss | 108 | 0.0 | [0.0, 0.0] | 0.3796 | [0.287, 0.4725] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9844 | [0.9609, 1.0] |
| B | 128 | 0.6562 | [0.5781, 0.7422] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0027 | [0.0, 0.0099] | 0.0027 | 0.0027 | 0.5373 |
| raw_oracle_entry | 0.1051 | [0.0992, 0.1401] | — | — | 0.5373 |
| split_full | 0.2956 | [0.2771, 0.3255] | 0.2974 | 0.4043 | 0.5373 |
| split_template | 0.6442 | [0.6214, 0.6696] | 0.6442 | 0.8374 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What was our total revenue this year? | What was our total revenue last year? | 0.9454 | What was our total revenue so far this year? | 0.9044 |
| How much revenue did we make this month? | How much revenue did we make last month? | 0.9594 | How much revenue did we make so far this month? | 0.9241 |
| Total revenue for the West last month | Total revenue for the West this month | 0.968 | Total revenue for the West in the previous month | 0.9374 |
| What was the total value of returns this year? | What was the total value of returns last year? | 0.9524 | What was the total value of returns so far this year? | 0.9224 |
| Largest sale last month | Largest sale this month | 0.9356 | Largest sale in the previous month | 0.9068 |
| What was the total value of returns last year? | What was the total value of returns this year? | 0.9524 | What was the total value of returns in the previous year? | 0.9256 |
| What was the total value of returns this month? | What was the total value of returns last month? | 0.9707 | What was the total value of returns so far this month? | 0.945 |
| What was the total value of returns last month? | What was the total value of returns this month? | 0.9707 | What was the total value of returns in the previous month? | 0.9467 |
| How many running shoes were sold this month? | How many running shoes were sold last month? | 0.98 | How many running shoes were sold so far this month? | 0.9568 |
| What was the total value of returns this week? | What was the total value of returns last week? | 0.9708 | What was the total value of returns so far this week? | 0.9496 |
| How much revenue did we make last month? | How much revenue did we make this month? | 0.9594 | How much revenue did we make in the previous month? | 0.941 |
| How many rain jackets were sold last year? | How many rain jackets were sold this year? | 0.9745 | How many rain jackets were sold in the previous year? | 0.9603 |
| Revenue minus returns this week | Revenue minus returns last week | 0.9553 | Revenue minus returns so far this week | 0.9419 |
| What were sales net of returns last year? | What were sales net of returns this year? | 0.9632 | What were sales net of returns in the previous year? | 0.9501 |
| How much did we refund on ski jackets last year? | How much did we refund on ski jackets this year? | 0.9883 | How much did we refund on ski jackets in the previous year? | 0.9754 |
