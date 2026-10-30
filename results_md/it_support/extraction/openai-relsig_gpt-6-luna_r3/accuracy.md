# Extraction: openai-relsig:gpt-6-luna

1202 questions. Frame accuracy (every slot right): **0.9834** [0.9769, 0.9897]. Slot micro-F1 0.9954. Questions with a span or value note: 0.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 10/116 (0.0862) vs included 10/122 (0.082); difference 0.0042 [-0.0111, 0.0177].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1202 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| team | 327 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 218 | 0 | 20 | 1.0 | 0.916 | 0.9561 |
| service | 102 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 196 | 0 | 0 | 1.0 | 1.0 | 1.0 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 19 | 1.0 |
| last_12_months | 39 | 1.0 |
| last_30_days | 27 | 1.0 |
| last_3_months | 92 | 1.0 |
| last_6_months | 13 | 1.0 |
| last_month | 152 | 1.0 |
| last_week | 48 | 1.0 |
| last_year | 189 | 1.0 |
| q2_2026 | 24 | 1.0 |
| q3_2026 | 87 | 1.0 |
| this_month | 129 | 1.0 |
| this_week | 166 | 1.0 |
| this_year | 217 | 1.0 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How many medium-priority tickets were opened last year? | `{"period": "2025-01-01/2025-12-31", "priority": "p3"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| Number of medium-priority tickets this month | `{"period": "2026-10-01/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many low-priority tickets were opened last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p4"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| Number of critical tickets in Q3 2026 | `{"period": "2026-07-01/2026-09-30", "priority": "p1"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| Number of low-priority tickets last year | `{"period": "2025-01-01/2025-12-31", "priority": "p4"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How many medium-priority tickets were opened this year? | `{"period": "2026-01-01/2026-10-27", "priority": "p3"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| Number of critical tickets this week | `{"period": "2026-10-26/2026-10-27", "priority": "p1"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many medium-priority tickets were opened this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many high-priority tickets were opened last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p2"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many critical tickets were opened in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p1"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets were opened last year, excluding critical ones? | `{"period": "2025-01-01/2025-12-31", "priority": "p1"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
| How many tickets were opened in the last 3 months, excluding high-priority ones? | `{"period": "2026-07-28/2026-10-27", "priority": "p2"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except medium-priority did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets were opened last month, excluding low-priority ones? | `{"period": "2026-09-01/2026-09-30", "priority": "p4"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets were opened this week, excluding critical ones? | `{"period": "2026-10-26/2026-10-27", "priority": "p1"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except high-priority did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except medium-priority did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except low-priority did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except low-priority did we get this year? | `{"period": "2026-01-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many tickets of every priority except medium-priority did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
