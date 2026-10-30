# Extraction: openai-relfull:gpt-6-luna

265 questions. Frame accuracy (every slot right): **0.9925** [0.9802, 1.0]. Slot micro-F1 0.9957. Questions with a span or value note: 0.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 263 | 2 | 2 | 0.9925 | 0.9925 | 0.9925 |
| department | 57 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| payer | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 32 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 1.0 |
| last_12_months | 9 | 0.7778 |
| last_30_days | 3 | 1.0 |
| last_3_months | 29 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 30 | 1.0 |
| last_week | 6 | 1.0 |
| last_year | 29 | 1.0 |
| q2_2026 | 3 | 1.0 |
| q3_2026 | 42 | 1.0 |
| this_month | 41 | 1.0 |
| this_week | 40 | 1.0 |
| this_year | 27 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How many total patient visits did the Southgate clinic see over the past full year? | `{"period": "2025-10-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` |  |
| Which 3 departments had the highest number of patient visits over the last year? | `{"period": "2025-10-28/2026-10-27", "n": 3}` | `{"period": "2025-01-01/2025-12-31", "n": 3}` |  |
