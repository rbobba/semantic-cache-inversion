# Extraction: openai-relfull:gpt-6-luna

248 questions. Frame accuracy (every slot right): **0.996** [0.9873, 1.0]. Slot micro-F1 0.9988. Questions with a span or value note: 0.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 247 | 0 | 1 | 1.0 | 0.996 | 0.998 |
| product | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| region | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| channel | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 1.0 |
| last_30_days | 12 | 1.0 |
| last_3_months | 31 | 1.0 |
| last_6_months | 12 | 1.0 |
| last_month | 39 | 1.0 |
| last_week | 9 | 0.8889 |
| last_year | 21 | 1.0 |
| q2_2026 | 6 | 1.0 |
| q3_2026 | 20 | 1.0 |
| this_month | 26 | 1.0 |
| this_week | 39 | 1.0 |
| this_year | 30 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How much total refunded for returns of water bottles? | `{"period": "2026-10-19/2026-10-25", "product": "water_bottles"}` | `{"product": "water_bottles"}` |  |
