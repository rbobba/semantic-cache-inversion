# Extraction: gemini-rel:gemini-3.1-flash-lite

1202 questions. Frame accuracy (every slot right): **0.9517** [0.9173, 0.9772]. Slot micro-F1 0.9863. Questions with a span or value note: 0.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 45/116 (0.3879) vs included 3/122 (0.0246); difference 0.3633 [0.1376, 0.5704].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1202 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| team | 327 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 190 | 1 | 48 | 0.9948 | 0.7983 | 0.8858 |
| service | 102 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 196 | 10 | 0 | 0.9515 | 1.0 | 0.9751 |

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
| How many medium-priority tickets were opened this year? | `{"period": "2026-01-01/2026-10-27", "priority": "p3"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many high-priority tickets were opened last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p2"}` | `{"period": "2026-09-01/2026-09-30", "priority": "p1"}` |  |
| How many tickets were opened in the last 3 months, excluding high-priority ones? | `{"period": "2026-07-28/2026-10-27", "priority": "p2"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get in the previous month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get in September 2026? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get this month? | `{"period": "2026-10-01/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get in August 2026? | `{"period": "2026-08-01/2026-08-31", "priority": "p3"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| How many tickets of every priority except P3 did we get in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-09-28/2026-10-27"}` |  |
| How many tickets of every priority except priority 3 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except medium-priority did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P2 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p2"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P4 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p4"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P2 did we get so far this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P2 did we get last week? | `{"period": "2026-10-19/2026-10-25", "priority": "p2"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| How many tickets of every priority except P2 did we get this month? | `{"period": "2026-10-01/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many tickets of every priority except priority 2 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except high-priority did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P1 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p1"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get over the past three months? | `{"period": "2026-07-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get in the last 6 months? | `{"period": "2026-04-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-04-28/2026-10-27"}` |  |
| How many tickets of every priority except priority 3 did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except medium-priority did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P2 did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p2"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "priority": "p4"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get so far this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get last week? | `{"period": "2026-10-19/2026-10-25", "priority": "p4"}` | `{"period": "2026-10-19/2026-10-25"}` |  |
| How many tickets of every priority except P4 did we get this month? | `{"period": "2026-10-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many tickets of every priority except priority 4 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except low-priority did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p4"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get this year? | `{"period": "2026-01-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get so far this year? | `{"period": "2026-01-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get year to date? | `{"period": "2026-01-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get in 2026? | `{"period": "2026-01-01/2026-10-27", "priority": "p4"}` | `{"period": "2026-01-01/2026-10-27"}` |  |
| How many tickets of every priority except P4 did we get last year? | `{"period": "2025-01-01/2025-12-31", "priority": "p4"}` | `{"period": "2025-01-01/2025-12-31"}` |  |
