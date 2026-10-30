# st:intfloat/e5-base-v2 prefix='query: ' holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.976 | 0.9247 | 0.9907 | 0.9973 | 0.9993 |
| **equivalent_surface (same wording=True)** | 290 | 0.976 | 0.9247 | 0.9907 | 0.9973 | 0.9993 |
| **filter_change** | 37 | 0.8964 | 0.8509 | 0.8939 | 0.9374 | 0.9565 |
| **intent_near_miss** | 176 | 0.9222 | 0.8764 | 0.9254 | 0.9549 | 0.9743 |
| **intent_near_miss (same wording=False)** | 176 | 0.9222 | 0.8764 | 0.9254 | 0.9549 | 0.9743 |
| **param_near_miss** | 637 | 0.946 | 0.8877 | 0.9538 | 0.9947 | 0.9988 |
| **param_near_miss (same wording=False)** | 228 | 0.9117 | 0.8636 | 0.9138 | 0.9598 | 0.9888 |
| **param_near_miss (same wording=True)** | 409 | 0.9651 | 0.9323 | 0.9662 | 0.9967 | 0.9988 |
| **paraphrase** | 266 | 0.9373 | 0.8843 | 0.9425 | 0.9724 | 0.9898 |
| equivalent_surface/account/alias | 10 | 0.9851 | 0.9796 | 0.9861 | 0.9899 | 0.9906 |
| equivalent_surface/amount/alias | 10 | 0.9945 | 0.9935 | 0.9945 | 0.9954 | 0.9956 |
| equivalent_surface/category/alias | 14 | 0.9878 | 0.9788 | 0.9897 | 0.9934 | 0.9939 |
| equivalent_surface/merchant/alias | 20 | 0.9921 | 0.9859 | 0.9923 | 0.9986 | 0.9991 |
| equivalent_surface/n/alias | 20 | 0.998 | 0.9962 | 0.9982 | 0.999 | 0.9993 |
| equivalent_surface/period/alias | 216 | 0.9705 | 0.9185 | 0.9883 | 0.9957 | 0.9981 |
| filter_change/filter_added/category_spend_total | 7 | 0.9279 | 0.8983 | 0.9373 | 0.9555 | 0.9565 |
| filter_change/filter_dropped/total_spend | 30 | 0.889 | 0.8485 | 0.8882 | 0.9253 | 0.9414 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.8895 | 0.8726 | 0.8946 | 0.9054 | 0.9086 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.9362 | 0.9226 | 0.937 | 0.9472 | 0.9551 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.9314 | 0.9143 | 0.9304 | 0.947 | 0.9506 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.9271 | 0.9108 | 0.9282 | 0.942 | 0.9459 |
| intent_near_miss/aggregation/total_spend | 7 | 0.8794 | 0.8377 | 0.874 | 0.9291 | 0.9321 |
| intent_near_miss/direction/income_total | 7 | 0.9434 | 0.9281 | 0.948 | 0.9577 | 0.9648 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.948 | 0.911 | 0.955 | 0.9701 | 0.9703 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.9234 | 0.9074 | 0.9185 | 0.9575 | 0.9592 |
| intent_near_miss/direction/total_spend | 7 | 0.9188 | 0.884 | 0.9139 | 0.9578 | 0.9603 |
| intent_near_miss/grouping/top_categories | 10 | 0.9037 | 0.8846 | 0.907 | 0.9247 | 0.9318 |
| intent_near_miss/grouping/top_merchants | 10 | 0.9243 | 0.9066 | 0.9261 | 0.9462 | 0.9501 |
| intent_near_miss/measure/income_total | 7 | 0.9191 | 0.8827 | 0.9091 | 0.9587 | 0.9711 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.902 | 0.8611 | 0.91 | 0.9306 | 0.9335 |
| intent_near_miss/measure/total_spend | 7 | 0.8719 | 0.8607 | 0.871 | 0.8874 | 0.8909 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.9395 | 0.9202 | 0.9288 | 0.9662 | 0.9713 |
| intent_near_miss/negation/category_spend_total | 10 | 0.9437 | 0.9241 | 0.9327 | 0.974 | 0.9743 |
| param_near_miss/account/neighbor | 20 | 0.9454 | 0.901 | 0.951 | 0.9779 | 0.978 |
| param_near_miss/amount/neighbor | 24 | 0.9245 | 0.848 | 0.9552 | 0.9741 | 0.9757 |
| param_near_miss/category/neighbor | 47 | 0.9308 | 0.8836 | 0.939 | 0.9598 | 0.9779 |
| param_near_miss/merchant/neighbor | 86 | 0.9201 | 0.8728 | 0.9301 | 0.9531 | 0.9717 |
| param_near_miss/n/neighbor | 46 | 0.9564 | 0.9076 | 0.9796 | 0.9887 | 0.9919 |
| param_near_miss/period/adjacent | 225 | 0.9567 | 0.8934 | 0.9678 | 0.9975 | 0.9988 |
| param_near_miss/period/granularity | 189 | 0.9491 | 0.9031 | 0.9601 | 0.9766 | 0.9904 |
| paraphrase/wording/template | 266 | 0.9373 | 0.8843 | 0.9425 | 0.9724 | 0.9898 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5625 | [0.4842, 0.6484] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.5625 | [0.4766, 0.6484] | 0.9844 | [0.9609, 1.0] |
| period_near_miss | 128 | 0.5625 | [0.4688, 0.6484] | 0.9844 | [0.9609, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.87 | [0.8, 0.93] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.5763 | [0.4915, 0.6695] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9219 | [0.875, 0.9688] |
| B | 128 | 0.6328 | [0.5469, 0.7188] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0038 | [0.0018, 0.0372] | 0.0038 | 0.0038 | 0.5047 |
| raw_oracle_entry | 0.2277 | [0.2004, 0.2703] | — | — | 0.5047 |
| split_full | 0.038 | [0.023, 0.0548] | 0.038 | 0.038 | 0.5047 |
| split_template | 0.167 | [0.1252, 0.2089] | 0.167 | 0.167 | 1.0 |
| split_full_extracted | 0.0361 | [0.0213, 0.0519] | 0.0361 | 0.0361 | 0.5047 |
| split_template_extracted | 0.148 | [0.1074, 0.1889] | 0.148 | 0.148 | 1.0 |
| split_template_extracted_slots | 0.148 | [0.1074, 0.1889] | 0.148 | 0.148 | 1.0 |
| split_template_negguard | 0.167 | [0.1252, 0.2089] | 0.167 | 0.167 | 1.0 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |
| split_template_fullsig | 0.9943 | [0.9875, 1.0] | 0.9943 | 0.9943 | 0.9943 |
| split_template_fullsig_gold | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9751 | 0.0361 | 0.0361 [0.0213, 0.0518] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9706 | 0.1461 | 0.1461 [0.1033, 0.1858] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9706 | 0.1461 | 0.1461 [0.1033, 0.1858] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9706 | 0.1461 | 0.1461 [0.1033, 0.1858] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_fullsig | 0.5 | 0.9943 | 0.9943 [0.9875, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_fullsig_gold | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What went out of my savings account this year? | What went out of my savings account last year? | 0.9975 | What went out of my savings account so far this year? | 0.9908 |
| How much did I spend last year? | How much did I spend this year? | 0.9942 | How much money did I spend in total last year? | 0.9876 |
| Largest charge last year | Largest charge this year | 0.9926 | Largest charge in the previous year | 0.9864 |
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9974 | What went out of my checking account so far this year? | 0.9913 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9967 | How much income did I receive so far this week? | 0.9907 |
| Total spent on groceries this month | Total spent on groceries last month | 0.9957 | Total spent on groceries so far this month | 0.9898 |
| How much did I spend this year? | How much did I spend last year? | 0.9942 | How much money did I spend in total this year? | 0.9884 |
| Total money coming in this year | Total money coming in last year | 0.9888 | Total money coming in so far this year | 0.9832 |
| What did I pay Starbucks in total this week? | What did I pay Starbucks in total last week? | 0.9981 | What did I pay Starbucks in total so far this week? | 0.9926 |
| Total money coming in this month | Total money coming in last month | 0.9917 | Total money coming in so far this month | 0.9866 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9973 | What did travel cost me so far this week? | 0.9923 |
| Income minus expenses last year | Income minus expenses this year | 0.9922 | Income minus expenses in the previous year | 0.9873 |
| How much money left my checking account this month? | How much money left my checking account last month? | 0.9977 | How much money left my checking account so far this month? | 0.993 |
| What were my overall expenses this week? | What were my overall expenses last week? | 0.9975 | What were my overall expenses so far this week? | 0.9928 |
| Total money coming in last year | Total money coming in this year | 0.9888 | Total money coming in in the previous year | 0.9843 |
