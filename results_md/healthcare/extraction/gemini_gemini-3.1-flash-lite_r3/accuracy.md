# Extraction: gemini:gemini-3.1-flash-lite

1399 questions. Frame accuracy (every slot right): **0.9614** [0.9495, 0.9726]. Slot micro-F1 0.9829. Questions with a span or value note: 0.

Negation (clinic_visits_excluding vs clinic_visits, slot clinic): excluded value wrong 11/112 (0.0982) vs included 0/114 (0.0); difference 0.0982 [0.0224, 0.1798].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1365 | 34 | 34 | 0.9757 | 0.9757 | 0.9757 |
| department | 345 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| clinic | 425 | 0 | 11 | 1.0 | 0.9748 | 0.9872 |
| payer | 89 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 95 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 205 | 9 | 0 | 0.9579 | 1.0 | 0.9785 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 21 | 1.0 |
| last_12_months | 36 | 1.0 |
| last_30_days | 34 | 0.0 |
| last_3_months | 127 | 1.0 |
| last_6_months | 17 | 1.0 |
| last_month | 183 | 1.0 |
| last_week | 38 | 1.0 |
| last_year | 189 | 1.0 |
| q2_2026 | 54 | 1.0 |
| q3_2026 | 188 | 1.0 |
| this_month | 184 | 1.0 |
| this_week | 132 | 1.0 |
| this_year | 196 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| Visit count for cardiology in the last 30 days | `{"period": "2026-09-28/2026-10-27", "department": "cardiology"}` | `{"period": "2026-09-27/2026-10-27", "department": "cardiology"}` |  |
| How many patient visits did family medicine handle in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "department": "family_medicine"}` | `{"period": "2026-09-27/2026-10-27", "department": "family_medicine"}` |  |
| How many patient visits did physical therapy handle in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "department": "physical_therapy"}` | `{"period": "2026-09-27/2026-10-27", "department": "physical_therapy"}` |  |
| What was the average wait time in dermatology in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "department": "dermatology"}` | `{"period": "2026-09-27/2026-10-27", "department": "dermatology"}` |  |
| What was the average wait time in radiology in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "department": "radiology"}` | `{"period": "2026-09-27/2026-10-27", "department": "radiology"}` |  |
| Mean waiting time in radiology in the last 30 days | `{"period": "2026-09-28/2026-10-27", "department": "radiology"}` | `{"period": "2026-09-27/2026-10-27", "department": "radiology"}` |  |
| Mean waiting time in pulmonology in the last 30 days | `{"period": "2026-09-28/2026-10-27", "department": "pulmonology"}` | `{"period": "2026-09-27/2026-10-27", "department": "pulmonology"}` |  |
| What was the average wait time in orthopedics in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "department": "orthopedics"}` | `{"period": "2026-09-27/2026-10-27", "department": "orthopedics"}` |  |
| Total charges billed by family medicine in the last 30 days | `{"period": "2026-09-28/2026-10-27", "department": "family_medicine"}` | `{"period": "2026-09-27/2026-10-27", "department": "family_medicine"}` |  |
| Total charges billed by orthopedics in the last 30 days | `{"period": "2026-09-28/2026-10-27", "department": "orthopedics"}` | `{"period": "2026-09-27/2026-10-27", "department": "orthopedics"}` |  |
| Number of incoming referrals at the Southgate clinic in the last 30 days | `{"period": "2026-09-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "southgate"}` |  |
| Number of incoming referrals at the Lakeside clinic in the last 30 days | `{"period": "2026-09-28/2026-10-27", "clinic": "lakeside"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "lakeside"}` |  |
| Number of incoming referrals at the Downtown clinic in the last 30 days | `{"period": "2026-09-28/2026-10-27", "clinic": "downtown"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "downtown"}` |  |
| How many patients did the Downtown clinic refer elsewhere in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "clinic": "downtown"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "downtown"}` |  |
| How many referrals did the Lakeside clinic send out in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "clinic": "lakeside"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "lakeside"}` |  |
| Visits at every site but the Southgate clinic so far this week | `{"period": "2026-10-26/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| Visits at every site but the Southgate site this week | `{"period": "2026-10-26/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many visits were there across all clinics except the Southgate clinic last month? | `{"period": "2026-09-01/2026-09-30", "clinic": "southgate"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many visits were there across all clinics except the Southgate clinic in the previous month? | `{"period": "2026-09-01/2026-09-30", "clinic": "southgate"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many visits were there across all clinics except the Southgate clinic this month? | `{"period": "2026-10-01/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many visits were there across all clinics except the Southgate clinic in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "southgate"}` |  |
| How many visits were there across all clinics except the Southgate site last month? | `{"period": "2026-09-01/2026-09-30", "clinic": "southgate"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Visits at every site but the Southgate clinic last year | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Visits at every site but the Southgate clinic in the previous year | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Visits at every site but the Southgate site last year | `{"period": "2025-01-01/2025-12-31", "clinic": "southgate"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Visits at every site but the Riverside clinic in the last 30 days | `{"period": "2026-09-28/2026-10-27", "clinic": "riverside"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "riverside"}` |  |
| How many visits were there across all clinics except the Midtown clinic in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "clinic": "midtown"}` | `{"period": "2026-09-27/2026-10-27", "clinic": "midtown"}` |  |
| Visits at every site but the Southgate clinic over the past three months | `{"period": "2026-07-28/2026-10-27", "clinic": "southgate"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| Visits at every site but the Northgate site this week | `{"period": "2026-10-26/2026-10-27", "clinic": "northgate"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many visits were billed to commercial insurance in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "payer": "commercial"}` | `{"period": "2026-09-27/2026-10-27", "payer": "commercial"}` |  |
| How many visits were billed to Medicare in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "payer": "medicare"}` | `{"period": "2026-09-27/2026-10-27", "payer": "medicare"}` |  |
| How many patient visits did we have in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| How many appointments were no-shows in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| Total missed appointments in the last 30 days | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| How often did patients miss appointments in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| How long did patients wait on average in the last 30 days? | `{"period": "2026-09-28/2026-10-27"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| Show the single longest patient wait last month | `{"period": "2026-09-01/2026-09-30"}` | `{"period": "2026-09-01/2026-09-30", "n": 1}` |  |
| Show the single longest patient wait last year | `{"period": "2025-01-01/2025-12-31"}` | `{"period": "2025-01-01/2025-12-31", "n": 1}` |  |
| Show the single longest patient wait this year | `{"period": "2026-01-01/2026-10-27"}` | `{"period": "2026-01-01/2026-10-27", "n": 1}` |  |
| Show the single longest patient wait this week | `{"period": "2026-10-26/2026-10-27"}` | `{"period": "2026-10-26/2026-10-27", "n": 1}` |  |
