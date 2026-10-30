# Extraction: gemini-relfull:gemini-3.1-flash-lite

248 questions. Frame accuracy (every slot right): **0.9677** [0.938, 0.9915]. Slot micro-F1 0.9815. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 240 | 8 | 8 | 0.9677 | 0.9677 | 0.9677 |
| merchant | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| account | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 1.0 |
| last_12_months | 15 | 0.6 |
| last_30_days | 3 | 1.0 |
| last_3_months | 46 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 25 | 1.0 |
| last_week | 6 | 0.6667 |
| last_year | 19 | 1.0 |
| q3_2026 | 43 | 1.0 |
| this_month | 23 | 1.0 |
| this_week | 37 | 1.0 |
| this_year | 25 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| how much savings or net cash do I actually have left over after looking at my total income minus spending for the past year | `{"period": "2025-10-28/2026-10-27"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Show me all transactions over $500 across my bank and credit card statements from October 28, 2025, through October 27, 2026 | `{"period": "2025-10-28/2026-10-27", "amount": 500}` | `{"period": "2026-01-01/2026-10-27", "amount": 500}` |  |
| Who are the top five merchants I spent the most money at over the past full year? | `{"period": "2025-10-28/2026-10-27", "n": 5}` | `{"period": "2025-01-01/2025-12-31", "n": 5}` |  |
| Which 3 merchants did I spend the most at during the week of October 19–25, 2026? | `{"period": "2026-10-19/2026-10-25", "n": 3}` | `{"period": "2026-10-01/2026-10-27", "n": 3}` |  |
| How much in refunds did I get from Netflix during the week of October 19–25, 2026? | `{"period": "2026-10-19/2026-10-25", "merchant": "netflix"}` | `{"period": "2026-10-01/2026-10-27", "merchant": "netflix"}` |  |
| List all of my transactions that were over $500 from the past year. | `{"period": "2025-10-28/2026-10-27", "amount": 500}` | `{"period": "2025-01-01/2025-12-31", "amount": 500}` |  |
| What is the total amount refunded to me by Shell over the past year? | `{"period": "2025-10-28/2026-10-27", "merchant": "shell"}` | `{"period": "2025-01-01/2025-12-31", "merchant": "shell"}` |  |
| Who are the 5 merchants I spent the most money with over the past year? | `{"period": "2025-10-28/2026-10-27", "n": 5}` | `{"period": "2025-01-01/2025-12-31", "n": 5}` |  |
