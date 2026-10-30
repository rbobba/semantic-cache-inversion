# Extraction: gemini-rel:gemini-3.1-flash-lite

1241 questions. Frame accuracy (every slot right): **0.9597** [0.9355, 0.9807]. Slot micro-F1 0.989. Questions with a span or value note: 0.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 39/105 (0.3714) vs included 0/104 (0.0); difference 0.3714 [0.2023, 0.5164].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1241 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| product | 449 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| region | 170 | 0 | 39 | 1.0 | 0.8134 | 0.8971 |
| channel | 92 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 105 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 201 | 11 | 0 | 0.9481 | 1.0 | 0.9734 |

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
| What was our total revenue in the last 3 months, not counting the Midwest? | `{"period": "2026-07-28/2026-10-27", "region": "midwest"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What was our total revenue in the last 3 months, not counting the Southeast? | `{"period": "2026-07-28/2026-10-27", "region": "southeast"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total revenue from every region but the West last year | `{"period": "2025-01-01/2025-12-31", "region": "west"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Total revenue from every region but the West in 2025 | `{"period": "2025-01-01/2025-12-31", "region": "west"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Total revenue from every region but the West during 2025 | `{"period": "2025-01-01/2025-12-31", "region": "west"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Total revenue from every region but the West in the previous year | `{"period": "2025-01-01/2025-12-31", "region": "west"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Total revenue from every region but the West this year | `{"period": "2026-01-01/2026-10-27", "region": "west"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the West in the last 12 months | `{"period": "2025-10-28/2026-10-27", "region": "west"}` | `{"period": "2025-10-28/2026-10-27"}` |  |
| Total revenue from every region but the Midwest last year | `{"period": "2025-01-01/2025-12-31", "region": "midwest"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Total revenue from every region but the Midwest last month | `{"period": "2026-09-01/2026-09-30", "region": "midwest"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Midwest in the previous month | `{"period": "2026-09-01/2026-09-30", "region": "midwest"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Midwest in September 2026 | `{"period": "2026-09-01/2026-09-30", "region": "midwest"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Midwest this month | `{"period": "2026-10-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest in August 2026 | `{"period": "2026-08-01/2026-08-31", "region": "midwest"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| Total revenue from every region but the Midwest in the last 30 days | `{"period": "2026-09-28/2026-10-27", "region": "midwest"}` | `{"period": "2026-09-28/2026-10-27"}` |  |
| Total revenue from every region but the West last month | `{"period": "2026-09-01/2026-09-30", "region": "west"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Midwest this week | `{"period": "2026-10-26/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest so far this week | `{"period": "2026-10-26/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest last week | `{"period": "2026-10-19/2026-10-25", "region": "midwest"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| Total revenue from every region but the Midwest region this week | `{"period": "2026-10-26/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the West this week | `{"period": "2026-10-26/2026-10-27", "region": "west"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest this year | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest so far this year | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest year to date | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest in 2026 | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest in the last 12 months | `{"period": "2025-10-28/2026-10-27", "region": "midwest"}` | `{"period": "2025-10-28/2026-10-27"}` |  |
| Total revenue from every region but the Midwest region this year | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| What was our total revenue in the last 3 months, not counting the West? | `{"period": "2026-07-28/2026-10-27", "region": "west"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| What were sales everywhere except the West region in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "region": "west"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total revenue from every region but the Northeast last month | `{"period": "2026-09-01/2026-09-30", "region": "northeast"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Northeast in the previous month | `{"period": "2026-09-01/2026-09-30", "region": "northeast"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Northeast in September 2026 | `{"period": "2026-09-01/2026-09-30", "region": "northeast"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Total revenue from every region but the Northeast this month | `{"period": "2026-10-01/2026-10-27", "region": "northeast"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| Total revenue from every region but the Northeast in August 2026 | `{"period": "2026-08-01/2026-08-31", "region": "northeast"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| Total revenue from every region but the Northeast in the last 30 days | `{"period": "2026-09-28/2026-10-27", "region": "northeast"}` | `{"period": "2026-09-28/2026-10-27"}` |  |
| Total revenue from every region but the Northeast so far this year | `{"period": "2026-01-01/2026-10-27", "region": "northeast"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Northeast year to date | `{"period": "2026-01-01/2026-10-27", "region": "northeast"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Northeast in the last 12 months | `{"period": "2025-10-28/2026-10-27", "region": "northeast"}` | `{"period": "2025-10-28/2026-10-27"}` |  |
| Total revenue from every region but the Southeast in September 2026 | `{"period": "2026-09-01/2026-09-30", "region": "southeast"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What was our largest order this month? | `{"period": "2026-10-01/2026-10-27"}` | `{"period": "2026-10-01/2026-10-27", "n": 1}` |  |
