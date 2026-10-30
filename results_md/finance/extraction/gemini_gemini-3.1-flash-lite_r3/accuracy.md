# Extraction: gemini:gemini-3.1-flash-lite

1295 questions. Frame accuracy (every slot right): **0.9266** [0.8978, 0.9508]. Slot micro-F1 0.9737. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 22/111 (0.1982) vs included 0/111 (0.0); difference 0.1982 [0.1299, 0.2875].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1266 | 29 | 29 | 0.9776 | 0.9776 | 0.9776 |
| merchant | 499 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 200 | 0 | 22 | 1.0 | 0.9009 | 0.9479 |
| account | 94 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 98 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 191 | 47 | 0 | 0.8025 | 1.0 | 0.8904 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 13 | 1.0 |
| last_12_months | 26 | 1.0 |
| last_30_days | 29 | 0.0 |
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
| What did I pay Amazon in total in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "amazon"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "amazon"}` |  |
| How much money went to Lowe's in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "lowes"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "lowes"}` |  |
| How much money went to Chevron in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "chevron"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "chevron"}` |  |
| Total spent at Trader Joe's in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "trader_joes"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "trader_joes"}` |  |
| How many times did I pay Chevron in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "chevron"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "chevron"}` |  |
| Count my transactions at Home Depot in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "home_depot"}` |  |
| Count my transactions at Walmart in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "walmart"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "walmart"}` |  |
| How many times did I pay Trader Joe's in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "trader_joes"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "trader_joes"}` |  |
| Average transaction amount at Home Depot in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "home_depot"}` |  |
| On average, how much did each purchase at Dunkin' cost in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "dunkin"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "dunkin"}` |  |
| On average, how much did each purchase at Target cost in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "target"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "target"}` |  |
| Total refunds from Dunkin' in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "dunkin"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "dunkin"}` |  |
| How much did I get refunded from Trader Joe's in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "merchant": "trader_joes"}` | `{"period": "2026-09-27/2026-10-27", "merchant": "trader_joes"}` |  |
| What was my total spending in Q3 2026, not counting shopping? | `{"period": "2026-07-01/2026-09-30", "category": "shopping"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| Total spent on groceries in the last 30 days | `{"period": "2026-09-28/2026-10-27", "category": "groceries"}` | `{"period": "2026-09-27/2026-10-27", "category": "groceries"}` |  |
| What was my total spending this week, not counting subscriptions? | `{"period": "2026-10-26/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending last year, not counting subscriptions? | `{"period": "2025-01-01/2025-12-31", "category": "subscriptions"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| What was my total spending this year, not counting subscriptions? | `{"period": "2026-01-01/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| What was my total spending last year, not counting utilities? | `{"period": "2025-01-01/2025-12-31", "category": "utilities"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How much did I spend on everything except travel in the last 12 months? | `{"period": "2025-10-28/2026-10-27", "category": "travel"}` | `{"period": "2025-10-28/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend in the last 3 months excluding subscriptions? | `{"period": "2026-07-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total spent on everything but subscriptions in Q3 2026 | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend in Q3 2026 excluding subscriptions? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| Total spent on everything but entertainment in the last 3 months | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How much did I spend on everything except fuel in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "gas"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except entertainment in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "entertainment"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending in Q3 2026, not counting subscriptions? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend on everything except grocery shopping in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "groceries"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| Total spent on everything but subscription services this week | `{"period": "2026-10-26/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending this week, not counting utilities? | `{"period": "2026-10-26/2026-10-27", "category": "utilities"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| What was my total spending in the last 3 months, not counting gas? | `{"period": "2026-07-28/2026-10-27", "category": "gas"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total spent on everything but fuel in the last 3 months | `{"period": "2026-07-28/2026-10-27", "category": "gas"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was my total spending last month, not counting subscriptions? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions in September 2026? | `{"period": "2026-09-01/2026-09-30", "category": "subscriptions"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How much did I spend on everything except subscriptions in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "category": "subscriptions"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| How much money left my checking account in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "account": "checking"}` | `{"period": "2026-09-27/2026-10-27", "account": "checking"}` |  |
| How much money left my Amex card in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "account": "amex"}` | `{"period": "2026-09-27/2026-10-27", "account": "amex"}` |  |
| What were my overall expenses in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| Show my most expensive transaction this month | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
