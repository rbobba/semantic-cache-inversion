# Extraction: gemini:gemini-3.5-flash

1358 questions. Frame accuracy (every slot right): **0.9867** [0.9788, 0.9929]. Slot micro-F1 0.9954. Questions with a span or value note: 0.

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1353 | 5 | 5 | 0.9963 | 0.9963 | 0.9963 |
| merchant | 506 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 231 | 0 | 1 | 1.0 | 0.9957 | 0.9978 |
| account | 110 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 206 | 12 | 0 | 0.945 | 1.0 | 0.9717 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 14 | 1.0 |
| last_12_months | 35 | 0.9429 |
| last_30_days | 27 | 1.0 |
| last_3_months | 171 | 0.9825 |
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
| Count my transactions at Amazon in the last 3 months | `{"period": "2026-07-28/2026-10-27", "merchant": "amazon"}` | `{"period": "2026-07-29/2026-10-27", "merchant": "amazon"}` |  |
| Count my transactions at Home Depot in the last 12 months | `{"period": "2025-10-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2025-10-29/2026-10-27", "merchant": "home_depot"}` |  |
| Count my transactions at Home Depot in the last 3 months | `{"period": "2026-07-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-07-29/2026-10-27", "merchant": "home_depot"}` |  |
| How much money went to shopping in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "category": "shopping"}` | `{"period": "2026-07-29/2026-10-27", "category": "shopping"}` |  |
| Total spent on everything but fuel this year | `{"period": "2026-01-01/2026-10-27", "category": "gas"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| What was the biggest single thing I bought this year? | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought last year? | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| Show my most expensive transaction this year | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought in the last 12 months? | `{"period": "2025-10-28/2026-10-27"}` | `{"period": "2025-10-28/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought in Q3 2026? | `{"period": "2026-07-01/2026-09-30"}` | `{"period": "2026-07-01/2026-09-30", "n": 1}` |  |
| What was the biggest single thing I bought in Q2 2026? | `{"period": "2026-04-01/2026-06-30"}` | `{"period": "2026-04-01/2026-06-30", "n": 1}` |  |
| What was the biggest single thing I bought so far this month? | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-28/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought in September 2026? | `{"period": "2026-09-01/2026-09-30"}` | `{"period": "2026-09-01/2026-09-30", "n": 1}` |  |
| What was the biggest single thing I bought in August 2026? | `{"period": "2026-08-01/2026-08-31"}` | `{"period": "2026-08-01/2026-08-31", "n": 1}` |  |
| Show my most expensive transaction year to date | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| What was the biggest single thing I bought in the last 3 months? | `{"period": "2026-07-28/2026-10-27"}` | `{"period": "2026-07-28/2026-10-27", "n": 1}` |  |
| Show me transactions over $100 in the last 12 months | `{"period": "2025-10-28/2026-10-27", "amount": 100}` | `{"period": "2025-10-29/2026-10-27", "amount": 100}` |  |
