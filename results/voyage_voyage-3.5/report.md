# voyage:voyage-3.5

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.915 | 0.7895 | 0.95 | 0.9806 | 0.9948 |
| **equivalent_surface (same wording=True)** | 262 | 0.915 | 0.7895 | 0.95 | 0.9806 | 0.9948 |
| **filter_change** | 37 | 0.7118 | 0.5725 | 0.714 | 0.8312 | 0.9102 |
| **intent_near_miss** | 176 | 0.7209 | 0.6067 | 0.7278 | 0.8131 | 0.8881 |
| **intent_near_miss (same wording=False)** | 176 | 0.7209 | 0.6067 | 0.7278 | 0.8131 | 0.8881 |
| **param_near_miss** | 637 | 0.8341 | 0.6951 | 0.8505 | 0.9551 | 0.9914 |
| **param_near_miss (same wording=False)** | 228 | 0.7451 | 0.6246 | 0.7505 | 0.8487 | 0.9113 |
| **param_near_miss (same wording=True)** | 409 | 0.8838 | 0.8014 | 0.8851 | 0.9737 | 0.9914 |
| **paraphrase** | 384 | 0.8127 | 0.7006 | 0.8248 | 0.9083 | 0.9717 |
| equivalent_surface/account/alias | 10 | 0.9613 | 0.949 | 0.9647 | 0.9686 | 0.9736 |
| equivalent_surface/amount/alias | 10 | 0.968 | 0.9511 | 0.9727 | 0.9808 | 0.986 |
| equivalent_surface/category/alias | 15 | 0.9527 | 0.9154 | 0.9637 | 0.9804 | 0.981 |
| equivalent_surface/merchant/alias | 12 | 0.9753 | 0.9668 | 0.9777 | 0.9865 | 0.9939 |
| equivalent_surface/n/alias | 20 | 0.9825 | 0.9656 | 0.9841 | 0.994 | 0.9948 |
| equivalent_surface/period/alias | 195 | 0.8964 | 0.7752 | 0.9367 | 0.9739 | 0.9897 |
| filter_change/filter_added/category_spend_total | 7 | 0.7721 | 0.6563 | 0.7749 | 0.8688 | 0.9102 |
| filter_change/filter_dropped/total_spend | 30 | 0.6977 | 0.5606 | 0.7016 | 0.8016 | 0.8614 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5767 | 0.4705 | 0.5924 | 0.6661 | 0.6689 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7315 | 0.6648 | 0.7287 | 0.8136 | 0.858 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7524 | 0.6863 | 0.7571 | 0.8118 | 0.8657 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7476 | 0.6911 | 0.7408 | 0.8244 | 0.8434 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5755 | 0.5004 | 0.5455 | 0.6817 | 0.7339 |
| intent_near_miss/direction/income_total | 7 | 0.7 | 0.6171 | 0.6752 | 0.8099 | 0.8123 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7698 | 0.6958 | 0.7941 | 0.8254 | 0.838 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7416 | 0.6816 | 0.7224 | 0.7959 | 0.8277 |
| intent_near_miss/direction/total_spend | 7 | 0.7139 | 0.6178 | 0.7062 | 0.801 | 0.8274 |
| intent_near_miss/grouping/top_categories | 10 | 0.7449 | 0.6681 | 0.775 | 0.8049 | 0.8084 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7556 | 0.7041 | 0.7716 | 0.7954 | 0.8084 |
| intent_near_miss/measure/income_total | 7 | 0.717 | 0.6394 | 0.71 | 0.8069 | 0.8586 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.665 | 0.5793 | 0.6502 | 0.7614 | 0.7688 |
| intent_near_miss/measure/total_spend | 7 | 0.6591 | 0.5495 | 0.6521 | 0.772 | 0.8008 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.7789 | 0.6892 | 0.796 | 0.8653 | 0.8881 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7437 | 0.6784 | 0.7307 | 0.8088 | 0.8147 |
| param_near_miss/account/neighbor | 20 | 0.8059 | 0.6737 | 0.8508 | 0.9129 | 0.9265 |
| param_near_miss/amount/neighbor | 25 | 0.7724 | 0.6245 | 0.8184 | 0.8747 | 0.9036 |
| param_near_miss/category/neighbor | 45 | 0.8278 | 0.7484 | 0.8305 | 0.9121 | 0.9644 |
| param_near_miss/merchant/neighbor | 87 | 0.7865 | 0.6545 | 0.8113 | 0.886 | 0.9313 |
| param_near_miss/n/neighbor | 45 | 0.8378 | 0.6938 | 0.8804 | 0.9277 | 0.9581 |
| param_near_miss/period/adjacent | 230 | 0.8564 | 0.7158 | 0.861 | 0.9801 | 0.9914 |
| param_near_miss/period/granularity | 185 | 0.8409 | 0.7417 | 0.8596 | 0.9253 | 0.9776 |
| paraphrase/wording/template | 384 | 0.8127 | 0.7006 | 0.8248 | 0.9083 | 0.9717 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4453 | [0.3594, 0.5314] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.4453 | [0.3516, 0.5391] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.4453 | [0.367, 0.5312] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.02 | [0.0, 0.05] | 0.94 | [0.89, 0.98] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3729 | [0.2797, 0.4661] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0065 | [0.0024, 0.0132] | 0.0065 | 0.0065 | 0.5317 |
| raw_oracle_entry | 0.1138 | [0.0983, 0.147] | — | — | 0.5317 |
| split_full | 0.2488 | [0.2332, 0.2694] | 0.2488 | 0.3943 | 0.5317 |
| split_template | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Total money coming in last year | Total money coming in this year | 0.8992 | What was my total income last year? | 0.6936 |
| Income minus expenses last year | Income minus expenses this year | 0.9021 | Income minus expenses in 2025 | 0.726 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9291 | What were my overall expenses in 2025? | 0.7974 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9789 | What was my largest purchase last year? | 0.866 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9732 | What was my average purchase at Shell last year? | 0.8658 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.977 | How much did I spend per transaction at Walmart in 2025, on average? | 0.8698 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9786 | How much did I get refunded from Spotify last year? | 0.8752 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9654 | What did I pay Starbucks in total last year? | 0.872 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9317 | How much did I spend per transaction at Uber last year, on average? | 0.8501 |
| How much income did I receive this month? | How much income did I receive last month? | 0.9619 | How much income did I receive so far this month? | 0.9082 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9724 | How much more did I earn than I spent so far this year? | 0.9226 |
| How much did I earn this year? | How much did I earn last year? | 0.9306 | How much did I earn so far this year? | 0.8817 |
| Total money coming in last month | Total money coming in this month | 0.9426 | Total money coming in in the previous month | 0.8951 |
| How much money did Starbucks give back to me this week? | How much money did Starbucks give back to me last week? | 0.9852 | How much money did Starbucks give back to me so far this week? | 0.9389 |
| How much money did Home Depot give back to me this month? | How much money did Home Depot give back to me last month? | 0.9861 | How much money did Home Depot give back to me so far this month? | 0.9417 |
