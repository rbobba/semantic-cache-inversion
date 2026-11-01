# Semantic Cache Inversion

A pre-registered empirical study of when semantic caching is safe for text-to-SQL, and when it isn't.

**The finding:** the words that most change an SQL query's answer — "this" vs "last", "sum" vs "count", "except" — are the words sentence embeddings weigh least. A similarity threshold cannot make a text-to-SQL cache safe, whatever the embedding model.

## Key results

**On 480 human-written questions across four analytics domains:**

- Similarity cannot tell a person's rewording from their period change. AUC 0.52–0.58 in 15 embedding configurations (2021–2026), from nine publishers. That is barely better than a coin toss.
- An extracted full signature (operation, measure, grouping, exclusion) made **zero wrong-template reuses** on the 468 meaning-preserving questions, with two extractor vendors. Correct reuse: 80–97%, against 1–33% for an exact-key cache.
- The remaining risk is the period value. "The past year" and explicit date ranges produce wrong answers that no signature or threshold catches.

**On synthetic questions in four domains (finance, retail, healthcare, IT support):**

- A one-word period swap outscores every reworded question of the same meaning for 78–100% of cached questions, in all 15 embedding models tested (comparison A).
- Relative period labels (the model labels it, code computes the dates) removed every date error in 15,411 extractions.
- Excluded values ("everything except travel") are dropped 16–40% of the time, while the same value is read correctly 100% of the time when included.

## Method

Every hypothesis, decision rule and prediction was written and committed **before** its run. Three stages recorded SHA-256 hashes of their pre-registration text. Predictions that turned out wrong are kept in place, not edited. The full record is in [STUDY_LOG.md](STUDY_LOG.md).

**15 embedding models** from nine publishers: sentence-transformers, BAAI, intfloat, Mixedbread, Snowflake, Qwen (open); Google, OpenAI, Voyage (commercial). Release years 2021–2026.

**Two extractor vendors:** Google Gemini (flash-lite) and OpenAI (gpt-6-luna), with three repeat runs each.

**480 human-written questions** by three volunteers who are not the author, across four analytics domains.

## Reproducing the results

Three levels, from minutes to hours:

| Level | What | Needs | Time |
|---|---|---|---|
| **1. Check** | Recomputes every number from the files on disk | Python | minutes |
| **2. Recompute** | Rebuilds every report from the saved model outputs | Python, CPU, model downloads | hours |
| **3. Replay** | Calls the extraction and embedding APIs again | API keys, money | hours |

```bash
python verify_claims.py           # level 1: check every cited number
python verify_claims.py --deep    # also re-resolve every saved model answer
```

See [REPRODUCE.md](REPRODUCE.md) for the full runbook.

## What's in this repo

| Path | Contents |
|---|---|
| `data/` | v1 dataset: 1,358 questions, 1,496 labelled pairs (finance) |
| `data_v2/` | v2 dataset with held-out template split (finance) |
| `data_md/` | Four-domain dataset: finance, retail, healthcare, IT support |
| `data_human/` | 480 human-written questions with meaning checks |
| `results*/` | Every model response (`raw.jsonl`), extraction, accuracy and evaluation report |
| `generate_dataset.py` | Deterministic dataset generator |
| `extract.py` | Parameter extraction (Gemini, OpenAI, Duckling, gold) |
| `evaluate.py` | Embedding, cache simulation, comparison A/B, bootstrap CIs |
| `guards.py` | Negation cue list and signature guards |
| `human*.py` | Human-question ingestion, evaluation and verdict scripts |
| `verify_claims.py` | Checks every number in the study log against the files |
| `STUDY_LOG.md` | The full study record: 22 sections of pre-registrations, results and corrections |
| `RELATED_WORK.md` | Literature review and positioning |
| `REPRODUCE.md` | Reproduction runbook (three levels) |
| `STATUS.md` | Current state and handoff notes |

## Pre-registered decisions

| Stage | Decision | Verdict |
|---|---|---|
| Go/no-go gate (H1) | Strong inversion ≥ 0.30 in 4 open models | **GO** |
| Real extraction | Where does the risk go? | **Moves to extraction** |
| Relative labels | Do they make the cache safe? | **No** — prediction was wrong |
| Four domains (G1) | Does the period inversion generalise? | **Yes** (all 3 new domains) |
| Human questions (HQ-P) | Can similarity separate rewording from period change? | **No** (AUC 0.52–0.58) |
| Full-signature guard (HQ-F) | Does it work on people's wording? | **Partially** — extractor-independent in retail |

Full table of all 17 hypotheses: [STUDY_LOG.md, STATUS section](STATUS.md).

## Citation

If you use this dataset, code or results, please cite:

```bibtex
@misc{bobba2026semantic,
  author = {Bobba, Ramakrishna},
  title = {Similarity Cannot Tell a Rewording from a Period Change: A Pre-Registered Study of Semantic Caching for Text-to-SQL},
  year = {2026},
  url = {https://github.com/rbobba/semantic-cache-inversion},
  note = {Dataset, code and all model outputs}
}
```

## License

Code: [MIT](LICENSE). Datasets: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Note on the study log

`STUDY_LOG.md` is the complete chronological record of the study. Some frozen sections reference `backend/...` paths from the parent application this study originated in; those sections cannot be edited because their SHA-256 hashes are part of the pre-registration evidence. References to "the agent" in frozen sections refer to an AI coding assistant used for local computation and analysis during the study.
