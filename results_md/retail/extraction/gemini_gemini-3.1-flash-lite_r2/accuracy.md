# Extraction: gemini:gemini-3.1-flash-lite

1241 questions. Frame accuracy (every slot right): **0.9186** [0.8892, 0.9438]. Slot micro-F1 0.9691. Questions with a span or value note: 0.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 35/105 (0.3333) vs included 0/104 (0.0); difference 0.3333 [0.1948, 0.4457].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1204 | 37 | 37 | 0.9702 | 0.9702 | 0.9702 |
| product | 449 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| region | 174 | 0 | 35 | 1.0 | 0.8325 | 0.9086 |
| channel | 92 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 105 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 201 | 33 | 0 | 0.859 | 1.0 | 0.9241 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 27 | 1.0 |
| last_12_months | 29 | 1.0 |
| last_30_days | 37 | 0.0 |
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
| What did running shoes generate in sales in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "running_shoes"}` | `{"period": "2026-09-27/2026-10-27", "product": "running_shoes"}` |  |
| What did hiking boots generate in sales in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "hiking_boots"}` | `{"period": "2026-09-27/2026-10-27", "product": "hiking_boots"}` |  |
| How much did yoga mats sell for in total in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "yoga_mats"}` | `{"period": "2026-09-27/2026-10-27", "product": "yoga_mats"}` |  |
| How much did rain jackets sell for in total in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "rain_jackets"}` | `{"period": "2026-09-27/2026-10-27", "product": "rain_jackets"}` |  |
| Total revenue from ski jackets in the last 30 days | `{"period": "2026-09-28/2026-10-27", "product": "ski_jackets"}` | `{"period": "2026-09-27/2026-10-27", "product": "ski_jackets"}` |  |
| How many units of ski jackets did we sell in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "ski_jackets"}` | `{"period": "2026-09-27/2026-10-27", "product": "ski_jackets"}` |  |
| How many running shoes were sold in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "running_shoes"}` | `{"period": "2026-09-27/2026-10-27", "product": "running_shoes"}` |  |
| On average, how much did customers pay for backpacks in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "backpacks"}` | `{"period": "2026-09-27/2026-10-27", "product": "backpacks"}` |  |
| What did running shoes sell for on average in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "running_shoes"}` | `{"period": "2026-09-27/2026-10-27", "product": "running_shoes"}` |  |
| On average, how much did customers pay for yoga mats in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "yoga_mats"}` | `{"period": "2026-09-27/2026-10-27", "product": "yoga_mats"}` |  |
| What did hiking boots sell for on average in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "hiking_boots"}` | `{"period": "2026-09-27/2026-10-27", "product": "hiking_boots"}` |  |
| How much did we refund on running shoes in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "running_shoes"}` | `{"period": "2026-09-27/2026-10-27", "product": "running_shoes"}` |  |
| How much did we refund on ski jackets in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "ski_jackets"}` | `{"period": "2026-09-27/2026-10-27", "product": "ski_jackets"}` |  |
| What was the value of trail shoes returned in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "product": "trail_shoes"}` | `{"period": "2026-09-27/2026-10-27", "product": "trail_shoes"}` |  |
| Total revenue for the Midwest in the last 30 days | `{"period": "2026-09-28/2026-10-27", "region": "midwest"}` | `{"period": "2026-09-27/2026-10-27", "region": "midwest"}` |  |
| Total revenue for the West in the last 30 days | `{"period": "2026-09-28/2026-10-27", "region": "west"}` | `{"period": "2026-09-27/2026-10-27", "region": "west"}` |  |
| How much revenue came from the Northeast in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "region": "northeast"}` | `{"period": "2026-09-27/2026-10-27", "region": "northeast"}` |  |
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
| Total revenue from every region but the Midwest in August 2026 | `{"period": "2026-08-01/2026-08-31", "region": "midwest"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| Total revenue from every region but the Midwest in the last 30 days | `{"period": "2026-09-28/2026-10-27", "region": "midwest"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| Total revenue from every region but the West last month | `{"period": "2026-09-01/2026-09-30", "region": "west"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| What were sales everywhere except the West in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "region": "west"}` | `{"period": "2026-09-27/2026-10-27", "region": "west"}` |  |
| How much did we sell in the last 3 months outside the West? | `{"period": "2026-07-28/2026-10-27", "region": "west"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Total revenue from every region but the Midwest this week | `{"period": "2026-10-26/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest so far this week | `{"period": "2026-10-26/2026-10-27", "region": "midwest"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest last week | `{"period": "2026-10-19/2026-10-25", "region": "midwest"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| Total revenue from every region but the West this week | `{"period": "2026-10-26/2026-10-27", "region": "west"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Total revenue from every region but the Midwest this year | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest so far this year | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest year to date | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Total revenue from every region but the Midwest in 2026 | `{"period": "2026-01-01/2026-10-27", "region": "midwest"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
