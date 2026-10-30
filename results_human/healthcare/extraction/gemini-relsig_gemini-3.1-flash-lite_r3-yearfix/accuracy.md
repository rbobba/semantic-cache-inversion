# Extraction: gemini-relsig:gemini-3.1-flash-lite

265 questions. Frame accuracy (every slot right): **0.9774** [0.9521, 0.9964]. Slot micro-F1 0.9871. Questions with a span or value note: 0.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 259 | 6 | 6 | 0.9774 | 0.9774 | 0.9774 |
| department | 57 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| payer | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 32 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 1.0 |
| last_12_months | 9 | 0.4444 |
| last_30_days | 3 | 1.0 |
| last_3_months | 29 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 30 | 1.0 |
| last_week | 6 | 0.8333 |
| last_year | 29 | 1.0 |
| q2_2026 | 3 | 1.0 |
| q3_2026 | 42 | 1.0 |
| this_month | 41 | 1.0 |
| this_week | 40 | 1.0 |
| this_year | 27 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| Which three departments had the most patient visits over the past year? | `{"period": "2025-10-28/2026-10-27", "n": 3}` | `{"period": "2025-01-01/2025-12-31", "n": 3}` |  |
| How many total patient visits did the Southgate clinic see over the past full year? | `{"period": "2025-10-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` |  |
| What was our total number of patient no-shows across the network over the past full year? | `{"period": "2025-10-28/2026-10-27"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How many incoming referrals did the Lakeside clinic get during the week of October 19–25, 2026? | `{"period": "2026-10-19/2026-10-25", "clinic": "lakeside"}` | `{"period": "2026-10-01/2026-10-27", "clinic": "lakeside"}` |  |
| Which 3 departments had the highest number of patient visits over the last year? | `{"period": "2025-10-28/2026-10-27", "n": 3}` | `{"period": "2025-01-01/2025-12-31", "n": 3}` |  |
| How many total patient visits did Southgate clinic have over the past year? | `{"period": "2025-10-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` |  |
