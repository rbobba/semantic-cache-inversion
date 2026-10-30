# voyage:voyage-4 holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9263 | 0.7682 | 0.9733 | 0.9905 | 0.9976 |
| **equivalent_surface (same wording=True)** | 290 | 0.9263 | 0.7682 | 0.9733 | 0.9905 | 0.9976 |
| **filter_change** | 37 | 0.7124 | 0.5914 | 0.7475 | 0.7904 | 0.8521 |
| **intent_near_miss** | 176 | 0.7552 | 0.6496 | 0.7717 | 0.8428 | 0.9005 |
| **intent_near_miss (same wording=False)** | 176 | 0.7552 | 0.6496 | 0.7717 | 0.8428 | 0.9005 |
| **param_near_miss** | 637 | 0.8327 | 0.6743 | 0.8557 | 0.9567 | 0.9833 |
| **param_near_miss (same wording=False)** | 228 | 0.7445 | 0.5964 | 0.7557 | 0.8789 | 0.96 |
| **param_near_miss (same wording=True)** | 409 | 0.8819 | 0.7751 | 0.9001 | 0.9655 | 0.9833 |
| **paraphrase** | 266 | 0.8457 | 0.714 | 0.8697 | 0.9444 | 0.9808 |
| equivalent_surface/account/alias | 10 | 0.9804 | 0.9708 | 0.9815 | 0.9875 | 0.9879 |
| equivalent_surface/amount/alias | 10 | 0.9895 | 0.9868 | 0.9893 | 0.9925 | 0.9947 |
| equivalent_surface/category/alias | 14 | 0.964 | 0.9193 | 0.9786 | 0.9901 | 0.9916 |
| equivalent_surface/merchant/alias | 20 | 0.9884 | 0.982 | 0.9888 | 0.9927 | 0.9937 |
| equivalent_surface/n/alias | 20 | 0.992 | 0.9847 | 0.9943 | 0.9961 | 0.9976 |
| equivalent_surface/period/alias | 216 | 0.9065 | 0.7522 | 0.9572 | 0.987 | 0.993 |
| filter_change/filter_added/category_spend_total | 7 | 0.7657 | 0.7109 | 0.776 | 0.8098 | 0.8394 |
| filter_change/filter_dropped/total_spend | 30 | 0.7 | 0.5485 | 0.7085 | 0.7849 | 0.8521 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.6653 | 0.6329 | 0.669 | 0.698 | 0.709 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7907 | 0.7606 | 0.7865 | 0.8348 | 0.8534 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8114 | 0.7715 | 0.8012 | 0.8593 | 0.8993 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7568 | 0.7147 | 0.7683 | 0.7849 | 0.7883 |
| intent_near_miss/aggregation/total_spend | 7 | 0.6077 | 0.5296 | 0.5859 | 0.6818 | 0.694 |
| intent_near_miss/direction/income_total | 7 | 0.7368 | 0.7038 | 0.7376 | 0.7712 | 0.7748 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7959 | 0.7214 | 0.7938 | 0.8698 | 0.8826 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.7575 | 0.7349 | 0.7528 | 0.7962 | 0.811 |
| intent_near_miss/direction/total_spend | 7 | 0.7211 | 0.6861 | 0.7244 | 0.7526 | 0.7531 |
| intent_near_miss/grouping/top_categories | 10 | 0.7878 | 0.7182 | 0.803 | 0.8252 | 0.843 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7949 | 0.7791 | 0.8155 | 0.8273 | 0.8343 |
| intent_near_miss/measure/income_total | 7 | 0.73 | 0.682 | 0.7198 | 0.7853 | 0.8137 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6298 | 0.559 | 0.6422 | 0.6697 | 0.757 |
| intent_near_miss/measure/total_spend | 7 | 0.6444 | 0.61 | 0.638 | 0.6891 | 0.6919 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8481 | 0.8163 | 0.8491 | 0.8761 | 0.9005 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8345 | 0.794 | 0.822 | 0.8859 | 0.8987 |
| param_near_miss/account/neighbor | 20 | 0.8023 | 0.6603 | 0.8243 | 0.9053 | 0.9084 |
| param_near_miss/amount/neighbor | 24 | 0.745 | 0.5852 | 0.7718 | 0.8578 | 0.9027 |
| param_near_miss/category/neighbor | 47 | 0.8154 | 0.6977 | 0.8304 | 0.9083 | 0.965 |
| param_near_miss/merchant/neighbor | 86 | 0.7676 | 0.6472 | 0.7748 | 0.8645 | 0.9151 |
| param_near_miss/n/neighbor | 46 | 0.8639 | 0.725 | 0.9101 | 0.9493 | 0.963 |
| param_near_miss/period/adjacent | 225 | 0.8559 | 0.6911 | 0.8866 | 0.9718 | 0.9833 |
| param_near_miss/period/granularity | 189 | 0.8457 | 0.7035 | 0.8814 | 0.9322 | 0.9636 |
| paraphrase/wording/template | 266 | 0.8457 | 0.714 | 0.8697 | 0.9444 | 0.9808 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.0547 | [0.0232, 0.0938] | 0.9453 | [0.9062, 0.9766] |
| param_near_miss | 128 | 0.0547 | [0.0156, 0.0938] | 0.9453 | [0.8984, 0.9844] |
| period_near_miss | 128 | 0.0547 | [0.0234, 0.0938] | 0.9375 | [0.8906, 0.9766] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.73 | [0.6498, 0.81] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3136 | [0.2288, 0.3983] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.7891 | [0.7188, 0.8594] |
| B | 128 | 0.0859 | [0.0391, 0.1406] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0209 | [0.0121, 0.0594] | 0.0209 | 0.0209 | 0.5047 |
| raw_oracle_entry | 0.3397 | [0.3199, 0.3778] | — | — | 0.5047 |
| split_full | 0.1727 | [0.1447, 0.2104] | 0.1727 | 0.1803 | 0.5047 |
| split_template | 0.9203 | [0.8878, 0.9514] | 0.9203 | 0.9848 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Largest charge last month | Largest charge this month | 0.973 | Largest charge in the previous month | 0.9313 |
| Largest charge last year | Largest charge this year | 0.9249 | Largest charge in the previous year | 0.9044 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9554 | How much more did I earn than I spent so far this year? | 0.9522 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9768 | How much money went to Chevron so far this month? | 0.9757 |
| How many times did I pay Trader Joe's last month? | How many times did I pay Trader Joe's this month? | 0.9822 | How many times did I pay Trader Joes last month? | 0.9813 |
| Average transaction amount at Home Depot last month | Average transaction amount at Home Depot this month | 0.9724 | Average transaction amount at Home Depot in the previous month | 0.9716 |
| Income minus expenses last month | Income minus expenses this month | 0.9589 | Income minus expenses in the previous month | 0.9584 |
| How much did I spend on everything except subscriptions last month? | How much did I spend on everything except subscriptions this month? | 0.9825 | How much did I spend on everything except subscription services last month? | 0.9831 |
| Number of purchases at Shell this week | Number of purchases at Shell last week | 0.9771 | Number of purchases at Shell so far this week | 0.9781 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9521 | What were my overall expenses so far this month? | 0.9548 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9721 | How much more did I earn than I spent so far this month? | 0.9762 |
| Count my transactions at Walmart last month | Count my transactions at Walmart this month | 0.9696 | Count my transactions at Walmart in the previous month | 0.9742 |
| How many times did I pay Chevron this month? | How many times did I pay Chevron last month? | 0.9833 | How many times did I pay Chevron so far this month? | 0.9881 |
| How much did I get refunded from Trader Joe's this month? | How much did I get refunded from Trader Joe's last month? | 0.9817 | How much did I get refunded from Trader Joes this month? | 0.9872 |
| How much did I get refunded from Lowe's this week? | How much did I get refunded from Lowe's last week? | 0.9829 | How much did I get refunded from Lowes this week? | 0.9889 |
