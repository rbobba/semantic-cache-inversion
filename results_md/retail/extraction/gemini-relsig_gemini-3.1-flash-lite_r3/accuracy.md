# Extraction: gemini-relsig:gemini-3.1-flash-lite

1241 questions. Frame accuracy (every slot right): **1.0** [1.0, 1.0]. Slot micro-F1 1.0. Questions with a span or value note: 0.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 0/105 (0.0) vs included 0/104 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1241 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| product | 449 | 0 | 0 | 1.0 | 1.0 | 1.0 |
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
