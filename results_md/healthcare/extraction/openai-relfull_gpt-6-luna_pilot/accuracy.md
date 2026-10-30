# Extraction: openai-relfull:gpt-6-luna

1399 questions. Frame accuracy (every slot right): **0.9993** [0.9978, 1.0]. Slot micro-F1 0.9998. Questions with a span or value note: 0.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 1/112 (0.0089) vs included 0/114 (0.0); difference 0.0089 [0.0, 0.0286].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1399 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| department | 345 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 435 | 0 | 1 | 1.0 | 0.9977 | 0.9989 |
| payer | 89 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 95 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 205 | 0 | 0 | 1.0 | 1.0 | 1.0 |

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
| Visits at every site but the Southgate site last year | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
