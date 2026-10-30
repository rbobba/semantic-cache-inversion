# Extraction: gemini-relfull:gemini-3.1-flash-lite

245 questions. Frame accuracy (every slot right): **0.9796** [0.9567, 0.9963]. Slot micro-F1 0.9878. Questions with a span or value note: 0.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 241 | 4 | 4 | 0.9837 | 0.9837 | 0.9837 |
| team | 57 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| service | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 15 | 1 | 1 | 0.9375 | 0.9375 | 0.9375 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| last_12_months | 6 | 0.6667 |
| last_30_days | 3 | 1.0 |
| last_3_months | 22 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 28 | 1.0 |
| last_week | 6 | 0.6667 |
| last_year | 38 | 1.0 |
| q3_2026 | 24 | 1.0 |
| this_month | 27 | 1.0 |
| this_week | 36 | 1.0 |
| this_year | 52 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| Can I get a report on every ticket over the last 6 months that took longer than 4 days to resolve? | `{"period": "2026-04-28/2026-10-27", "amount": 4}` | `{"period": "2026-04-28/2026-10-27", "amount": 96}` |  |
| How many printing service orders over $100 did we handle over the past full year? | `{"period": "2025-10-28/2026-10-27", "service": "printing"}` | `{"period": "2025-01-01/2025-12-31", "service": "printing"}` |  |
| How many tickets did the cloud team resolve during the week of October 19–25, 2026? | `{"period": "2026-10-19/2026-10-25", "team": "cloud"}` | `{"period": "2026-10-01/2026-10-27", "team": "cloud"}` |  |
| How many tickets were about email during the week of October 19–25, 2026? | `{"period": "2026-10-19/2026-10-25", "service": "email"}` | `{"period": "2026-10-01/2026-10-27", "service": "email"}` |  |
| What is the total number of print tickets handled over the last year? | `{"period": "2025-10-28/2026-10-27", "service": "printing"}` | `{"period": "2025-01-01/2025-12-31", "service": "printing"}` |  |
