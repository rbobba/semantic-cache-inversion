# Reproducing the study

This is the runbook for checking, recomputing or replaying every result in
`README.md`. Each step says which hypothesis or table it serves, who can run
it, and what it costs.

## Three levels

| Level | What it does | Needs | Time | Must match |
|---|---|---|---|---|
| **1. Check** | Recomputes every cited number from the files on disk and checks the README still says it | Python only | minutes | exactly |
| **2. Recompute** | Rebuilds every report from the committed model outputs and the pinned open models | Python, a CPU, the model downloads | hours | exactly (see below) |
| **3. Replay** | Calls the extraction and embedding APIs again | Credentials and money | hours | no: a fresh sample, tagged separately |

Levels 1 and 2 involve no API calls. Everything downstream of a model's answer
is deterministic: the date resolution, the scoring, the bootstrap (fixed
seeds) and the verdicts. So recomputing from the saved answers must give the
same numbers. Level 3 asks the models again. Their answers vary from run to
run, which is why the study ran r1–r3, so a replay is a fourth sample. It is
compared with r1–r3 and **never replaces them**.

## Setup

```powershell
cd research\semantic-cache-inversion
python -m venv .venv                 # Python 3.11 was used
.venv\Scripts\activate               # source .venv/bin/activate elsewhere
pip install -r requirements.txt
pip install ruff                     # only to lint; the study uses --line-length 100
```

The open embedding models download on first use. `evaluate.py` pins each
one to the revision every report used (`ST_REVISIONS`, also listed in
`results_md/EMBEDDERS.txt`). After the first download, set
`$env:HF_HUB_OFFLINE = "1"` so nothing is fetched again.

On Windows, untick **QuickEdit Mode** in the console's Properties, and stop
the PC from sleeping while plugged in. A click in the window pauses all
output, and sleep drops API connections. Both happened during the study and
cost hours, though no data.

### What is in git, and what is not

| In git | Not in git (rebuilt at level 2) |
|---|---|
| Datasets (`data*/`) with their manifests | Cached vectors (`**/embeddings_*.npy`, about 2 GB) |
| Every model answer (`raw.jsonl`), extraction and accuracy file | `results_md/**/report.json` (539 files, about 0.7 MB each). Their hashes are in `results_md/REPORTS_SHA256.txt` |
| Reports for `results/`, `results_v2/` and `results_human/` | The writers' original sheets (kept outside the repo; their hashes are in `STATUS.md`) |
| `results_md/VERDICTS.txt`, `results_human/VERDICTS.txt` and `DETAILS.md` | |

## Level 1: check

```powershell
python verify_claims.py           # every check
python verify_claims.py --deep    # also re-resolve every saved model answer (a few minutes)
```

Expected: `0 failed`. What it checks:
- **Integrity.**
  - Every dataset file against its manifest's SHA-256.
  - The three recorded pre-registration hashes (sections 11, 16 and 18).
  - Every frozen section (9, 11, 14, 15, 16, 18) against the commit that froze
    it. Section 14's Addendum A is the one disclosed addition.
  - The `results_md` reports against their recorded hashes.
  - Both `VERDICTS.txt` files against a fresh run of the verdict scripts.
- **Claims.** The results tables of sections 7, 8, 10, 12, 13, 19 and 21, and
  their headline sentences, recomputed from the reports.
- **`--deep`.** Every `raw.jsonl` is resolved again with the current
  `extract.py` and compared byte for byte with the committed extraction.

A **SKIP** means an input is gitignored and not on disk yet: on a fresh
clone, the `results_md` reports and the cached vectors. Level 2 rebuilds the
open-model ones. The commercial ones need level 3, or the release archive
(Zenodo, once published).

## Level 2: recompute, no API calls

Work in this order. After each step, `git status` shows whether a committed
file changed. For the gitignored reports, `verify_claims.py --only integrity`
compares them with their hashes.

### 2.1 Datasets (every hypothesis)

```powershell
python generate_dataset.py --out data                  # v1: sections 7-10, 13 part 1
python generate_dataset.py --v2 --out data_v2          # v2: sections 12, 13 part 2b
python generate_dataset.py --multi-domain --out data_md   # four domains: sections 14-16, 18
```

The generator is deterministic, so `git status` should show no change.
`data_human/` cannot be rebuilt without the writers' sheets. It was made by
`python human.py --sheet A=<sheet> --sheet B=<sheet> --sheet C=<sheet>`, and
its manifest hashes are checked at level 1.

### 2.2 Inversion on v1: the gate H1 (section 7) and the 15-model table (section 8)

```powershell
python evaluate.py --embedder tfidf
python evaluate.py --embedder st:sentence-transformers/all-MiniLM-L6-v2
python evaluate.py --embedder st:sentence-transformers/all-mpnet-base-v2
python evaluate.py --embedder st:BAAI/bge-base-en-v1.5
python evaluate.py --embedder st:intfloat/e5-base-v2 --prefix "query: "
python evaluate.py --embedder st:Qwen/Qwen3-Embedding-0.6B
python evaluate.py --embedder st:Snowflake/snowflake-arctic-embed-l-v2.0 --prefix "query: "
python evaluate.py --embedder st:mixedbread-ai/mxbai-embed-large-v1
```

These overwrite the committed reports in `results/`. Current code adds fields
the older reports lack: comparison A/B, and later cache designs. So check
values, not bytes. Copy the committed report aside first (or use
`git show HEAD:<path>`), then:

```powershell
python verify_claims.py --same-values <committed report.json> <regenerated report.json>
```

It must report `0 differ, 0 missing`. This was tested on 2026-10-30: 314 of
314 values matched, and the recomputed MiniLM vectors were bit-identical to
the cached ones.

Section 8's A/B intervals came from session code that was never committed.
The point estimates reproduce exactly; the intervals agree to within 0.015
(README section 22).

### 2.3 Real extraction on v1 and v2: sections 9-13

The saved answers are resolved again by `verify_claims.py --deep`. The
evaluations, for each `<x>` in `gold`, `duckling`,
`gemini_gemini-3.1-flash-lite`, `gemini_gemini-3.5-flash` and
`gemini-rel_gemini-3.1-flash-lite`, and each of the four open embedders
(add `--prefix "query: "` for e5):

```powershell
python evaluate.py --embedder <e> --extracted results/extraction/<x>/extracted.jsonl
```

Dataset v2, held-out wording (section 12 and section 13 part 2b):

```powershell
python evaluate.py --data data_v2 --out results_v2 --embedder <e> [--holdout]
python evaluate.py --data data_v2 --out results_v2 --embedder <e> --holdout --extracted results_v2/extraction/<x>/extracted.jsonl
```

Section 13's paired differences (absolute against relative):

```powershell
python evaluate.py --compare results/extraction/gemini_gemini-3.1-flash-lite/<e>/report.json results/extraction/gemini-rel_gemini-3.1-flash-lite/<e>/report.json
```

`gold` and `duckling` can also be extracted again. Gold is deterministic.
Duckling needs the pinned image from section 9:
`docker run -d -p 8010:8000 rasa/duckling@sha256:459e6033…`.

### 2.4 Four domains: G1-G4, H-N, H-S, H-N-O, H-S-O (sections 14-16, results in 19)

```powershell
python run_md_evals.py inversion    # G1: 7 open configurations x 4 domains, both splits
python run_md_evals.py extraction   # G4, H-N, H-S, H-N-O, H-S-O, and the pilots
python run_md_evals.py gold         # the gold-extraction sanity check
python md_verdicts.py > results_md/VERDICTS.txt
```

These rebuild 475 of the 539 hashed reports; the other 64 are commercial
(level 3). G2 and G3 need no embedder: they come from the committed
`accuracy.json` files. Then:
- `python verify_claims.py --only integrity` must show the hashes matching;
- `git status` must show `VERDICTS.txt` unchanged.

### 2.5 Human-written questions: HQ-P, HQ-D, HQ-C, HQ-S, HQ-F (section 18, results in 21)

```powershell
python run_human_evals.py similarity   # HQ-P, the 7 open configurations (about 75 min; Qwen3 and Snowflake are slow on CPU)
python run_human_evals.py cache        # HQ-D, HQ-C, HQ-S, HQ-F (about 60 min)
```

Section 20's exploratory year fix: the `-yearfix` extractions are checked by
`verify_claims.py --deep`. Their evaluations:

```powershell
python run_human_evals.py cache openai yearfix
```

Then the verdicts and details:

```powershell
python human_verdicts.py; python human_verdicts.py --exclude=copied; python human_verdicts.py --exclude=meaning
python human_verdicts.py --suffix=-yearfix   # and the two --exclude variants
python human_details.py                      # writes results_human/DETAILS.md
```

`results_human/VERDICTS.txt` is the six outputs above, in that order, each
followed by a blank line; level 1 rebuilds and compares it. These reports are
committed, so `git status` must show no change.

### 2.6 Finally

```powershell
python verify_claims.py --deep
```

## Level 3: replay, with API calls

Run these yourself: they use your credentials (Vertex through
`gcloud auth application-default login`, plus `OPENAI_API_KEY` and
`VOYAGE_API_KEY`). Every extraction script takes `-Tags`, so a replay writes
to its own folders and never touches r1–r3:

| Serves | Command | Cost (2026-10) |
|---|---|---|
| G2, G3, G4, H-N (section 14) | `.\run_extractions.ps1 -Tags replay1 -SkipFlash` | about $5; 3.5-flash (without `-SkipFlash`) adds about $34 |
| H-S (section 15) | `.\run_guard_extractions.ps1 -Tags replay1` | about $3 |
| H-N-O, H-S-O (section 16) | `.\run_openai_extractions.ps1 -Tags replay1` | about $1 |
| HQ-D, HQ-S, HQ-F (section 18) | `.\run_human_extractions.ps1 -Vendor gemini -Tags replay1` | about $1 |
| | `.\run_human_extractions.ps1 -Vendor openai -Tags replay1` | about $0.50 |
| Section 8 and G1, commercial embedders | `.\run_embeddings.ps1` (four domains); the `evaluate.py` lines in README section 3 for v1 | cents |
| HQ-P, secondary embedders | `.\run_human_embeddings.ps1` | cents |
| Sections 10 and 13 (v1 and v2 extraction) | `python extract.py --extractor <arm>:<model> --tag replay1 --project <project> --workers 2`, with `--data data_v2 --out results_v2/extraction` for v2 | under $1 per flash-lite run; about $9 for 3.5-flash |

A replay is one tag, so it costs one third of r1–r3. The OpenAI figures come
from logged token counts (README section 19); the Gemini figures are the
estimates in the script headers, which were not checked against a bill.

Then evaluate the replay folders exactly as in level 2, naming the tag:
`python run_md_evals.py extraction replay1` and
`python run_human_evals.py cache replay1`.

**Before running a replay, write down how it will be judged**, as every
stage of this study was: for example, "each verdict is recomputed with
replay1 in place of r3, and the replay confirms when no verdict changes".
Writing the rule after seeing the replay would turn it into fitting.

The commercial embedders cannot be pinned: a provider can change a model
behind the same name. A replay of them tests the claim as it stands today,
not the original vectors.

## Known differences, and why they do not change a result

| What | Detail | Where |
|---|---|---|
| Section 8's A/B intervals | Computed by session code that was not committed. The points reproduce exactly; the intervals are within 0.015. | README section 22 |
| Section 11's recorded hash | Taken with the newline after the commands block; sections 16 and 18 without it. The text is unchanged since its freeze commit. | README section 22 |
| Report paths | Reports made with `--extracted` stored an absolute path until 2026-10-30. That path was rewritten to the study-relative one in all 1,279 such reports, with no other byte changed, and the hashes were updated. | README section 22 |
| Older reports | Current code adds fields to reports made earlier. Every value they hold is unchanged (`--same-values`). | This file, 2.2 |
| Other hardware | Vectors were bit-identical on the study's machine. A different CPU or BLAS library can change the last bits, which could move a rounded figure by one in its last digit. | — |
