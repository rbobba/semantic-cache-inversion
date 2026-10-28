"""Measure parameter near-miss inversion and compare cache designs.

Reads the frozen dataset from generate_dataset.py, embeds every question with
one embedding model, and reports:

  A. Similarity by pair type — does a one-span near-miss ("this month" ->
     "last month") score above a genuine rephrasing?
  B. Inversion per cached question — for how many cached questions does some
     wrong question score at or above every (or the best) correct one?
  C. A cache simulation comparing four designs on the same queries:
       raw_global       one similarity threshold on the raw question
       raw_oracle_entry the best possible per-entry threshold, chosen with
                        the labels in hand. No per-entry method (vCache
                        included) can beat it at zero false reuse, so it is
                        an upper bound, not a competitor.
       split_full       parameters extracted into the key; the masked
                        question is embedded; full SQL reused only when the
                        parameters match exactly
       split_template   as split_full, but the SQL *template* is reused and
                        refilled with the new question's parameters
     The split designs use the gold parameters (oracle extraction). A real
     extractor can only do worse; README step 5 measures by how much.

Every headline number carries a 95% bootstrap interval, resampling cached
questions together with the queries generated from them, because queries
from one anchor are not independent of each other.

Usage:
    python evaluate.py --embedder tfidf
    python evaluate.py --embedder st:sentence-transformers/all-MiniLM-L6-v2
    python evaluate.py --embedder st:intfloat/e5-base-v2 --prefix "query: "
    python evaluate.py --embedder vertex:text-embedding-004 --project <gcp-project>
    python evaluate.py --embedder npz:my_vectors.npz        # bring your own
    python evaluate.py --summarize
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
THRESHOLDS = np.round(np.arange(0.50, 1.0001, 0.005), 3)
FALSE_REUSE_BUDGETS = (0.0, 0.01, 0.05)


# ── Data ─────────────────────────────────────────────────────────────────


def load(data_dir: Path) -> tuple[list[dict], list[dict], dict]:
    def jsonl(name: str) -> list[dict]:
        with (data_dir / name).open(encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]

    manifest = json.loads((data_dir / "manifest.json").read_text(encoding="utf-8"))
    return jsonl("questions.jsonl"), jsonl("pairs.jsonl"), manifest


# ── Embedders ────────────────────────────────────────────────────────────
#
# Each returns L2-normalised float32 rows in the order of `texts`, so cosine
# similarity is a dot product.


def _normalise(m: np.ndarray) -> np.ndarray:
    m = m.astype(np.float32)
    norms = np.linalg.norm(m, axis=1, keepdims=True)
    return m / np.where(norms == 0, 1, norms)


def embed_tfidf(texts: list[str]) -> np.ndarray:
    """Word unigram + bigram TF-IDF. The lexical baseline.

    Included because it answers the first question a reviewer asks: is the
    inversion a property of neural embeddings, or just of shared words?
    """

    def grams(t: str) -> list[str]:
        toks = re.findall(r"[a-z0-9$'\[\]]+", t.lower())
        return toks + [a + " " + b for a, b in itertools.pairwise(toks)]

    docs = [Counter(grams(t)) for t in texts]
    vocab = {g: i for i, g in enumerate(sorted({g for d in docs for g in d}))}
    df = np.zeros(len(vocab))
    for d in docs:
        for g in d:
            df[vocab[g]] += 1
    idf = np.log((1 + len(docs)) / (1 + df)) + 1
    m = np.zeros((len(texts), len(vocab)), dtype=np.float32)
    for i, d in enumerate(docs):
        for g, c in d.items():
            m[i, vocab[g]] = (1 + math.log(c)) * idf[vocab[g]]
    return _normalise(m)


def embed_sentence_transformers(texts: list[str], model: str, prefix: str) -> np.ndarray:
    from sentence_transformers import SentenceTransformer

    st = SentenceTransformer(model)
    return _normalise(st.encode([prefix + t for t in texts], batch_size=64, show_progress_bar=True))


def embed_vertex(
    texts: list[str],
    model: str,
    project: str,
    location: str,
    dimensions: int,
    task_type: str | None,
) -> np.ndarray:
    """Vertex AI, called the way the application calls it.

    The defaults (768 dimensions, no task type) mirror EmbeddingService in
    backend/src/fin_insights/adapters/llm/embedding_service.py, so the result
    describes the production configuration rather than a tuned variant.
    --task-type SEMANTIC_SIMILARITY is the variant worth trying second.
    """
    from google import genai
    from google.genai import types

    client = genai.Client(vertexai=True, project=project, location=location)
    out: list[list[float]] = []
    for i in range(0, len(texts), 100):
        cfg = types.EmbedContentConfig(output_dimensionality=dimensions)
        if task_type:
            cfg.task_type = task_type
        res = client.models.embed_content(model=model, contents=texts[i : i + 100], config=cfg)
        out.extend(e.values for e in res.embeddings)
    return _normalise(np.array(out))


def embed_npz(texts: list[str], path: Path) -> np.ndarray:
    """Vectors computed elsewhere: an .npz with `texts` and `vectors` arrays."""
    z = np.load(path, allow_pickle=False)
    index = {t: i for i, t in enumerate(z["texts"].tolist())}
    missing = [t for t in texts if t not in index]
    if missing:
        raise SystemExit(f"{len(missing)} texts missing from {path}, e.g. {missing[0]!r}")
    return _normalise(z["vectors"][[index[t] for t in texts]])


def embed(texts: list[str], args: argparse.Namespace, cache_dir: Path) -> np.ndarray:
    key = hashlib.sha256(
        ("\n".join(texts) + args.prefix + str(args.task_type)).encode()
    ).hexdigest()[:16]
    cache = cache_dir / f"embeddings_{key}.npy"
    if cache.exists():
        return np.load(cache)
    kind, _, name = args.embedder.partition(":")
    if kind == "tfidf":
        vecs = embed_tfidf(texts)
    elif kind == "st":
        vecs = embed_sentence_transformers(texts, name, args.prefix)
    elif kind == "vertex":
        if not args.project:
            raise SystemExit("--project is required for vertex embedders")
        vecs = embed_vertex(
            texts, name, args.project, args.location, args.dimensions, args.task_type
        )
    elif kind == "npz":
        vecs = embed_npz(texts, Path(name))
    else:
        raise SystemExit(f"unknown embedder {args.embedder!r}")
    cache_dir.mkdir(parents=True, exist_ok=True)
    np.save(cache, vecs)
    return vecs


# ── Statistics helpers ───────────────────────────────────────────────────


def ci(samples: list[float]) -> list[float]:
    a = np.array([s for s in samples if s is not None and not math.isnan(s)])
    if a.size == 0:
        return [float("nan"), float("nan")]
    return [round(float(np.percentile(a, 2.5)), 4), round(float(np.percentile(a, 97.5)), 4)]


def describe(x: np.ndarray) -> dict:
    return {
        "n": int(x.size),
        "mean": round(float(x.mean()), 4),
        "p10": round(float(np.percentile(x, 10)), 4),
        "median": round(float(np.median(x)), 4),
        "p90": round(float(np.percentile(x, 90)), 4),
        "max": round(float(x.max()), 4),
    }


# ── A + B: pair-level analysis ───────────────────────────────────────────


def pair_analysis(
    pairs: list[dict], qidx: dict[str, int], raw: np.ndarray, rng: np.random.Generator, n_boot: int
) -> dict:
    sims = np.array([raw[qidx[p["anchor_id"]]] @ raw[qidx[p["candidate_id"]]] for p in pairs])

    by_type: dict[str, list[float]] = defaultdict(list)
    for p, s in zip(pairs, sims, strict=True):
        by_type[f"{p['relation']}/{p['dimension']}/{p['kind']}"].append(s)
        by_type[f"{p['relation']}"].append(s)
        # Near-misses are mostly one-span edits of the cached wording and
        # rephrasings mostly are not. Splitting by wording lets a reader check
        # that the inversion is not just "same template scores higher".
        if p["relation"] in ("param_near_miss", "equivalent_surface", "intent_near_miss"):
            by_type[f"{p['relation']} (same wording={p['same_wording']})"].append(s)
    similarity = {k: describe(np.array(v)) for k, v in sorted(by_type.items())}

    # Per-anchor inversion. "Strong": the best wrong question scores at or
    # above the best right one, so no threshold on this entry yields a
    # correct reuse without a false one. "Weak": it scores at or above the
    # worst right one, so no threshold catches every rephrasing safely.
    negative_sets = {
        "any_negative": lambda p: not p["same_sql"],
        "param_near_miss": lambda p: p["relation"] == "param_near_miss",
        "period_near_miss": lambda p: (
            p["relation"] == "param_near_miss" and p["dimension"] == "period"
        ),
        "entity_near_miss": lambda p: (
            p["relation"] == "param_near_miss" and p["dimension"] != "period"
        ),
        "intent_near_miss": lambda p: p["relation"] in ("intent_near_miss", "filter_change"),
    }
    anchors: dict[str, list[tuple[dict, float]]] = defaultdict(list)
    for p, s in zip(pairs, sims, strict=True):
        anchors[p["anchor_id"]].append((p, float(s)))
    anchor_ids = sorted(anchors)

    inversion: dict[str, dict] = {}
    for name, is_neg in negative_sets.items():
        strong, weak, culprits = [], [], Counter()
        for a in anchor_ids:
            pos = [s for p, s in anchors[a] if p["same_sql"]]
            neg = [(s, p) for p, s in anchors[a] if is_neg(p)]
            if not pos or not neg:
                strong.append(np.nan)
                weak.append(np.nan)
                continue
            top_s, top_p = max(neg, key=lambda x: x[0])
            strong.append(float(top_s >= max(pos)))
            weak.append(float(top_s >= min(pos)))
            if top_s >= max(pos):
                culprits[f"{top_p['relation']}/{top_p['dimension']}"] += 1
        strong_a, weak_a = np.array(strong), np.array(weak)
        valid = ~np.isnan(strong_a)
        boot_s, boot_w = [], []
        idx = np.flatnonzero(valid)
        for _ in range(n_boot):
            r = rng.choice(idx, size=idx.size, replace=True)
            boot_s.append(float(strong_a[r].mean()))
            boot_w.append(float(weak_a[r].mean()))
        inversion[name] = {
            "anchors": int(valid.sum()),
            "strong_rate": round(float(strong_a[valid].mean()), 4),
            "strong_ci95": ci(boot_s),
            "weak_rate": round(float(weak_a[valid].mean()), 4),
            "weak_ci95": ci(boot_w),
            "strong_culprits": dict(culprits.most_common()),
        }

    # The examples a paper's motivating figure is made of.
    worst = []
    for a in anchor_ids:
        pos = [(s, p) for p, s in anchors[a] if p["same_sql"]]
        neg = [(s, p) for p, s in anchors[a] if not p["same_sql"]]
        if pos and neg:
            bn, pn = max(neg, key=lambda x: x[0])
            bp, pp = max(pos, key=lambda x: x[0])
            worst.append(
                (bn - bp, pn["anchor_text"], pn["candidate_text"], bn, pp["candidate_text"], bp)
            )
    worst.sort(reverse=True)
    examples = [
        {
            "cached": w[1],
            "wrong": w[2],
            "wrong_sim": round(w[3], 4),
            "best_correct": w[4],
            "correct_sim": round(w[5], 4),
        }
        for w in worst[:15]
    ]
    return {
        "similarity_by_pair_type": similarity,
        "inversion": inversion,
        "top_inversions": examples,
    }


# ── C: cache simulation ──────────────────────────────────────────────────


def cache_simulation(
    questions: list[dict],
    raw: np.ndarray,
    masked: np.ndarray,
    rng: np.random.Generator,
    n_boot: int,
) -> dict:
    anchors = [q for q in questions if q["is_anchor"]]
    queries = [q for q in questions if not q["is_anchor"]]
    a_index = {q["id"]: i for i, q in enumerate(anchors)}
    qpos = {q["id"]: i for i, q in enumerate(questions)}
    A, Q = len(anchors), len(queries)

    ai = np.array([qpos[q["id"]] for q in anchors])
    qi = np.array([qpos[q["id"]] for q in queries])
    S_raw = raw[qi] @ raw[ai].T  # (Q, A)
    S_mask = masked[qi] @ masked[ai].T

    def key(q: dict) -> str:
        return json.dumps(q["params"], sort_keys=True)

    same_intent = np.array([[q["intent"] == a["intent"] for a in anchors] for q in queries])
    same_params = np.array([[key(q) == key(a) for a in anchors] for q in queries])
    same_slots = np.array([[q["slots"] == a["slots"] for a in anchors] for q in queries])
    same_sql = same_intent & same_params

    designs = {
        # name: (similarity matrix, eligibility, correctness)
        "raw_global": (S_raw, np.ones_like(same_sql), same_sql),
        "split_full": (S_mask, same_slots & same_params, same_sql),
        "split_template": (S_mask, same_slots, same_intent),
    }
    group = np.array([a_index[q["group"]] for q in queries])

    # Routing does not depend on the resample — the cache is fixed and only
    # the queries are redrawn — so compute it once per design.
    routed = {}
    for name, (S, elig, correct) in designs.items():
        M = np.where(elig, S, -np.inf)
        nn = M.argmax(axis=1)
        best = M[np.arange(Q), nn]
        ok = correct[np.arange(Q), nn] & np.isfinite(best)
        possible = (correct & elig).any(axis=1)
        routed[name] = (nn, best, ok, possible)

    def run(weights_g: np.ndarray) -> dict[str, dict]:
        """One evaluation. weights_g[i] = how many times anchor i's query group was drawn.

        The cache stays whole. Resampling it too would remove, in each draw,
        the only cached entry some queries could correctly reuse, and bias
        every resample below the point estimate.
        """
        w_q = weights_g[group].astype(float)
        total = w_q.sum()
        out: dict[str, dict] = {}
        for name, (nn, best, ok, possible) in routed.items():
            out[name] = _zero_and_budget(best, ok, w_q, total)
            out[name]["possible"] = float((w_q * possible).sum() / total)
            if name == "raw_global":
                out["raw_oracle_entry"] = _oracle_per_entry(best, ok, nn, w_q, total, A)
                out["raw_oracle_entry"]["possible"] = out[name]["possible"]
        return out

    full = run(np.ones(A, dtype=int))
    boots: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for _ in range(n_boot):
        draw = np.bincount(rng.integers(0, A, size=A), minlength=A)
        for name, metrics in run(draw).items():
            for m, v in metrics.items():
                boots[name][m].append(v)

    result = {}
    for name, metrics in full.items():
        result[name] = {
            m: {"value": round(v, 4), "ci95": ci(boots[name][m])} for m, v in metrics.items()
        }

    # Threshold curves on the full data — for plotting, not for headlines.
    curves = {}
    for name, (S, elig, correct) in designs.items():
        M = np.where(elig, S, -np.inf)
        nn = M.argmax(axis=1)
        best = M[np.arange(Q), nn]
        ok = correct[np.arange(Q), nn] & np.isfinite(best)
        rows = []
        for t in THRESHOLDS:
            reused = best >= t
            n_re, n_ok = int(reused.sum()), int((reused & ok).sum())
            rows.append(
                {
                    "threshold": float(t),
                    "reuse_rate": n_re / Q,
                    "correct_reuse_rate": n_ok / Q,
                    "false_reuse_share": (n_re - n_ok) / n_re if n_re else 0.0,
                }
            )
        curves[name] = rows
    return {"n_cached": A, "n_queries": Q, "designs": result, "curves": curves}


def _zero_and_budget(best: np.ndarray, ok: np.ndarray, w: np.ndarray, total: float) -> dict:
    """Best correct-reuse rate achievable while false reuse stays within budget.

    Budget is a share of reuses (1 - precision). At 0 it is the largest
    threshold-above-every-false-match: everything strictly above the highest
    false similarity is reused.
    """
    out = {}
    finite = np.isfinite(best)
    order = np.argsort(-best[finite], kind="stable")
    b, o, ww = best[finite][order], ok[finite][order], w[finite][order]
    cum_ok = np.cumsum(ww * o)
    cum_all = np.cumsum(ww)
    # Only cut between distinct similarity values: a threshold cannot split ties.
    last_of_value = np.r_[b[1:] != b[:-1], True]
    # A bootstrap draw gives undrawn anchors' queries weight 0, so a prefix
    # can have zero total weight; that 0/0 is "no reuses yet", not an error.
    with np.errstate(invalid="ignore", divide="ignore"):
        false_share = 1 - cum_ok / cum_all
    for budget in FALSE_REUSE_BUDGETS:
        if b.size == 0:
            out[f"correct_reuse_at_false_{budget:g}"] = 0.0
            continue
        feasible = last_of_value & (false_share <= budget + 1e-12)
        best_ok = cum_ok[feasible].max() if feasible.any() else 0.0
        out[f"correct_reuse_at_false_{budget:g}"] = float(best_ok / total)
    return out


def _oracle_per_entry(best, ok, nn, w, total, n_anchors) -> dict:
    """Per-entry thresholds chosen with the labels: the ceiling for any
    per-entry method at zero false reuse.

    For each cached entry, the threshold sits just above the highest-scoring
    wrong query routed to it; every correct query above that is reused.
    """
    # Only queries in this sample may set a threshold.
    finite = np.isfinite(best) & (w > 0)
    max_false = np.full(n_anchors, -np.inf)
    sel = finite & ~ok
    np.maximum.at(max_false, nn[sel], best[sel])
    reused_ok = finite & ok & (best > max_false[nn])
    return {"correct_reuse_at_false_0": float((w * reused_ok).sum() / total)}


# ── Reporting ────────────────────────────────────────────────────────────


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")


def write_markdown(report: dict, path: Path) -> None:
    inv = report["pairs"]["inversion"]
    sim = report["pairs"]["similarity_by_pair_type"]
    des = report["cache"]["designs"]
    lines = [
        f"# {report['embedder']}",
        "",
        f"Dataset sha256(pairs) `{report['dataset_sha256_pairs'][:16]}`, "
        f"{report['cache']['n_cached']} cached questions, {report['cache']['n_queries']} queries, "
        f"{report['bootstrap']} bootstrap resamples.",
        "",
        "## A. Similarity to the cached question, by pair type",
        "",
        "| Pair type | n | mean | p10 | median | p90 | max |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for k, v in sim.items():
        if k.count("/") == 0:
            lines.append(
                f"| **{k}** | {v['n']} | {v['mean']} | {v['p10']} | {v['median']} | {v['p90']} | {v['max']} |"
            )
    for k, v in sim.items():
        if k.count("/") == 2:
            lines.append(
                f"| {k} | {v['n']} | {v['mean']} | {v['p10']} | {v['median']} | {v['p90']} | {v['max']} |"
            )
    lines += [
        "",
        "## B. Inversion per cached question",
        "",
        "Strong: the best wrong question scores ≥ the best correct one. Weak: ≥ the worst correct one.",
        "",
        "| Negatives considered | anchors | strong | 95% CI | weak | 95% CI |",
        "|---|---:|---:|---|---:|---|",
    ]
    for k, v in inv.items():
        lines.append(
            f"| {k} | {v['anchors']} | {v['strong_rate']} | {v['strong_ci95']} | {v['weak_rate']} | {v['weak_ci95']} |"
        )
    lines += [
        "",
        "## C. Cache simulation — share of queries correctly reused",
        "",
        "| Design | at 0% false reuse | 95% CI | at ≤1% | at ≤5% | possible |",
        "|---|---:|---|---:|---:|---:|",
    ]
    for name, m in des.items():
        z = m["correct_reuse_at_false_0"]
        one = m.get("correct_reuse_at_false_0.01", {}).get("value", "—")
        five = m.get("correct_reuse_at_false_0.05", {}).get("value", "—")
        lines.append(
            f"| {name} | {z['value']} | {z['ci95']} | {one} | {five} | {m['possible']['value']} |"
        )
    lines += [
        "",
        "split_* use gold parameters (oracle extraction). split_template counts a reuse as correct "
        "when the intent matches, because the template is refilled with the new parameters.",
        "",
        "## Largest inversions",
        "",
        "| Cached | Wrong match | sim | Best correct | sim |",
        "|---|---|---:|---|---:|",
    ]
    for e in report["pairs"]["top_inversions"]:
        lines.append(
            f"| {e['cached']} | {e['wrong']} | {e['wrong_sim']} | {e['best_correct']} | {e['correct_sim']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def summarize(results_dir: Path) -> None:
    rows = []
    for rp in sorted(results_dir.glob("*/report.json")):
        r = json.loads(rp.read_text(encoding="utf-8"))
        inv, des = r["pairs"]["inversion"], r["cache"]["designs"]
        sha = r["dataset_sha256_pairs"][:12]

        def z(name: str, des: dict = des) -> str:
            m = des[name]["correct_reuse_at_false_0"]
            return f"{m['value']:.3f} {m['ci95']}"

        rows.append(
            f"| {r['embedder']} | {sha} | {inv['param_near_miss']['strong_rate']:.3f} "
            f"{inv['param_near_miss']['strong_ci95']} | {inv['period_near_miss']['strong_rate']:.3f} | "
            f"{inv['entity_near_miss']['strong_rate']:.3f} | {inv['intent_near_miss']['strong_rate']:.3f} | "
            f"{z('raw_global')} | {z('raw_oracle_entry')} | {z('split_full')} | {z('split_template')} |"
        )
    header = [
        "| Embedder | dataset | strong inversion: param near-miss [CI] | period | entity | intent "
        "| raw_global @0 | raw_oracle_entry @0 | split_full @0 | split_template @0 |",
        "|---|---|---|---:|---:|---:|---|---|---|---|",
    ]
    out = "\n".join(header + rows) + "\n"
    (results_dir / "SUMMARY.md").write_text(out, encoding="utf-8")
    print(out)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--data", type=Path, default=HERE / "data")
    ap.add_argument("--out", type=Path, default=HERE / "results")
    ap.add_argument("--embedder", default="tfidf")
    ap.add_argument(
        "--prefix", default="", help='text prepended to every input, e.g. "query: " for e5'
    )
    ap.add_argument("--project", default="")
    ap.add_argument("--location", default="us-central1")
    ap.add_argument("--dimensions", type=int, default=768)
    ap.add_argument("--task-type", default=None)
    ap.add_argument("--bootstrap", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--summarize", action="store_true")
    args = ap.parse_args()
    # Windows consoles default to cp1252, which cannot print the report's "≥".
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.summarize:
        summarize(args.out)
        return

    questions, pairs, manifest = load(args.data)
    label = (
        args.embedder
        + (f" prefix={args.prefix!r}" if args.prefix else "")
        + (f" task_type={args.task_type}" if args.task_type else "")
    )
    out_dir = args.out / slug(label)

    texts = sorted({q["text"] for q in questions} | {q["masked_text"] for q in questions})
    tindex = {t: i for i, t in enumerate(texts)}
    vecs = embed(texts, args, out_dir)
    raw = vecs[[tindex[q["text"]] for q in questions]]
    masked = vecs[[tindex[q["masked_text"]] for q in questions]]
    qidx = {q["id"]: i for i, q in enumerate(questions)}

    rng = np.random.default_rng(args.seed)
    report = {
        "embedder": label,
        "dataset_sha256_pairs": manifest["sha256"]["pairs.jsonl"],
        "bootstrap": args.bootstrap,
        "pairs": pair_analysis(pairs, qidx, raw, rng, args.bootstrap),
        "cache": cache_simulation(questions, raw, masked, rng, args.bootstrap),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    write_markdown(report, out_dir / "report.md")
    print((out_dir / "report.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
