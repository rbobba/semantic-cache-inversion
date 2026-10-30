# voyage:voyage-3-large

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 1167 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9359 | 0.8267 | 0.9652 | 0.9866 | 0.9977 |
| **equivalent_surface (same wording=True)** | 290 | 0.9359 | 0.8267 | 0.9652 | 0.9866 | 0.9977 |
| **filter_change** | 37 | 0.7604 | 0.6702 | 0.7588 | 0.8553 | 0.8672 |
| **intent_near_miss** | 176 | 0.7868 | 0.6964 | 0.7883 | 0.8606 | 0.9329 |
| **intent_near_miss (same wording=False)** | 176 | 0.7868 | 0.6964 | 0.7883 | 0.8606 | 0.9329 |
| **param_near_miss** | 637 | 0.8639 | 0.7497 | 0.8803 | 0.9621 | 0.9929 |
| **param_near_miss (same wording=False)** | 228 | 0.8065 | 0.6968 | 0.8081 | 0.9065 | 0.962 |
| **param_near_miss (same wording=True)** | 409 | 0.8959 | 0.8154 | 0.9027 | 0.9723 | 0.9929 |
| **paraphrase** | 266 | 0.8783 | 0.7912 | 0.8867 | 0.9571 | 0.9819 |
| equivalent_surface/account/alias | 10 | 0.9718 | 0.9477 | 0.9771 | 0.9856 | 0.9856 |
| equivalent_surface/amount/alias | 10 | 0.9847 | 0.9805 | 0.9859 | 0.9874 | 0.9891 |
| equivalent_surface/category/alias | 14 | 0.9617 | 0.9248 | 0.9721 | 0.9838 | 0.9909 |
| equivalent_surface/merchant/alias | 20 | 0.9843 | 0.9753 | 0.9842 | 0.9902 | 0.9918 |
| equivalent_surface/n/alias | 20 | 0.9902 | 0.9818 | 0.9918 | 0.9962 | 0.9977 |
| equivalent_surface/period/alias | 216 | 0.9208 | 0.8089 | 0.9564 | 0.98 | 0.9928 |
| filter_change/filter_added/category_spend_total | 7 | 0.8236 | 0.7646 | 0.84 | 0.8668 | 0.8672 |
| filter_change/filter_dropped/total_spend | 30 | 0.7457 | 0.6647 | 0.7446 | 0.853 | 0.8563 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.7051 | 0.6719 | 0.7056 | 0.7388 | 0.7491 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7883 | 0.7396 | 0.7861 | 0.8465 | 0.8664 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8175 | 0.7666 | 0.8226 | 0.8586 | 0.9002 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7668 | 0.7018 | 0.7816 | 0.8221 | 0.8334 |
| intent_near_miss/aggregation/total_spend | 7 | 0.6721 | 0.6286 | 0.6529 | 0.7213 | 0.7324 |
| intent_near_miss/direction/income_total | 7 | 0.7906 | 0.7488 | 0.7909 | 0.8334 | 0.8482 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8289 | 0.8031 | 0.8367 | 0.8536 | 0.8642 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7943 | 0.7513 | 0.7872 | 0.8473 | 0.8527 |
| intent_near_miss/direction/total_spend | 7 | 0.7702 | 0.699 | 0.786 | 0.8283 | 0.8284 |
| intent_near_miss/grouping/top_categories | 10 | 0.8156 | 0.7575 | 0.8133 | 0.8753 | 0.883 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8342 | 0.822 | 0.8417 | 0.8578 | 0.8729 |
| intent_near_miss/measure/income_total | 7 | 0.7871 | 0.7691 | 0.7805 | 0.8135 | 0.8255 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7269 | 0.6759 | 0.7383 | 0.7675 | 0.7959 |
| intent_near_miss/measure/total_spend | 7 | 0.7024 | 0.6657 | 0.6851 | 0.7438 | 0.7613 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8512 | 0.8039 | 0.8487 | 0.8965 | 0.9055 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8614 | 0.7904 | 0.8648 | 0.9235 | 0.9329 |
| param_near_miss/account/neighbor | 20 | 0.8439 | 0.7405 | 0.8829 | 0.9356 | 0.9428 |
| param_near_miss/amount/neighbor | 24 | 0.8422 | 0.7488 | 0.8851 | 0.9158 | 0.9401 |
| param_near_miss/category/neighbor | 47 | 0.8435 | 0.7437 | 0.8595 | 0.9133 | 0.9493 |
| param_near_miss/merchant/neighbor | 86 | 0.8072 | 0.7227 | 0.8168 | 0.8771 | 0.9238 |
| param_near_miss/n/neighbor | 46 | 0.8771 | 0.7943 | 0.9117 | 0.9473 | 0.9552 |
| param_near_miss/period/adjacent | 225 | 0.8976 | 0.7905 | 0.9228 | 0.982 | 0.9929 |
| param_near_miss/period/granularity | 189 | 0.8563 | 0.7474 | 0.8812 | 0.9225 | 0.951 |
| paraphrase/wording/template | 266 | 0.8783 | 0.7912 | 0.8867 | 0.9571 | 0.9819 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.2969 | [0.2188, 0.375] | 0.9141 | [0.8594, 0.9533] |
| param_near_miss | 128 | 0.2969 | [0.2266, 0.375] | 0.9141 | [0.8594, 0.9609] |
| period_near_miss | 128 | 0.2969 | [0.2109, 0.3828] | 0.9062 | [0.8516, 0.9531] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.63 | [0.53, 0.72] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.2881 | [0.2034, 0.3729] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.7812 | [0.7031, 0.8516] |
| B | 128 | 0.3984 | [0.3125, 0.4766] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0077 | [0.0034, 0.0225] | 0.0077 | 0.0077 | 0.5081 |
| raw_oracle_entry | 0.162 | [0.1478, 0.2014] | — | — | 0.5081 |
| split_full | 0.3059 | [0.2865, 0.3568] | 0.3882 | 0.4387 | 0.5081 |
| split_template | 1.0 | [1.0, 1.0] | 1.0 | 1.0 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge in Q3 2026 | Largest charge in Q2 2026 | 0.9689 | Largest charge in the third quarter of 2026 | 0.9272 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9617 | How much income did I receive so far this week? | 0.9314 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9886 | How much more did I earn than I spent so far this month? | 0.9675 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9868 | How much did I get refunded from Shell so far this year? | 0.9659 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9832 | What did travel cost me so far this week? | 0.9639 |
| How many times did I pay Uber last year? | How many times did I pay Uber this year? | 0.9837 | How many times did I pay Uber in the previous year? | 0.9647 |
| How much did I spend on everything except travel last year? | How much did I spend on everything except travel this year? | 0.9821 | How much did I spend last year excluding travel? | 0.9663 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9779 | How much more did I earn than I spent so far this year? | 0.9623 |
| How much more did I earn than I spent this week? | How much more did I earn than I spent last week? | 0.986 | How much more did I earn than I spent so far this week? | 0.9704 |
| Income minus expenses last month | Income minus expenses this month | 0.9552 | Income minus expenses in the previous month | 0.9404 |
| Income minus expenses in Q3 2026 | Income minus expenses in Q2 2026 | 0.9383 | Income minus expenses in the third quarter of 2026 | 0.9238 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.986 | How much money went to Chevron so far this month? | 0.9721 |
| What were my overall expenses this week? | What were my overall expenses last week? | 0.9624 | What were my overall expenses so far this week? | 0.9485 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9599 | What were my overall expenses so far this month? | 0.9466 |
| Count my transactions at Target in Q3 2026 | Count my transactions at Target in Q2 2026 | 0.9623 | Count my transactions at Target in the third quarter of 2026 | 0.949 |
