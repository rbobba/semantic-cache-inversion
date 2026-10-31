"""The local evaluations of README sections 14-16 and 18's pilots, on data_md.
Rebuilds every open-model report listed in results_md/REPORTS_SHA256.txt; the
commercial ones come from run_embeddings.ps1. Skips any report that exists.

  python run_md_evals.py inversion    # 7 open configurations x 4 domains, gold and held-out
  python run_md_evals.py extraction   # 4 open embedders x every extraction run, both splits
  python run_md_evals.py extraction replay1   # the same, for a replay's tag only
  python run_md_evals.py gold         # the gold-extraction sanity check (bge, new domains)

Each report is a separate evaluate.py process, as when the hashed reports were
made. The extraction step needs the extractions on disk (they are committed).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DOMAINS = ("finance", "retail", "healthcare", "it_support")
OPEN4 = (
    ("st:sentence-transformers/all-MiniLM-L6-v2", "", "st_sentence-transformers_all-MiniLM-L6-v2"),
    (
        "st:sentence-transformers/all-mpnet-base-v2",
        "",
        "st_sentence-transformers_all-mpnet-base-v2",
    ),
    ("st:BAAI/bge-base-en-v1.5", "", "st_BAAI_bge-base-en-v1.5"),
    ("st:intfloat/e5-base-v2", "query: ", "st_intfloat_e5-base-v2_prefix_query"),
)
SECONDARY3 = (
    ("st:Qwen/Qwen3-Embedding-0.6B", "", "st_Qwen_Qwen3-Embedding-0.6B"),
    (
        "st:Snowflake/snowflake-arctic-embed-l-v2.0",
        "query: ",
        "st_Snowflake_snowflake-arctic-embed-l-v2.0_prefix_query",
    ),
    ("st:mixedbread-ai/mxbai-embed-large-v1", "", "st_mixedbread-ai_mxbai-embed-large-v1"),
)
ARMS = (
    "gemini-rel_gemini-3.1-flash-lite",
    "gemini-relsig_gemini-3.1-flash-lite",
    "openai-relsig_gpt-6-luna",
)
TAGS = ("r1", "r2", "r3")
PILOTS = ("gemini-relfull_gemini-3.1-flash-lite", "openai-relfull_gpt-6-luna")


def run(cmd: list[str], out: Path, what: str) -> None:
    if out.exists():
        return
    r = subprocess.run(
        [sys.executable, "evaluate.py", *cmd],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    ok = r.returncode == 0 and out.exists()
    print(f"{'ok' if ok else 'FAIL'} {what}", flush=True)
    if not ok:
        print(r.stderr[-2000:], flush=True)


def emb_args(emb: str, prefix: str) -> list[str]:
    return ["--embedder", emb, *(["--prefix", prefix] if prefix else [])]


def inversion() -> None:
    for d in DOMAINS:
        for emb, prefix, slug in OPEN4 + SECONDARY3:
            for hold in (False, True):
                out = (
                    ROOT / "results_md" / d / (slug + ("_holdout" if hold else "")) / "report.json"
                )
                cmd = ["--data", f"data_md/{d}", "--out", f"results_md/{d}", *emb_args(emb, prefix)]
                run(cmd + (["--holdout"] if hold else []), out, f"{d} {out.parent.name}")


def extraction() -> None:
    if sys.argv[2:]:
        runs = [(arm, t) for arm in ARMS for t in sys.argv[2:]]
    else:
        runs = [(arm, t) for arm in ARMS for t in TAGS]
        runs += [(arm, t) for arm in PILOTS for t in ("pilot", "pilot2")]
    for d in DOMAINS:
        for arm, t in runs:
            run_dir = ROOT / "results_md" / d / "extraction" / f"{arm}_{t}"
            if not (run_dir / "extracted.jsonl").exists():
                print(f"SKIP (no extraction) {d} {run_dir.name}", flush=True)
                continue
            for emb, prefix, slug in OPEN4:
                for hold in (False, True):
                    out = run_dir / (slug + ("_holdout" if hold else "")) / "report.json"
                    cmd = [
                        "--data",
                        f"data_md/{d}",
                        "--out",
                        f"results_md/{d}",
                        *emb_args(emb, prefix),
                        "--extracted",
                        str(run_dir / "extracted.jsonl"),
                    ]
                    run(
                        cmd + (["--holdout"] if hold else []),
                        out,
                        f"{d} {run_dir.name} {out.parent.name}",
                    )


def gold() -> None:
    emb, prefix, slug = OPEN4[2]
    for d in DOMAINS[1:]:
        run_dir = ROOT / "results_md" / d / "extraction" / "gold"
        cmd = ["--data", f"data_md/{d}", "--out", f"results_md/{d}", *emb_args(emb, prefix)]
        cmd += ["--extracted", str(run_dir / "extracted.jsonl")]
        run(cmd, run_dir / slug / "report.json", f"{d} gold {slug}")


if __name__ == "__main__":
    {"inversion": inversion, "extraction": extraction, "gold": gold}[sys.argv[1]]()
    print("ALL DONE", flush=True)
