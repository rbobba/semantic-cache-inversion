# voyage:voyage-4

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9288 | 0.7796 | 0.9727 | 0.9898 | 0.9976 |
| **equivalent_surface (same wording=True)** | 262 | 0.9288 | 0.7796 | 0.9727 | 0.9898 | 0.9976 |
| **filter_change** | 37 | 0.7307 | 0.6425 | 0.7333 | 0.8364 | 0.8582 |
| **intent_near_miss** | 176 | 0.751 | 0.6352 | 0.7686 | 0.8334 | 0.9208 |
| **intent_near_miss (same wording=False)** | 176 | 0.751 | 0.6352 | 0.7686 | 0.8334 | 0.9208 |
| **param_near_miss** | 637 | 0.8334 | 0.6782 | 0.8568 | 0.9503 | 0.9832 |
| **param_near_miss (same wording=False)** | 228 | 0.7449 | 0.614 | 0.7568 | 0.8676 | 0.9432 |
| **param_near_miss (same wording=True)** | 409 | 0.8827 | 0.7687 | 0.9024 | 0.9623 | 0.9832 |
| **paraphrase** | 384 | 0.8355 | 0.7097 | 0.8575 | 0.9382 | 0.9748 |
| equivalent_surface/account/alias | 10 | 0.9769 | 0.9692 | 0.9805 | 0.9865 | 0.9897 |
| equivalent_surface/amount/alias | 10 | 0.9918 | 0.9889 | 0.991 | 0.9961 | 0.9962 |
| equivalent_surface/category/alias | 15 | 0.9596 | 0.9094 | 0.9781 | 0.9877 | 0.9879 |
| equivalent_surface/merchant/alias | 12 | 0.9895 | 0.9822 | 0.9905 | 0.9966 | 0.997 |
| equivalent_surface/n/alias | 20 | 0.9914 | 0.9862 | 0.9929 | 0.9957 | 0.9976 |
| equivalent_surface/period/alias | 195 | 0.9106 | 0.7632 | 0.9613 | 0.9857 | 0.9902 |
| filter_change/filter_added/category_spend_total | 7 | 0.7878 | 0.721 | 0.7827 | 0.8436 | 0.8582 |
| filter_change/filter_dropped/total_spend | 30 | 0.7174 | 0.6377 | 0.7284 | 0.8102 | 0.8445 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6227 | 0.5327 | 0.616 | 0.7162 | 0.7394 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7836 | 0.7036 | 0.7955 | 0.8312 | 0.8859 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8002 | 0.7628 | 0.8066 | 0.8562 | 0.8677 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7803 | 0.7155 | 0.7833 | 0.8686 | 0.8883 |
| intent_near_miss/aggregation/total_spend | 7 | 0.62 | 0.5425 | 0.6343 | 0.6961 | 0.7009 |
| intent_near_miss/direction/income_total | 7 | 0.6975 | 0.6354 | 0.6657 | 0.7822 | 0.8039 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7925 | 0.7558 | 0.7941 | 0.8481 | 0.8551 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7793 | 0.747 | 0.7877 | 0.7998 | 0.8328 |
| intent_near_miss/direction/total_spend | 7 | 0.7078 | 0.6688 | 0.7137 | 0.7478 | 0.7568 |
| intent_near_miss/grouping/top_categories | 10 | 0.7592 | 0.6521 | 0.8113 | 0.8236 | 0.8382 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7769 | 0.7204 | 0.8006 | 0.8116 | 0.825 |
| intent_near_miss/measure/income_total | 7 | 0.6974 | 0.6304 | 0.7181 | 0.7606 | 0.7953 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6489 | 0.5836 | 0.6467 | 0.7134 | 0.8026 |
| intent_near_miss/measure/total_spend | 7 | 0.6835 | 0.6214 | 0.6839 | 0.7561 | 0.7653 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.838 | 0.8139 | 0.8285 | 0.8835 | 0.9208 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8143 | 0.7894 | 0.8161 | 0.8434 | 0.858 |
| param_near_miss/account/neighbor | 20 | 0.789 | 0.6729 | 0.8122 | 0.9055 | 0.9091 |
| param_near_miss/amount/neighbor | 25 | 0.7685 | 0.5838 | 0.7855 | 0.9221 | 0.9457 |
| param_near_miss/category/neighbor | 45 | 0.8227 | 0.7026 | 0.8347 | 0.9197 | 0.9522 |
| param_near_miss/merchant/neighbor | 87 | 0.7619 | 0.6424 | 0.7832 | 0.8576 | 0.9054 |
| param_near_miss/n/neighbor | 45 | 0.8615 | 0.728 | 0.9086 | 0.9514 | 0.9629 |
| param_near_miss/period/adjacent | 230 | 0.8574 | 0.7089 | 0.8897 | 0.9721 | 0.9832 |
| param_near_miss/period/granularity | 185 | 0.8464 | 0.708 | 0.8911 | 0.929 | 0.9679 |
| paraphrase/wording/template | 384 | 0.8355 | 0.7097 | 0.8575 | 0.9382 | 0.9748 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.1562 | [0.0938, 0.2266] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.1562 | [0.1016, 0.2266] | 0.9844 | [0.9609, 1.0] |
| period_near_miss | 128 | 0.1562 | [0.1016, 0.2266] | 0.9766 | [0.9453, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.77 | [0.68, 0.85] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.4576 | [0.3644, 0.5424] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0626 | [0.0517, 0.0791] | 0.0626 | 0.0707 | 0.5317 |
| raw_oracle_entry | 0.1683 | [0.1541, 0.1995] | — | — | 0.5317 |
| split_full | 0.3 | [0.2776, 0.335] | 0.3211 | 0.3537 | 0.5317 |
| split_template | 0.9732 | [0.9599, 0.9844] | 0.9732 | 0.9846 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9105 | Income minus expenses during 2025 | 0.7826 |
| Total money coming in last year | Total money coming in in the last 12 months | 0.87 | What was my total income last year? | 0.7548 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9621 | What was my average purchase at Shell last year? | 0.8898 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9439 | What was my largest purchase last year? | 0.8763 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9573 | How much did I spend per transaction at Walmart during 2025, on average? | 0.8933 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9331 | How much did I spend per transaction at Uber last year, on average? | 0.8734 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.963 | How much did I get refunded from Spotify last year? | 0.9083 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9416 | How much did I get refunded from Shell last year? | 0.9037 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9122 | Total expenses last year | 0.8837 |
| Total spent on gas last year | Total spent on gas this year | 0.9078 | How much did I spend on gas last year? | 0.8926 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9516 | How many transactions did I have at Starbucks last year? | 0.9408 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9475 | What did I pay Starbucks in total last year? | 0.9394 |
| How much money did Home Depot give back to me this month? | How much money did Home Depot give back to me last month? | 0.9823 | How much money did Home Depot give back to me so far this month? | 0.9763 |
| How much income did I receive this month? | How much income did I receive last month? | 0.9431 | How much income did I receive so far this month? | 0.9373 |
| How much money did Starbucks give back to me this week? | How much money did Starbucks give back to me last week? | 0.9792 | How much money did Starbucks give back to me so far this week? | 0.9739 |
