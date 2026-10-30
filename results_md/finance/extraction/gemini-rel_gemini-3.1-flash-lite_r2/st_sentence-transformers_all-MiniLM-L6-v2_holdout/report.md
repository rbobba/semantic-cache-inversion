# st:sentence-transformers/all-MiniLM-L6-v2 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9307 | 0.8315 | 0.9619 | 0.9912 | 0.9962 |
| **equivalent_surface (same wording=True)** | 290 | 0.9307 | 0.8315 | 0.9619 | 0.9912 | 0.9962 |
| **filter_change** | 37 | 0.6242 | 0.4547 | 0.6163 | 0.7534 | 0.858 |
| **intent_near_miss** | 176 | 0.7287 | 0.5796 | 0.734 | 0.8654 | 0.9722 |
| **intent_near_miss (same wording=False)** | 176 | 0.7287 | 0.5796 | 0.734 | 0.8654 | 0.9722 |
| **param_near_miss** | 637 | 0.8217 | 0.6127 | 0.854 | 0.9799 | 0.9952 |
| **param_near_miss (same wording=False)** | 228 | 0.7031 | 0.5191 | 0.7034 | 0.8815 | 0.9447 |
| **param_near_miss (same wording=True)** | 409 | 0.8878 | 0.74 | 0.9204 | 0.9848 | 0.9952 |
| **paraphrase** | 266 | 0.7938 | 0.615 | 0.8241 | 0.9147 | 0.9721 |
| equivalent_surface/account/alias | 10 | 0.9004 | 0.8623 | 0.8991 | 0.9456 | 0.9482 |
| equivalent_surface/amount/alias | 10 | 0.9801 | 0.9727 | 0.9817 | 0.9867 | 0.9877 |
| equivalent_surface/category/alias | 14 | 0.9427 | 0.905 | 0.9483 | 0.9696 | 0.9735 |
| equivalent_surface/merchant/alias | 20 | 0.9527 | 0.8666 | 0.9714 | 0.9948 | 0.996 |
| equivalent_surface/n/alias | 20 | 0.9934 | 0.9887 | 0.9936 | 0.9961 | 0.9962 |
| equivalent_surface/period/alias | 216 | 0.9211 | 0.8142 | 0.946 | 0.9885 | 0.9946 |
| filter_change/filter_added/category_spend_total | 7 | 0.7129 | 0.6292 | 0.7113 | 0.7947 | 0.858 |
| filter_change/filter_dropped/total_spend | 30 | 0.6035 | 0.4471 | 0.6047 | 0.7309 | 0.7594 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5775 | 0.5276 | 0.5956 | 0.6176 | 0.6309 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7551 | 0.6316 | 0.7882 | 0.8326 | 0.8578 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7704 | 0.7222 | 0.784 | 0.8591 | 0.883 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7562 | 0.6977 | 0.7631 | 0.7995 | 0.8762 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5281 | 0.4352 | 0.5108 | 0.6301 | 0.6367 |
| intent_near_miss/direction/income_total | 7 | 0.7104 | 0.654 | 0.7133 | 0.7599 | 0.7646 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8521 | 0.7718 | 0.8637 | 0.9136 | 0.9413 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7303 | 0.6759 | 0.7171 | 0.8087 | 0.8297 |
| intent_near_miss/direction/total_spend | 7 | 0.666 | 0.6072 | 0.6512 | 0.7309 | 0.7353 |
| intent_near_miss/grouping/top_categories | 10 | 0.6571 | 0.5996 | 0.6546 | 0.7177 | 0.7667 |
| intent_near_miss/grouping/top_merchants | 10 | 0.6638 | 0.5877 | 0.6829 | 0.7422 | 0.7766 |
| intent_near_miss/measure/income_total | 7 | 0.767 | 0.6487 | 0.7382 | 0.8783 | 0.923 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6432 | 0.5488 | 0.643 | 0.7718 | 0.7965 |
| intent_near_miss/measure/total_spend | 7 | 0.5963 | 0.5678 | 0.5855 | 0.6378 | 0.647 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8827 | 0.8521 | 0.8756 | 0.9308 | 0.9392 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8831 | 0.84 | 0.8538 | 0.9674 | 0.9722 |
| param_near_miss/account/neighbor | 20 | 0.7324 | 0.5863 | 0.7528 | 0.8594 | 0.8886 |
| param_near_miss/amount/neighbor | 24 | 0.7967 | 0.5963 | 0.906 | 0.9389 | 0.9431 |
| param_near_miss/category/neighbor | 47 | 0.7552 | 0.6581 | 0.773 | 0.8431 | 0.9181 |
| param_near_miss/merchant/neighbor | 86 | 0.659 | 0.5059 | 0.6723 | 0.7864 | 0.8485 |
| param_near_miss/n/neighbor | 46 | 0.8775 | 0.7136 | 0.9572 | 0.9812 | 0.9883 |
| param_near_miss/period/adjacent | 225 | 0.8683 | 0.6331 | 0.9311 | 0.989 | 0.9952 |
| param_near_miss/period/granularity | 189 | 0.8558 | 0.7144 | 0.8817 | 0.9549 | 0.9848 |
| paraphrase/wording/template | 266 | 0.7938 | 0.615 | 0.8241 | 0.9147 | 0.9721 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5156 | [0.4297, 0.6018] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.5156 | [0.4297, 0.6016] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.5156 | [0.4219, 0.6016] | 0.9922 | [0.9766, 1.0] |
| entity_near_miss | 100 | 0.01 | [0.0, 0.03] | 0.54 | [0.44, 0.64] |
| intent_near_miss | 118 | 0.0169 | [0.0, 0.0424] | 0.4237 | [0.3305, 0.5085] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9844 | [0.9609, 1.0] |
| B | 128 | 0.625 | [0.5469, 0.7109] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0 | [0.0, 0.0151] | 0.0 | 0.0 | 0.5047 |
| raw_oracle_entry | 0.2277 | [0.2019, 0.2656] | — | — | 0.5047 |
| split_full | 0.0 | [0.0, 0.0238] | 0.0 | 0.0 | 0.5047 |
| split_template | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 1.0 |
| split_full_extracted | 0.0 | [0.0, 0.0151] | 0.0 | 0.0 | 0.4858 |
| split_template_extracted | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.9317 |
| split_template_extracted_slots | 0.0 | [0.0, 0.0] | 0.0 | 0.0 | 0.962 |
| split_template_negguard | 0.0455 | [0.0275, 0.0668] | 0.0455 | 0.0455 | 0.962 |
| split_template_guarded_goldsig | 0.962 | [0.9329, 0.9846] | 0.962 | 0.962 | 0.962 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted_slots | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_negguard | inf | 0.0 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_guarded_goldsig | 0.5 | 0.962 | 0.962 [0.9329, 0.9846] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |

Similarity as a detector of value errors (right-intent matches): AUC 0.8788 [0.7948, 0.9416], 11 with a template value wrong vs 360 right; median similarity 0.9481 vs 0.8532. 0.5 = no signal.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge in Q3 2026 | Largest charge in Q2 2026 | 0.9578 | Largest charge in the third quarter of 2026 | 0.8055 |
| Count my transactions at Target in Q3 2026 | Count my transactions at Target in Q2 2026 | 0.967 | Count my transactions at Target in the third quarter of 2026 | 0.8181 |
| Income minus expenses in Q3 2026 | Income minus expenses in Q2 2026 | 0.9665 | Income minus expenses in the third quarter of 2026 | 0.8368 |
| How much money went to Target in Q3 2026? | How much money went to Target in Q2 2026? | 0.9673 | What was my total spending at Target in Q3 2026? | 0.8953 |
| What did I pay Lyft in total in Q3 2026? | What did I pay Lyft in total in Q2 2026? | 0.9752 | What did I pay Lyft in total in the third quarter of 2026? | 0.9048 |
| What went out of my savings account in Q3 2026? | What went out of my savings account in Q2 2026? | 0.9646 | What went out of my savings in Q3 2026? | 0.9123 |
| How much money went to Home Depot in Q3 2026? | How much money went to Home Depot in Q2 2026? | 0.9697 | How much did I spend at Home Depot in Q3 2026? | 0.9268 |
| Total spent on everything but shopping in Q3 2026 | Total spent on everything but shopping in Q2 2026 | 0.9439 | What was my total spending in Q3 2026, not counting shopping? | 0.9079 |
| Total spent on shopping in Q3 2026 | Total spent on shopping in Q2 2026 | 0.9328 | How much did I spend on shopping in Q3 2026? | 0.9134 |
| What was my total spending in Q3 2026? | What was my total spending in Q2 2026? | 0.9551 | How much money did I spend in total in Q3 2026? | 0.9368 |
| Largest charge last month | Largest charge this month | 0.9634 | Largest charge in the previous month | 0.9451 |
| How much did I spend this year? | How much did I spend last year? | 0.9574 | How much did I spend so far this year? | 0.9468 |
| Total spent on gas in Q3 2026 | Total spent on gas in Q2 2026 | 0.9448 | Total spent on fuel in Q3 2026 | 0.9344 |
| Largest charge last year | Largest charge this year | 0.9675 | Largest charge in the previous year | 0.9572 |
| Average transaction amount at Home Depot last month | Average transaction amount at Home Depot this month | 0.9837 | Average transaction amount at Home Depot in the previous month | 0.9737 |
