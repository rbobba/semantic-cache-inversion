# vertex:gemini-embedding-001 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.952 | 0.8648 | 0.9779 | 0.991 | 0.9981 |
| **equivalent_surface (same wording=True)** | 290 | 0.952 | 0.8648 | 0.9779 | 0.991 | 0.9981 |
| **filter_change** | 37 | 0.8013 | 0.719 | 0.8024 | 0.8785 | 0.918 |
| **intent_near_miss** | 176 | 0.8394 | 0.7784 | 0.8412 | 0.9012 | 0.9359 |
| **intent_near_miss (same wording=False)** | 176 | 0.8394 | 0.7784 | 0.8412 | 0.9012 | 0.9359 |
| **param_near_miss** | 637 | 0.906 | 0.8077 | 0.92 | 0.9822 | 0.9954 |
| **param_near_miss (same wording=False)** | 228 | 0.8559 | 0.7685 | 0.8578 | 0.9359 | 0.9783 |
| **param_near_miss (same wording=True)** | 409 | 0.9339 | 0.8602 | 0.9476 | 0.9861 | 0.9954 |
| **paraphrase** | 266 | 0.8995 | 0.8256 | 0.908 | 0.9607 | 0.9827 |
| equivalent_surface/account/alias | 10 | 0.9766 | 0.9685 | 0.9764 | 0.9869 | 0.9872 |
| equivalent_surface/amount/alias | 10 | 0.9869 | 0.9855 | 0.9866 | 0.9879 | 0.99 |
| equivalent_surface/category/alias | 14 | 0.9692 | 0.9471 | 0.9741 | 0.9806 | 0.99 |
| equivalent_surface/merchant/alias | 20 | 0.9835 | 0.9753 | 0.9851 | 0.9892 | 0.9913 |
| equivalent_surface/n/alias | 20 | 0.9942 | 0.9909 | 0.9941 | 0.9968 | 0.9981 |
| equivalent_surface/period/alias | 216 | 0.9413 | 0.8563 | 0.9725 | 0.9895 | 0.9948 |
| filter_change/filter_added/category_spend_total | 7 | 0.8502 | 0.7867 | 0.8647 | 0.8955 | 0.918 |
| filter_change/filter_dropped/total_spend | 30 | 0.7899 | 0.7179 | 0.7854 | 0.8761 | 0.8807 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.806 | 0.7855 | 0.7968 | 0.8371 | 0.8622 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8547 | 0.8277 | 0.847 | 0.8897 | 0.9182 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8686 | 0.835 | 0.87 | 0.9041 | 0.9122 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8469 | 0.8045 | 0.8524 | 0.8845 | 0.8889 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7848 | 0.7303 | 0.772 | 0.8467 | 0.8659 |
| intent_near_miss/direction/income_total | 7 | 0.8332 | 0.7888 | 0.8346 | 0.8758 | 0.9169 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8492 | 0.8162 | 0.8389 | 0.8884 | 0.9065 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8074 | 0.7755 | 0.8059 | 0.8468 | 0.8562 |
| intent_near_miss/direction/total_spend | 7 | 0.8037 | 0.7672 | 0.7946 | 0.8543 | 0.8736 |
| intent_near_miss/grouping/top_categories | 10 | 0.8474 | 0.7853 | 0.8465 | 0.91 | 0.9194 |
| intent_near_miss/grouping/top_merchants | 10 | 0.891 | 0.8747 | 0.9003 | 0.9232 | 0.9261 |
| intent_near_miss/measure/income_total | 7 | 0.8196 | 0.7958 | 0.8196 | 0.8461 | 0.8504 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.8156 | 0.776 | 0.8152 | 0.8526 | 0.8744 |
| intent_near_miss/measure/total_spend | 7 | 0.7756 | 0.756 | 0.7666 | 0.7984 | 0.8004 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8682 | 0.8236 | 0.8659 | 0.9024 | 0.9039 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8521 | 0.7974 | 0.846 | 0.9139 | 0.9359 |
| param_near_miss/account/neighbor | 20 | 0.8278 | 0.7812 | 0.822 | 0.8856 | 0.9183 |
| param_near_miss/amount/neighbor | 24 | 0.9218 | 0.8424 | 0.9691 | 0.9762 | 0.9792 |
| param_near_miss/category/neighbor | 47 | 0.8852 | 0.8129 | 0.8834 | 0.9543 | 0.9748 |
| param_near_miss/merchant/neighbor | 86 | 0.8535 | 0.7736 | 0.8642 | 0.913 | 0.9476 |
| param_near_miss/n/neighbor | 46 | 0.9293 | 0.8312 | 0.9547 | 0.9841 | 0.9904 |
| param_near_miss/period/adjacent | 225 | 0.9255 | 0.8381 | 0.9427 | 0.9893 | 0.9954 |
| param_near_miss/period/granularity | 189 | 0.9124 | 0.8318 | 0.9341 | 0.9631 | 0.9822 |
| paraphrase/wording/template | 266 | 0.8995 | 0.8256 | 0.908 | 0.9607 | 0.9827 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.3281 | [0.2498, 0.4062] | 0.9844 | [0.9609, 1.0] |
| param_near_miss | 128 | 0.3281 | [0.2578, 0.4062] | 0.9844 | [0.9609, 1.0] |
| period_near_miss | 128 | 0.3281 | [0.2422, 0.4141] | 0.9844 | [0.9609, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.72 | [0.62, 0.8] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3051 | [0.2203, 0.3898] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8984 | [0.8438, 0.9453] |
| B | 128 | 0.4688 | [0.3828, 0.5469] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0038 | [0.0019, 0.0445] | 0.0038 | 0.0038 | 0.5047 |
| raw_oracle_entry | 0.2903 | [0.2695, 0.332] | — | — | 0.5047 |
| split_full | 0.1708 | [0.1391, 0.2411] | 0.1708 | 0.241 | 0.5047 |
| split_template | 0.9507 | [0.9266, 0.9744] | 0.9507 | 0.9848 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge last month | Largest charge this month | 0.981 | Largest charge in the previous month | 0.9421 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9802 | How much more did I earn than I spent so far this year? | 0.9518 |
| Count my transactions at Walmart last month | Count my transactions at Walmart this month | 0.9886 | Count my transactions at Walmart in the previous month | 0.9683 |
| How much income did I receive this week? | How much income did I receive last week? | 0.9841 | How much income did I receive so far this week? | 0.9652 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9862 | What were my overall expenses so far this month? | 0.9675 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9797 | What did travel cost me so far this week? | 0.9615 |
| Count my transactions at Home Depot last month | Count my transactions at Home Depot this month | 0.9884 | Count my transactions at Home Depot in the previous month | 0.9704 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9843 | How much more did I earn than I spent so far this month? | 0.9687 |
| How much more did I earn than I spent this week? | How much more did I earn than I spent last week? | 0.9873 | How much more did I earn than I spent so far this week? | 0.9746 |
| Largest charge last year | Largest charge this year | 0.9676 | Largest charge in the previous year | 0.9549 |
| Average transaction amount at Walmart this week | Average transaction amount at Walmart last week | 0.9856 | Average transaction amount at Walmart so far this week | 0.9749 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9859 | How much did I get refunded from Shell so far this year? | 0.9755 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9873 | Average transaction amount at Uber in the previous year | 0.9781 |
| What went out of my savings account this year? | What went out of my savings account last year? | 0.9842 | What went out of my savings account so far this year? | 0.9757 |
| How much did I spend on everything except subscriptions last year? | How much did I spend on everything except subscriptions this year? | 0.9844 | How much did I spend on everything except subscriptions in the previous year? | 0.9761 |
