# Extraction: openai-relsig:gpt-6-luna

248 questions. Frame accuracy (every slot right): **0.996** [0.9874, 1.0]. Slot micro-F1 0.9977. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 247 | 1 | 1 | 0.996 | 0.996 | 0.996 |
| merchant | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| account | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 1.0 |
| last_12_months | 15 | 0.9333 |
| last_30_days | 3 | 1.0 |
| last_3_months | 46 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 25 | 1.0 |
| last_week | 6 | 1.0 |
| last_year | 19 | 1.0 |
| q3_2026 | 43 | 1.0 |
| this_month | 23 | 1.0 |
| this_week | 37 | 1.0 |
| this_year | 25 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| What is the total amount refunded to me by Shell over the past year? | `{"period": "2025-10-28/2026-10-27", "merchant": "shell"}` | `{"period": "2025-01-01/2025-12-31", "merchant": "shell"}` |  |
