# Meaning check (README section 18)

Done by the agent on 2026-10-30, after `human.py` and before any extraction
of these questions was run. Each of the 480 questions was read against its
spec (goal, details, period) in `meaning_check.csv`.

**N, the question changes the meaning,** when it asks for something a
correct answer to the spec would not answer:
- a different quantity (revenue for net sales, amount billed for visits,
  tickets closed for tickets received);
- a different operation (how many, where the spec asks for a list);
- a lost or changed value (the exclusion dropped, 4 days for 4 hours);
- no period, or a period that does not say which one.

**Y otherwise,** including wording an analyst would read as the spec
without asking: "how many patients visited" for visits, "Q3" without a year
in October 2026, "the 5 customers by total spend" without "top", a question
that also asks whether any exist. Borderline Y rows carry a note.

Spelling, grammar, extra context ("across all channels", "based on my bank
statements") and stated date ranges matching the period do not count.

Result: 468 Y, 12 N (writer A 9, writer B 0, writer C 3). The hypotheses are
decided on all rows; `--exclude meaning` re-runs them without the 12.
