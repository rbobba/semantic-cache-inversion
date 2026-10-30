# Extraction: openai-relsig:gpt-6-luna

248 questions. Frame accuracy (every slot right): **0.9153** [0.8719, 0.9545]. Slot micro-F1 0.9739. Questions with a span or value note: 20.

Negation (category_spend_excluding vs category_spend_total, slot category): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 227 | 1 | 21 | 0.9956 | 0.9153 | 0.9538 |
| merchant | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| account | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 0.3333 |
| last_12_months | 15 | 0.9333 |
| last_30_days | 3 | 1.0 |
| last_3_months | 46 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 25 | 0.8 |
| last_week | 6 | 1.0 |
| last_year | 19 | 1.0 |
| q3_2026 | 43 | 0.7209 |
| this_month | 23 | 0.9565 |
| this_week | 37 | 1.0 |
| this_year | 25 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| how much total income did I actually bring in during Q3—from July 1st through September 30th—based on my bank and card statements? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'during Q3—from July 1st through September 30th', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many times did I shop at Whole Foods back in Q3? | `{"period": "2026-07-01/2026-09-30", "merchant": "whole_foods"}` | `{"merchant": "whole_foods"}` | period: unparseable value {'text': 'back in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my total spending on Lyft rides for the third quarter? | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` | `{"merchant": "lyft"}` | period: unparseable value {'text': 'for the third quarter', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my average receipt amount at Trader Joe's during Q3? | `{"period": "2026-07-01/2026-09-30", "merchant": "trader_joes"}` | `{"merchant": "trader_joes"}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much did I spend in Q3, excluding subscription expenses? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"category": "subscriptions"}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much money did I get back in refunds from Dunkin' in September? | `{"period": "2026-09-01/2026-09-30", "merchant": "dunkin"}` | `{"merchant": "dunkin"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many times did I make a purchase at Home Depot in August | `{"period": "2026-08-01/2026-08-31", "merchant": "home_depot"}` | `{"merchant": "home_depot"}` | period: unparseable value {'text': 'in August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Who are the top five merchants I spent the most money at over the past full year? | `{"period": "2025-10-28/2026-10-27", "n": 5}` | `{"period": "2025-01-01/2025-12-31", "n": 5}` |  |
| What were my top three biggest spending categories back in September? | `{"period": "2026-09-01/2026-09-30", "n": 3}` | `{"n": 3}` | period: unparseable value {'text': 'back in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the single most expensive item I bought during the third quarter? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'during the third quarter', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my total spending in Q3, excluding gas? | `{"period": "2026-07-01/2026-09-30", "category": "gas"}` | `{"category": "gas"}` | period: unparseable value {'text': 'Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many times did I shop at Whole Foods during Q3? | `{"period": "2026-07-01/2026-09-30", "merchant": "whole_foods"}` | `{"merchant": "whole_foods"}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my total spending on Lyft rides in the third quarter? | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` | `{"merchant": "lyft"}` | period: unparseable value {'text': 'in the third quarter', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my average transaction size at Trader Joe's in Q3? | `{"period": "2026-07-01/2026-09-30", "merchant": "trader_joes"}` | `{"merchant": "trader_joes"}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much total money did I spend in Q3 if you exclude recurring subscriptions? | `{"period": "2026-07-01/2026-09-30", "category": "subscriptions"}` | `{"category": "subscriptions"}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much have I spent at Chevron in total during October? | `{"period": "2026-10-01/2026-10-27", "merchant": "chevron"}` | `{"merchant": "chevron"}` | period: unparseable value {'text': 'during October', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 10} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How much money was refunded to me by Dunkin' in September? | `{"period": "2026-09-01/2026-09-30", "merchant": "dunkin"}` | `{"merchant": "dunkin"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many times did I make a transaction at Home Depot in August? | `{"period": "2026-08-01/2026-08-31", "merchant": "home_depot"}` | `{"merchant": "home_depot"}` | period: unparseable value {'text': 'in August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What were my top 3 categories for spending during September? | `{"period": "2026-09-01/2026-09-30", "n": 3}` | `{"n": 3}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was my highest single expense during Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the total sum of all my spending throughout September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'throughout September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
