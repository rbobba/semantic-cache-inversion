# Extraction: duckling

1358 questions. Frame accuracy (every slot right): **0.606** [0.5322, 0.6774]. Slot micro-F1 0.783. Questions with a span or value note: 0.

| Slot | TP | FP | FN | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| period | 835 | 312 | 523 | 0.728 | 0.6149 | 0.6667 |
| merchant | 506 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| category | 232 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| account | 110 | 0 | 0 | 1.0 | 1.0 | 1.0 |
| amount | 49 | 0 | 57 | 1.0 | 0.4623 | 0.6323 |
| n | 206 | 182 | 0 | 0.5309 | 1.0 | 0.6936 |

## Period accuracy by gold value

| Period | n | accuracy |
|---|---:|---:|
| aug_2026 | 14 | 0.8571 |
| last_12_months | 35 | 0.0 |
| last_30_days | 27 | 0.0 |
| last_3_months | 171 | 0.0 |
| last_6_months | 20 | 0.0 |
| last_month | 136 | 0.9265 |
| last_week | 42 | 0.9524 |
| last_year | 174 | 0.9425 |
| q2_2026 | 40 | 0.0 |
| q3_2026 | 172 | 0.1163 |
| this_month | 171 | 0.9181 |
| this_week | 172 | 0.9535 |
| this_year | 184 | 0.8261 |

## First 40 errors

| Question | gold | extracted | note |
|---|---|---|---|
| How much money went to Lyft in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| What did I pay Lyft in total in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| How much did I spend at Lyft in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| Sum of my purchases at Lyft in the last 3 months | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| How much money went to Lyft over the past three months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| How much money went to Lyft in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` | `{"n": 3, "merchant": "lyft"}` |  |
| How much did I spend at Lyft in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` | `{"n": 3, "merchant": "lyft"}` |  |
| How much money went to Lyft in the last 6 months? | `{"period": "2026-04-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-04-01/2026-09-30", "merchant": "lyft"}` |  |
| How much money went to Uber in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "uber"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "uber"}` |  |
| Sum of my purchases at Uber in the last 3 months | `{"period": "2026-07-28/2026-10-27", "merchant": "uber"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "uber"}` |  |
| How many times did I pay Lyft in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| On average, how much did each purchase at Lyft cost in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| How much money did Lyft give back to me in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "lyft"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "lyft"}` |  |
| Total expenses in the last 3 months | `{"period": "2026-07-28/2026-10-27"}` | `{"period": "2026-07-01/2026-09-30"}` |  |
| How much did I spend at Starbucks in the last 12 months? | `{"period": "2025-10-28/2026-10-27", "merchant": "starbucks"}` | `{"period": "2025-10-01/2026-09-30", "merchant": "starbucks"}` |  |
| What was my total spending at Netflix in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| How much money went to Netflix in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| Sum of my purchases at Netflix in Q3 2026 | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| Total spent at Netflix in Q3 2026 | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| What was my total spending at Netflix in Q2 2026? | `{"period": "2026-04-01/2026-06-30", "merchant": "netflix"}` | `{"n": 2, "merchant": "netflix"}` |  |
| Sum of my purchases at Netflix in Q2 2026 | `{"period": "2026-04-01/2026-06-30", "merchant": "netflix"}` | `{"n": 2, "merchant": "netflix"}` |  |
| What was my total spending at Netflix in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "netflix"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` |  |
| What was my total spending at Spotify in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` | `{"n": 3, "merchant": "spotify"}` |  |
| What did I pay Spotify in total in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` | `{"n": 3, "merchant": "spotify"}` |  |
| Number of purchases at Netflix in Q3 2026 | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| How much did I spend per transaction at Netflix in Q3 2026, on average? | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| What was the total of my returns to Netflix in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` | `{"n": 3, "merchant": "netflix"}` |  |
| How much money did I spend in total in Q3 2026? | `{"period": "2026-07-01/2026-09-30"}` | `{"n": 3}` |  |
| Sum of my purchases at Home Depot in the last 30 days | `{"period": "2026-09-28/2026-10-27", "merchant": "home_depot"}` | `{"period": "2026-09-27/2026-10-26", "merchant": "home_depot"}` |  |
| What did I pay Spotify in total in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| How much did I spend at Spotify in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| What was my total spending at Spotify in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| Total spent at Spotify in the last 3 months | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| What did I pay Spotify in total over the past three months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| How much money went to Spotify in Q3 2026? | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` | `{"n": 3, "merchant": "spotify"}` |  |
| What did I pay Spotify in total in the last 6 months? | `{"period": "2026-04-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-04-01/2026-09-30", "merchant": "spotify"}` |  |
| What did I pay Netflix in total in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "netflix"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` |  |
| How much did I spend at Netflix in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "netflix"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "netflix"}` |  |
| How many times did I pay Spotify in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
| On average, how much did each purchase at Spotify cost in the last 3 months? | `{"period": "2026-07-28/2026-10-27", "merchant": "spotify"}` | `{"period": "2026-07-01/2026-09-30", "merchant": "spotify"}` |  |
