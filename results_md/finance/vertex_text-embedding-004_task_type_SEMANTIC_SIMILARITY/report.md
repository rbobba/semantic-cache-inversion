# vertex:text-embedding-004 task_type=SEMANTIC_SIMILARITY

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 1167 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9642 | 0.8954 | 0.9842 | 0.9961 | 0.999 |
| **equivalent_surface (same wording=True)** | 290 | 0.9642 | 0.8954 | 0.9842 | 0.9961 | 0.999 |
| **filter_change** | 37 | 0.8081 | 0.7235 | 0.8178 | 0.8885 | 0.896 |
| **intent_near_miss** | 176 | 0.8354 | 0.7611 | 0.8439 | 0.8929 | 0.9336 |
| **intent_near_miss (same wording=False)** | 176 | 0.8354 | 0.7611 | 0.8439 | 0.8929 | 0.9336 |
| **param_near_miss** | 637 | 0.9034 | 0.8033 | 0.9198 | 0.9868 | 0.9978 |
| **param_near_miss (same wording=False)** | 228 | 0.8453 | 0.7526 | 0.8458 | 0.9374 | 0.9873 |
| **param_near_miss (same wording=True)** | 409 | 0.9358 | 0.878 | 0.9384 | 0.9927 | 0.9978 |
| **paraphrase** | 266 | 0.8929 | 0.7985 | 0.8985 | 0.9658 | 0.9907 |
| equivalent_surface/account/alias | 10 | 0.9733 | 0.9545 | 0.9776 | 0.9825 | 0.9848 |
| equivalent_surface/amount/alias | 10 | 0.9931 | 0.9916 | 0.9932 | 0.9946 | 0.9951 |
| equivalent_surface/category/alias | 14 | 0.9814 | 0.9607 | 0.984 | 0.9914 | 0.996 |
| equivalent_surface/merchant/alias | 20 | 0.9927 | 0.9829 | 0.9955 | 0.9982 | 0.9987 |
| equivalent_surface/n/alias | 20 | 0.9971 | 0.9958 | 0.9966 | 0.9988 | 0.999 |
| equivalent_surface/period/alias | 216 | 0.9556 | 0.8899 | 0.9767 | 0.9935 | 0.9976 |
| filter_change/filter_added/category_spend_total | 7 | 0.8631 | 0.8201 | 0.8752 | 0.896 | 0.896 |
| filter_change/filter_dropped/total_spend | 30 | 0.7953 | 0.6927 | 0.8022 | 0.8709 | 0.8925 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7944 | 0.7423 | 0.8 | 0.8405 | 0.8661 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8676 | 0.825 | 0.8658 | 0.9133 | 0.9278 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8645 | 0.8193 | 0.8736 | 0.8906 | 0.9279 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8326 | 0.784 | 0.8311 | 0.8759 | 0.8983 |
| intent_near_miss/aggregation/total_spend | 7 | 0.792 | 0.7537 | 0.788 | 0.8299 | 0.8349 |
| intent_near_miss/direction/income_total | 7 | 0.8495 | 0.83 | 0.844 | 0.8753 | 0.8923 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8458 | 0.8113 | 0.8521 | 0.8708 | 0.9198 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7812 | 0.7423 | 0.7712 | 0.8438 | 0.8634 |
| intent_near_miss/direction/total_spend | 7 | 0.8081 | 0.7528 | 0.805 | 0.8579 | 0.8645 |
| intent_near_miss/grouping/top_categories | 10 | 0.8531 | 0.7882 | 0.8751 | 0.9031 | 0.9049 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8579 | 0.8354 | 0.8663 | 0.8856 | 0.8979 |
| intent_near_miss/measure/income_total | 7 | 0.8184 | 0.7647 | 0.7961 | 0.8784 | 0.8873 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.797 | 0.7439 | 0.7984 | 0.8701 | 0.8748 |
| intent_near_miss/measure/total_spend | 7 | 0.7637 | 0.7327 | 0.7627 | 0.8007 | 0.8121 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8666 | 0.8526 | 0.867 | 0.8903 | 0.8979 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8744 | 0.8132 | 0.8763 | 0.9253 | 0.9336 |
| param_near_miss/account/neighbor | 20 | 0.8712 | 0.7712 | 0.8819 | 0.9462 | 0.9492 |
| param_near_miss/amount/neighbor | 24 | 0.8714 | 0.7793 | 0.9199 | 0.9356 | 0.9411 |
| param_near_miss/category/neighbor | 47 | 0.8874 | 0.818 | 0.8926 | 0.9452 | 0.9829 |
| param_near_miss/merchant/neighbor | 86 | 0.8484 | 0.7636 | 0.8636 | 0.9176 | 0.9424 |
| param_near_miss/n/neighbor | 46 | 0.8923 | 0.8072 | 0.9142 | 0.95 | 0.9638 |
| param_near_miss/period/adjacent | 225 | 0.9263 | 0.8208 | 0.9525 | 0.9947 | 0.9978 |
| param_near_miss/period/granularity | 189 | 0.9154 | 0.8534 | 0.9298 | 0.961 | 0.9758 |
| paraphrase/wording/template | 266 | 0.8929 | 0.7985 | 0.8985 | 0.9658 | 0.9907 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.3906 | [0.3125, 0.4844] | 0.9531 | [0.9141, 0.9844] |
| param_near_miss | 128 | 0.3906 | [0.3125, 0.4688] | 0.9531 | [0.9141, 0.9844] |
| period_near_miss | 128 | 0.3906 | [0.3047, 0.4766] | 0.9531 | [0.9141, 0.9844] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.78 | [0.69, 0.86] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.322 | [0.2458, 0.4153] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8359 | [0.7656, 0.8984] |
| B | 128 | 0.5625 | [0.4766, 0.6406] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0094 | [0.0051, 0.0222] | 0.0094 | 0.0094 | 0.5081 |
| raw_oracle_entry | 0.1165 | [0.1056, 0.1546] | — | — | 0.5081 |
| split_full | 0.3111 | [0.2918, 0.3336] | 0.329 | 0.383 | 0.5081 |
| split_template | 0.9212 | [0.8986, 0.9438] | 0.9366 | 0.9863 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9834 | How much did I get refunded from Shell so far this year? | 0.966 |
| Largest charge last month | Largest charge this month | 0.9837 | Largest charge in the previous month | 0.9693 |
| What was my largest purchase this year? | What was my largest purchase last year? | 0.9905 | What was my largest purchase so far this year? | 0.9781 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9941 | How much money went to Chevron so far this month? | 0.9824 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9934 | What were my overall expenses so far this month? | 0.9819 |
| How much did I spend on everything except travel last year? | How much did I spend on everything except travel this year? | 0.9917 | How much did I spend on everything except travel in the previous year? | 0.9809 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9817 | How much more did I earn than I spent year to date? | 0.9712 |
| How many times did I pay Chevron this month? | How many times did I pay Chevron last month? | 0.9956 | How many times did I pay Chevron so far this month? | 0.9861 |
| How much income did I receive last month? | How much income did I receive this month? | 0.9889 | How much income did I receive in the previous month? | 0.9803 |
| How much did I spend last month? | How much did I spend this month? | 0.99 | How much did I spend in the previous month? | 0.9818 |
| Total spent at Amazon this year | Total spent at Amazon last year | 0.9891 | Total spent at Amazon.com this year | 0.9815 |
| Total spent on shopping this year | Total spent on shopping last year | 0.9807 | Total spent on shopping so far this year | 0.9736 |
| How many times did I pay Uber last year? | How many times did I pay Uber this year? | 0.9954 | How many times did I pay Uber in the previous year? | 0.9882 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9932 | How much more did I earn than I spent so far this month? | 0.9868 |
| Total refunds from Dunkin' this month | Total refunds from Dunkin' last month | 0.9958 | Total refunds from Dunkin' so far this month | 0.9899 |
