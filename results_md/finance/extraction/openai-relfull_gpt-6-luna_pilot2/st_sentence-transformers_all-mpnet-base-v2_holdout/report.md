# st:sentence-transformers/all-mpnet-base-v2 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9356 | 0.8206 | 0.9694 | 0.995 | 0.9993 |
| **equivalent_surface (same wording=True)** | 290 | 0.9356 | 0.8206 | 0.9694 | 0.995 | 0.9993 |
| **filter_change** | 37 | 0.6208 | 0.4825 | 0.6351 | 0.7708 | 0.8275 |
| **intent_near_miss** | 176 | 0.7317 | 0.5869 | 0.7544 | 0.8418 | 0.9465 |
| **intent_near_miss (same wording=False)** | 176 | 0.7317 | 0.5869 | 0.7544 | 0.8418 | 0.9465 |
| **param_near_miss** | 637 | 0.8477 | 0.671 | 0.876 | 0.9844 | 0.9971 |
| **param_near_miss (same wording=False)** | 228 | 0.7385 | 0.574 | 0.7491 | 0.8917 | 0.9678 |
| **param_near_miss (same wording=True)** | 409 | 0.9086 | 0.7916 | 0.9299 | 0.9879 | 0.9971 |
| **paraphrase** | 266 | 0.798 | 0.6306 | 0.8273 | 0.9241 | 0.9759 |
| equivalent_surface/account/alias | 10 | 0.94 | 0.9248 | 0.9516 | 0.9672 | 0.9689 |
| equivalent_surface/amount/alias | 10 | 0.9846 | 0.9806 | 0.9841 | 0.9896 | 0.9903 |
| equivalent_surface/category/alias | 14 | 0.9515 | 0.9189 | 0.9512 | 0.9736 | 0.9894 |
| equivalent_surface/merchant/alias | 20 | 0.9821 | 0.9663 | 0.9868 | 0.9959 | 0.9974 |
| equivalent_surface/n/alias | 20 | 0.9971 | 0.9951 | 0.9977 | 0.999 | 0.9993 |
| equivalent_surface/period/alias | 216 | 0.9221 | 0.7833 | 0.9631 | 0.9902 | 0.9982 |
| filter_change/filter_added/category_spend_total | 7 | 0.7438 | 0.6635 | 0.7691 | 0.8077 | 0.8275 |
| filter_change/filter_dropped/total_spend | 30 | 0.5921 | 0.4793 | 0.579 | 0.7031 | 0.7743 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5317 | 0.485 | 0.5106 | 0.5854 | 0.5865 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7801 | 0.726 | 0.7916 | 0.8373 | 0.8545 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7721 | 0.6991 | 0.767 | 0.8571 | 0.8643 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7467 | 0.7075 | 0.7503 | 0.7786 | 0.8095 |
| intent_near_miss/aggregation/total_spend | 7 | 0.4857 | 0.3291 | 0.4405 | 0.6724 | 0.6875 |
| intent_near_miss/direction/income_total | 7 | 0.7801 | 0.7386 | 0.7769 | 0.8305 | 0.8409 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8146 | 0.721 | 0.8213 | 0.8915 | 0.8989 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7342 | 0.6719 | 0.7404 | 0.8229 | 0.8293 |
| intent_near_miss/direction/total_spend | 7 | 0.7135 | 0.6417 | 0.6904 | 0.7881 | 0.7921 |
| intent_near_miss/grouping/top_categories | 10 | 0.7305 | 0.6555 | 0.7611 | 0.788 | 0.7988 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7269 | 0.6982 | 0.755 | 0.7699 | 0.7711 |
| intent_near_miss/measure/income_total | 7 | 0.7076 | 0.5926 | 0.6543 | 0.8413 | 0.8547 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6888 | 0.5948 | 0.7037 | 0.7529 | 0.7775 |
| intent_near_miss/measure/total_spend | 7 | 0.6017 | 0.5734 | 0.5875 | 0.6399 | 0.6539 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.7953 | 0.7278 | 0.7917 | 0.893 | 0.9213 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8403 | 0.7418 | 0.8345 | 0.9432 | 0.9465 |
| param_near_miss/account/neighbor | 20 | 0.7603 | 0.5742 | 0.7876 | 0.8889 | 0.8937 |
| param_near_miss/amount/neighbor | 24 | 0.8316 | 0.6644 | 0.9186 | 0.9482 | 0.9549 |
| param_near_miss/category/neighbor | 47 | 0.7699 | 0.6463 | 0.7722 | 0.8866 | 0.9519 |
| param_near_miss/merchant/neighbor | 86 | 0.7662 | 0.6419 | 0.7747 | 0.8716 | 0.9163 |
| param_near_miss/n/neighbor | 46 | 0.8818 | 0.7324 | 0.948 | 0.9854 | 0.9899 |
| param_near_miss/period/adjacent | 225 | 0.8712 | 0.6618 | 0.928 | 0.9924 | 0.9971 |
| param_near_miss/period/granularity | 189 | 0.8792 | 0.7643 | 0.8996 | 0.9621 | 0.9881 |
| paraphrase/wording/template | 266 | 0.798 | 0.6306 | 0.8273 | 0.9241 | 0.9759 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5391 | [0.4531, 0.625] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5391 | [0.4531, 0.625] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5391 | [0.4531, 0.625] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.72 | [0.63, 0.8] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3898 | [0.2966, 0.4746] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9922 | [0.9766, 1.0] |
| B | 128 | 0.7266 | [0.6562, 0.7893] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0076 | [0.0018, 0.0164] | 0.0076 | 0.0076 | 0.5047 |
| raw_oracle_entry | 0.2011 | [0.1834, 0.2441] | — | — | 0.5047 |
| split_full | 0.0038 | [0.0, 0.054] | 0.0038 | 0.0038 | 0.5047 |
| split_template | 0.2941 | [0.24, 0.3471] | 0.2941 | 0.2941 | 1.0 |
| split_full_extracted | 0.0038 | [0.0, 0.0328] | 0.0038 | 0.0038 | 0.5047 |
| split_template_extracted | 0.1898 | [0.154, 0.2991] | 0.2657 | 0.3169 | 1.0 |
| split_template_extracted_slots | 0.1898 | [0.154, 0.2991] | 0.2657 | 0.3169 | 1.0 |
| split_template_negguard | 0.1898 | [0.154, 0.4482] | 0.4118 | 0.4118 | 1.0 |
| split_template_guarded_goldsig | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |
| split_template_fullsig | 0.9658 | [0.9446, 0.9824] | 0.9658 | 0.9658 | 0.9658 |
| split_template_fullsig_gold | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9701 | 0.0038 | 0.0038 [0.0, 0.0095] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.8609 | 0.3245 | 0.3169 [0.2655, 0.366] | 0.0234 [0.0055, 0.0465] | 4 | 4 | 0 | 0 |
| split_template_extracted_slots | 0.8609 | 0.3245 | 0.3169 [0.2655, 0.366] | 0.0234 [0.0055, 0.0465] | 4 | 4 | 0 | 0 |
| split_template_negguard | 0.8609 | 0.3188 | 0.3169 [0.2655, 0.366] | 0.006 [0.0, 0.0184] | 1 | 1 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_fullsig | 0.5 | 0.9658 | 0.9658 [0.9446, 0.9824] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_fullsig_gold | 0.5 | 1.0 | 1.0 [1.0, 1.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge in Q3 2026 | Largest charge in Q2 2026 | 0.9655 | Largest charge in the third quarter of 2026 | 0.8855 |
| Total money coming in this month | Total money coming in last month | 0.9413 | Total money coming in so far this month | 0.8748 |
| Total money coming in last year | Total money coming in this year | 0.9241 | Total money coming in in the previous year | 0.8773 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9822 | Average transaction amount at Uber in the previous year | 0.9415 |
| Largest charge last year | Largest charge this year | 0.976 | Largest charge in the previous year | 0.9399 |
| Largest charge last month | Largest charge this month | 0.9805 | Largest charge in the previous month | 0.945 |
| How much did I spend on everything except travel last year? | How much did I spend on everything except travel this year? | 0.9871 | How much did I spend last year excluding travel? | 0.9545 |
| How much income did I receive last month? | How much income did I receive this month? | 0.9771 | How much income did I receive in the previous month? | 0.9461 |
| Total money coming in this year | Total money coming in last year | 0.9241 | Total money coming in year to date | 0.8944 |
| Total spent on groceries this month | Total spent on groceries last month | 0.983 | Total spent on grocery shopping this month | 0.9534 |
| How many times did I pay Uber last year? | How many times did I pay Uber this year? | 0.9925 | How many times did I pay Uber in the previous year? | 0.9645 |
| Average transaction amount at Home Depot last month | Average transaction amount at Home Depot this month | 0.9825 | Average transaction amount at Home Depot in the previous month | 0.9547 |
| Count my transactions at Target in Q3 2026 | Count my transactions at Target in Q2 2026 | 0.9772 | Count my transactions at Target in the third quarter of 2026 | 0.9516 |
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9931 | What went out of my checking account so far this year? | 0.9684 |
| How much did I spend on everything except subscriptions last year? | How much did I spend on everything except subscriptions this year? | 0.9913 | How much did I spend on everything except subscription services last year? | 0.9693 |
