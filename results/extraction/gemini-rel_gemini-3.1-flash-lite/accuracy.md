# Extraction: gemini-rel:gemini-3.1-flash-lite

1358 questions. Frame accuracy (every slot right): **0.9404** [0.9086, 0.9682]. Slot micro-F1 0.9839. Questions with a span or value note: 0.

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1358 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| merchant | 506 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 193 | 0 | 39 | 1.0 | 0.8319 | 0.9082 |
| account | 110 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 206 | 42 | 0 | 0.8306 | 1.0 | 0.9075 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 14 | 1.0 |
| last_12_months | 35 | 1.0 |
| last_30_days | 27 | 1.0 |
| last_3_months | 171 | 1.0 |
| last_6_months | 20 | 1.0 |
| last_month | 136 | 1.0 |
| last_week | 42 | 1.0 |
| last_year | 174 | 1.0 |
| q2_2026 | 40 | 1.0 |
| q3_2026 | 172 | 1.0 |
| this_month | 171 | 1.0 |
| this_week | 172 | 1.0 |
| this_year | 184 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| What was my total spending in the last 3 months, not counting travel? | `{"period": "2026-07-28/2026-10-27", "category": "travel"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding travel? | `{"period": "2026-07-28/2026-10-27", "category": "travel"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except travel in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "travel"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 6 months excluding travel? | `{"period": "2026-04-28/2026-10-27", "category": "travel"}` | `{"period": "2026-04-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding gas? | `{"period": "2026-07-28/2026-10-27", "category": "gas"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting entertainment? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding entertainment? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except entertainment in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending over the past three months, not counting entertainment? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending in the last 6 months, not counting entertainment? | `{"period": "2026-04-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-04-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total spent on everything but restaurants this month | `{"period": "2026-10-01/2026-10-27", "category": "dining"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| Total spent on everything but eating out this month | `{"period": "2026-10-01/2026-10-27", "category": "dining"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions last month? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend last month excluding subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending last month, not counting subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions in September 2026? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions this month? | `{"period": "2026-10-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| What was my total spending this month, not counting subscriptions? | `{"period": "2026-10-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions in August 2026? | `{"period": "2026-08-01/2026-08-31", "category": "subscriptions"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| How much did I spend on everything except subscriptions in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-09-28/2026-10-27"}` |  |
| How much did I spend on everything except subscription services last month? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending last month, not counting utilities? | `{"period": "2026-09-01/2026-09-30", "category": "utilities"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except entertainment last month? | `{"period": "2026-09-01/2026-09-30", "category": "entertainment"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total spent on everything but dining out so far this week | `{"period": "2026-10-26/2026-10-27", "category": "dining"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How much did I spend on everything except dining out last week? | `{"period": "2026-10-19/2026-10-25", "category": "dining"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| Total spent on everything but restaurants this week | `{"period": "2026-10-26/2026-10-27", "category": "dining"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total spent on everything but eating out this week | `{"period": "2026-10-26/2026-10-27", "category": "dining"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How much did I spend this week excluding groceries? | `{"period": "2026-10-26/2026-10-27", "category": "groceries"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending this week, not counting groceries? | `{"period": "2026-10-26/2026-10-27", "category": "groceries"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How much did I spend last week excluding groceries? | `{"period": "2026-10-19/2026-10-25", "category": "groceries"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| Total spent on everything but shopping this week | `{"period": "2026-10-26/2026-10-27", "category": "shopping"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending last month, not counting gas? | `{"period": "2026-09-01/2026-09-30", "category": "gas"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend this month excluding gas? | `{"period": "2026-10-01/2026-10-27", "category": "gas"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend on everything except fuel last month? | `{"period": "2026-09-01/2026-09-30", "category": "gas"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend this year excluding entertainment? | `{"period": "2026-01-01/2026-10-27", "category": "entertainment"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How much did I spend on everything except entertainment this year? | `{"period": "2026-01-01/2026-10-27", "category": "entertainment"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total spent on everything but entertainment last year | `{"period": "2025-01-01/2025-12-31", "category": "entertainment"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| What was the biggest single thing I bought this year? | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
