# Extraction: gemini:gemini-3.1-flash-lite

1202 questions. Frame accuracy (every slot right): **0.9334** [0.9006, 0.959]. Slot micro-F1 0.9747. Questions with a span or value note: 0.

Negation (priority_count_excluding vs priority_count, slot priority): excluded value wrong 45/116 (0.3879) vs included 1/122 (0.0082); difference 0.3797 [0.1466, 0.5893].

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 1175 | 27 | 27 | 0.9775 | 0.9775 | 0.9775 |
| team | 327 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| priority | 192 | 1 | 46 | 0.9948 | 0.8067 | 0.891 |
| service | 102 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 106 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| n | 196 | 8 | 0 | 0.9608 | 1.0 | 0.98 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 19 | 1.0 |
| last_12_months | 39 | 1.0 |
| last_30_days | 27 | 0.0 |
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
| Ticket intake for the cloud team in the last 30 days | `{"period": "2026-09-28/2026-10-27", "team": "cloud"}` | `{"period": "2026-09-27/2026-10-27", "team": "cloud"}` |  |
| Resolved ticket count for the database team in the last 30 days | `{"period": "2026-09-28/2026-10-27", "team": "database"}` | `{"period": "2026-09-27/2026-10-27", "team": "database"}` |  |
| Resolved ticket count for the security team in the last 30 days | `{"period": "2026-09-28/2026-10-27", "team": "security"}` | `{"period": "2026-09-27/2026-10-27", "team": "security"}` |  |
| How many tickets did the database team resolve in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "team": "database"}` | `{"period": "2026-09-27/2026-10-27", "team": "database"}` |  |
| Average time to resolve for the security team in the last 30 days | `{"period": "2026-09-28/2026-10-27", "team": "security"}` | `{"period": "2026-09-27/2026-10-27", "team": "security"}` |  |
| Average time to resolve for the network team in the last 30 days | `{"period": "2026-09-28/2026-10-27", "team": "network"}` | `{"period": "2026-09-27/2026-10-27", "team": "network"}` |  |
| How long did the database team take to resolve tickets on average in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "team": "database"}` | `{"period": "2026-09-27/2026-10-27", "team": "database"}` |  |
| Number of P3 tickets in the last 30 days | `{"period": "2026-09-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-09-27/2026-10-27", "priority": "p3"}` |  |
| How many P4 tickets were opened in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "priority": "p4"}` | `{"period": "2026-09-27/2026-10-27", "priority": "p4"}` |  |
| How many P2 tickets were opened in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "priority": "p2"}` | `{"period": "2026-09-27/2026-10-27", "priority": "p2"}` |  |
| How many high-priority tickets were opened last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p2"}` | `{"period": "2026-09-01/2026-09-30", "priority": "p1"}` |  |
| How many tickets were opened in the last 3 months, excluding high-priority ones? | `{"period": "2026-07-28/2026-10-27", "priority": "p2"}` | `{"period": "2026-07-28/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get in the previous month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get in September 2026? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P3 did we get this month? | `{"period": "2026-10-01/2026-10-27", "priority": "p3"}` | `{"period": "2026-10-01/2026-10-27"}` |  |
| How many tickets of every priority except P3 did we get in August 2026? | `{"period": "2026-08-01/2026-08-31", "priority": "p3"}` | `{"period": "2026-08-01/2026-08-31"}` |  |
| How many tickets of every priority except P3 did we get in the last 30 days? | `{"period": "2026-09-28/2026-10-27", "priority": "p3"}` | `{"period": "2026-09-27/2026-10-27"}` |  |
| How many tickets of every priority except priority 3 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except medium-priority did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p3"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P2 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p2"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets of every priority except P4 did we get last month? | `{"period": "2026-09-01/2026-09-30", "priority": "p4"}` | `{"period": "2026-09-01/2026-09-30"}` |  |
| How many tickets were opened in the last 30 days, excluding P4 ones? | `{"period": "2026-09-28/2026-10-27", "priority": "p4"}` | `{"period": "2026-09-27/2026-10-27", "priority": "p4"}` |  |
| How many tickets of every priority except P2 did we get this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
| How many tickets of every priority except P2 did we get so far this week? | `{"period": "2026-10-26/2026-10-27", "priority": "p2"}` | `{"period": "2026-10-26/2026-10-27"}` |  |
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
