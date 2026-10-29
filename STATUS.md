# Status and handoff: semantic-cache study

Read this first when resuming. README.md is the full record (sections 1–13).
This page is where things stand, so the next session does not re-derive it.

Last updated: 2026-10-28.

## The claim, as the evidence supports it today

Semantic caching of text-to-SQL fails on the **small words that change the
SQL**, and similarity cannot be tuned around them.

1. **Period words (this/last).** On the raw question, a one-word period swap
   outscores genuine rewordings for 82–98% of cached questions, in all 15
   embedding configurations from 2021 to 2026 (comparison A). This was
   confirmed on dataset v2 (H-A, section 12).
   - Fixable by design: mask the period out of the similarity, have the model
     *label* it, and let code or SQL compute the dates. That gives 0 period
     errors on 2,653 questions (section 13).
2. **Operator words (sum/count, except, refund/spend).** On unseen wording,
   template similarity confuses them even with perfect extraction. Safe reuse
   falls to 0–29%, against v1's artefactual 97% (section 12).
3. **Negated parameters ("except X").** The cheap extractor drops an excluded
   category in 16–36% of such questions while getting the same category right
   100% of the time when it is included. An unrelated prompt change doubled the
   rate. gemini-3.5-flash: 1% (section 13).

## Decisions on record

| Step | Decision | Where |
|---|---|---|
| Gate, H1 on four open models | **GO** | README section 7 |
| Step 5, real extraction | **O2**: the risk moves to extraction | section 10 |
| Relative-date arm, Part 1 | **R2**: broader than dates. Prediction R1 was **wrong**. | section 13 |
| v2 held-out replication, Part 2b | 3 of 4; **not met as registered**, because MiniLM reuses nothing | section 13 |
| Comparison A on v2 | **Confirmed**, lower bounds 0.81–0.96 | section 12 |

## Corrections already made (keep them made)

- `split_template` slot-order bug: +0.005 in each model; conservative.
  Section 4.
- "Extraction errors are invisible to similarity" becomes "a weak signal (AUC
  0.36–0.41), not a usable filter". Section 10.
- v1's 0.97 template reuse was the threat-1 artefact. Section 12.

## Open, in priority order

0. **Four-domain generalisation (README section 14, pre-registered).**
   - Domains: finance, retail, healthcare and IT support, in `data_md/`.
   - The author runs `.\run_extractions.ps1`: 24 flash-lite runs plus 4
     3.5-flash runs.
   - The agent then runs the embedders and tests G1–G4.
   - This also covers run-to-run variance, with three repeats.
1. **Human-written questions (step 4a).** Send `data_md/human_spec_sheet.csv`
   (160 rows, mixed domains) and `data_md/human_writer_instructions.md` to
   **three** people who are not the author.
   - `data_v2/human_spec_sheet.csv` is **superseded**. Do not send it.
   - Write the analysis pre-registration **before** opening the filled sheets.
   - Ingestion code is not written yet.
2. (Merged into item 0.)
3. **Fresh-generation comparison (step 4d).** Does the cache add errors relative
   to the production NLQ, which writes relative SQL?
4. **Blind label audit (step 2).** 150 rows of `data/review_sheet.csv`.
5. A second schema (step 4c). Needed for a major venue; optional for a
   workshop paper.

## Publication plan (agreed 2026-10-28)

The study goes public only once the human-question results are in and the
claim is final.

**Moving it to its own repo**
- Use `git subtree split --prefix=research/semantic-cache-inversion` into a
  separate public repo.
- **Keep the history.** It is the evidence that each pre-registration came
  before its results. Every study commit touches only this folder, which was
  checked. Do **not** squash it to one commit (unlike the finanalyticshub
  showcase).

**Before the first push**
- Replace private `backend/...` path references with plain descriptions.
- Remove the GCP project ID.
- Add a table mapping old commit hashes to new ones.
- Licences: MIT or Apache-2.0 for code, CC BY 4.0 for data.
- Add `CITATION.cff` and a dataset card.

**Release**
- Tag v1.0, then archive on Zenodo for a DOI.
- Post an arXiv preprint citing the repo and the DOI.
- Later: a workshop or conference submission, and a blog post.

## How the work is split

- **Credentialed runs (Vertex/Gemini, OpenAI, Voyage) are run by the author**
  (CLAUDE.md rule 1). Project `financial-insights-967`, `--workers 2`, which
  avoids 429s. Use `--limit 5` for a smoke test.
- Local runs (open embedders, Duckling in Docker on port 8010, evaluation) can
  be run by the agent.
- Commits only on an explicit request. Never push to `main`.

## Key commands

```
python generate_dataset.py --v2 --out data_v2
python extract.py [--data data_v2 --out results_v2/extraction] --extractor {gold|duckling|gemini:<m>|gemini-rel:<m>}
python evaluate.py [--data data_v2 --out results_v2] --embedder <e> [--holdout] [--extracted <extracted.jsonl>]
python evaluate.py --compare <report_A.json> <report_B.json>
python evaluate.py --summarize | --summarize-extraction
```
