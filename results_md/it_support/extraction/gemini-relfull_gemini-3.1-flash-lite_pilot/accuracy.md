# Extraction: gemini-relfull:gemini-3.1-flash-lite

1202 questions. Frame accuracy (every slot right): **0.9992** [0.9968, 1.0]. Slot micro-F1 0.9998. Questions with a span or value note: 0.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 1/116 (0.0086) vs included 0/122 (0.0); difference 0.0086 [0.0, 0.0282].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1202 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| team | 327 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 237 | 0 | 1 | 1.0 | 0.9958 | 0.9979 |
| service | 102 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 196 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 19 | 1.0 |
| last_12_months | 39 | 1.0 |
| last_30_days | 27 | 1.0 |
| last_3_months | 92 | 1.0 |
| last_6_months | 13 | 1.0 |
| last_month | 152 | 1.0 |
| last_week | 48 | 1.0 |
| last_year | 189 | 1.0 |
| q2_2026 | 24 | 1.0 |
| q3_2026 | 87 | 1.0 |
| this_month | 129 | 1.0 |
| this_week | 166 | 1.0 |
| this_year | 217 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How many tickets of every priority except P4 did we get last year? | `{"period": "2025-01-01/2025-12-31", "priority": "p4"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
