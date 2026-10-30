# Extraction: openai-relsig:gpt-6-luna

1295 questions. Frame accuracy (every slot right): **0.9992** [0.9975, 1.0]. Slot micro-F1 0.9998. Questions with a span or value note: 0.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 1/111 (0.009) vs included 0/111 (0.0); difference 0.009 [0.0, 0.0326].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1295 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| merchant | 499 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 221 | 0 | 1 | 1.0 | 0.9955 | 0.9977 |
| account | 94 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 98 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 191 | 0 | 0 | 1.0 | 1.0 | 1.0 |

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
| How much did I spend on everything except fuel in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "category": "gas"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
