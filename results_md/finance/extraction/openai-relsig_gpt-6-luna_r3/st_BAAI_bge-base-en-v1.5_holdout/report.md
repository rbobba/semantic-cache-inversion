# st:BAAI/bge-base-en-v1.5 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9519 | 0.8692 | 0.9757 | 0.9922 | 0.9973 |
| **equivalent_surface (same wording=True)** | 290 | 0.9519 | 0.8692 | 0.9757 | 0.9922 | 0.9973 |
| **filter_change** | 37 | 0.8062 | 0.6979 | 0.813 | 0.8835 | 0.9277 |
| **intent_near_miss** | 176 | 0.8494 | 0.7789 | 0.8571 | 0.9098 | 0.9631 |
| **intent_near_miss (same wording=False)** | 176 | 0.8494 | 0.7789 | 0.8571 | 0.9098 | 0.9631 |
| **param_near_miss** | 637 | 0.8918 | 0.7892 | 0.9024 | 0.9841 | 0.9965 |
| **param_near_miss (same wording=False)** | 228 | 0.8334 | 0.7429 | 0.8352 | 0.9215 | 0.9853 |
| **param_near_miss (same wording=True)** | 409 | 0.9244 | 0.861 | 0.9233 | 0.99 | 0.9965 |
| **paraphrase** | 266 | 0.8865 | 0.8054 | 0.9026 | 0.9475 | 0.9864 |
| equivalent_surface/account/alias | 10 | 0.9659 | 0.9593 | 0.967 | 0.9702 | 0.9745 |
| equivalent_surface/amount/alias | 10 | 0.9871 | 0.983 | 0.9874 | 0.9903 | 0.9929 |
| equivalent_surface/category/alias | 14 | 0.9717 | 0.9537 | 0.9774 | 0.9819 | 0.9857 |
| equivalent_surface/merchant/alias | 20 | 0.9853 | 0.9749 | 0.9853 | 0.996 | 0.9969 |
| equivalent_surface/n/alias | 20 | 0.9948 | 0.9928 | 0.995 | 0.9965 | 0.9973 |
| equivalent_surface/period/alias | 216 | 0.9412 | 0.8588 | 0.9709 | 0.987 | 0.9925 |
| filter_change/filter_added/category_spend_total | 7 | 0.8496 | 0.7934 | 0.8379 | 0.9065 | 0.9277 |
| filter_change/filter_dropped/total_spend | 30 | 0.7961 | 0.6951 | 0.8004 | 0.8624 | 0.8856 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7715 | 0.7508 | 0.7677 | 0.7964 | 0.8032 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8544 | 0.8024 | 0.8621 | 0.8966 | 0.9081 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8698 | 0.8149 | 0.8685 | 0.9176 | 0.935 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8458 | 0.8031 | 0.8411 | 0.8821 | 0.9242 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7682 | 0.7188 | 0.7554 | 0.8321 | 0.8472 |
| intent_near_miss/direction/income_total | 7 | 0.8609 | 0.8369 | 0.8518 | 0.8933 | 0.9019 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.886 | 0.824 | 0.8979 | 0.9189 | 0.932 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8348 | 0.7898 | 0.8415 | 0.8669 | 0.8752 |
| intent_near_miss/direction/total_spend | 7 | 0.8354 | 0.8069 | 0.8397 | 0.8651 | 0.872 |
| intent_near_miss/grouping/top_categories | 10 | 0.8389 | 0.7838 | 0.8502 | 0.894 | 0.8942 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8792 | 0.8628 | 0.8838 | 0.9033 | 0.9086 |
| intent_near_miss/measure/income_total | 7 | 0.8489 | 0.8001 | 0.8557 | 0.905 | 0.9393 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.8302 | 0.7832 | 0.8394 | 0.8751 | 0.8762 |
| intent_near_miss/measure/total_spend | 7 | 0.762 | 0.7288 | 0.7721 | 0.7848 | 0.7858 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.9149 | 0.9006 | 0.9119 | 0.9385 | 0.9487 |
| intent_near_miss/negation/category_spend_total | 10 | 0.9003 | 0.8673 | 0.8847 | 0.954 | 0.9631 |
| param_near_miss/account/neighbor | 20 | 0.8586 | 0.7614 | 0.8795 | 0.9195 | 0.9315 |
| param_near_miss/amount/neighbor | 24 | 0.8554 | 0.7273 | 0.8571 | 0.9414 | 0.9508 |
| param_near_miss/category/neighbor | 47 | 0.8687 | 0.7949 | 0.878 | 0.9191 | 0.9453 |
| param_near_miss/merchant/neighbor | 86 | 0.8488 | 0.7674 | 0.8592 | 0.9154 | 0.9294 |
| param_near_miss/n/neighbor | 46 | 0.9103 | 0.8054 | 0.9406 | 0.9684 | 0.9777 |
| param_near_miss/period/adjacent | 225 | 0.9213 | 0.8073 | 0.9465 | 0.9923 | 0.9965 |
| param_near_miss/period/granularity | 189 | 0.8857 | 0.8047 | 0.9025 | 0.938 | 0.9613 |
| paraphrase/wording/template | 266 | 0.8865 | 0.8054 | 0.9026 | 0.9475 | 0.9864 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5547 | [0.4688, 0.6406] | 0.9766 | [0.9453, 1.0] |
| param_near_miss | 128 | 0.5547 | [0.4688, 0.6406] | 0.9766 | [0.9453, 1.0] |
| period_near_miss | 128 | 0.5547 | [0.4764, 0.6484] | 0.9766 | [0.9453, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.76 | [0.67, 0.83] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.5169 | [0.4322, 0.6102] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.875 | [0.8125, 0.9297] |
| B | 128 | 0.6719 | [0.5938, 0.75] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0019 | [0.0018, 0.0256] | 0.0019 | 0.0019 | 0.5047 |
| raw_oracle_entry | 0.2467 | [0.2234, 0.2805] | — | — | 0.5047 |
| split_full | 0.0152 | [0.006, 0.0378] | 0.0152 | 0.0152 | 0.5047 |
| split_template | 0.26 | [0.2175, 0.2993] | 0.26 | 0.26 | 1.0 |
| split_full_extracted | 0.0152 | [0.006, 0.0291] | 0.0152 | 0.0152 | 0.5047 |
| split_template_extracted | 0.2334 | [0.1917, 0.274] | 0.2334 | 0.2334 | 1.0 |
| split_template_extracted_slots | 0.2334 | [0.1917, 0.274] | 0.2334 | 0.2334 | 1.0 |
| split_template_negguard | 0.2334 | [0.1917, 0.274] | 0.2334 | 0.2334 | 1.0 |
| split_template_guarded | 0.6565 | [0.5939, 0.9894] | 0.981 | 0.981 | 0.981 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9535 | 0.0152 | 0.0152 [0.0058, 0.0264] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.9274 | 0.2334 | 0.2334 [0.1917, 0.274] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | 0.9274 | 0.2334 | 0.2334 [0.1917, 0.274] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | 0.9274 | 0.2334 | 0.2334 [0.1917, 0.274] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded | 0.5 | 0.9848 | 0.981 [0.9675, 0.9921] | 0.0039 [0.0, 0.0098] | 2 | 2 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9949 | What went out of my checking account so far this year? | 0.9671 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9926 | How much money went to Chevron so far this month? | 0.9676 |
| What went out of my savings account this year? | What went out of my savings account last year? | 0.9962 | What went out of my savings account so far this year? | 0.9716 |
| Total spent on everything but shopping in Q3 2026 | Total spent on everything but shopping in Q2 2026 | 0.9756 | Total spent on everything but shopping in the third quarter of 2026 | 0.9513 |
| Total money coming in this month | Total money coming in last month | 0.9797 | Total money coming in so far this month | 0.9595 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9901 | How much income did I receive so far this week? | 0.9705 |
| How much money left my Amex card this month? | How much money left my Amex card last month? | 0.9902 | How much money left my Amex card so far this month? | 0.9723 |
| How much did I spend this year? | How much did I spend last year? | 0.9822 | How much did I spend so far this year? | 0.9646 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9919 | What did travel cost me so far this week? | 0.9755 |
| What did I pay Starbucks in total this week? | What did I pay Starbucks in total last week? | 0.9946 | What did I pay Starbucks in total so far this week? | 0.979 |
| How much money left my checking account this month? | How much money left my checking account last month? | 0.9879 | How much money left my checking account so far this month? | 0.9725 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9901 | What were my overall expenses so far this month? | 0.9752 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9939 | How much did I get refunded from Shell so far this year? | 0.9796 |
| What did I pay Whole Foods in total this week? | What did I pay Whole Foods in total last week? | 0.9947 | What did I pay Whole Foods in total so far this week? | 0.9804 |
| Count my transactions at Target in Q3 2026 | Count my transactions at Target in Q2 2026 | 0.9819 | Count my transactions at Target in the third quarter of 2026 | 0.9682 |
