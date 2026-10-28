# st:sentence-transformers/all-mpnet-base-v2

Dataset sha256(pairs) `2fbf585caab5daaa`, 128 cached questions, 1230 queries, 1000 bootstrap resamples.

## A. Similarity to the cached question, by pair type

| Pair type | n | mean | p10 | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **equivalent_surface** | 262 | 0.9364 | 0.812 | 0.9718 | 0.9953 | 0.9987 |
| **equivalent_surface (same wording=True)** | 262 | 0.9364 | 0.812 | 0.9718 | 0.9953 | 0.9987 |
| **filter_change** | 37 | 0.6464 | 0.4943 | 0.6418 | 0.7894 | 0.8424 |
| **intent_near_miss** | 176 | 0.7382 | 0.5946 | 0.7599 | 0.8459 | 0.9451 |
| **intent_near_miss (same wording=False)** | 176 | 0.7382 | 0.5946 | 0.7599 | 0.8459 | 0.9451 |
| **param_near_miss** | 637 | 0.8509 | 0.6605 | 0.8767 | 0.9851 | 0.997 |
| **param_near_miss (same wording=False)** | 228 | 0.7335 | 0.5789 | 0.7508 | 0.8758 | 0.9607 |
| **param_near_miss (same wording=True)** | 409 | 0.9163 | 0.8181 | 0.9375 | 0.9902 | 0.997 |
| **paraphrase** | 384 | 0.7865 | 0.609 | 0.81 | 0.921 | 0.9747 |
| equivalent_surface/account/alias | 10 | 0.8949 | 0.7606 | 0.944 | 0.9705 | 0.9764 |
| equivalent_surface/amount/alias | 10 | 0.9823 | 0.9749 | 0.9835 | 0.9861 | 0.9896 |
| equivalent_surface/category/alias | 15 | 0.9536 | 0.9175 | 0.9588 | 0.9773 | 0.9862 |
| equivalent_surface/merchant/alias | 12 | 0.9843 | 0.9767 | 0.9869 | 0.9971 | 0.9976 |
| equivalent_surface/n/alias | 20 | 0.9971 | 0.995 | 0.9981 | 0.9985 | 0.9987 |
| equivalent_surface/period/alias | 195 | 0.9257 | 0.8011 | 0.9673 | 0.9896 | 0.9978 |
| filter_change/filter_added/category_spend_total | 7 | 0.7341 | 0.6242 | 0.7876 | 0.8278 | 0.8424 |
| filter_change/filter_dropped/total_spend | 30 | 0.6259 | 0.4867 | 0.6326 | 0.7472 | 0.7921 |
| intent_near_miss/aggregation/largest_purchase | 7 | 0.5112 | 0.3132 | 0.5386 | 0.6597 | 0.7267 |
| intent_near_miss/aggregation/merchant_avg | 20 | 0.782 | 0.7213 | 0.7751 | 0.8775 | 0.9101 |
| intent_near_miss/aggregation/merchant_spend_total | 20 | 0.7996 | 0.7527 | 0.81 | 0.8383 | 0.8829 |
| intent_near_miss/aggregation/merchant_txn_count | 20 | 0.7534 | 0.6734 | 0.7616 | 0.8653 | 0.8922 |
| intent_near_miss/aggregation/total_spend | 7 | 0.5402 | 0.4053 | 0.5282 | 0.6848 | 0.7186 |
| intent_near_miss/direction/income_total | 7 | 0.707 | 0.5998 | 0.7127 | 0.8054 | 0.8399 |
| intent_near_miss/direction/merchant_refunds | 10 | 0.8026 | 0.7307 | 0.8142 | 0.8895 | 0.9079 |
| intent_near_miss/direction/merchant_spend_total | 10 | 0.8194 | 0.753 | 0.8354 | 0.8523 | 0.8907 |
| intent_near_miss/direction/total_spend | 7 | 0.7075 | 0.6256 | 0.7207 | 0.7738 | 0.7832 |
| intent_near_miss/grouping/top_categories | 10 | 0.7345 | 0.6822 | 0.7496 | 0.7902 | 0.795 |
| intent_near_miss/grouping/top_merchants | 10 | 0.709 | 0.6501 | 0.731 | 0.7659 | 0.7674 |
| intent_near_miss/measure/income_total | 7 | 0.689 | 0.5796 | 0.6409 | 0.8131 | 0.8386 |
| intent_near_miss/measure/net_cash_flow | 14 | 0.6872 | 0.5816 | 0.7123 | 0.7838 | 0.8118 |
| intent_near_miss/measure/total_spend | 7 | 0.6823 | 0.5929 | 0.6306 | 0.8082 | 0.8457 |
| intent_near_miss/negation/category_spend_excluding | 10 | 0.823 | 0.7585 | 0.7933 | 0.9261 | 0.9451 |
| intent_near_miss/negation/category_spend_total | 10 | 0.7857 | 0.7113 | 0.7963 | 0.8417 | 0.8861 |
| param_near_miss/account/neighbor | 20 | 0.7491 | 0.5875 | 0.7988 | 0.8792 | 0.8933 |
| param_near_miss/amount/neighbor | 25 | 0.8107 | 0.5671 | 0.9266 | 0.968 | 0.9702 |
| param_near_miss/category/neighbor | 45 | 0.7961 | 0.6569 | 0.8014 | 0.8999 | 0.9753 |
| param_near_miss/merchant/neighbor | 87 | 0.7672 | 0.638 | 0.787 | 0.8764 | 0.9194 |
| param_near_miss/n/neighbor | 45 | 0.8754 | 0.6876 | 0.9594 | 0.9805 | 0.9886 |
| param_near_miss/period/adjacent | 230 | 0.8718 | 0.6949 | 0.9177 | 0.9928 | 0.997 |
| param_near_miss/period/granularity | 185 | 0.8881 | 0.792 | 0.913 | 0.9673 | 0.991 |
| paraphrase/wording/template | 384 | 0.7865 | 0.609 | 0.81 | 0.921 | 0.9747 |

## B. Inversion per cached question

Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.

| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |
|---|---:|---:|---|---:|---|
| any_negative | 128 | 0.5859 | [0.5078, 0.6719] | 1.0 | [1.0, 1.0] |
| param_near_miss | 128 | 0.5859 | [0.5078, 0.6719] | 1.0 | [1.0, 1.0] |
| period_near_miss | 128 | 0.5859 | [0.5078, 0.6641] | 1.0 | [1.0, 1.0] |
| entity_near_miss | 100 | 0.0 | [0.0, 0.0] | 0.8 | [0.72, 0.8702] |
| intent_near_miss | 118 | 0.0085 | [0.0, 0.0254] | 0.5847 | [0.4915, 0.6695] |

A: same-wording period swap ≥ best reworded correct question. B: ≥ best one-span, date-free correct rewording.

| Comparison | n | rate | 95% CI |
|---|---:|---:|---|
| A | 128 | 0.9688 | [0.9375, 0.9922] |
| B | 111 | 0.6937 | [0.6126, 0.7748] |

## C. Cache simulation — share of queries correctly reused

| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |
|---|---:|---|---:|---:|---:|
| raw_global | 0.0179 | [0.0114, 0.0265] | 0.0179 | 0.0187 | 0.5317 |
| raw_oracle_entry | 0.0659 | [0.0574, 0.0916] | — | — | 0.5317 |
| split_full | 0.2146 | [0.2008, 0.2303] | 0.2203 | 0.2829 | 0.5317 |
| split_template | 0.9618 | [0.9482, 0.9745] | 0.9618 | 0.9732 | 1.0 |
| split_full_extracted | 0.1854 | [0.1722, 0.2017] | 0.1886 | 0.2374 | 0.5154 |
| split_template_extracted | 0.0 | [0.0, 0.1005] | 0.0 | 0.1081 | 0.9341 |
| split_template_extracted_slots | 0.0 | [0.0, 0.1018] | 0.0 | 0.9358 | 0.965 |

split_* use gold parameters (oracle extraction). split_template counts a reuse as correct when the intent matches, because the template is refilled with the new parameters.

## D. Real extraction at the oracle-calibrated threshold

| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] | false reuses | wrong template only | wrong values only | both |
|---|---:|---:|---|---|---:|---:|---:|---:|
| split_full_extracted | 0.9701 | 0.1854 | 0.1854 [0.1721, 0.1993] | 0.0 [0.0, 0.0] | 0 | 0 | 0 | 0 |
| split_template_extracted | 0.937 | 0.926 | 0.8707 [0.8405, 0.8955] | 0.0597 [0.0391, 0.0849] | 68 | 0 | 68 | 0 |
| split_template_extracted_slots | 0.937 | 0.926 | 0.9008 [0.8807, 0.9198] | 0.0272 [0.0188, 0.0364] | 31 | 0 | 31 | 0 |

Similarity as a detector of value errors (right-intent matches): AUC 0.371 [0.2809, 0.4798], 38 with a template value wrong vs 1152 right; median similarity 1.0 vs 1.0. 0.5 = no signal.

## Largest inversions

| Cached | Wrong match | sim | Best correct | sim |
|---|---|---:|---|---:|
| Income minus expenses last year | Income minus expenses this year | 0.9495 | Income minus expenses during 2025 | 0.693 |
| Total money coming in last year | Total money coming in this year | 0.9241 | What was my total income last year? | 0.6996 |
| Average transaction amount at Uber last year | Average transaction amount at Uber this year | 0.9822 | Average transaction amount at Uber during 2025 | 0.8385 |
| What were my overall expenses last year? | What were my overall expenses this year? | 0.9837 | What was my total spending last year? | 0.875 |
| What was the biggest single thing I bought last year? | What was the biggest single thing I bought this year? | 0.9929 | What was my largest purchase last year? | 0.9004 |
| How much did I spend at Starbucks last year? | How much did I spend at Starbucks this year? | 0.9932 | What did I pay Starbucks in total last year? | 0.903 |
| Count my transactions at Starbucks last year | Count my transactions at Starbucks this year | 0.9755 | How many transactions did I have at Starbucks last year? | 0.8867 |
| Total refunds from Shell last year | Total refunds from Shell this year | 0.9742 | How much did I get refunded from Shell last year? | 0.8911 |
| How much did I spend per transaction at Walmart last year, on average? | How much did I spend per transaction at Walmart this year, on average? | 0.996 | How much did I spend per transaction at Walmart during 2025, on average? | 0.9152 |
| Total spent on gas last year | Total spent on gas this year | 0.9767 | Total spent on fuel last year | 0.8992 |
| On average, how much did each purchase at Shell cost last year? | On average, how much did each purchase at Shell cost this year? | 0.993 | On average, how much did each purchase at Shell cost during 2025? | 0.9386 |
| How much money did Spotify give back to me last year? | How much money did Spotify give back to me this year? | 0.9921 | How much money did Spotify give back to me during 2025? | 0.9415 |
| Total money coming in last month | Total money coming in this month | 0.9413 | Total money coming in in the previous month | 0.9049 |
| What was my total spending last month? | What was my total spending this month? | 0.9825 | What was my total spending in the previous month? | 0.953 |
| Total spent on everything but dining out this month | Total spent on everything but dining out last month | 0.9876 | Total spent on everything but eating out this month | 0.9588 |
