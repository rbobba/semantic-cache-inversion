# Parameter near-misses in semantic caching for text-to-SQL

A study plan, a labelled dataset, and an evaluation harness for one question:
**when a semantic cache reuses generated SQL, do questions that differ only in a
parameter look more alike than questions that mean the same thing?**

---

## 1. The problem statement

The sentence we started from —

> *In text-to-SQL, near-misses on parameters such as dates, merchants and
> accounts score higher than correct rephrasings. No threshold, global or
> per-entry (vCache), can separate them. Only splitting the parameters out of
> the embedding can.*

— is **a hypothesis plus a conclusion, not a problem statement**, and two of
its three sentences overclaim:

- *"score higher"* is, so far, one measurement on one embedding model
  (text-embedding-004: 0.9953 for "this month" against "last month", 0.9780 for
  the best correct rephrasing, recorded in `backend/src/fin_insights/config.py`).
- *"No threshold … can"* is only provable **at zero false reuse**, and only
  against an oracle bound (section 4). vCache trades a user-set error rate for
  hits; at a non-zero error rate it can and will reuse.
- *"Only splitting … can"* is unfalsifiable as worded, and the baseline run
  below already shows it is incomplete: splitting out parameters does nothing
  for questions that share every parameter but compute something different
  (sum vs count, spend vs refunds, X vs everything except X).

### Problem statement (use this)

> Semantic caches for LLM-generated SQL reuse a stored query when a new
> question's embedding is close enough to a cached one. In analytical questions,
> the tokens that most change the answer — the time window, the merchant, the
> account, the threshold — are short spans inside otherwise identical wording.
> We ask whether sentence embeddings place such **parameter near-misses** closer
> to the cached question than genuine rephrasings; if so, how much safe reuse any
> similarity threshold can deliver, global or per cache entry; and how much a
> design that **separates parameters from the embedded text** recovers, and what
> it leaves unsolved.

### Research questions

| | Question | Measured by |
|---|---|---|
| RQ1 | How often does a parameter near-miss score at or above the best correct rephrasing of the same cached question, across embedding models and parameter types? | Strong/weak inversion rate per cached question (report section B) |
| RQ2 | At zero false reuse, what share of queries can a global threshold reuse correctly, and what is the ceiling for any per-entry threshold? | `raw_global`, `raw_oracle_entry` (report section C) |
| RQ3 | How much does parameter separation recover, under oracle and under real parameter extraction, and which near-misses remain? | `split_full`, `split_template`; residual by `intent_near_miss` dimension |

### Hypotheses — pre-registered 2026-10-28, before any neural model was run

These were committed before the first neural embedding was computed; that commit
is the evidence. A threshold chosen after seeing results is not a test.

- **H1 (inversion is general) — the go/no-go rule.**
  - **Metric:** the strong inversion rate in the `param_near_miss` row of
    report section B. It is the share of cached questions where some parameter
    near-miss scores ≥ the best correct question.
  - **GO** only if, in **all 4** open models below, the rate is ≥ **0.30** and
    the lower bound of its 95% bootstrap CI is > **0.20**.
  - **Otherwise NO-GO.** Narrowing to a single dimension (period only, say) after
    the fact counts as a new hypothesis, to be tested on fresh data, not as a pass.
  - **The 4 models:**
    - `sentence-transformers/all-MiniLM-L6-v2`
    - `sentence-transformers/all-mpnet-base-v2`
    - `BAAI/bge-base-en-v1.5`
    - `intfloat/e5-base-v2`, with the `"query: "` prefix
  - **text-embedding-004** (the production model) is reported alongside, but it
    does not count toward the rule. It is the model the observation came from,
    so it cannot also be the test of generality.
  - **The lexical TF-IDF control** does not count either.
  - **Dataset:** `pairs.jsonl` SHA-256 `2fbf585caab5daaa70283afbd96f1e960dd8abcf509d9969129cfd3cadfd75bb`,
    `questions.jsonl` SHA-256 `91f52c7c28f373ba5759982f1cddc3ca5fa031ca518f843ab1f493be65d446d3`
    (generator 1.0.0, seed 20261027).
  - **Deviation from the plan:** step 2, the blind label audit, is deferred so
    the gate can run first. If the audit changes any label, the gate is re-run on
    the corrected dataset, and both results are reported.
- **H2 (thresholds cannot recover it).** At zero false reuse, `raw_oracle_entry`
  reuses less than half of what `split_full` reuses. *Secondary; adopted as
  originally proposed. Not part of the go/no-go.*
- **H3 (separation is incomplete).** *Secondary; adopted as originally proposed.* Under parameter separation, intent
  near-misses (aggregation, direction, negation, measure, grouping) remain the
  dominant source of false reuse.

### The claim the paper can make if H1–H3 hold

> Parameter near-misses invert the similarity ordering that threshold-based
> semantic caches rely on. Where the inversion occurs, no per-entry threshold
> yields a correct reuse without a false one. Moving parameters into the cache
> key recovers X% safe reuse where thresholds recover Y%, and leaves intent
> near-misses as the open problem.

The argument that turns an observation into a result is the **oracle bound**
(section 4): it covers vCache and every other per-entry method at zero error,
without having to reimplement them.

---

## 2. What is in this folder

| File | Purpose |
|---|---|
| `generate_dataset.py` | Builds the dataset deterministically from a seed. Labels are computed from structure, never typed. |
| `data/questions.jsonl` | 1,358 questions. Each has `text`, `masked_text` (parameters replaced by `[PERIOD]`, `[MERCHANT]`, …), `intent`, normalised `params`, and `is_anchor`. |
| `data/pairs.jsonl` | 1,496 labelled pairs (cached question → new question) with `relation`, `dimension`, `kind`, `same_wording`, `same_sql`, `same_template`. |
| `data/review_sheet.csv` | The same pairs, shuffled, **labels removed** — for the blind second labeller (step 2). |
| `data/manifest.json` | Seed, reference date, counts by pair type, label rules, SHA-256 of every file. |
| `evaluate.py` | Embeds with one model, writes `results/<model>/report.md` and `report.json`. `--summarize` builds the cross-model table. |
| `requirements.txt` | numpy always; sentence-transformers or google-genai depending on the embedder. |

### How labels are defined

Every question is rendered from an intent (what is computed), a template (the
wording), and parameter values with a chosen surface form. Two questions are:

- **`same_sql`** when the intent and the normalised parameters are equal.
  Periods are normalised to absolute date ranges against a fixed reference date
  of **2026-10-27**, which is why "last month" and "in September 2026" are
  equivalent and "last month" and "in the last 30 days" are not.
- **`same_template`** when the intent is equal. This is the label for a design
  that reuses the SQL *template* and refills the parameters.

### What the pairs are

| Relation | `same_sql` | What it tests | Count |
|---|---|---|---:|
| `paraphrase` | ✔ | Different template, same intent and parameters | 384 |
| `equivalent_surface` | ✔ | Same template, one parameter reworded with the same value ("Costco" → "Costco Wholesale", "last month" → "in September 2026") | 262 |
| `param_near_miss` | ✘ | One parameter changed to a confusable value. Period: `adjacent` (this → last month) or `granularity` (last month → last 30 days). Also merchant, category, account, amount, top-N. Mostly the same template; one reworded version per slot | 637 |
| `intent_near_miss` | ✘ | Same parameters, different computation: aggregation, direction, negation, measure, grouping | 176 |
| `filter_change` | ✘ | A filter dropped or added | 37 |

`equivalent_surface` exists so that one-span negatives are always set against
one-span positives. Without it, a reviewer could say the near-misses win only
because they share a template with the cached question.

---

## 3. Running it

```bash
cd research/semantic-cache-inversion
python -m venv .venv && .venv/Scripts/activate      # Windows; source .venv/bin/activate elsewhere
pip install -r requirements.txt

python generate_dataset.py --out data               # deterministic; check the hashes match manifest.json
python evaluate.py --embedder tfidf                 # lexical control, no download
python evaluate.py --embedder st:sentence-transformers/all-MiniLM-L6-v2
python evaluate.py --embedder st:sentence-transformers/all-mpnet-base-v2
python evaluate.py --embedder st:BAAI/bge-base-en-v1.5
python evaluate.py --embedder st:intfloat/e5-base-v2 --prefix "query: "
python evaluate.py --summarize                      # writes results/SUMMARY.md
```

The model list is a starting point: two older general-purpose models and two
current retrieval models. Check each model card for its recommended input
prefix before running it — e5 requires `"query: "`, and a missing prefix is a
reviewer's easy objection.

**text-embedding-004 (the production model).** This calls Vertex AI with your
credentials, so run it yourself:

```bash
gcloud auth application-default login
python evaluate.py --embedder vertex:text-embedding-004 --project <your-project>
python evaluate.py --embedder vertex:text-embedding-004 --project <your-project> --task-type SEMANTIC_SIMILARITY
```

The first call mirrors the application exactly: 768 dimensions and no task
type, as in `backend/src/fin_insights/adapters/llm/embedding_service.py`. The
second shows whether the task type changes the picture. About 1,500 short texts
cost a fraction of a cent at the rate in `observability/pricing.py`.

**Any other model** (OpenAI, Cohere, a local server): write an `.npz` file with
two arrays, `texts` and `vectors`, covering every `text` and `masked_text` in
`questions.jsonl`, then run `--embedder npz:path/to/file.npz`.

---

## 4. How to read a report

**Section A — similarity by pair type.** The motivating table. The finding
holds for a model when `param_near_miss` sits at or above `paraphrase` and
`equivalent_surface`. Compare the `same wording=True` rows separately; they
answer "is it just template overlap?"

**Section B — inversion per cached question.**
- *Strong inversion*: the best-scoring wrong question scores ≥ the best correct
  one. At that cached entry, **no threshold of any kind** produces a correct
  reuse without first producing a false one.
- *Weak inversion*: it scores ≥ the worst correct one, so no threshold catches
  every correct rephrasing safely.
- Rows split the wrong questions into period, entity (merchant, category,
  account, amount, top-N) and intent near-misses. RQ1's answer is the
  `param_near_miss` row.

**Section C — cache simulation.** The 128 anchors are the cache; the 1,230 other
questions are incoming queries routed to their nearest cached entry.
- `correct reuse at 0% false reuse` — the share of all queries reused
  correctly at the best threshold that produces no false reuse.
- `raw_oracle_entry` chooses a separate threshold for every cached entry using
  the labels. That is cheating on purpose: it is the **ceiling** for vCache and
  any other per-entry method at zero error. If the ceiling is low, the
  per-entry argument is settled without reimplementing anything.
- `possible` — the share of queries for which a correct cached entry exists at
  all. It is the denominator that keeps the other numbers honest.
- Confidence intervals come from a cluster bootstrap: each cached question and
  the queries generated from it are resampled together, and the cache is held
  fixed.

### Baseline result (TF-IDF, lexical control)

Run 2026-10-27 on dataset `pairs.jsonl` SHA-256 `2fbf585c…`, 1,000 resamples:

| Design | Correct reuse at 0% false reuse [95% CI] | Possible |
|---|---|---:|
| raw_global | 0.000 [0.000, 0.000] | 0.532 |
| raw_oracle_entry | 0.002 [0.001, 0.011] | 0.532 |
| split_full (oracle params) | 0.225 [0.210, 0.242] | 0.532 |
| split_template (oracle params) | 0.952 [0.937, 0.965] → **0.957 [0.942, 0.970]** | 0.995 → **1.000** |

Strong inversion against parameter near-misses: 0.992 [0.977, 1.000].

*Correction, 2026-10-28:* `split_template` compared slot lists in template
order, so "…{period}, not counting {category}" and "…except {category}
{period}" counted as different slots and some valid reuses were skipped. It now
compares slot sets. The error was conservative: it never caused a false reuse.
It changed only the `split_template` column, by +0.005 in every model; every
other number was rerun and is identical. Found by the gold-extraction
sanity check in section 9.

**This proves nothing about embeddings** — a word-overlap model is bound to score
"this month" close to "last month". It is here to verify the harness, and as the
control that any neural model must be compared with. Two things in it are worth
noticing, though:

1. `split_full` reaches only 0.225 of a possible 0.532. With the parameters
   exact, what still forces the threshold up is intent near-misses: "How much did
   I spend at [MERCHANT] [PERIOD]?" against "How many transactions did I have at
   [MERCHANT] [PERIOD]?". That is H3, showing up in the control already.
2. `split_template` at 0.957 is **inflated by construction** — see threat 1.

---

## 5. Threats to validity — built into this dataset

Read these before trusting any number, and put them in the paper.

1. **Closed template vocabulary.** Every question comes from 4–6 templates per
   intent, so a query's masked text often exactly matches a cached entry's, and
   the `split_*` designs score well partly for that reason. Real users do not
   write from templates. Step 4a fixes this, and **no claim about `split_*`
   should be made until it has**.
2. **Rephrasings are templated too.** Lexical diversity among the positives is
   limited. That makes the raw inversion more likely in neural models than real
   traffic would, not less — another reason for step 4a.
3. **Reference-date semantics.** "This year" and "in 2026" are labelled
   equivalent because no transaction can be dated after the reference date.
   Someone could reasonably disagree. Step 4d replaces these definitions with
   execution results.
4. **Oracle extraction.** The `split_*` designs are given the gold parameters.
   Step 5 measures the cost of real extraction.
5. **One domain, one schema, English only.**
6. **Labels are equivalence of intent and parameters, not of query results.**
   Step 4d closes this.

---

## 6. Step-by-step plan

Each step ends in an artefact; don't start the next without it.

### Step 1 — Freeze the labels (½ day)
1. Regenerate and confirm the hashes in `data/manifest.json` match.
2. Write your H1–H3 thresholds into section 1 of this file.
3. Commit the dataset, the manifest and this README **before embedding with any
   neural model**. The commit is your evidence that labels and thresholds came
   first.

*Artefact: a commit hash that predates every neural result.*

### Step 2 — Audit the labels blind (1 day, needs a second person)
1. Give a colleague 150 random rows of `data/review_sheet.csv`. It has no labels
   and no relation types. Ask them to fill `reuse_sql_is_correct` with Y or N.
2. Compute agreement with `same_sql`:
   ```python
   import csv, json
   gold = {json.loads(l)["pair_id"]: json.loads(l)["same_sql"] for l in open("data/pairs.jsonl", encoding="utf-8")}
   rows = [r for r in csv.DictReader(open("filled_sheet.csv", encoding="utf-8")) if r["reuse_sql_is_correct (Y/N)"]]
   a = [gold[r["pair_id"]] for r in rows]; b = [r["reuse_sql_is_correct (Y/N)"].strip().upper() == "Y" for r in rows]
   po = sum(x == y for x, y in zip(a, b)) / len(a)
   pe = (sum(a) / len(a)) * (sum(b) / len(b)) + (1 - sum(a) / len(a)) * (1 - sum(b) / len(b))
   print(f"n={len(a)} agreement={po:.3f} kappa={(po - pe) / (1 - pe):.3f}")
   ```
3. Read every disagreement. If a whole class is disputed (for example "this
   year" against "in 2026"), change the rule in the generator, regenerate, and
   recommit — this is the one moment you may change labels.

*Artefact: kappa, plus a list of disagreements and how each was resolved.
Kappa ≥ 0.8 is a common bar for "the labels are not the problem".*

### Step 3 — The go/no-go run (1–2 days)
1. Run the lexical control and the four open models from section 3. Then run
   text-embedding-004 yourself, with and without `SEMANTIC_SIMILARITY`.
2. `python evaluate.py --summarize`, then compare the `param_near_miss`
   column with your H1 threshold.
3. **Decide:**
   - **Go** if H1 holds. The inversion is a property of embeddings, not of one
     model.
   - **Stop** if it shows only in text-embedding-004 or only in the lexical
     control. The claim then shrinks to "scores overlap", which vCache already
     reports. Move to the alternative topic (accounting identities as a
     label-free extraction check).
   - **Narrow** if it holds for periods but not for entities, or the reverse. A
     paper about temporal near-misses alone is still a paper.
4. Sanity check: the new data should reproduce the original production
   observation. In the text-embedding-004 report, look for a
   "this month"/"last month" merchant pair scoring above that anchor's best
   rephrasing.

*Artefact: `results/SUMMARY.md` and a written go/no-go decision.*

### Step 4 — Make the dataset defensible (1–2 weeks)
- **4a. Human-written queries (the most important step).** Give 2–3 people a
  list of specifications — intent plus parameters, never a template — and ask
  each to write 2–3 questions however they would naturally ask. For example: "you
  want the number of purchases at Target in September 2026". Aim for 300+
  questions. Label them from the specification, then use them as held-out
  queries against the generated cache. This addresses threats 1 and 2.
  Extending `generate_dataset.py` to read a CSV of `spec_id, intent, params,
  text` is a small change.
- **4b. Template hold-out.** Split each intent's templates into a cache half and
  a query half, so no query can match a cached template exactly. This is a
  generator option worth adding, and it is cheaper than 4a, though weaker.
- **4c. A second schema.** Re-run on a public text-to-SQL benchmark database.
  Verify which benchmarks include a finance-like database before choosing one;
  I have not checked BIRD's or Spider's contents.
- **4d. Execution-equivalence labels.** Write gold SQL for each intent, run each
  question's SQL against a small synthetic transactions table, and confirm that
  `same_sql` holds exactly when the result sets match. This removes threats 3
  and 6.

*Artefact: dataset v2 with its own manifest, plus a short labelling protocol.*

### Step 5 — Real parameter extraction (3–5 days)
1. Build an extractor that returns normalised parameters and the spans to mask:
   rules plus a date normaliser, or an LLM with a structured-output schema
   (the application already enforces response schemas for extraction).
2. Report slot accuracy on its own, by slot type.
3. Re-run the `split_*` designs with extracted parameters in place of gold ones
   (add a `--params-file` option to `evaluate.py`). Report the gap to the oracle.
   That gap is the honest cost of the design.

*Artefact: an extraction accuracy table and split-design results under real
extraction.*

### Step 6 — Stronger baselines (3–5 days)
Reviewers will ask "why not just verify before reusing?" Answer with numbers:
- **vCache itself** at its own error bounds, if the authors' code is public (check
  first). Report it at δ = 1% and 5% alongside the oracle bound at 0%.
- **A cross-encoder verifier** run on the top-1 match before reuse.
- **An LLM judge** run on the top-1 match. Record its cost and added latency per
  query, because a verification call can cost more than the generation the
  cache was meant to save.

*Artefact: one table of correct reuse, false reuse, added latency and cost per
query, by design.*

### Step 7 — Statistics that survive review (1–2 days)
- Keep the cluster bootstrap. Regenerate the dataset with 3 seeds and report
  how much the results vary between them.
- Report every number per dimension (period adjacent, period granularity,
  merchant, category, account, amount, top-N; and each intent relation).
- Report the thresholds that achieved each headline number. A reader should be
  able to deploy the result.

### Step 8 — Literature check before writing (½ day)
Already known, from 2026-10-27 searches:
- **vCache** (arXiv 2502.03771): a global threshold is insufficient, so it
  learns a threshold per entry under an error bound.
- **MeanCache** (arXiv 2403.02694): the false-hit versus missed-hit trade-off.
- **AWS architecture blog**: parameterised Text2SQL templates, with no false-reuse
  evaluation.
- **arXiv 2605.20630**: time-aware semantic caching for agent plans; proposes
  parameter-aware caching as future work.

Before drafting, search arXiv and the ACL Anthology for "NL2SQL cache", "text-to-SQL
semantic cache", "query template cache", "temporal expressions sentence
embeddings" and "numeracy embeddings". If someone has published an evaluated
parameter-separated Text2SQL cache, your contribution narrows to the inversion
measurement and the oracle bound. That is still publishable, but it changes the
framing.

### Step 9 — Write-up
Outline:
1. Introduction — the Costco "this month" / "last month" example and the
   production numbers.
2. Background — semantic caching, vCache, MeanCache, template caching.
3. Definitions — strong and weak inversion, and the oracle per-entry bound with
   its one-paragraph proof: if strong inversion holds at entry *e*, no
   threshold at *e* admits a correct reuse without a false one.
4. Dataset and labelling protocol, including kappa.
5. RQ1 — inversion across models and dimensions.
6. RQ2 — thresholds against the oracle bound.
7. RQ3 — parameter separation under oracle and real extraction; the intent
   near-misses that remain.
8. Threats to validity (section 5).
9. Release: dataset, generator and harness.

**Venue.** Aim realistically at an IEEE conference industry or practitioner
track, a workshop on LLM systems or data management, or a practitioner magazine
article. A top-tier research venue would need the 4a/4d dataset at larger scale
and a stronger novel method than parameter separation.

### When to stop

- H1 fails in step 3.
- Step 8 finds an evaluated parameter-separated Text2SQL cache, *and* someone
  has already reported the inversion.
- Kappa in step 2 stays below about 0.7 after one round of rule fixes. That
  means the task itself is ambiguous, which is a different paper.

---

## 7. Gate result — 2026-10-28: **GO**

Judged against the H1 rule pre-registered in commit `7ca986a`, on dataset
`pairs.jsonl` `2fbf585c…`, with 1,000 cluster-bootstrap resamples.

The table shows strong inversion against parameter near-misses. **Rule: ≥ 0.30,
with the CI lower bound > 0.20, in all 4 open models.**

| Model | Counts toward rule | Strong inversion [95% CI] | Passes |
|---|---|---|---|
| all-MiniLM-L6-v2 | yes | 0.469 [0.383, 0.555] | ✔ |
| all-mpnet-base-v2 | yes | 0.586 [0.508, 0.672] | ✔ |
| bge-base-en-v1.5 | yes | 0.562 [0.477, 0.648] | ✔ |
| e5-base-v2 (`query: `) | yes | 0.547 [0.461, 0.641] | ✔ |
| text-embedding-004 (production configuration) | no | 0.523 [0.438, 0.617] | — |
| text-embedding-004, `SEMANTIC_SIMILARITY` | no | 0.484 [0.398, 0.578] | — |
| TF-IDF (lexical control) | no | 0.992 [0.977, 1.000] | — |

H1 holds in all four. The production model and its similarity task type agree,
so the task type does not remove the effect.

### What the result is — and is not

**1. It is temporal, not "parameters" in general.**
- In every neural model, every strong inversion was caused by a **period**
  near-miss.
- Entity near-misses (merchant, category, account, amount, top-N) invert for
  only 0–2% of cached questions.
- Entities do still **overlap** with correct rephrasings. Their weak inversion is
  61–88%, so a threshold that keeps every rephrasing admits them. They are
  unsafe, but they are not inverted.
- The registered metric passed as registered. The paper's claim, however, must
  be about time expressions, not about "dates, merchants and accounts".

**2. Specifically, it is relative ("this" ↔ "last") time expressions.** The table
shows strong inversion by the cached question's period. Six of the seven periods
are shown; the seventh, `last_month`, ranges from 0.57 to 0.71.

| Cached period | MiniLM | mpnet | bge | e5 | text-emb-004 |
|---|---:|---:|---:|---:|---:|
| this_week | 0.38 | 0.71 | 0.81 | 0.81 | 0.81 |
| this_month | 0.59 | 0.76 | 0.76 | 0.82 | 0.76 |
| this_year | 0.42 | 0.63 | 0.84 | 0.84 | 0.74 |
| last_year | 0.88 | 0.76 | 0.76 | 0.82 | 0.76 |
| q3_2026 (neighbour Q2 2026) | 0.55 | 0.65 | 0.15 | 0.00 | 0.00 |
| last_3_months (only granularity neighbours) | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

- **Relative calendar periods invert in every model.**
- **Explicit quarters** ("Q3 2026" → "Q2 2026") are separated correctly by three
  of the five neural models.
- **Granularity changes** ("last 3 months" → "last 6 months" or "Q3 2026") never
  invert.

**3. The "embeddings can't know today's date" objection does not explain it.**
- 65 of the 646 correct pairs need the reference date to be equivalent, such as
  "last year" ↔ "during 2025".
- Recomputing inversion without them leaves every rate **unchanged**, in every
  model.
- So each inverted question's near-miss outscores even the rephrasings that need
  no date knowledge. For example: "What were my overall expenses **this** year?"
  scores 0.984 against "… **last** year?", while "What was my total spending last
  year?" scores 0.875 (mpnet).

**4. Secondary hypotheses, under the step-5 caveats** (oracle parameters,
templated wording):
- **H2 holds.** At zero false reuse, the per-entry oracle reuses 6.6–11.0% of
  queries; `split_full` reuses 21.3–27.3%. A global threshold reuses 0.5–1.8%.
- **H3 holds by construction of `split_full`.** With parameters exact, the only
  remaining false candidates are intent near-misses, and they hold `split_full`
  to about 0.22–0.27 of a possible 0.53.
- `split_template`'s 0.96 is the template artefact described in section 5
  (threat 1), and supports no claim. (After the slot-order correction in
  section 4, it is 0.96–1.00.)

### Consequence for the problem statement

> Relative time expressions ("this month" / "last month") invert the similarity
> ordering that threshold-based semantic caches rely on, in all six neural
> embedding configurations tested. For about half of cached questions, the
> wrong-period question scores at or above every correct rephrasing, so no
> threshold of any kind reuses them safely. Other parameters (merchants,
> categories, accounts) overlap with correct rephrasings but do not invert.

Next: step 2 (the blind label audit), then step 4a (human-written questions).
The period finding needs testing above all on questions people actually write.

---

## 8. Extended evaluation — 2026-10-28 (after the gate, not part of it)

Eleven more configurations were run on the same frozen dataset: Google's
`gemini-embedding-001`, three Voyage models (Voyage is the provider Anthropic's
documentation points to, since Anthropic has no embedding model of its own),
OpenAI's `text-embedding-3-small` and `text-embedding-3-large` (default
dimensions), and three recent open models. AWS models were not run.

### Results

The table shows the pre-registered metric (strong inversion against parameter
near-misses), plus correct reuse at zero false reuse.

| Model | Year | Strong inversion [95% CI] | Global threshold @0 | Oracle per-entry @0 | split_full @0 |
|---|---|---|---:|---:|---:|
| all-MiniLM-L6-v2 | 2021 | 0.469 [0.383, 0.555] | 0.008 | 0.071 | 0.213 |
| all-mpnet-base-v2 | 2021 | 0.586 [0.508, 0.672] | 0.018 | 0.066 | 0.215 |
| e5-base-v2 | 2023 | 0.547 [0.461, 0.641] | 0.009 | 0.081 | 0.214 |
| bge-base-en-v1.5 | 2023 | 0.562 [0.477, 0.648] | 0.005 | 0.081 | 0.218 |
| text-embedding-3-small | 2024 | 0.562 [0.477, 0.648] | 0.002 | 0.064 | 0.214 |
| text-embedding-3-large | 2024 | 0.414 [0.328, 0.508] | 0.012 | 0.098 | 0.225 |
| mxbai-embed-large-v1 | 2024 | 0.508 [0.422, 0.594] | 0.006 | 0.106 | 0.226 |
| snowflake-arctic-embed-l-v2.0 | 2024 | 0.508 [0.422, 0.594] | 0.021 | 0.107 | 0.224 |
| text-embedding-004 | 2024 | 0.523 [0.438, 0.617] | 0.005 | 0.093 | 0.242 |
| text-embedding-004, SEMANTIC_SIMILARITY | 2024 | 0.484 [0.398, 0.578] | 0.011 | 0.110 | 0.273 |
| voyage-3-large | 2025 | 0.297 [0.219, 0.375] | 0.011 | 0.144 | 0.272 |
| voyage-3.5 | 2025 | 0.445 [0.352, 0.539] | 0.006 | 0.114 | 0.249 |
| gemini-embedding-001 | 2025 | 0.438 [0.352, 0.531] | 0.002 | 0.102 | 0.320 |
| Qwen3-Embedding-0.6B | 2025 | 0.219 [0.156, 0.297] | 0.011 | 0.112 | 0.215 |
| voyage-4 | 2026 | **0.156 [0.102, 0.227]** | 0.063 | 0.168 | 0.300 |

Years are approximate release years.

Correct reuse is possible for 0.532 of queries in every row.

**Under the pre-registered rule, voyage-4, Qwen3 and voyage-3-large would not
pass.** Strong inversion falls in the newest models.

### What is actually falling — decomposed (exploratory, defined after seeing the data)

Strong inversion takes the best of **all** correct questions. Those come in two
kinds, and the newest models treat them differently. So the comparison was
split. In both, the period near-miss uses the same wording as the cached
question, with only the period changed.

- **A — period swap ≥ the best *reworded* correct question** (a different
  template, the same meaning). This is how users usually rephrase.
- **B — period swap ≥ the best *one-span* correct question** that needs no date
  knowledge ("this month" → "so far this month", "last month" → "in the previous
  month").

| Model | A: swap ≥ reworded [95% CI] | B: swap ≥ one-span [95% CI] |
|---|---|---|
| all-MiniLM-L6-v2 | 0.96 [0.93, 0.99] | 0.54 [0.45, 0.63] |
| all-mpnet-base-v2 | 0.97 [0.94, 0.99] | 0.69 [0.61, 0.77] |
| e5-base-v2 | 0.92 [0.88, 0.97] | 0.61 [0.52, 0.71] |
| bge-base-en-v1.5 | 0.88 [0.81, 0.93] | 0.70 [0.62, 0.78] |
| text-embedding-3-small | 0.98 [0.95, 1.00] | 0.75 [0.67, 0.83] |
| text-embedding-3-large | 0.95 [0.90, 0.98] | 0.56 [0.47, 0.65] |
| mxbai-embed-large-v1 | 0.87 [0.80, 0.92] | 0.56 [0.46, 0.65] |
| snowflake-arctic-embed-l-v2.0 | 0.84 [0.78, 0.90] | 0.56 [0.47, 0.65] |
| text-embedding-004 | 0.92 [0.88, 0.96] | 0.59 [0.50, 0.68] |
| text-embedding-004, SEMANTIC_SIMILARITY | 0.90 [0.84, 0.95] | 0.54 [0.45, 0.64] |
| voyage-3-large | 0.82 [0.75, 0.89] | 0.44 [0.35, 0.53] |
| voyage-3.5 | 0.91 [0.87, 0.96] | 0.50 [0.41, 0.60] |
| gemini-embedding-001 | 0.93 [0.88, 0.97] | 0.44 [0.35, 0.53] |
| Qwen3-Embedding-0.6B | 0.95 [0.91, 0.98] | 0.21 [0.14, 0.28] |
| voyage-4 | 0.84 [0.77, 0.90] | 0.14 [0.07, 0.21] |

Sample sizes: A has n = 128 cached questions, B has n = 111.

**Reading:**
- **A is stable across every model and year, at 0.82–0.98.** A one-word period
  swap of a cached question outscores every differently-worded correct question
  for most cached questions, in the newest models too.
- **B is what is improving.** The newest models increasingly rank "so far this
  month" above "last month" when the rest of the wording is identical. This is
  what moves the strong-inversion rate.
- **Operationally, A is the one that matters.** A cache's value is catching
  rewordings, and a threshold low enough to accept a reworded question accepts
  the period swap first for 82–98% of cached questions.
- **OpenAI fits the same pattern.** Both 2024 models invert A (0.95, 0.98).
  `text-embedding-3-small` has the highest B of any model (0.75), and the larger
  `text-embedding-3-large` is lower (0.56). Size alone does not explain B across
  vendors (mpnet is larger than MiniLM and scores higher). B declines roughly
  with release date: 0.54–0.75 for 2021–2024 models, 0.21–0.50 for 2025, 0.14
  for 2026. That is 15 uncontrolled models, so it is a trend, not a finding.
  Neither OpenAI model separates the reworded case.
- **The cache simulation agrees.** Even the best model (voyage-4) reuses only
  6.3% of queries safely with a global threshold, against 53% possible.

### A confound this exposed (fix in dataset v2)

`last_year` has no one-span correct question that avoids a date, because its
only aliases are "in 2025" and "during 2025". So its 17 cached questions are
missing from comparison B. They also keep strong inversion high (0.71–0.76) in
every model, newest included. That persistence is a gap in the dataset, not a
finding.

Dataset v2 should give every period a one-span alias that needs no date (for
`last_year`: "the previous year", "the prior year"). Changing the frozen v1
dataset is not allowed.

### Revised claim (exploratory until confirmed on fresh data)

> When a cached analytical question is repeated with only its time period
> changed ("this month" → "last month"), the new question scores higher than
> differently-worded questions with the same meaning, for 82–98% of cached
> questions, in all 15 embedding configurations tested (2021–2026): three
> commercial APIs (Google, Voyage, OpenAI) and six open-model publishers.
> Newer models increasingly separate period swaps from minimally edited
> equivalents, but not from reworded ones. So a global similarity threshold
> cannot accept rewordings without also accepting wrong-period reuse.

Comparisons A and B were defined after seeing results. They are exploratory, and
the paper must present them that way. Confirm them on dataset v2 with
human-written questions (step 4a), with A and B pre-registered before that run.

---

## 9. Step 5 pre-registration — real parameter extraction (frozen 2026-10-28)

Written and committed before any LLM extractor was run on any dataset question.
The one exception, Duckling on the period wordings, is disclosed below.

### Question

How often does the template cache reuse SQL wrongly, and why, when the
parameters come from a real extractor rather than the gold labels? This is the
second half of RQ3. Industry practice has moved to this design (see the sources
below), but none of the sources found reports a false-reuse rate for it.

### Extractors (`extract.py`)

| Arm | Role | What it is |
|---|---|---|
| `gemini:gemini-3.1-flash-lite` | **primary** | The application's query-path model (`rewriter_model`, `backend/src/fin_insights/config.py:123`), called the way the app calls Gemini: temperature 0, `response_json_schema` enforced (`vertex_client.py:1618-1625`), location `global` (`config.py:105`). |
| `gemini:gemini-3.5-flash` | secondary | The application's `nlq_model` (`config.py:121`), called the same way. |
| `duckling` | secondary | Rule-based. Image `rasa/duckling@sha256:459e6033f87b0f3f525ed0d0066ae89cfe31d512f32ac1d469431fa6ce1bdef5` (built 2022-04-21). Handles period, amount and top-N; it is not told the dataset's conventions. Merchants, categories and accounts come from a gazetteer of the dataset's own wordings, which is an **entity oracle**, so this arm measures temporal and numeric extraction only. |
| `gold` | sanity check | The labels. It must reproduce the oracle designs exactly, and it does (bge, every number identical). |

**What the Gemini prompt states:**
- the reference date
- the dataset's date conventions, as a production prompt states its own
- the canonical ids of merchants, categories and accounts, since an app knows its own taxonomy and the user's accounts

Aliases ("Costco Wholesale", "fuel", "American Express card") are **not** listed;
mapping them is part of the task.

### Metrics

**Extraction**
- Slot precision, recall and F1 on exact normalised values, plus frame
  accuracy (every slot of a question right). These are the standard pair for
  slot filling on ATIS and SNIPS ([survey, arXiv 2103.03095](https://arxiv.org/pdf/2103.03095)).
- A wrong value counts as one false positive and one false negative.
- Cluster-bootstrap 95% CIs.

**Cache (`evaluate.py --extracted`)**
- `split_full_extracted` and `split_template_extracted` route on extracted
  values and extracted masked text only. Correctness is judged against gold.
- A template reuse is correct only if two things hold: the cached entry has the
  query's intent, **and** the query's own values were extracted exactly.

**Operating point**
- The threshold at which the design's oracle twin had zero false reuse. It is
  calibrated once on gold and then frozen: what a team would calibrate in the
  lab and then deploy.
- Reported at that threshold:
  - the false share of reuses
  - correct reuse
  - the cause of every false reuse: wrong template, wrong values, or both

**Embedders**
- The four open gate models (MiniLM, mpnet, bge, and e5 with `query: `) decide.
- text-embedding-004 (production) is reported but does not count toward the
  decision.

### Where the 1% bar comes from

- Portkey (Swetha Sridhar, 18 Apr 2026) recommends backtesting on about 5,000
  real queries and tuning "until accuracy consistently stays above 99%"
  ([source](https://portkey.ai/blog/semantic-caching-thresholds/)).
- A production NL-to-SQL cache reports 98.7% accuracy on direct cache returns,
  i.e. 1.3% wrong ([arXiv 2601.11687](https://arxiv.org/html/2601.11687v1)).

A false share of at most 1% is at least as strict as both.

### Decision rule

Let F be the calibrated false share of `split_template_extracted` under the
primary extractor. The outcomes are checked in this order, and each must hold
for all four open embedders.

| Outcome | Condition | Claim |
|---|---|---|
| **O3: no advantage** | `split_template_extracted`'s correct reuse at ≤1% false reuse is not above `raw_global`'s at ≤1% | Neither design reuses this kind of question safely. |
| **O1: extraction adds no measurable risk** | F ≤ 1% | The parameter-split design survives real extraction on this data. |
| **O2: the risk moves to extraction** | otherwise | Named by the dominant cause in the breakdown and the slots and periods behind it. |

### How each outcome may be read (fixed in advance)

The v1 questions come from 4–6 templates per intent with a closed vocabulary
(threat 1). That makes **both** extraction and template matching easier than
they are in real traffic. So the outcomes are not symmetric:

- **O2 or O3 on v1 is strong evidence.** The design fails even on easy input.
- **O1 on v1 is weak evidence.** It shows extraction did not break on templated
  questions, and says nothing about real ones. "Template caching is safe" may
  not be claimed until step 4a (human-written questions) or 4b (template
  hold-out).

### Disclosed before freezing

**Duckling was probed** on the dataset's 28 period wordings (not on full
questions) while `extract.py` was being designed, so its period behaviour is
known in advance:
- "year to date", "in Q3 2026" and "in Q2 2026" are not parsed.
- "last N months" becomes whole calendar months ending last month. For example,
  "last 3 months" is 07-01 to 09-30, where the dataset uses the rolling
  07-28 to 10-27.
- "last 30 days" becomes 09-27 to 10-26, which excludes today; the dataset uses
  09-28 to 10-27.
- "this month" and "this year" become the whole month or year, which
  `extract.py` clips to the reference date.

Duckling's period accuracy is therefore largely predictable, which is why it is
secondary.

**Other disclosures:**
- No Gemini model has been run on any dataset question.
- The gold sanity check found the slot-order bug corrected in section 4.
- The routing and cause attribution were checked on a synthetic extraction with
  5% of periods corrupted (run in a scratch directory, not committed). It
  produced 62 false template reuses, all attributed to wrong values. The
  full-SQL design stayed at 0 false reuses, because a corrupted key simply
  misses.

### Out of scope here

- **Date conventions are genuinely ambiguous.** "Last 3 months" can be calendar
  or rolling: Duckling and the dataset disagree, and both are defensible. The
  Gemini prompt states the dataset's convention.
- **Relative SQL is not tested.** The production NLQ writes relative SQL
  (`CURRENT_DATE`, `backend/src/fin_insights/adapters/llm/prompts/v1/nlq/_examples.py:29`).
  A cache keyed on relative tokens ("last_month") instead of absolute ranges is
  an alternative design not tested here.

### Commands

```
docker run -d --name duckling-research -p 8010:8000 rasa/duckling@sha256:459e6033f87b0f3f525ed0d0066ae89cfe31d512f32ac1d469431fa6ce1bdef5
python extract.py --extractor duckling
python extract.py --extractor gemini:gemini-3.1-flash-lite --project <gcp-project>
python extract.py --extractor gemini:gemini-3.5-flash --project <gcp-project>
# for each extractor x {MiniLM, mpnet, bge, e5 --prefix "query: "}:
python evaluate.py --embedder <embedder> --extracted results/extraction/<extractor>/extracted.jsonl
python evaluate.py --summarize-extraction
```
