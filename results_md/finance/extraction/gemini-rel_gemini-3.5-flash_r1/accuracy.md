# Extraction: gemini-rel:gemini-3.5-flash

1295 questions. Frame accuracy (every slot right): **0.9969** [0.9937, 0.9993]. Slot micro-F1 0.9992. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 0/111 (0.0) vs included 0/111 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1295 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| merchant | 499 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 222 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| account | 94 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 98 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 191 | 4 | 0 | 0.9795 | 1.0 | 0.9896 |

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
| What was the biggest single thing I bought last year? | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| Show my most expensive transaction this year | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| Show my most expensive transaction last year | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| What was the biggest single thing I bought this month? | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
