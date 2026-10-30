# st:mixedbread-ai/mxbai-embed-large-v1

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 1167 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9376 | 0.8106 | 0.9749 | 0.9911 | 0.9972 |
| **equivalent_surface (same wording=True)** | 290 | 0.9376 | 0.8106 | 0.9749 | 0.9911 | 0.9972 |
| **filter_change** | 37 | 0.7696 | 0.6855 | 0.7784 | 0.8434 | 0.8956 |
| **intent_near_miss** | 176 | 0.8286 | 0.7546 | 0.8347 | 0.8955 | 0.9297 |
| **intent_near_miss (same wording=False)** | 176 | 0.8286 | 0.7546 | 0.8347 | 0.8955 | 0.9297 |
| **param_near_miss** | 637 | 0.8696 | 0.7466 | 0.8804 | 0.9849 | 0.9957 |
| **param_near_miss (same wording=False)** | 228 | 0.8062 | 0.7097 | 0.8125 | 0.9076 | 0.981 |
| **param_near_miss (same wording=True)** | 409 | 0.905 | 0.8208 | 0.9063 | 0.9902 | 0.9957 |
| **paraphrase** | 266 | 0.8721 | 0.7738 | 0.8863 | 0.9428 | 0.9871 |
| equivalent_surface/account/alias | 10 | 0.97 | 0.965 | 0.9672 | 0.9781 | 0.979 |
| equivalent_surface/amount/alias | 10 | 0.9835 | 0.972 | 0.9864 | 0.9894 | 0.99 |
| equivalent_surface/category/alias | 14 | 0.9615 | 0.9132 | 0.9737 | 0.9827 | 0.9851 |
| equivalent_surface/merchant/alias | 20 | 0.9869 | 0.9815 | 0.9895 | 0.9949 | 0.9949 |
| equivalent_surface/n/alias | 20 | 0.9945 | 0.9912 | 0.9953 | 0.9971 | 0.9972 |
| equivalent_surface/period/alias | 216 | 0.9226 | 0.7927 | 0.9723 | 0.9853 | 0.9929 |
| filter_change/filter_added/category_spend_total | 7 | 0.8187 | 0.743 | 0.8165 | 0.8871 | 0.8956 |
| filter_change/filter_dropped/total_spend | 30 | 0.7582 | 0.6806 | 0.7561 | 0.8416 | 0.8443 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.755 | 0.729 | 0.7596 | 0.7729 | 0.7745 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.8506 | 0.7947 | 0.856 | 0.902 | 0.9066 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.8549 | 0.8032 | 0.8632 | 0.9013 | 0.9179 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.8473 | 0.8071 | 0.8428 | 0.8875 | 0.921 |
| intent_near_miss/aggregation/total_spend | 7 | 0.7395 | 0.669 | 0.7109 | 0.818 | 0.8302 |
| intent_near_miss/direction/income_total | 7 | 0.8339 | 0.8158 | 0.8281 | 0.8544 | 0.8747 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8596 | 0.8125 | 0.8514 | 0.915 | 0.9211 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8111 | 0.778 | 0.8014 | 0.8558 | 0.8795 |
| intent_near_miss/direction/total_spend | 7 | 0.81 | 0.7762 | 0.8261 | 0.8337 | 0.8397 |
| intent_near_miss/grouping/top_categories | 10 | 0.8117 | 0.7508 | 0.8299 | 0.85 | 0.8768 |
| intent_near_miss/grouping/top_merchants | 10 | 0.8416 | 0.8378 | 0.8495 | 0.8575 | 0.8619 |
| intent_near_miss/measure/income_total | 7 | 0.838 | 0.7952 | 0.8335 | 0.8858 | 0.9181 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.7724 | 0.7341 | 0.7827 | 0.8132 | 0.8189 |
| intent_near_miss/measure/total_spend | 7 | 0.7671 | 0.7506 | 0.7567 | 0.7945 | 0.7982 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.8758 | 0.8546 | 0.8776 | 0.9028 | 0.9117 |
| intent_near_miss/negation/category_spend_total | 10 | 0.8766 | 0.833 | 0.8677 | 0.9264 | 0.9297 |
| param_near_miss/account/neighbor | 20 | 0.8494 | 0.7624 | 0.8564 | 0.9248 | 0.9403 |
| param_near_miss/amount/neighbor | 24 | 0.8264 | 0.6983 | 0.8289 | 0.9497 | 0.9538 |
| param_near_miss/category/neighbor | 47 | 0.8413 | 0.7492 | 0.8518 | 0.9067 | 0.9599 |
| param_near_miss/merchant/neighbor | 86 | 0.8077 | 0.7267 | 0.8187 | 0.8881 | 0.9176 |
| param_near_miss/n/neighbor | 46 | 0.8737 | 0.7561 | 0.9021 | 0.9578 | 0.9636 |
| param_near_miss/period/adjacent | 225 | 0.9063 | 0.7596 | 0.932 | 0.9921 | 0.9957 |
| param_near_miss/period/granularity | 189 | 0.8678 | 0.7804 | 0.8916 | 0.9321 | 0.9618 |
| paraphrase/wording/template | 266 | 0.8721 | 0.7738 | 0.8863 | 0.9428 | 0.9871 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.4922 | [0.4141, 0.5781] | 0.9453 | [0.8984, 0.9844] |
| param_near_miss | 128 | 0.4922 | [0.4139, 0.5781] | 0.9453 | [0.9062, 0.9844] |
| period_near_miss | 128 | 0.4922 | [0.4062, 0.5781] | 0.9453 | [0.8984, 0.9844] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.75 | [0.67, 0.8302] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.5424 | [0.4574, 0.6356] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.8359 | [0.7734, 0.8984] |
| B | 128 | 0.6016 | [0.5156, 0.6875] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0077 | [0.0033, 0.0134] | 0.0077 | 0.0077 | 0.5081 |
| raw_oracle_entry | 0.1148 | [0.1002, 0.1487] | — | — | 0.5081 |
| split_full | 0.2554 | [0.2391, 0.2756] | 0.2708 | 0.3599 | 0.5081 |
| split_template | 0.7207 | [0.6986, 0.744] | 0.7207 | 0.9366 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| How much more did I earn than I spent this week? | How much more did I earn than I spent last week? | 0.9885 | How much more did I earn than I spent so far this week? | 0.9601 |
| What did travel cost me this week? | What did travel cost me last week? | 0.9921 | What did travel cost me so far this week? | 0.9642 |
| How much did I spend this year? | How much did I spend last year? | 0.9751 | How much money did I spend in total this year? | 0.9529 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9824 | How much more did I earn than I spent so far this month? | 0.9606 |
| What were my overall expenses this week? | What were my overall expenses last week? | 0.9927 | What were my overall expenses so far this week? | 0.972 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9896 | What were my overall expenses so far this month? | 0.969 |
| What went out of my checking account this year? | What went out of my checking account last year? | 0.9906 | What went out of my checking account year to date? | 0.9703 |
| How much money left my checking account this week? | How much money left my checking account last week? | 0.9935 | How much money left my checking account so far this week? | 0.9732 |
| How much money left my Amex card last year? | How much money left my Amex card this year? | 0.9882 | How much money left my Amex card in the previous year? | 0.9681 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.9899 | How much money went to Chevron so far this month? | 0.9703 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.977 | How much more did I earn than I spent year to date? | 0.9581 |
| How much money left my checking account this month? | How much money left my checking account last month? | 0.9912 | How much money left my checking account so far this month? | 0.9725 |
| What was my largest purchase this year? | What was my largest purchase last year? | 0.9821 | What was my largest purchase so far this year? | 0.9637 |
| What did I pay Starbucks in total this week? | What did I pay Starbucks in total last week? | 0.9957 | What did I pay Starbucks in total so far this week? | 0.9775 |
| On average, how much did each purchase at Uber cost this week? | On average, how much did each purchase at Uber cost last week? | 0.9956 | On average, how much did each purchase at Uber cost so far this week? | 0.9775 |
