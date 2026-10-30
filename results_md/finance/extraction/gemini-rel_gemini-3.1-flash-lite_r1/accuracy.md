# Extraction: gemini-rel:gemini-3.1-flash-lite

1295 questions. Frame accuracy (every slot right): **0.9359** [0.9042, 0.9623]. Slot micro-F1 0.9827. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 39/111 (0.3514) vs included 0/111 (0.0); difference 0.3514 [0.2208, 0.4872].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1295 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| merchant | 499 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 183 | 0 | 39 | 1.0 | 0.8243 | 0.9037 |
| account | 94 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 98 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 191 | 44 | 0 | 0.8128 | 1.0 | 0.8967 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 13 | 1.0 |
| last_12_months | 26 | 1.0 |
| last_30_days | 29 | 1.0 |
| last_3_months | 160 | 1.0 |
| last_6_months | 22 | 1.0 |
| last_month | 132 | 1.0 |
| last_week | 50 | 1.0 |
| last_year | 135 | 1.0 |
| q2_2026 | 44 | 1.0 |
| q3_2026 | 171 | 1.0 |
| this_month | 175 | 1.0 |
| this_week | 187 | 1.0 |
| this_year | 151 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How much did I spend in the last 3 months excluding utilities? | `{"period": "2026-07-28/2026-10-27", "category": "utilities"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding gas? | `{"period": "2026-07-28/2026-10-27", "category": "gas"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding shopping? | `{"period": "2026-07-28/2026-10-27", "category": "shopping"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending this week, not counting subscriptions? | `{"period": "2026-10-26/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending last year, not counting subscriptions? | `{"period": "2025-01-01/2025-12-31", "category": "subscriptions"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How much did I spend last year excluding subscriptions? | `{"period": "2025-01-01/2025-12-31", "category": "subscriptions"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| What was my total spending this year, not counting subscriptions? | `{"period": "2026-01-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| What was my total spending last year, not counting utilities? | `{"period": "2025-01-01/2025-12-31", "category": "utilities"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How much did I spend last year excluding travel? | `{"period": "2025-01-01/2025-12-31", "category": "travel"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How much did I spend on everything except travel in the last 12 months? | `{"period": "2025-10-28/2026-10-27", "category": "travel"}` | `{"period": "2025-10-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in Q3 2026 excluding subscriptions? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except fuel in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "gas"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except entertainment in Q2 2026? | `{"period": "2026-04-01/2026-06-30", "category": "entertainment"}` | `{"period": "2026-04-01/2026-06-30"}` |  |
| How much did I spend in Q2 2026 excluding entertainment? | `{"period": "2026-04-01/2026-06-30", "category": "entertainment"}` | `{"period": "2026-04-01/2026-06-30"}` |  |
| How much did I spend on everything except entertainment in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except groceries in the third quarter of 2026? | `{"period": "2026-07-01/2026-09-30", "category": "groceries"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except shopping in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "shopping"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| Total spent on everything but subscriptions this week | `{"period": "2026-10-26/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total spent on everything but subscriptions last week | `{"period": "2026-10-19/2026-10-25", "category": "subscriptions"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| How much did I spend last week excluding subscriptions? | `{"period": "2026-10-19/2026-10-25", "category": "subscriptions"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| Total spent on everything but subscription services this week | `{"period": "2026-10-26/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total spent on everything but utilities this week | `{"period": "2026-10-26/2026-10-27", "category": "utilities"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending this week, not counting utilities? | `{"period": "2026-10-26/2026-10-27", "category": "utilities"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting gas? | `{"period": "2026-07-28/2026-10-27", "category": "gas"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting travel? | `{"period": "2026-07-28/2026-10-27", "category": "travel"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions last month? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending last month, not counting subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend last month excluding subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions in September 2026? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions this month? | `{"period": "2026-10-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions in August 2026? | `{"period": "2026-08-01/2026-08-31", "category": "subscriptions"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| How much did I spend on everything except subscriptions in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-09-28/2026-10-27"}` |  |
| How much did I spend on everything except subscription services last month? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending last month, not counting utilities? | `{"period": "2026-09-01/2026-09-30", "category": "utilities"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except entertainment last month? | `{"period": "2026-09-01/2026-09-30", "category": "entertainment"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending in Q2 2026, not counting shopping? | `{"period": "2026-04-01/2026-06-30", "category": "shopping"}` | `{"period": "2026-04-01/2026-06-30"}` |  |
| Show my most expensive transaction this month | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
