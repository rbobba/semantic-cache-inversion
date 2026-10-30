# openai:text-embedding-3-small

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 1167 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9315 | 0.8397 | 0.959 | 0.9821 | 0.9966 |
| **equivalent_surface (same wording=True)** | 290 | 0.9315 | 0.8397 | 0.959 | 0.9821 | 0.9966 |
| **filter_change** | 37 | 0.6528 | 0.5058 | 0.6692 | 0.7648 | 0.8578 |
| **intent_near_miss** | 176 | 0.7472 | 0.6281 | 0.7634 | 0.8416 | 0.9225 |
| **intent_near_miss (same wording=False)** | 176 | 0.7472 | 0.6281 | 0.7634 | 0.8416 | 0.9225 |
| **param_near_miss** | 637 | 0.8331 | 0.6455 | 0.8563 | 0.9713 | 0.9921 |
| **param_near_miss (same wording=False)** | 228 | 0.7224 | 0.5916 | 0.7208 | 0.8703 | 0.9314 |
| **param_near_miss (same wording=True)** | 409 | 0.8947 | 0.7791 | 0.9174 | 0.9798 | 0.9921 |
| **paraphrase** | 266 | 0.8035 | 0.6575 | 0.8247 | 0.9061 | 0.9463 |
| equivalent_surface/account/alias | 10 | 0.9588 | 0.9328 | 0.9637 | 0.9813 | 0.9826 |
| equivalent_surface/amount/alias | 10 | 0.9724 | 0.9661 | 0.9709 | 0.9822 | 0.9831 |
| equivalent_surface/category/alias | 14 | 0.9502 | 0.9172 | 0.9613 | 0.9672 | 0.9692 |
| equivalent_surface/merchant/alias | 20 | 0.9727 | 0.962 | 0.9707 | 0.984 | 0.9921 |
| equivalent_surface/n/alias | 20 | 0.9829 | 0.9691 | 0.9839 | 0.9948 | 0.9966 |
| equivalent_surface/period/alias | 216 | 0.9185 | 0.8146 | 0.9454 | 0.976 | 0.9912 |
| filter_change/filter_added/category_spend_total | 7 | 0.7349 | 0.6074 | 0.7644 | 0.826 | 0.8578 |
| filter_change/filter_dropped/total_spend | 30 | 0.6336 | 0.4931 | 0.6484 | 0.7544 | 0.7653 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6142 | 0.5492 | 0.6348 | 0.6741 | 0.6766 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7922 | 0.7366 | 0.7902 | 0.8396 | 0.8494 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8131 | 0.7736 | 0.7976 | 0.8785 | 0.8889 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7915 | 0.7372 | 0.7926 | 0.8507 | 0.8631 |
| intent_near_miss/aggregation/total_spend | 7 | 0.577 | 0.4626 | 0.565 | 0.6974 | 0.7215 |
| intent_near_miss/direction/income_total | 7 | 0.7293 | 0.6875 | 0.7228 | 0.7797 | 0.8192 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7998 | 0.7325 | 0.8069 | 0.8693 | 0.87 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7534 | 0.7118 | 0.74 | 0.8181 | 0.8256 |
| intent_near_miss/direction/total_spend | 7 | 0.6823 | 0.6162 | 0.6836 | 0.752 | 0.7553 |
| intent_near_miss/grouping/top_categories | 10 | 0.742 | 0.6866 | 0.7634 | 0.7827 | 0.7855 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7601 | 0.7238 | 0.7728 | 0.8222 | 0.8234 |
| intent_near_miss/measure/income_total | 7 | 0.699 | 0.6216 | 0.7096 | 0.7764 | 0.8205 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6472 | 0.5712 | 0.6432 | 0.7106 | 0.7628 |
| intent_near_miss/measure/total_spend | 7 | 0.6288 | 0.5834 | 0.63 | 0.6677 | 0.6766 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8249 | 0.7763 | 0.8262 | 0.8825 | 0.8832 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8194 | 0.736 | 0.8033 | 0.9139 | 0.9225 |
| param_near_miss/account/neighbor | 20 | 0.7814 | 0.6455 | 0.8056 | 0.8947 | 0.9046 |
| param_near_miss/amount/neighbor | 24 | 0.8054 | 0.6045 | 0.8943 | 0.9487 | 0.9605 |
| param_near_miss/category/neighbor | 47 | 0.7735 | 0.6169 | 0.7943 | 0.8754 | 0.9454 |
| param_near_miss/merchant/neighbor | 86 | 0.7267 | 0.6083 | 0.7473 | 0.8364 | 0.8978 |
| param_near_miss/n/neighbor | 46 | 0.8465 | 0.6616 | 0.9183 | 0.9497 | 0.9614 |
| param_near_miss/period/adjacent | 225 | 0.8665 | 0.6544 | 0.9072 | 0.9826 | 0.9921 |
| param_near_miss/period/granularity | 189 | 0.8622 | 0.7246 | 0.8955 | 0.9474 | 0.9887 |
| paraphrase/wording/template | 266 | 0.8035 | 0.6575 | 0.8247 | 0.9061 | 0.9463 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5469 | [0.4688, 0.6328] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5469 | [0.4609, 0.6328] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5469 | [0.4531, 0.6328] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.66 | [0.56, 0.75] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.5 | [0.4068, 0.5932] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9844 | [0.9609, 1.0] |
| B | 128 | 0.7109 | [0.6328, 0.7814] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0043 | [0.0016, 0.0106] | 0.0043 | 0.0043 | 0.5081 |
| raw_oracle_entry | 0.0763 | [0.0688, 0.1032] | — | — | 0.5081 |
| split_full | 0.2511 | [0.2342, 0.2685] | 0.2511 | 0.335 | 0.5081 |
| split_template | 0.6332 | [0.6113, 0.6579] | 0.6332 | 0.8166 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge in Q3 2026 | Largest charge in Q2 2026 | 0.9706 | Largest charge in the third quarter of 2026 | 0.9102 |
| How much income did I receive last month? | How much income did I receive this month? | 0.958 | How much income did I receive in the previous month? | 0.9132 |
| On average, how much did each purchase at Target cost this month? | On average, how much did each purchase at Target cost last month? | 0.9824 | On average, how much did each purchase at Target cost so far this month? | 0.9413 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9619 | What were my overall expenses so far this month? | 0.9231 |
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9649 | What went out of my checking account so far this year? | 0.9358 |
| How much money went to Lowe's this month? | How much money went to Lowe's last month? | 0.9848 | How much money went to Lowe's so far this month? | 0.9597 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9687 | How much more did I earn than I spent so far this year? | 0.9437 |
| Income minus expenses last year | Income minus expenses this year | 0.9527 | Income minus expenses in the previous year | 0.9286 |
| Income minus expenses last month | Income minus expenses this month | 0.9515 | Income minus expenses in the previous month | 0.9276 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9895 | How much money went to Chevron so far this month? | 0.9659 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9531 | How much income did I receive so far this week? | 0.93 |
| Total money coming in this month | Total money coming in last month | 0.9411 | Total money coming in so far this month | 0.9188 |
| How much did I spend last month? | How much did I spend this month? | 0.959 | How much money did I spend in total last month? | 0.9378 |
| What was my largest purchase this year? | What was my largest purchase last year? | 0.962 | What was my largest purchase so far this year? | 0.9416 |
| Total spent on everything but shopping in Q3 2026 | Total spent on everything but shopping in Q2 2026 | 0.9665 | Total spent on everything but shopping in the third quarter of 2026 | 0.9463 |
