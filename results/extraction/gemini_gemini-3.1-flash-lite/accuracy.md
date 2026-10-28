# Extraction: gemini:gemini-3.1-flash-lite

1358 questions. Frame accuracy (every slot right): **0.9345** [0.9092, 0.9573]. Slot micro-F1 0.9769. Questions with a span or value note: 0.

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1331 | 27 | 27 | 0.9801 | 0.9801 | 0.9801 |
| merchant | 506 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 214 | 0 | 18 | 1.0 | 0.9224 | 0.9596 |
| account | 110 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 206 | 45 | 0 | 0.8207 | 1.0 | 0.9015 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 14 | 1.0 |
| last_12_months | 35 | 1.0 |
| last_30_days | 27 | 0.0 |
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
| Sum of my purchases at Home Depot in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "home_depot"}` |  |
| Count my transactions at Uber in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "uber"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "uber"}` |  |
| How many transactions did I have at Walmart in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "walmart"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "walmart"}` |  |
| How many transactions did I have at Chevron in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "chevron"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "chevron"}` |  |
| How much did I spend per transaction at Uber in the last 30 days, on average? | `{"period": "2026-09-28/2026-10-27", "merchant": "uber"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "uber"}` |  |
| How much did I get refunded from Target in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "target"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "target"}` |  |
| How much money did Home Depot give back to me in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "home_depot"}` |  |
| How much did I spend on groceries in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "groceries"}` | `{"period": "2026-09-27/2026-10-27", "category": "groceries"}` |  |
| How much did I spend in Q3 2026 excluding travel? | `{"period": "2026-07-01/2026-09-30", "category": "travel"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| What was my total spending in Q3 2026, not counting travel? | `{"period": "2026-07-01/2026-09-30", "category": "travel"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| What was my total spending in the last 3 months, not counting entertainment? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except entertainment in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending in the last 6 months, not counting entertainment? | `{"period": "2026-04-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-04-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total spent on everything but dining out in the last 30 days | `{"period": "2026-09-28/2026-10-27", "category": "dining"}` | `{"period": "2026-09-27/2026-10-27", "category": "dining"}` |  |
| Total spent on everything but restaurants this month | `{"period": "2026-10-01/2026-10-27", "category": "dining"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| Total spent on everything but eating out this month | `{"period": "2026-10-01/2026-10-27", "category": "dining"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend last month excluding subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending last month, not counting subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions in September 2026? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was my total spending this month, not counting subscriptions? | `{"period": "2026-10-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How much did I spend on everything except subscriptions in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-09-27/2026-10-27", "category": "subscriptions"}` |  |
| What was my total spending last month, not counting utilities? | `{"period": "2026-09-01/2026-09-30", "category": "utilities"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total spent on everything but restaurants this week | `{"period": "2026-10-26/2026-10-27", "category": "dining"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total spent on everything but eating out this week | `{"period": "2026-10-26/2026-10-27", "category": "dining"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending this week, not counting shopping? | `{"period": "2026-10-26/2026-10-27", "category": "shopping"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending last month, not counting gas? | `{"period": "2026-09-01/2026-09-30", "category": "gas"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except gas in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "gas"}` | `{"period": "2026-09-27/2026-10-27", "category": "gas"}` |  |
| What was my total spending this year, not counting entertainment? | `{"period": "2026-01-01/2026-10-27", "category": "entertainment"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How much money left my Amex card in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "account": "amex"}` | `{"period": "2026-09-27/2026-10-27", "account": "amex"}` |  |
| How much did I spend from my checking account in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "account": "checking"}` | `{"period": "2026-09-27/2026-10-27", "account": "checking"}` |  |
| What was the biggest single thing I bought this year? | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| Largest charge last year | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| Total expenses in the last 30 days | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| What was my largest purchase this month? | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
| Largest charge in Q3 2026 | `{"period": "2026-07-01/2026-09-30"}` | `{"period": "2026-07-01/2026-09-30", "n": 1}` |  |
| What was my total spending in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| What was my largest purchase last month? | `{"period": "2026-09-01/2026-09-30"}` | `{"period": "2026-09-01/2026-09-30", "n": 1}` |  |
| Show my most expensive transaction this week | `{"period": "2026-10-26/2026-10-27"}` | `{"period": "2026-10-26/2026-10-27", "n": 1}` |  |
| Show my most expensive transaction in the last 3 months | `{"period": "2026-07-28/2026-10-27"}` | `{"period": "2026-07-28/2026-10-27", "n": 1}` |  |
