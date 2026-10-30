# Extraction: openai-relfull:gpt-6-luna

248 questions. Frame accuracy (every slot right): **0.9355** [0.8973, 0.9718]. Slot micro-F1 0.9811. Questions with a span or value note: 15.

Negation (region_revenue_excluding vs region_revenue, slot region): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 232 | 0 | 16 | 1.0 | 0.9355 | 0.9667 |
| product | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| region | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| channel | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 0.3333 |
| last_30_days | 12 | 1.0 |
| last_3_months | 31 | 1.0 |
| last_6_months | 12 | 1.0 |
| last_month | 39 | 0.7949 |
| last_week | 9 | 0.8889 |
| last_year | 21 | 1.0 |
| q2_2026 | 6 | 0.6667 |
| q3_2026 | 20 | 0.85 |
| this_month | 26 | 1.0 |
| this_week | 39 | 1.0 |
| this_year | 30 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How much total refunded for returns of water bottles? | `{"period": "2026-10-19/2026-10-25", "product": "water_bottles"}` | `{"product": "water_bottles"}` |  |
| How many orders did we receive through our in-store channel in September? | `{"period": "2026-09-01/2026-09-30", "channel": "in_store"}` | `{"channel": "in_store"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much did we refund customers for returned trail shoes in August? | `{"period": "2026-08-01/2026-08-31", "product": "trail_shoes"}` | `{"product": "trail_shoes"}` | period: unparseable value {'text': 'in August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the average selling price of backpacks in September? | `{"period": "2026-09-01/2026-09-30", "product": "backpacks"}` | `{"product": "backpacks"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much total revenue did we make from rain jackets back in September? | `{"period": "2026-09-01/2026-09-30", "product": "rain_jackets"}` | `{"product": "rain_jackets"}` | period: unparseable value {'text': 'back in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the total dollar amount of all customer returns across our business in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our single biggest order by value in September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the total revenue generated in the West region during Q3? | `{"period": "2026-07-01/2026-09-30", "region": "west"}` | `{"region": "west"}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many in-store orders did we process during September? | `{"period": "2026-09-01/2026-09-30", "channel": "in_store"}` | `{"channel": "in_store"}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the total dollar amount refunded for trail shoe returns in August? | `{"period": "2026-08-01/2026-08-31", "product": "trail_shoes"}` | `{"product": "trail_shoes"}` | period: unparseable value {'text': 'in August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the average sale price of our backpacks in September? | `{"period": "2026-09-01/2026-09-30", "product": "backpacks"}` | `{"product": "backpacks"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our net revenue for Q2? | `{"period": "2026-04-01/2026-06-30"}` | `{}` | period: unparseable value {'text': 'Q2', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 2} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our total gross revenue in the second quarter? | `{"period": "2026-04-01/2026-06-30"}` | `{}` | period: unparseable value {'text': 'in the second quarter', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 2} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much total revenue did rain jackets bring in during September? | `{"period": "2026-09-01/2026-09-30", "product": "rain_jackets"}` | `{"product": "rain_jackets"}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the absolute total dollar amount returned by customers in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our highest-value single order in September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
