# Extraction: gemini-rel:gemini-3.5-flash

1241 questions. Frame accuracy (every slot right): **0.9976** [0.9944, 1.0]. Slot micro-F1 0.9993. Questions with a span or value note: 0.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 0/105 (0.0) vs included 0/104 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1241 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| product | 446 | 0 | 3 | 1.0 | 0.9933 | 0.9966 |
| region | 209 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| channel | 92 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 105 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 201 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 27 | 1.0 |
| last_12_months | 29 | 1.0 |
| last_30_days | 37 | 1.0 |
| last_3_months | 118 | 1.0 |
| last_6_months | 19 | 1.0 |
| last_month | 212 | 1.0 |
| last_week | 42 | 1.0 |
| last_year | 150 | 1.0 |
| q2_2026 | 28 | 1.0 |
| q3_2026 | 113 | 1.0 |
| this_month | 156 | 1.0 |
| this_week | 141 | 1.0 |
| this_year | 169 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| Total revenue from rucksacks this week | `{"period": "2026-10-26/2026-10-27", "product": "backpacks"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many raincoats were sold last year? | `{"period": "2025-01-01/2025-12-31", "product": "rain_jackets"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How much did we refund on rucksacks this week? | `{"period": "2026-10-26/2026-10-27", "product": "backpacks"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
