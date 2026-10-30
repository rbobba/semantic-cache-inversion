# Extraction: openai-relsig:gpt-6-luna

265 questions. Frame accuracy (every slot right): **0.9283** [0.8893, 0.9623]. Slot micro-F1 0.9759. Questions with a span or value note: 16.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 0/19 (0.0) vs included 0/19 (0.0); difference 0.0 [0.0, 0.0].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 246 | 3 | 19 | 0.988 | 0.9283 | 0.9572 |
| department | 57 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 76 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| payer | 19 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 16 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 32 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 3 | 0.3333 |
| last_12_months | 9 | 0.6667 |
| last_30_days | 3 | 1.0 |
| last_3_months | 29 | 1.0 |
| last_6_months | 3 | 1.0 |
| last_month | 30 | 0.8333 |
| last_week | 6 | 1.0 |
| last_year | 29 | 1.0 |
| q2_2026 | 3 | 0.6667 |
| q3_2026 | 42 | 0.8095 |
| this_month | 41 | 1.0 |
| this_week | 40 | 1.0 |
| this_year | 27 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| What was the average patient wait time in radiology during September? | `{"period": "2026-09-01/2026-09-30", "department": "radiology"}` | `{"department": "radiology"}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many referrals did the Riverside clinic send out during the third quarter? | `{"period": "2026-07-01/2026-09-30", "clinic": "riverside"}` | `{"clinic": "riverside"}` | period: unparseable value {'text': 'during the third quarter', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was our total patient visit count for physical therapy back in September? | `{"period": "2026-09-01/2026-09-30", "department": "physical_therapy"}` | `{"department": "physical_therapy"}` | period: unparseable value {'text': 'back in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Who were our top three busiest providers by patient volume in Q3? | `{"period": "2026-07-01/2026-09-30", "n": 3}` | `{"n": 3}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Which patient visits in August had a wait time longer than 45 minutes? | `{"period": "2026-08-01/2026-08-31", "amount": 45}` | `{"amount": 45}` | period: unparseable value {'text': 'August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many total referrals did the Downtown clinic receive during September? | `{"period": "2026-09-01/2026-09-30", "clinic": "downtown"}` | `{"clinic": "downtown"}` | period: unparseable value {'text': 'during September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many referrals did the Midtown clinic send out back in Q3? | `{"period": "2026-07-01/2026-09-30", "clinic": "midtown"}` | `{"clinic": "midtown"}` | period: unparseable value {'text': 'back in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many total patient visits did the Southgate clinic see over the past full year? | `{"period": "2025-10-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` |  |
| What was our total number of patient no-shows across the network over the past full year? | `{"period": "2025-10-28/2026-10-27"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Can I get the total number of visits across all clinics except Downtown for Q3? | `{"period": "2026-07-01/2026-09-30", "clinic": "downtown"}` | `{"clinic": "downtown"}` | period: unparseable value {'text': 'for Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many patient visits were billed to Medicare in Q2? | `{"period": "2026-04-01/2026-06-30", "payer": "medicare"}` | `{"payer": "medicare"}` | period: unparseable value {'text': 'in Q2', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 2} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Which 3 departments had the highest number of patient visits over the last year? | `{"period": "2025-10-28/2026-10-27", "n": 3}` | `{"period": "2025-01-01/2025-12-31", "n": 3}` |  |
| How many external referrals did the Riverside clinic send out in Q3? | `{"period": "2026-07-01/2026-09-30", "clinic": "riverside"}` | `{"clinic": "riverside"}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What was the total volume of patient visits for physical therapy in September? | `{"period": "2026-09-01/2026-09-30", "department": "physical_therapy"}` | `{"department": "physical_therapy"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Who were the top 3 healthcare providers by visit count during Q3? | `{"period": "2026-07-01/2026-09-30", "n": 3}` | `{"n": 3}` | period: unparseable value {'text': 'during Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| What percentage of scheduled appointments were no-shows in Q3? | `{"period": "2026-07-01/2026-09-30"}` | `{}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| Can you list all patient visits in August that had a wait time over 45 minutes? | `{"period": "2026-08-01/2026-08-31", "amount": 45}` | `{"amount": 45}` | period: unparseable value {'text': 'in August', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 8} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many incoming referrals did the Downtown clinic receive in September? | `{"period": "2026-09-01/2026-09-30", "clinic": "downtown"}` | `{"clinic": "downtown"}` | period: unparseable value {'text': 'in September', 'kind': 'calendar_month', 'n': None, 'year': None, 'number': 9} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
| How many outgoing referrals did Midtown clinic issue in Q3? | `{"period": "2026-07-01/2026-09-30", "clinic": "midtown"}` | `{"clinic": "midtown"}` | period: unparseable value {'text': 'in Q3', 'kind': 'calendar_quarter', 'n': None, 'year': None, 'number': 3} (int() argument must be a string, a bytes-like object or a real number, not 'NoneType') |
