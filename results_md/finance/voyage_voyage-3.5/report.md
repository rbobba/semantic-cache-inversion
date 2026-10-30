# voyage:voyage-3.5

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 1167 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9122 | 0.7779 | 0.9485 | 0.9805 | 0.9952 |
| **equivalent_surface (same wording=True)** | 290 | 0.9122 | 0.7779 | 0.9485 | 0.9805 | 0.9952 |
| **filter_change** | 37 | 0.7084 | 0.5712 | 0.7366 | 0.8128 | 0.8823 |
| **intent_near_miss** | 176 | 0.7286 | 0.6135 | 0.7438 | 0.8155 | 0.8763 |
| **intent_near_miss (same wording=False)** | 176 | 0.7286 | 0.6135 | 0.7438 | 0.8155 | 0.8763 |
| **param_near_miss** | 637 | 0.8297 | 0.6886 | 0.8465 | 0.9557 | 0.9874 |
| **param_near_miss (same wording=False)** | 228 | 0.7442 | 0.6082 | 0.7488 | 0.8616 | 0.9341 |
| **param_near_miss (same wording=True)** | 409 | 0.8773 | 0.7849 | 0.88 | 0.9687 | 0.9874 |
| **paraphrase** | 266 | 0.8237 | 0.6888 | 0.843 | 0.9189 | 0.9604 |
| equivalent_surface/account/alias | 10 | 0.9607 | 0.9527 | 0.9595 | 0.9701 | 0.9761 |
| equivalent_surface/amount/alias | 10 | 0.9679 | 0.9617 | 0.9711 | 0.9746 | 0.9759 |
| equivalent_surface/category/alias | 14 | 0.9494 | 0.9007 | 0.9617 | 0.9789 | 0.9838 |
| equivalent_surface/merchant/alias | 20 | 0.9665 | 0.9438 | 0.9729 | 0.984 | 0.9871 |
| equivalent_surface/n/alias | 20 | 0.9847 | 0.9643 | 0.9892 | 0.9941 | 0.9952 |
| equivalent_surface/period/alias | 216 | 0.8932 | 0.7649 | 0.9331 | 0.9725 | 0.9878 |
| filter_change/filter_added/category_spend_total | 7 | 0.7698 | 0.665 | 0.747 | 0.87 | 0.8823 |
| filter_change/filter_dropped/total_spend | 30 | 0.694 | 0.5637 | 0.7309 | 0.7735 | 0.8211 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5868 | 0.5336 | 0.565 | 0.6619 | 0.7235 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7322 | 0.6901 | 0.7386 | 0.774 | 0.7777 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7853 | 0.7258 | 0.7935 | 0.8304 | 0.8572 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7287 | 0.6513 | 0.7323 | 0.7902 | 0.7974 |
| intent_near_miss/aggregation/total_spend | 7 | 0.538 | 0.4491 | 0.5014 | 0.6627 | 0.6873 |
| intent_near_miss/direction/income_total | 7 | 0.7615 | 0.7185 | 0.7472 | 0.8208 | 0.8271 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7957 | 0.7279 | 0.7949 | 0.8515 | 0.8559 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7377 | 0.6722 | 0.7605 | 0.7836 | 0.79 |
| intent_near_miss/direction/total_spend | 7 | 0.7116 | 0.6577 | 0.7276 | 0.7558 | 0.788 |
| intent_near_miss/grouping/top_categories | 10 | 0.7576 | 0.7051 | 0.7589 | 0.8115 | 0.8546 |
| intent_near_miss/grouping/top_merchants | 10 | 0.768 | 0.7322 | 0.7805 | 0.8106 | 0.8325 |
| intent_near_miss/measure/income_total | 7 | 0.7401 | 0.6612 | 0.7343 | 0.8234 | 0.8763 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6454 | 0.5708 | 0.6474 | 0.7102 | 0.7239 |
| intent_near_miss/measure/total_spend | 7 | 0.6426 | 0.5617 | 0.6319 | 0.7369 | 0.7584 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.7947 | 0.7705 | 0.7969 | 0.8271 | 0.8627 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7869 | 0.6944 | 0.7943 | 0.8546 | 0.8705 |
| param_near_miss/account/neighbor | 20 | 0.7942 | 0.6532 | 0.837 | 0.8824 | 0.9126 |
| param_near_miss/amount/neighbor | 24 | 0.7649 | 0.6511 | 0.7989 | 0.8817 | 0.9008 |
| param_near_miss/category/neighbor | 47 | 0.8212 | 0.7121 | 0.8303 | 0.9129 | 0.9514 |
| param_near_miss/merchant/neighbor | 86 | 0.7838 | 0.674 | 0.8081 | 0.8617 | 0.9092 |
| param_near_miss/n/neighbor | 46 | 0.8379 | 0.6703 | 0.8905 | 0.9269 | 0.9661 |
| param_near_miss/period/adjacent | 225 | 0.8541 | 0.6947 | 0.8823 | 0.9786 | 0.9874 |
| param_near_miss/period/granularity | 189 | 0.8335 | 0.7361 | 0.8469 | 0.9311 | 0.9732 |
| paraphrase/wording/template | 266 | 0.8237 | 0.6888 | 0.843 | 0.9189 | 0.9604 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4531 | [0.3672, 0.5391] | 0.9766 | [0.9453, 1.0] |
| param_near_miss | 128 | 0.4531 | [0.3672, 0.5391] | 0.9766 | [0.9453, 1.0] |
| period_near_miss | 128 | 0.4531 | [0.3594, 0.5391] | 0.9609 | [0.9297, 0.9922] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.83 | [0.75, 0.9] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.2966 | [0.2119, 0.3729] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8828 | [0.8203, 0.9375] |
| B | 128 | 0.5547 | [0.4688, 0.6406] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0103 | [0.0051, 0.0175] | 0.0103 | 0.0103 | 0.5081 |
| raw_oracle_entry | 0.1105 | [0.0993, 0.1422] | — | — | 0.5081 |
| split_full | 0.2931 | [0.2742, 0.3253] | 0.3488 | 0.4165 | 0.5081 |
| split_template | 0.9443 | [0.9279, 0.9608] | 0.9871 | 0.9871 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Count my transactions at Home Depot last month | Count my transactions at Home Depot this month | 0.9613 | How many transactions did I have at Home Depot last month? | 0.9092 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9725 | How much more did I earn than I spent so far this year? | 0.9218 |
| How much money went to Lowe's this month? | How much money went to Lowe's last month? | 0.9705 | How much money went to Lowe's so far this month? | 0.9277 |
| Count my transactions at Walmart last month | Count my transactions at Walmart this month | 0.9558 | How many transactions did I have at Walmart last month? | 0.9149 |
| How much did I get refunded from Lowe's this week? | How much did I get refunded from Lowe's last week? | 0.9834 | How much did I get refunded from Lowes this week? | 0.9444 |
| Number of purchases at Shell this week | Number of purchases at Shell last week | 0.9796 | Number of purchases at Shell so far this week | 0.9415 |
| How much did I get refunded from Lowe's this year? | How much did I get refunded from Lowe's last year? | 0.9765 | How much did I get refunded from Lowes this year? | 0.9385 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9797 | How much did I get refunded from Shell year to date? | 0.9424 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9718 | How much income did I receive so far this week? | 0.9364 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9813 | How much money went to Chevron so far this month? | 0.9487 |
| Average transaction amount at Walmart this week | Average transaction amount at Walmart last week | 0.9739 | Average transaction amount at Walmart so far this week | 0.9426 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9577 | What were my overall expenses so far this month? | 0.9279 |
| On average, how much did each purchase at Target cost this month? | On average, how much did each purchase at Target cost last month? | 0.9805 | On average, how much did each purchase at Target cost so far this month? | 0.9531 |
| What was my spending on subscriptions this week? | What was my spending on subscriptions last week? | 0.9788 | How much did I spend on subscriptions this week? | 0.9522 |
| Average transaction amount at Home Depot last month | Average transaction amount at Home Depot this month | 0.9589 | Average transaction amount at Home Depot in the previous month | 0.9339 |
