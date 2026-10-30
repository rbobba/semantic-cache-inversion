"""Section 18's local runs, in one process so each model loads once.

Calls human_eval.cache / human_eval.similarity exactly as the CLI would; the
only change is that SentenceTransformer(model) returns a kept instance.
Skips any report that already exists. Usage:
  python run_human_evals.py cache        # 4 open embedders x 48 runs x 3 excludes
  python run_human_evals.py similarity   # 4 open + 3 secondary open, x 3 excludes
"""

import argparse
import functools
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

import sentence_transformers  # noqa: E402

_orig = sentence_transformers.SentenceTransformer
sentence_transformers.SentenceTransformer = functools.lru_cache(maxsize=1)(_orig)

import human_eval  # noqa: E402
from evaluate import slug  # noqa: E402

OPEN = [
    ("st:sentence-transformers/all-MiniLM-L6-v2", ""),
    ("st:sentence-transformers/all-mpnet-base-v2", ""),
    ("st:BAAI/bge-base-en-v1.5", ""),
    ("st:intfloat/e5-base-v2", "query: "),
]
SECONDARY = [
    ("st:Qwen/Qwen3-Embedding-0.6B", ""),
    ("st:Snowflake/snowflake-arctic-embed-l-v2.0", "query: "),
    ("st:mixedbread-ai/mxbai-embed-large-v1", ""),
]
EXCLUDES = (None, "copied", "meaning")


def ns(emb, prefix, **kw):
    a = argparse.Namespace(
        data=ROOT / "data_human",
        out=ROOT / "results_human",
        embedder=emb,
        prefix=prefix,
        task_type=None,
        project="",
        location="us-central1",
        domain=None,
        extracted=None,
        exclude=None,
    )
    for k, v in kw.items():
        setattr(a, k, v)
    return a


def main(mode):
    t0 = time.time()
    if mode == "similarity":
        for emb, prefix in OPEN + SECONDARY:
            for ex in EXCLUDES:
                a = ns(emb, prefix, exclude=ex)
                out = (
                    a.out
                    / "similarity"
                    / (slug(human_eval.label(a)) + (f"_excl_{ex}" if ex else ""))
                )
                if (out / "report.json").exists():
                    continue
                human_eval.similarity(a)
                print(
                    f"ok similarity {out.name} {time.time() - t0:.0f}s", file=sys.stderr, flush=True
                )
    else:
        for emb, prefix in OPEN:
            for d in human_eval.DOMAIN_NAMES:
                for run in sorted((ROOT / "results_human" / d / "extraction").iterdir()):
                    if not all(s in run.name for s in sys.argv[2:]):
                        continue
                    for ex in EXCLUDES:
                        a = ns(emb, prefix, domain=d, extracted=run / "extracted.jsonl", exclude=ex)
                        out = run / (slug(human_eval.label(a)) + (f"_excl_{ex}" if ex else ""))
                        if (out / "report.json").exists():
                            continue
                        human_eval.cache(a)
                        print(f"ok {d} {run.name} {out.name} {time.time() - t0:.0f}s", flush=True)
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
