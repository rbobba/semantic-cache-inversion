# vertex:gemini-embedding-001

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9539 | 0.8765 | 0.9804 | 0.9925 | 0.9972 |
| **equivalent_surface (same wording=True)** | 262 | 0.9539 | 0.8765 | 0.9804 | 0.9925 | 0.9972 |
| **filter_change** | 37 | 0.8093 | 0.7437 | 0.8126 | 0.8883 | 0.9424 |
| **intent_near_miss** | 176 | 0.8289 | 0.7661 | 0.8353 | 0.8874 | 0.932 |
| **intent_near_miss (same wording=False)** | 176 | 0.8289 | 0.7661 | 0.8353 | 0.8874 | 0.932 |
| **param_near_miss** | 637 | 0.9023 | 0.802 | 0.915 | 0.9834 | 0.996 |
| **param_near_miss (same wording=False)** | 228 | 0.8426 | 0.7629 | 0.8464 | 0.9248 | 0.9656 |
| **param_near_miss (same wording=True)** | 409 | 0.9355 | 0.8688 | 0.9478 | 0.9869 | 0.996 |
| **paraphrase** | 384 | 0.8886 | 0.81 | 0.8964 | 0.9522 | 0.9822 |
| equivalent_surface/account/alias | 10 | 0.9685 | 0.9274 | 0.9818 | 0.9856 | 0.9868 |
| equivalent_surface/amount/alias | 10 | 0.9884 | 0.9854 | 0.988 | 0.992 | 0.9922 |
| equivalent_surface/category/alias | 15 | 0.9703 | 0.9517 | 0.9731 | 0.984 | 0.9866 |
| equivalent_surface/merchant/alias | 12 | 0.9842 | 0.9817 | 0.986 | 0.9889 | 0.991 |
| equivalent_surface/n/alias | 20 | 0.993 | 0.9892 | 0.994 | 0.9965 | 0.9972 |
| equivalent_surface/period/alias | 195 | 0.9442 | 0.8602 | 0.972 | 0.9913 | 0.9955 |
| filter_change/filter_added/category_spend_total | 7 | 0.8471 | 0.7923 | 0.8335 | 0.924 | 0.9424 |
| filter_change/filter_dropped/total_spend | 30 | 0.8005 | 0.7258 | 0.8039 | 0.8794 | 0.903 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7758 | 0.7165 | 0.7698 | 0.8341 | 0.8347 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8429 | 0.7554 | 0.8527 | 0.8947 | 0.9221 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8562 | 0.8097 | 0.8622 | 0.8931 | 0.9222 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8412 | 0.7911 | 0.8383 | 0.8928 | 0.932 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7938 | 0.7412 | 0.7788 | 0.8713 | 0.8794 |
| intent_near_miss/direction/income_total | 7 | 0.8029 | 0.753 | 0.7693 | 0.8696 | 0.8853 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8378 | 0.8024 | 0.8444 | 0.8638 | 0.8755 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8291 | 0.8071 | 0.8382 | 0.846 | 0.8466 |
| intent_near_miss/direction/total_spend | 7 | 0.7995 | 0.7717 | 0.7965 | 0.8337 | 0.8386 |
| intent_near_miss/grouping/top_categories | 10 | 0.8249 | 0.7552 | 0.8241 | 0.8942 | 0.9118 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8473 | 0.8219 | 0.8371 | 0.8968 | 0.9054 |
| intent_near_miss/measure/income_total | 7 | 0.811 | 0.7847 | 0.819 | 0.836 | 0.8415 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.8046 | 0.7688 | 0.8063 | 0.8575 | 0.8751 |
| intent_near_miss/measure/total_spend | 7 | 0.7952 | 0.7546 | 0.8061 | 0.8257 | 0.829 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.86 | 0.8256 | 0.8634 | 0.9023 | 0.9211 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8384 | 0.8006 | 0.8237 | 0.8932 | 0.8943 |
| param_near_miss/account/neighbor | 20 | 0.8184 | 0.7606 | 0.8305 | 0.8897 | 0.9185 |
| param_near_miss/amount/neighbor | 25 | 0.9188 | 0.8335 | 0.9572 | 0.9802 | 0.996 |
| param_near_miss/category/neighbor | 45 | 0.8736 | 0.821 | 0.8772 | 0.9297 | 0.9511 |
| param_near_miss/merchant/neighbor | 87 | 0.8442 | 0.769 | 0.8562 | 0.9115 | 0.9425 |
| param_near_miss/n/neighbor | 45 | 0.9203 | 0.8186 | 0.9477 | 0.9817 | 0.9919 |
| param_near_miss/period/adjacent | 230 | 0.9221 | 0.8184 | 0.939 | 0.9894 | 0.9955 |
| param_near_miss/period/granularity | 185 | 0.9143 | 0.826 | 0.9364 | 0.9649 | 0.9839 |
| paraphrase/wording/template | 384 | 0.8886 | 0.81 | 0.8964 | 0.9522 | 0.9822 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4375 | [0.3516, 0.5234] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.4375 | [0.3516, 0.5312] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.4297 | [0.3516, 0.5156] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.79 | [0.71, 0.87] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3729 | [0.2881, 0.4576] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0024 | [0.0007, 0.0094] | 0.0024 | 0.0024 | 0.5317 |
| raw_oracle_entry | 0.1024 | [0.0899, 0.1315] | — | — | 0.5317 |
| split_full | 0.3203 | [0.2967, 0.3516] | 0.3382 | 0.3967 | 0.5317 |
| split_template | 0.9951 | [0.9911, 0.9984] | 0.9951 | 0.9951 | 0.9951 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9375 | What was left over after expenses last year? | 0.851 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9873 | On average, how much did each purchase at Uber cost last year? | 0.9084 |
| Total money coming in last year | Total money coming in this year | 0.9232 | What was my total income last year? | 0.8447 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9798 | How much money did I spend in total last year? | 0.9078 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9857 | How much money did Spotify give back to me during 2025? | 0.9147 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9785 | How much did I get refunded from Shell last year? | 0.9202 |
| What went out of my Visa card this year? | What went out of my Visa card last year? | 0.9677 | What went out of my Visa card so far this year? | 0.9125 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.9853 | Average transaction amount at Shell last year | 0.9344 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9855 | What was my largest purchase last year? | 0.9365 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.9908 | What was my average purchase at Walmart last year? | 0.954 |
| How much income did I receive this month? | How much income did I receive last month? | 0.9833 | How much income did I receive so far this month? | 0.9479 |
| How much did I earn this year? | How much did I earn last year? | 0.9728 | How much did I earn so far this year? | 0.9392 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9792 | How many transactions did I have at Starbucks last year? | 0.947 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9802 | How much more did I earn than I spent so far this year? | 0.9518 |
| What was my total spending last month? | What was my total spending this month? | 0.9836 | What was my total spending in the previous month? | 0.9578 |
