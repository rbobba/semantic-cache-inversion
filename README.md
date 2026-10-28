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
| split_template (oracle params) | 0.952 [0.937, 0.965] | 0.995 |

Strong inversion against parameter near-misses: 0.992 [0.977, 1.000].

**This proves nothing about embeddings** — a word-overlap model is bound to score
"this month" close to "last month". It is here to verify the harness, and as the
control that any neural model must be compared with. Two things in it are worth
noticing, though:

1. `split_full` reaches only 0.225 of a possible 0.532. With the parameters
   exact, what still forces the threshold up is intent near-misses: "How much did
   I spend at [MERCHANT] [PERIOD]?" against "How many transactions did I have at
   [MERCHANT] [PERIOD]?". That is H3, showing up in the control already.
2. `split_template` at 0.952 is **inflated by construction** — see threat 1.

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
