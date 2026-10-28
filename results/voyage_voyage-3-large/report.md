# voyage:voyage-3-large

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9377 | 0.8452 | 0.9655 | 0.9871 | 0.9971 |
| **equivalent_surface (same wording=True)** | 262 | 0.9377 | 0.8452 | 0.9655 | 0.9871 | 0.9971 |
| **filter_change** | 37 | 0.7752 | 0.694 | 0.7758 | 0.8704 | 0.9207 |
| **intent_near_miss** | 176 | 0.7801 | 0.6844 | 0.7814 | 0.8607 | 0.9376 |
| **intent_near_miss (same wording=False)** | 176 | 0.7801 | 0.6844 | 0.7814 | 0.8607 | 0.9376 |
| **param_near_miss** | 637 | 0.8675 | 0.7629 | 0.8797 | 0.9637 | 0.9912 |
| **param_near_miss (same wording=False)** | 228 | 0.8051 | 0.7051 | 0.8078 | 0.8929 | 0.9604 |
| **param_near_miss (same wording=True)** | 409 | 0.9022 | 0.8259 | 0.905 | 0.9752 | 0.9912 |
| **paraphrase** | 384 | 0.8723 | 0.7831 | 0.8822 | 0.947 | 0.9859 |
| equivalent_surface/account/alias | 10 | 0.9707 | 0.9371 | 0.9784 | 0.9866 | 0.9869 |
| equivalent_surface/amount/alias | 10 | 0.9823 | 0.9751 | 0.9842 | 0.9866 | 0.9919 |
| equivalent_surface/category/alias | 15 | 0.9671 | 0.9421 | 0.9779 | 0.9862 | 0.9871 |
| equivalent_surface/merchant/alias | 12 | 0.9897 | 0.9844 | 0.9899 | 0.9958 | 0.9961 |
| equivalent_surface/n/alias | 20 | 0.9885 | 0.9805 | 0.9906 | 0.9935 | 0.9971 |
| equivalent_surface/period/alias | 195 | 0.9231 | 0.8234 | 0.9591 | 0.9841 | 0.9907 |
| filter_change/filter_added/category_spend_total | 7 | 0.8221 | 0.7633 | 0.7938 | 0.9085 | 0.9207 |
| filter_change/filter_dropped/total_spend | 30 | 0.7643 | 0.6926 | 0.7613 | 0.8604 | 0.8881 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6663 | 0.616 | 0.664 | 0.72 | 0.7286 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7734 | 0.6751 | 0.7804 | 0.8281 | 0.8512 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8009 | 0.7581 | 0.8012 | 0.8553 | 0.8686 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7744 | 0.7159 | 0.7703 | 0.8653 | 0.9058 |
| intent_near_miss/aggregation/total_spend | 7 | 0.6764 | 0.6057 | 0.6875 | 0.7392 | 0.7496 |
| intent_near_miss/direction/income_total | 7 | 0.763 | 0.7072 | 0.7231 | 0.8384 | 0.8413 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8312 | 0.8011 | 0.8345 | 0.861 | 0.8791 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8231 | 0.7688 | 0.828 | 0.8715 | 0.886 |
| intent_near_miss/direction/total_spend | 7 | 0.7624 | 0.7267 | 0.758 | 0.8019 | 0.8232 |
| intent_near_miss/grouping/top_categories | 10 | 0.7964 | 0.7351 | 0.8122 | 0.8508 | 0.8685 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8088 | 0.7725 | 0.816 | 0.8435 | 0.869 |
| intent_near_miss/measure/income_total | 7 | 0.7579 | 0.7021 | 0.7632 | 0.8031 | 0.8454 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7299 | 0.6804 | 0.7258 | 0.7933 | 0.8086 |
| intent_near_miss/measure/total_spend | 7 | 0.7184 | 0.6843 | 0.7084 | 0.7633 | 0.7811 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8643 | 0.8347 | 0.854 | 0.9211 | 0.9376 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8448 | 0.7928 | 0.8518 | 0.8749 | 0.8798 |
| param_near_miss/account/neighbor | 20 | 0.8347 | 0.7352 | 0.8617 | 0.9341 | 0.9351 |
| param_near_miss/amount/neighbor | 25 | 0.8495 | 0.75 | 0.8851 | 0.9402 | 0.9487 |
| param_near_miss/category/neighbor | 45 | 0.8472 | 0.7793 | 0.8576 | 0.9065 | 0.9415 |
| param_near_miss/merchant/neighbor | 87 | 0.8183 | 0.7109 | 0.8335 | 0.9018 | 0.9272 |
| param_near_miss/n/neighbor | 45 | 0.8765 | 0.7863 | 0.8982 | 0.9471 | 0.9652 |
| param_near_miss/period/adjacent | 230 | 0.8983 | 0.7943 | 0.921 | 0.9819 | 0.9912 |
| param_near_miss/period/granularity | 185 | 0.861 | 0.7714 | 0.882 | 0.9258 | 0.954 |
| paraphrase/wording/template | 384 | 0.8723 | 0.7831 | 0.8822 | 0.947 | 0.9859 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.2969 | [0.2109, 0.3828] | 0.9531 | [0.9141, 0.9844] |
| param_near_miss | 128 | 0.2969 | [0.2188, 0.3752] | 0.9531 | [0.9139, 0.9844] |
| period_near_miss | 128 | 0.2969 | [0.2188, 0.3828] | 0.9531 | [0.9141, 0.9844] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.75 | [0.65, 0.83] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.2966 | [0.2034, 0.3814] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0114 | [0.0066, 0.0277] | 0.0114 | 0.0154 | 0.5317 |
| raw_oracle_entry | 0.1439 | [0.128, 0.1821] | — | — | 0.5317 |
| split_full | 0.2715 | [0.2552, 0.2944] | 0.3236 | 0.4228 | 0.5317 |
| split_template | 0.9951 | [0.9911, 0.9984] | 0.9951 | 0.9951 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.928 | How much more did I earn than I spent last year? | 0.8247 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9698 | How much did I spend per transaction at Walmart during 2025, on average? | 0.8988 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9462 | How much did I spend per transaction at Uber last year, on average? | 0.8812 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9557 | Total expenses last year | 0.8952 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9803 | What was my largest purchase last year? | 0.9204 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9421 | How much did I get refunded from Shell last year? | 0.8868 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9844 | How much did I get refunded from Spotify last year? | 0.9307 |
| Total money coming in last year | Total money coming in this year | 0.867 | What was my total income last year? | 0.8179 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9565 | What was my average purchase at Shell last year? | 0.9108 |
| How much did I spend on everything except gas last month? | How much did I spend on everything except gas this month? | 0.9912 | How much did I spend last month excluding gas? | 0.9562 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9615 | How much income did I receive so far this week? | 0.9312 |
| How much more did I earn than I spent last month? | How much more did I earn than I spent this month? | 0.9886 | How much more did I earn than I spent in the previous month? | 0.9619 |
| How much did I earn this year? | How much did I earn last year? | 0.9377 | How much did I earn so far this year? | 0.9125 |
| Total spent on gas last year | Total spent on gas this year | 0.9408 | Total spent on fuel last year | 0.9168 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9663 | How many transactions did I have at Starbucks last year? | 0.9447 |
