# st:Qwen/Qwen3-Embedding-0.6B holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9506 | 0.8704 | 0.9749 | 0.9915 | 0.9965 |
| **equivalent_surface (same wording=True)** | 290 | 0.9506 | 0.8704 | 0.9749 | 0.9915 | 0.9965 |
| **filter_change** | 37 | 0.7706 | 0.6582 | 0.7809 | 0.8608 | 0.9296 |
| **intent_near_miss** | 176 | 0.7957 | 0.7161 | 0.7992 | 0.8746 | 0.9289 |
| **intent_near_miss (same wording=False)** | 176 | 0.7957 | 0.7161 | 0.7992 | 0.8746 | 0.9289 |
| **param_near_miss** | 637 | 0.8743 | 0.7222 | 0.8966 | 0.9784 | 0.9962 |
| **param_near_miss (same wording=False)** | 228 | 0.7891 | 0.6665 | 0.8013 | 0.9014 | 0.9603 |
| **param_near_miss (same wording=True)** | 409 | 0.9218 | 0.8419 | 0.9355 | 0.9825 | 0.9962 |
| **paraphrase** | 266 | 0.8539 | 0.7165 | 0.8696 | 0.9358 | 0.9729 |
| equivalent_surface/account/alias | 10 | 0.965 | 0.94 | 0.9723 | 0.9883 | 0.9897 |
| equivalent_surface/amount/alias | 10 | 0.9873 | 0.9815 | 0.9862 | 0.9934 | 0.9943 |
| equivalent_surface/category/alias | 14 | 0.9662 | 0.9274 | 0.9739 | 0.9838 | 0.9923 |
| equivalent_surface/merchant/alias | 20 | 0.9691 | 0.9384 | 0.9733 | 0.992 | 0.9943 |
| equivalent_surface/n/alias | 20 | 0.9854 | 0.9657 | 0.9914 | 0.9955 | 0.9965 |
| equivalent_surface/period/alias | 216 | 0.9424 | 0.8552 | 0.9716 | 0.989 | 0.9943 |
| filter_change/filter_added/category_spend_total | 7 | 0.8476 | 0.7886 | 0.8539 | 0.9086 | 0.9296 |
| filter_change/filter_dropped/total_spend | 30 | 0.7526 | 0.651 | 0.7593 | 0.8476 | 0.8778 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6801 | 0.6354 | 0.6735 | 0.7255 | 0.7433 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8221 | 0.7711 | 0.8256 | 0.8588 | 0.9284 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8586 | 0.8163 | 0.8522 | 0.9159 | 0.9289 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8088 | 0.7399 | 0.8047 | 0.8536 | 0.9279 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7321 | 0.6827 | 0.7322 | 0.7824 | 0.812 |
| intent_near_miss/direction/income_total | 7 | 0.7962 | 0.7598 | 0.793 | 0.8391 | 0.8551 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8317 | 0.7331 | 0.8531 | 0.8925 | 0.9212 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.771 | 0.7499 | 0.7603 | 0.7937 | 0.8355 |
| intent_near_miss/direction/total_spend | 7 | 0.7942 | 0.7542 | 0.8035 | 0.8258 | 0.8547 |
| intent_near_miss/grouping/top_categories | 10 | 0.7619 | 0.7196 | 0.7663 | 0.8268 | 0.8303 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7698 | 0.7493 | 0.7781 | 0.8076 | 0.8115 |
| intent_near_miss/measure/income_total | 7 | 0.7708 | 0.7358 | 0.7529 | 0.8222 | 0.8333 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7322 | 0.6594 | 0.7394 | 0.7913 | 0.798 |
| intent_near_miss/measure/total_spend | 7 | 0.7231 | 0.6946 | 0.7224 | 0.7562 | 0.7666 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8689 | 0.8451 | 0.8706 | 0.8846 | 0.8999 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8492 | 0.8071 | 0.8443 | 0.8954 | 0.8987 |
| param_near_miss/account/neighbor | 20 | 0.8393 | 0.7684 | 0.8424 | 0.9129 | 0.9205 |
| param_near_miss/amount/neighbor | 24 | 0.8746 | 0.6695 | 0.9404 | 0.9938 | 0.9962 |
| param_near_miss/category/neighbor | 47 | 0.8607 | 0.7544 | 0.8749 | 0.9306 | 0.9738 |
| param_near_miss/merchant/neighbor | 86 | 0.7688 | 0.6656 | 0.7804 | 0.8539 | 0.8803 |
| param_near_miss/n/neighbor | 46 | 0.9034 | 0.7756 | 0.9469 | 0.984 | 0.9874 |
| param_near_miss/period/adjacent | 225 | 0.8936 | 0.753 | 0.9272 | 0.9841 | 0.9898 |
| param_near_miss/period/granularity | 189 | 0.8994 | 0.8177 | 0.9162 | 0.9568 | 0.9816 |
| paraphrase/wording/template | 266 | 0.8539 | 0.7165 | 0.8696 | 0.9358 | 0.9729 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.125 | [0.0703, 0.1875] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.125 | [0.0703, 0.1875] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.1016 | [0.0547, 0.1562] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.03 | [0.0, 0.06] | 0.63 | [0.5398, 0.72] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3729 | [0.2881, 0.4661] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9453 | [0.9062, 0.9844] |
| B | 128 | 0.125 | [0.0703, 0.1797] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0133 | [0.006, 0.0253] | 0.0133 | 0.0133 | 0.5047 |
| raw_oracle_entry | 0.2619 | [0.2322, 0.2994] | — | — | 0.5047 |
| split_full | 0.019 | [0.0106, 0.0474] | 0.019 | 0.019 | 0.5047 |
| split_template | 0.1176 | [0.0891, 0.148] | 0.1176 | 0.1176 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much income did I receive last month? | How much income did I receive this month? | 0.9637 | How much income did I receive in the previous month? | 0.9442 |
| Which 5 merchants did I spend the most at last year? | Which 5 merchants did I spend the most at this year? | 0.9816 | Which 5 merchants did I spend the most at in the previous year? | 0.9712 |
| Income minus expenses in the last 3 months | Income minus expenses in the last 6 months | 0.9615 | Income minus expenses over the past three months | 0.9513 |
| Total spent on groceries this month | Total spent on groceries last month | 0.9833 | Total spent on grocery shopping this month | 0.9756 |
| How many times did I pay Uber last year? | How many times did I pay Uber this year? | 0.9796 | How many times did I pay Uber in the previous year? | 0.9753 |
| Count my transactions at Home Depot last month | Count my transactions at Home Depot this month | 0.9896 | Count my transactions at Home Depot in the previous month | 0.9861 |
| Show me transactions over $200 this week | Show me transactions over $100 this week | 0.9962 | Show me transactions over 200 dollars this week | 0.9932 |
| Show me transactions over $100 this week | Show me transactions over $200 this week | 0.9962 | Show me transactions over $100 so far this week | 0.9933 |
| Largest charge last month | Largest charge this month | 0.9697 | Largest charge in the previous month | 0.9673 |
| How much did I spend last month? | How much did I spend this month? | 0.9744 | How much money did I spend in total last month? | 0.9721 |
| How much did I spend on everything except subscriptions last month? | How much did I spend on everything except subscriptions this month? | 0.9869 | How much did I spend on everything except subscriptions in the previous month? | 0.9846 |
| What was my spending on subscriptions this week? | What was my spending on subscriptions last week? | 0.9852 | What was my spending on subscriptions so far this week? | 0.9831 |
| Count my transactions at Walmart last month | Count my transactions at Walmart this month | 0.9891 | Count my transactions at Walmart in the previous month | 0.9877 |
| Total refunds from Whole Foods last year | Total refunds from Whole Foods this year | 0.9843 | Total refunds from Whole Foods in the previous year | 0.983 |
| On average, how much did each purchase at Dunkin' cost last month? | On average, how much did each purchase at Dunkin' cost this month? | 0.9838 | On average, how much did each purchase at Dunkin Donuts cost last month? | 0.9828 |
