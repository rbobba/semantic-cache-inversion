# Extraction: gemini-relsig:gemini-3.1-flash-lite

1399 questions. Frame accuracy (every slot right): **0.9936** [0.9879, 0.9979]. Slot micro-F1 0.9983. Questions with a span or value note: 0.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 0/112 (0.0) vs included 0/114 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1399 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| department | 345 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 436 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| payer | 88 | 0 | 1 | 1.0 | 0.9888 | 0.9944 |
| amount | 95 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 205 | 8 | 0 | 0.9624 | 1.0 | 0.9809 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 21 | 1.0 |
| last_12_months | 36 | 1.0 |
| last_30_days | 34 | 1.0 |
| last_3_months | 127 | 1.0 |
| last_6_months | 17 | 1.0 |
| last_month | 183 | 1.0 |
| last_week | 38 | 1.0 |
| last_year | 189 | 1.0 |
| q2_2026 | 54 | 1.0 |
| q3_2026 | 188 | 1.0 |
| this_month | 184 | 1.0 |
| this_week | 132 | 1.0 |
| this_year | 196 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How many visits were billed to private insurance last month? | `{"period": "2026-09-01/2026-09-30", "payer": "commercial"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Show the single longest patient wait last month | `{"period": "2026-09-01/2026-09-30"}` | `{"period": "2026-09-01/2026-09-30", "n": 1}` |  |
| Show the single longest patient wait last year | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| Show the single longest patient wait this week | `{"period": "2026-10-26/2026-10-27"}` | `{"period": "2026-10-26/2026-10-27", "n": 1}` |  |
| Show the single longest patient wait last week | `{"period": "2026-10-19/2026-10-25"}` | `{"period": "2026-10-19/2026-10-25", "n": 1}` |  |
| Show the single longest patient wait this month | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
| Show the single longest patient wait in Q3 2026 | `{"period": "2026-07-01/2026-09-30"}` | `{"period": "2026-07-01/2026-09-30", "n": 1}` |  |
| Show the single longest patient wait in Q2 2026 | `{"period": "2026-04-01/2026-06-30"}` | `{"period": "2026-04-01/2026-06-30", "n": 1}` |  |
| Show the single longest patient wait in the last 3 months | `{"period": "2026-07-28/2026-10-27"}` | `{"period": "2026-07-28/2026-10-27", "n": 1}` |  |
