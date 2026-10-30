# openai:text-embedding-3-large holdout

Dataset sha256(pairs) `8b64ae311cc4e08c`, 128 cached questions, 527 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 290 | 0.9239 | 0.8183 | 0.956 | 0.9821 | 0.996 |
| **equivalent_surface (same wording=True)** | 290 | 0.9239 | 0.8183 | 0.956 | 0.9821 | 0.996 |
| **filter_change** | 37 | 0.646 | 0.521 | 0.6615 | 0.7574 | 0.8226 |
| **intent_near_miss** | 176 | 0.7142 | 0.561 | 0.715 | 0.8227 | 0.8938 |
| **intent_near_miss (same wording=False)** | 176 | 0.7142 | 0.561 | 0.715 | 0.8227 | 0.8938 |
| **param_near_miss** | 637 | 0.829 | 0.6434 | 0.8596 | 0.9623 | 0.9902 |
| **param_near_miss (same wording=False)** | 228 | 0.7181 | 0.5716 | 0.7188 | 0.8616 | 0.942 |
| **param_near_miss (same wording=True)** | 409 | 0.8909 | 0.7969 | 0.9044 | 0.9693 | 0.9902 |
| **paraphrase** | 266 | 0.795 | 0.6313 | 0.8182 | 0.9171 | 0.9616 |
| equivalent_surface/account/alias | 10 | 0.9669 | 0.9539 | 0.9692 | 0.9775 | 0.9787 |
| equivalent_surface/amount/alias | 10 | 0.9677 | 0.9537 | 0.9735 | 0.9772 | 0.9774 |
| equivalent_surface/category/alias | 14 | 0.9556 | 0.9274 | 0.9624 | 0.9709 | 0.9857 |
| equivalent_surface/merchant/alias | 20 | 0.9817 | 0.9749 | 0.9825 | 0.9875 | 0.9929 |
| equivalent_surface/n/alias | 20 | 0.9877 | 0.9796 | 0.9878 | 0.9948 | 0.996 |
| equivalent_surface/period/alias | 216 | 0.9066 | 0.796 | 0.9407 | 0.9716 | 0.9847 |
| filter_change/filter_added/category_spend_total | 7 | 0.7357 | 0.6427 | 0.7389 | 0.8215 | 0.8226 |
| filter_change/filter_dropped/total_spend | 30 | 0.6251 | 0.5079 | 0.6373 | 0.7373 | 0.7585 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5888 | 0.5452 | 0.58 | 0.6468 | 0.6732 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.7574 | 0.701 | 0.7681 | 0.8117 | 0.8399 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7811 | 0.7406 | 0.7699 | 0.8314 | 0.8595 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.741 | 0.6936 | 0.7319 | 0.8038 | 0.8136 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5666 | 0.4887 | 0.5619 | 0.6423 | 0.6731 |
| intent_near_miss/direction/income_total | 7 | 0.7039 | 0.6539 | 0.6965 | 0.7569 | 0.8223 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.7801 | 0.69 | 0.793 | 0.8595 | 0.8603 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.6983 | 0.6467 | 0.6908 | 0.7754 | 0.7793 |
| intent_near_miss/direction/total_spend | 7 | 0.661 | 0.5747 | 0.666 | 0.7613 | 0.8043 |
| intent_near_miss/grouping/top_categories | 10 | 0.7324 | 0.6106 | 0.7641 | 0.814 | 0.8288 |
| intent_near_miss/grouping/top_merchants | 10 | 0.7453 | 0.6926 | 0.7557 | 0.8218 | 0.8253 |
| intent_near_miss/measure/income_total | 7 | 0.6409 | 0.5553 | 0.6357 | 0.7465 | 0.7721 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6301 | 0.5558 | 0.6444 | 0.7049 | 0.7102 |
| intent_near_miss/measure/total_spend | 7 | 0.5692 | 0.5192 | 0.575 | 0.6283 | 0.6303 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.7682 | 0.6801 | 0.7704 | 0.8554 | 0.863 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7939 | 0.7006 | 0.7944 | 0.8931 | 0.8938 |
| param_near_miss/account/neighbor | 20 | 0.7905 | 0.6807 | 0.8018 | 0.8999 | 0.9175 |
| param_near_miss/amount/neighbor | 24 | 0.8043 | 0.6312 | 0.8921 | 0.9215 | 0.9295 |
| param_near_miss/category/neighbor | 47 | 0.78 | 0.6294 | 0.7897 | 0.8816 | 0.939 |
| param_near_miss/merchant/neighbor | 86 | 0.7508 | 0.6189 | 0.7773 | 0.8588 | 0.8777 |
| param_near_miss/n/neighbor | 46 | 0.8156 | 0.6234 | 0.8908 | 0.9267 | 0.9466 |
| param_near_miss/period/adjacent | 225 | 0.8565 | 0.6732 | 0.895 | 0.9742 | 0.9902 |
| param_near_miss/period/granularity | 189 | 0.8547 | 0.7151 | 0.8892 | 0.9394 | 0.9757 |
| paraphrase/wording/template | 266 | 0.795 | 0.6313 | 0.8182 | 0.9171 | 0.9616 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.3359 | [0.2578, 0.4219] | 0.9922 | [0.9766, 1.0] |
| param_near_miss | 128 | 0.3359 | [0.2578, 0.4141] | 0.9922 | [0.9766, 1.0] |
| period_near_miss | 128 | 0.3359 | [0.25, 0.4219] | 0.9922 | [0.9688, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.74 | [0.65, 0.82] |
| intent_near_miss | 118 | 0.0 | [0.0, 0.0] | 0.3814 | [0.2966, 0.4661] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9453 | [0.9062, 0.9844] |
| B | 128 | 0.5625 | [0.4766, 0.6484] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0076 | [0.0036, 0.0466] | 0.0076 | 0.0076 | 0.5047 |
| raw_oracle_entry | 0.2808 | [0.2608, 0.3257] | — | — | 0.5047 |
| split_full | 0.055 | [0.0364, 0.1088] | 0.055 | 0.1195 | 0.5047 |
| split_template | 0.6717 | [0.6206, 0.7292] | 0.6717 | 0.7533 | 1.0 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last month | Income minus expenses this month | 0.9419 | Income minus expenses in the previous month | 0.8893 |
| What were my overall expenses this month? | What were my overall expenses last month? | 0.9604 | What were my overall expenses so far this month? | 0.9213 |
| Largest charge last month | Largest charge this month | 0.9605 | Largest charge in the previous month | 0.9224 |
| How much income did I receive this week? | How much income did I receive last week? | 0.965 | How much income did I receive so far this week? | 0.9271 |
| How much more did I earn than I spent this year? | How much more did I earn than I spent last year? | 0.9648 | How much more did I earn than I spent so far this year? | 0.9274 |
| How much more did I earn than I spent this month? | How much more did I earn than I spent last month? | 0.9656 | How much more did I earn than I spent so far this month? | 0.9329 |
| How much did I get refunded from Shell this year? | How much did I get refunded from Shell last year? | 0.9856 | How much did I get refunded from Shell so far this year? | 0.9536 |
| Largest charge last year | Largest charge this year | 0.9431 | Largest charge in the previous year | 0.9128 |
| What were my overall expenses this week? | What were my overall expenses last week? | 0.9674 | What were my overall expenses so far this week? | 0.9387 |
| How much income did I receive last month? | How much income did I receive this month? | 0.9632 | How much income did I receive in the previous month? | 0.9353 |
| Count my transactions at Home Depot last month | Count my transactions at Home Depot this month | 0.9771 | Count my transactions at Home Depot in the previous month | 0.9503 |
| Income minus expenses last year | Income minus expenses this year | 0.9336 | Income minus expenses in the previous year | 0.9068 |
| How much money went to Chevron this month? | How much money went to Chevron last month? | 0.985 | How much money went to Chevron so far this month? | 0.9592 |
| Count my transactions at Walmart last month | Count my transactions at Walmart this month | 0.9766 | Count my transactions at Walmart in the previous month | 0.9514 |
| How many times did I pay Uber last year? | How many times did I pay Uber this year? | 0.956 | How many times did I pay Uber in the previous year? | 0.9313 |
