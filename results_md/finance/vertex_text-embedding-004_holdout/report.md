# vertex:text-embedding-004 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9504 | 0.8568 | 0.978 | 0.9949 | 0.9991 |
| **equivalent_surface (same wording=True)** | 290 | 0.9504 | 0.8568 | 0.978 | 0.9949 | 0.9991 |
| **filter_change** | 37 | 0.7195 | 0.6008 | 0.7336 | 0.8443 | 0.8575 |
| **intent_near_miss** | 176 | 0.7859 | 0.6904 | 0.7928 | 0.8763 | 0.9335 |
| **intent_near_miss (same wording=False)** | 176 | 0.7859 | 0.6904 | 0.7928 | 0.8763 | 0.9335 |
| **param_near_miss** | 637 | 0.8766 | 0.7457 | 0.898 | 0.9858 | 0.998 |
| **param_near_miss (same wording=False)** | 228 | 0.7976 | 0.6659 | 0.7993 | 0.9288 | 0.9874 |
| **param_near_miss (same wording=True)** | 409 | 0.9206 | 0.83 | 0.9354 | 0.9918 | 0.998 |
| **paraphrase** | 266 | 0.8561 | 0.7375 | 0.8675 | 0.9549 | 0.9908 |
| equivalent_surface/account/alias | 10 | 0.9599 | 0.9403 | 0.9654 | 0.9693 | 0.9735 |
| equivalent_surface/amount/alias | 10 | 0.9896 | 0.9872 | 0.9896 | 0.9919 | 0.9928 |
| equivalent_surface/category/alias | 14 | 0.9664 | 0.9384 | 0.9733 | 0.9868 | 0.9956 |
| equivalent_surface/merchant/alias | 20 | 0.9888 | 0.978 | 0.9933 | 0.9979 | 0.9983 |
| equivalent_surface/n/alias | 20 | 0.9958 | 0.9922 | 0.9959 | 0.9985 | 0.9991 |
| equivalent_surface/period/alias | 216 | 0.9393 | 0.8476 | 0.9708 | 0.9919 | 0.9973 |
| filter_change/filter_added/category_spend_total | 7 | 0.7982 | 0.7317 | 0.7989 | 0.857 | 0.8575 |
| filter_change/filter_dropped/total_spend | 30 | 0.7012 | 0.59 | 0.696 | 0.8278 | 0.8486 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7314 | 0.6442 | 0.7478 | 0.8021 | 0.8451 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8296 | 0.7902 | 0.8283 | 0.889 | 0.9098 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8385 | 0.7799 | 0.8581 | 0.884 | 0.8958 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7914 | 0.7371 | 0.7933 | 0.8439 | 0.8803 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7437 | 0.6775 | 0.7348 | 0.8272 | 0.8275 |
| intent_near_miss/direction/income_total | 7 | 0.7647 | 0.7243 | 0.7645 | 0.8035 | 0.8261 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7933 | 0.7231 | 0.8026 | 0.8465 | 0.8792 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7324 | 0.6731 | 0.7259 | 0.8056 | 0.8156 |
| intent_near_miss/direction/total_spend | 7 | 0.7008 | 0.6332 | 0.7131 | 0.766 | 0.7793 |
| intent_near_miss/grouping/top_categories | 10 | 0.7823 | 0.7043 | 0.8012 | 0.8578 | 0.8636 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7767 | 0.7456 | 0.7873 | 0.82 | 0.8411 |
| intent_near_miss/measure/income_total | 7 | 0.7752 | 0.7176 | 0.7693 | 0.8325 | 0.8328 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7192 | 0.6649 | 0.7266 | 0.7651 | 0.7831 |
| intent_near_miss/measure/total_spend | 7 | 0.7133 | 0.6784 | 0.706 | 0.7482 | 0.7704 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8663 | 0.8516 | 0.8639 | 0.8895 | 0.8965 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8543 | 0.788 | 0.8536 | 0.9289 | 0.9335 |
| param_near_miss/account/neighbor | 20 | 0.8194 | 0.6963 | 0.8262 | 0.9082 | 0.9241 |
| param_near_miss/amount/neighbor | 24 | 0.863 | 0.723 | 0.9405 | 0.9578 | 0.9669 |
| param_near_miss/category/neighbor | 47 | 0.8372 | 0.7476 | 0.8426 | 0.9211 | 0.9791 |
| param_near_miss/merchant/neighbor | 86 | 0.7932 | 0.6803 | 0.8112 | 0.8861 | 0.914 |
| param_near_miss/n/neighbor | 46 | 0.8983 | 0.7664 | 0.9442 | 0.9745 | 0.9809 |
| param_near_miss/period/adjacent | 225 | 0.9056 | 0.7566 | 0.9468 | 0.9943 | 0.998 |
| param_near_miss/period/granularity | 189 | 0.8923 | 0.7878 | 0.9156 | 0.961 | 0.9789 |
| paraphrase/wording/template | 266 | 0.8561 | 0.7375 | 0.8675 | 0.9549 | 0.9908 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4609 | [0.375, 0.5547] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.4609 | [0.375, 0.5469] | 0.9844 | [0.9609, 1.0] |
| period_near_miss | 128 | 0.4609 | [0.375, 0.5469] | 0.9766 | [0.9453, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.72 | [0.63, 0.81] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.2966 | [0.2203, 0.3814] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8906 | [0.8359, 0.9453] |
| B | 128 | 0.5938 | [0.5, 0.6721] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0019 | [0.0018, 0.0308] | 0.0019 | 0.0019 | 0.5047 |
| raw_oracle_entry | 0.2315 | [0.2089, 0.2793] | — | — | 0.5047 |
| split_full | 0.055 | [0.0373, 0.1071] | 0.055 | 0.0816 | 0.5047 |
| split_template | 0.2922 | [0.2495, 0.3395] | 0.2922 | 0.2922 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge last month | Largest charge this month | 0.9872 | Largest charge in the previous month | 0.9409 |
| Income minus expenses last month | Income minus expenses this month | 0.9674 | Income minus expenses in the previous month | 0.9275 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9846 | How much did I get refunded from Shell so far this year? | 0.9576 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9853 | How much more did I earn than I spent year to date? | 0.9605 |
| Income minus expenses last year | Income minus expenses this year | 0.9478 | Income minus expenses in the previous year | 0.9238 |
| How much did I spend on everything except travel last year? | How much did I spend on everything except travel this year? | 0.989 | How much did I spend on everything except travel in the previous year? | 0.967 |
| How much income did I receive last month? | How much income did I receive this month? | 0.9913 | How much income did I receive in the previous month? | 0.9703 |
| How much did I spend last month? | How much did I spend this month? | 0.9913 | How much money did I spend in total last month? | 0.9729 |
| What went out of my savings account this year? | What went out of my savings account last year? | 0.9867 | What went out of my savings this year? | 0.9688 |
| Largest charge last year | Largest charge this year | 0.9639 | Largest charge in the previous year | 0.949 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9932 | What were my overall expenses so far this month? | 0.979 |
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9816 | What went out of my checking this year? | 0.9674 |
| What did I pay Amazon in total last month? | What did I pay Amazon in total this month? | 0.9956 | What did I pay Amazon.com in total last month? | 0.9819 |
| Total spent at Amazon this year | Total spent at Amazon last year | 0.986 | Total spent at Amazon so far this year | 0.9724 |
| Average transaction amount at Home Depot last month | Average transaction amount at Home Depot this month | 0.9946 | Average transaction amount at Home Depot in the previous month | 0.9816 |
