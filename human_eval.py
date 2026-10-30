"""Section 18's analysis of the human-written questions.

Raw similarity (no extraction needed), all four domains at once:
  python human_eval.py --embedder <e> [--prefix "query: "] [--exclude copied|meaning]
  (commercial embedders take evaluate.py's --task-type and --project as well)

The cache designs on one extraction run:
  python human_eval.py --embedder <e> [--prefix ...] --domain <d>
      --extracted results_human/<d>/extraction/<arm>_<tag>/extracted.jsonl [--exclude ...]

The cache is each domain's synthetic cached questions; the queries are the
writers' questions (human.py). Cache designs are computed by evaluate.py's own
cache_simulation, unchanged, so they mean what they mean in sections 15-16.
The oracle designs need gold spans, which human wording does not have, and are
not reported.

--exclude copied   drops questions the naturalness screen flagged
--exclude meaning  drops questions marked N in data_human/meaning_check.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from domains import DOMAINS
from evaluate import cache_simulation, embed, slug
from guards import has_negation_cue

HERE = Path(__file__).parent
DOMAIN_NAMES = ("finance", "retail", "healthcare", "it_support")


def load(data: Path, domain: str, exclude: str | None) -> list[dict]:
    with (data / domain / "questions.jsonl").open(encoding="utf-8") as f:
        qs = [json.loads(line) for line in f if line.strip()]
    if exclude == "copied":
        qs = [q for q in qs if q["is_anchor"] or not (q["copied"] or q["duplicate"])]
    elif exclude == "meaning":
        with (data / "meaning_check.csv").open(encoding="utf-8") as f:
            changed = {r["id"] for r in csv.DictReader(f) if r["same_meaning (Y/N)"] == "N"}
        qs = [q for q in qs if q["id"] not in changed]
    return qs


def auc(pos: np.ndarray, neg: np.ndarray) -> float:
    """P(a rewording scores above a period change); ties count half."""
    d = pos[:, None] - neg[None, :]
    return float(((d > 0) + 0.5 * (d == 0)).mean())


def clustered_auc(sim: np.ndarray, is_pos: np.ndarray, cluster: np.ndarray, seed: int) -> dict:
    """AUC with a 95% interval from resampling specs, so a spec's three
    versions move together."""
    rng = np.random.default_rng(seed)
    ids = np.unique(cluster)
    rows = {c: np.flatnonzero(cluster == c) for c in ids}
    draws = []
    for _ in range(1000):
        take = np.concatenate([rows[c] for c in rng.choice(ids, ids.size)])
        p, n = sim[take][is_pos[take]], sim[take][~is_pos[take]]
        if p.size and n.size:
            draws.append(auc(p, n))
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return {
        "auc": round(auc(sim[is_pos], sim[~is_pos]), 4),
        "ci95": [round(float(lo), 4), round(float(hi), 4)],
        "n_rewordings": int(is_pos.sum()),
        "n_period_changes": int((~is_pos).sum()),
    }


def args_for(a: argparse.Namespace) -> argparse.Namespace:
    return argparse.Namespace(
        embedder=a.embedder,
        prefix=a.prefix,
        task_type=a.task_type,
        dimensions=None,
        project=a.project,
        location=a.location,
        region=None,
    )


def label(a: argparse.Namespace) -> str:
    # The same label evaluate.py gives the configuration, so slugs match.
    return (
        a.embedder
        + (f" prefix={a.prefix!r}" if a.prefix else "")
        + (f" task_type={a.task_type}" if a.task_type else "")
    )


def similarity(a: argparse.Namespace) -> None:
    sims, pos, cluster, dom = [], [], [], []
    for d in DOMAIN_NAMES:
        qs = load(a.data, d, a.exclude)
        texts = sorted({q["text"] for q in qs})
        ti = {t: i for i, t in enumerate(texts)}
        v = embed(texts, args_for(a), a.out / d / slug(label(a)))
        by_id = {q["id"]: q for q in qs}
        for q in qs:
            if q["is_anchor"]:
                continue
            # The cached question this one was written from: same intent,
            # same values, period kept or changed.
            anchor = by_id[q["anchor_id"]]
            sims.append(float(v[ti[q["text"]]] @ v[ti[anchor["text"]]]))
            pos.append(q["kind"] == "same_meaning")
            cluster.append(f"{d}/{q['spec_id']}")
            dom.append(d)
    sims, pos, cluster, dom = map(np.array, (sims, pos, cluster, dom))
    out = {
        "embedder": label(a),
        "exclude": a.exclude,
        "pooled": clustered_auc(sims, pos, cluster, 7),
    }
    for d in DOMAIN_NAMES:
        m = dom == d
        out[d] = clustered_auc(sims[m], pos[m], cluster[m], 7)
    path = a.out / "similarity" / (slug(label(a)) + (f"_excl_{a.exclude}" if a.exclude else ""))
    path.mkdir(parents=True, exist_ok=True)
    (path / "report.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


def cache(a: argparse.Namespace) -> None:
    qs = load(a.data, a.domain, a.exclude)
    with a.extracted.open(encoding="utf-8") as f:
        ext = {r["id"]: r for r in map(json.loads, f) if r}
    missing = {q["id"] for q in qs} - set(ext)
    if missing:
        raise SystemExit(f"{a.extracted} lacks {len(missing)} questions, e.g. {min(missing)}")
    texts = sorted({q["text"] for q in qs} | {ext[q["id"]]["masked_text"] for q in qs})
    ti = {t: i for i, t in enumerate(texts)}
    v = embed(texts, args_for(a), a.out / a.domain / slug(label(a)))
    raw = v[[ti[q["text"]] for q in qs]]
    ext_masked = v[[ti[ext[q["id"]]["masked_text"]] for q in qs]]
    sim = cache_simulation(
        qs,
        raw,
        ext_masked,  # stands in for the gold masks; only oracle designs read it
        np.random.default_rng(7),
        1000,
        ext=ext,
        ext_masked=ext_masked,
        holdout=False,
        domain=a.domain,
    )
    human = [q for q in qs if not q["is_anchor"]]
    period_errors = [
        q["id"] for q in human if ext[q["id"]]["params"].get("period") != q["params"]["period"]
    ]
    excluding = {neg[0] for neg in DOMAINS[a.domain].negations}
    neg_q = [q for q in human if q["intent"] in excluding]
    other_q = [q for q in human if q["intent"] not in excluding]
    report = {
        "domain": a.domain,
        "embedder": label(a),
        "extracted": a.extracted.as_posix(),
        "exclude": a.exclude,
        "n_human": len(human),
        "period_errors": {"n": len(period_errors), "ids": period_errors},
        "negation_cue": {
            "caught": sum(has_negation_cue(q["text"]) for q in neg_q),
            "of_excluding": len(neg_q),
            "false_cues": sum(has_negation_cue(q["text"]) for q in other_q),
            "of_other": len(other_q),
        },
        "cache": {
            k: sim[k] for k in ("n_cached", "n_queries", "designs", "calibrated", "shortlist_sweep")
        },
    }
    out = a.extracted.parent / (slug(label(a)) + (f"_excl_{a.exclude}" if a.exclude else ""))
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{a.domain} {out.name}: written")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--data", type=Path, default=HERE / "data_human")
    ap.add_argument("--out", type=Path, default=HERE / "results_human")
    ap.add_argument("--embedder", required=True)
    ap.add_argument("--prefix", default="")
    ap.add_argument("--task-type", default=None)
    ap.add_argument("--project", default="", help="GCP project, for vertex embedders")
    ap.add_argument("--location", default="us-central1", help="Vertex location")
    ap.add_argument("--domain", choices=DOMAIN_NAMES)
    ap.add_argument("--extracted", type=Path)
    ap.add_argument("--exclude", choices=("copied", "meaning"))
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if a.extracted:
        if not a.domain:
            raise SystemExit("--extracted needs --domain")
        cache(a)
    else:
        similarity(a)


if __name__ == "__main__":
    main()
