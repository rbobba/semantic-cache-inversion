# Extraction: openai-relfull:gpt-6-luna

245 questions. Frame accuracy (every slot right): **0.951** [0.9173, 0.9788]. Slot micro-F1 0.9827. Questions with a span or value note: 10.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 234 | 1 | 11 | 0.9957 | 0.9551 | 0.975 |
| team | 57 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 38 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| service | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 15 | 1 | 1 | 0.9375 | 0.9375 | 0.9375 |
| n | 35 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| last_12_months | 6 | 0.8333 |
| last_30_days | 3 | 1.0 |
| last_3_months | 22 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 28 | 0.8214 |
| last_week | 6 | 1.0 |
| last_year | 38 | 1.0 |
| q3_2026 | 24 | 0.7917 |
| this_month | 27 | 1.0 |
| this_week | 36 | 1.0 |
| this_year | 52 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| Can I get a report on every ticket over the last 6 months that took longer than 4 days to resolve? | `{"period": "2026-04-28/2026-10-27", "amount": 4}` | `{"period": "2026-04-28/2026-10-27", "amount": 96}` |  |
| How many tickets did we get in September for everything besides P3 issues? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"priority": "p3"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the grand total of tickets our team wrapped up and resolved in September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What is the net difference between the number of tickets we opened and the number we closed back in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'back in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many IT tickets did we resolve in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the difference between opened and resolved tickets in September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our overall average resolution time for tickets in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many new tickets were opened during Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many tickets were closed in September that weren't P3 priority? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"priority": "p3"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many tickets did the team fully resolve during September? | `{"period": "2026-09-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What is the total number of print tickets handled over the last year? | `{"period": "2025-10-28/2026-10-27", "service": "printing"}` | `{"period": "2025-01-01/2025-12-31", "service": "printing"}` |  |
| What was the net difference between our open and closed tickets in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
