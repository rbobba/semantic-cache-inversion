# Status and handoff: semantic-cache study

Read this first when resuming. README.md is the full record (sections 1–16).
This page is where things stand, so the next session does not re-derive it.

Last updated: 2026-10-29.

## The claim, as the evidence supports it today

Semantic caching of text-to-SQL fails on the **small words that change the
SQL**, and similarity cannot be tuned around them.

1. **Period words (this/last).** On the raw question, a one-word period swap
   outscores genuine rewordings for 78–100% of cached questions, in all 15
   embedding configurations from 2021 to 2026 and all four domains
   (comparison A; G1, section 19). The older "82–98%" was finance v1 only.
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
| Four domains: G1, G2, G3 / G4 | **Generalise** / **partially** (IT support's G4 is an artefact) | section 19 |
| Guarded cache: H-N, H-N-O / H-S, H-S-O | **Generalise** / **partially: finance only**, both vendors | section 19 |
| Full-signature guard on human questions | Pre-registered, **frozen 2026-10-30** (`af42f97e…`) after two pilots | section 18 |

## Corrections already made (keep them made)

- `split_template` slot-order bug: +0.005 in each model; conservative.
  Section 4.
- "Extraction errors are invisible to similarity" becomes "a weak signal (AUC
  0.36–0.41), not a usable filter". Section 10.
- v1's 0.97 template reuse was the threat-1 artefact. Section 12.
- arXiv:2601.11687 is an NL-to-pandas cache, not NL-to-SQL. Its numbers
  still hold. Section 17.

## Positioning (RELATED_WORK.md, checked 2026-10-29)

- Closest work: Bindschaedler 2026 (exact LLM intent signatures for OLAP)
  and Rathore et al. 2026 (COGNI: gated cache in production BI).
- **The guarded cache is not new; present it as tested, not proposed.**
- What is new: measuring the near-miss problem (comparison A), the industry
  template cache with real extractors, the negation asymmetry, the
  relative-time fix, and gated designs on held-out wording across domains
  and vendors, all pre-registered.
- Before submission, repeat the search in Scholar, Semantic Scholar and the
  VLDB/SIGMOD proceedings, and check papers citing the two closest works.

## Open, in priority order

**Now (2026-10-30):** section 18 is frozen after two pilots of the
full-signature prompt (no wrong reuse on held-out wording, either vendor).
Next, in order: the agent runs `human.py` on the three sheets and commits the
meaning check; the author runs `run_human_extractions.ps1` for each vendor
and `run_human_embeddings.ps1`; the agent runs `human_eval.py` and applies
section 18's rules. Items 0 and 1 below are otherwise done.

0. **Four-domain generalisation (README section 14, pre-registered).**
   - Domains: finance, retail, healthcare and IT support, in `data_md/`.
   - The author runs `.\run_extractions.ps1`: 24 flash-lite runs plus 4
     3.5-flash runs.
   - The agent then runs the embedders and tests G1–G4.
   - This also covers run-to-run variance, with three repeats.
   - Section 15 (guarded cache): the author runs `.\run_guard_extractions.ps1`
     after the Gemini runs above finish.
   - Section 16 (second extractor vendor, shortlist floor sweep): the author
     runs `.\run_openai_extractions.ps1 -SmokeOnly`, then without the switch.
     It can run alongside the Gemini scripts. Model `gpt-6-luna`, chosen by a
     written rule.
1. **Human-written questions (step 4a).** Send `data_md/human_spec_sheet.csv`
   (160 rows, mixed domains) and `data_md/human_writer_instructions.md` to
   **three** people who are not the author.
   - `data_v2/human_spec_sheet.csv` is **superseded**. Do not send it.
   - Each writer gets their **own copy** and answers all 160 rows.
   - Write the analysis pre-registration **before** opening the filled sheets.
   - Ingestion (`human.py`) and analysis (`human_eval.py`) were written and
     committed (`0c4edcf`) before any sheet was opened.
   - **All three sheets returned on 2026-10-29, unopened.** They are kept
     outside the repo. Recorded before the analysis pre-registration:

     | Writer | Saved | Bytes | SHA-256 |
     |---|---|---:|---|
     | 1 | 14:56 | 38,204 | `2a6af411070beb86e358ad710de24401f1daaa1219ac5a9153338fbeb1b531ba` |
     | 2 | 19:40 | 37,646 | `b4b93b68637c5cbce57854afd662b9cbcb94d54b1ea608be90396da54f3b80ac` |
     | 3 | 19:59 | 36,192 | `2c7dbdfc2e1bfc5d6f7917488f062940a66cb0184cdf9f0e3183ce9aa0846087` |

     Writer 1's sheet had been saved over the blank in `data_md/`; the blank
     was restored.
   - The committed blank had LF line endings, while the manifest and the
     generator use CRLF. The rows are identical. The generator's output was
     restored, so the file now matches `manifest.json` (`ba8ddbad…`).
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

## Results in git (from 2026-10-30)

- Committed: every `raw.jsonl` (what the model returned, which a rerun cannot
  reproduce), `extracted.jsonl`, `accuracy.*` and each `report.md`.
- Not committed: `results_md/**/report.json` (about 0.7 MB each). Each is
  rebuilt exactly from `extracted.jsonl` and the embedders pinned in
  `results_md/EMBEDDERS.txt`; `results_md/REPORTS_SHA256.txt` holds the hash
  of every one. Regenerate that file whenever reports are added. The full set
  goes to the release archive.
- `results_v2` keeps its committed `report.json` files, from before this
  rule.

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
