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
     With --extracted, both split designs are rerun on a real extractor's
     parameters and masked text (from extract.py) and reported beside the
     oracle ones. Routing then sees only extracted values; correctness is
     still judged against gold. Each extracted design is also evaluated at
     the threshold its oracle twin needed for zero false reuse: the
     threshold a team would have calibrated in the lab, then deployed.

Every headline number carries a 95% bootstrap interval, resampling cached
questions together with the queries generated from them, because queries
from one anchor are not independent of each other.

Usage:
    python evaluate.py --embedder tfidf
    python evaluate.py --embedder st:sentence-transformers/all-MiniLM-L6-v2
    python evaluate.py --embedder st:intfloat/e5-base-v2 --prefix "query: "
    python evaluate.py --embedder vertex:text-embedding-004 --project <gcp-project>
    python evaluate.py --embedder openai:text-embedding-3-large
    python evaluate.py --embedder voyage:voyage-4
    python evaluate.py --embedder bedrock:amazon.titan-embed-text-v2:0 --region us-east-1
    python evaluate.py --embedder bedrock:cohere.embed-v4:0 --region us-east-1
    python evaluate.py --embedder npz:my_vectors.npz        # bring your own

`--task-type` is the provider's task or input-type knob: Vertex task_type,
Voyage input_type, Cohere input_type. `--dimensions` is passed through only
when given, except Vertex, which defaults to the application's 768.
    python evaluate.py --summarize
    python evaluate.py --embedder st:BAAI/bge-base-en-v1.5 \\
        --extracted results/extraction/gemini_gemini-3.1-flash-lite/extracted.jsonl
    python evaluate.py --summarize-extraction
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
from guards import (
    GOLD_FULL_SIGNATURES,
    GOLD_SIGNATURES,
    full_signature_key,
    has_negation_cue,
    negation_consistent,
    signature_key,
)

HERE = Path(__file__).parent
THRESHOLDS = np.round(np.arange(0.50, 1.0001, 0.005), 3)
FALSE_REUSE_BUDGETS = (0.0, 0.01, 0.05)
# The guarded designs use similarity only to shortlist. 0.50 is the lower
# bound of the "guide" band in a published production cache for analytics
# questions (arXiv 2601.11687; it generates pandas code, not SQL): below it,
# a cached plan is not even offered as a hint.
GUARD_SHORTLIST_THRESHOLD = 0.50
# Sensitivity of the guarded designs to that floor (README section 16). None
# is no floor at all: similarity only ranks, so the result cannot depend on
# how an embedder spreads its scores.
GUARD_SHORTLIST_SWEEP = (None, 0.30, 0.40, 0.50, 0.60, 0.70)


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


# The Hugging Face revision of each open model, as every report used it: read
# from the local model cache on 2026-10-30, where each held one snapshot. A
# later revision could change the vectors (README section 22).
ST_REVISIONS = {
    "sentence-transformers/all-MiniLM-L6-v2": "1110a243fdf4706b3f48f1d95db1a4f5529b4d41",
    "sentence-transformers/all-mpnet-base-v2": "e8c3b32edf5434bc2275fc9bab85f82640a19130",
    "BAAI/bge-base-en-v1.5": "a5beb1e3e68b9ab74eb54cfd186867f64f240e1a",
    "intfloat/e5-base-v2": "f52bf8ec8c7124536f0efb74aca902b2995e5bcd",
    "Qwen/Qwen3-Embedding-0.6B": "97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3",
    "Snowflake/snowflake-arctic-embed-l-v2.0": "ac6544c8a46e00af67e330e85a9028c66b8cfd9a",
    "mixedbread-ai/mxbai-embed-large-v1": "b33106f585b9ce46904ad7443a3b52b7a63e231c",
}


def embed_sentence_transformers(texts: list[str], model: str, prefix: str) -> np.ndarray:
    from sentence_transformers import SentenceTransformer

    st = SentenceTransformer(model, revision=ST_REVISIONS.get(model))
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

    The defaults (768 dimensions, no task type) mirror the production
    embedding configuration, so the result describes what the application
    uses rather than a tuned variant.
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


def embed_openai(texts: list[str], model: str, dimensions: int | None) -> np.ndarray:
    """OpenAI embeddings API. Reads OPENAI_API_KEY from the environment."""
    from openai import OpenAI

    client = OpenAI(max_retries=8)
    extra = {"dimensions": dimensions} if dimensions else {}
    out: list[list[float]] = []
    for i in range(0, len(texts), 256):
        res = client.embeddings.create(model=model, input=texts[i : i + 256], **extra)
        out.extend(d.embedding for d in sorted(res.data, key=lambda d: d.index))
    return _normalise(np.array(out))


def embed_voyage(texts: list[str], model: str, input_type: str | None) -> np.ndarray:
    """Voyage AI — the provider Anthropic's documentation points to, since
    Anthropic has no embedding model of its own. Reads VOYAGE_API_KEY.

    input_type defaults to None: both sides of a cache lookup are questions,
    so the symmetric setting is the honest one. "query" is worth a second run.
    """
    import voyageai

    # The SDK retries rate-limit errors itself; a free account without a
    # payment method can have very low limits, so allow it to wait.
    client = voyageai.Client(max_retries=8)
    out: list[list[float]] = []
    for i in range(0, len(texts), 128):
        res = client.embed(texts[i : i + 128], model=model, input_type=input_type)
        out.extend(res.embeddings)
    return _normalise(np.array(out))


def embed_bedrock(
    texts: list[str], model: str, region: str | None, dimensions: int | None, input_type: str | None
) -> np.ndarray:
    """Amazon Bedrock: Titan Text Embeddings and Cohere Embed. Uses the
    standard AWS credential chain (profile, env vars, SSO).

    Titan takes one text per call; Cohere takes up to 96. Cohere requires an
    input_type; "search_query" on both sides keeps the comparison symmetric.
    """
    import time

    import boto3
    from botocore.exceptions import ClientError

    client = boto3.client("bedrock-runtime", region_name=region)

    def invoke(body: dict) -> dict:
        for attempt in range(6):
            try:
                res = client.invoke_model(modelId=model, body=json.dumps(body))
                return json.loads(res["body"].read())
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "ThrottlingException" or attempt == 5:
                    raise
                time.sleep(2**attempt)
        raise AssertionError("unreachable")

    out: list[list[float]] = []
    if model.startswith("amazon.titan"):
        for t in texts:
            body = {"inputText": t, "normalize": True}
            if dimensions:
                body["dimensions"] = dimensions
            out.append(invoke(body)["embedding"])
    elif model.startswith("cohere."):
        for i in range(0, len(texts), 96):
            body = {
                "texts": texts[i : i + 96],
                "input_type": input_type or "search_query",
                "embedding_types": ["float"],
            }
            if dimensions:
                body["output_dimension"] = dimensions
            emb = invoke(body)["embeddings"]
            # v3 returns a list of vectors; v4 keys them by embedding type.
            out.extend(emb["float"] if isinstance(emb, dict) else emb)
    else:
        raise SystemExit(f"unsupported Bedrock model {model!r} (titan or cohere only)")
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
            texts, name, args.project, args.location, args.dimensions or 768, args.task_type
        )
    elif kind == "openai":
        vecs = embed_openai(texts, name, args.dimensions)
    elif kind == "voyage":
        vecs = embed_voyage(texts, name, args.task_type)
    elif kind == "bedrock":
        vecs = embed_bedrock(texts, name, args.region, args.dimensions, args.task_type)
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


_YEAR = re.compile(r"\b20\d\d\b")


def ab_comparisons(
    pairs: list[dict], qidx: dict[str, int], raw: np.ndarray, seed: int, n_boot: int
) -> dict:
    """Comparisons A and B (README section 8; pre-registered for v2 in section 11).

    For each cached question, its best period swap in the SAME wording is
    compared against:
      A  the best reworded correct question (relation "paraphrase");
      B  the best one-span correct rewording of the period that needs no
         date knowledge (neither side, or both, name a year).
    Each is the share of cached questions where the swap scores at or above.
    Its own generator, so adding this changes no other number in a report.
    """

    def sim(p: dict) -> float:
        return float(raw[qidx[p["anchor_id"]]] @ raw[qidx[p["candidate_id"]]])

    def one_span_dateless(p: dict) -> bool:
        return (
            p["relation"] == "equivalent_surface"
            and p["dimension"] == "period"
            and bool(_YEAR.search(p["anchor_text"])) == bool(_YEAR.search(p["candidate_text"]))
        )

    by_anchor: dict[str, list[dict]] = defaultdict(list)
    for p in pairs:
        by_anchor[p["anchor_id"]].append(p)
    flags: dict[str, list[float]] = {"A": [], "B": []}
    for ps in by_anchor.values():
        neg = [
            sim(p)
            for p in ps
            if p["relation"] == "param_near_miss"
            and p["dimension"] == "period"
            and p["same_wording"]
        ]
        para = [sim(p) for p in ps if p["relation"] == "paraphrase"]
        span = [sim(p) for p in ps if one_span_dateless(p)]
        if neg and para:
            flags["A"].append(float(max(neg) >= max(para)))
        if neg and span:
            flags["B"].append(float(max(neg) >= max(span)))
    rng = np.random.default_rng(seed)
    out = {}
    for k, v in flags.items():
        a = np.array(v)
        boots = [float(a[rng.integers(0, a.size, a.size)].mean()) for _ in range(n_boot)]
        out[k] = {"n": int(a.size), "rate": round(float(a.mean()), 4), "ci95": ci(boots)}
    return out


# ── C: cache simulation ──────────────────────────────────────────────────


def cache_simulation(
    questions: list[dict],
    raw: np.ndarray,
    masked: np.ndarray,
    rng: np.random.Generator,
    n_boot: int,
    ext: dict[str, dict] | None = None,
    ext_masked: np.ndarray | None = None,
    holdout: bool = False,
    domain: str = "finance",
) -> dict:
    anchors = [q for q in questions if q["is_anchor"]]
    # --holdout (dataset v2): only queries worded with a template no cached
    # entry of their intent uses, so no query can match a cached wording
    # exactly — the closest the generated data gets to unseen phrasing.
    queries = [
        q for q in questions if not q["is_anchor"] and (not holdout or q.get("split") == "query")
    ]
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
    # A set, not the template's order: "{period}, not counting {category}"
    # and "except {category} {period}" fill the same two slots.
    same_slots = np.array(
        [[sorted(q["slots"]) == sorted(a["slots"]) for a in anchors] for q in queries]
    )
    same_sql = same_intent & same_params

    designs = {
        # name: (similarity matrix, eligibility, correctness)
        "raw_global": (S_raw, np.ones_like(same_sql), same_sql),
        "split_full": (S_mask, same_slots & same_params, same_sql),
        "split_template": (S_mask, same_slots, same_intent),
    }
    calibrate_from: dict[str, str] = {}
    fixed_thresholds: dict[str, float] = {}
    params_right = np.ones(Q, dtype=bool)
    slots_right = np.ones(Q, dtype=bool)
    if ext is not None:

        def ekey(q: dict) -> str:
            return json.dumps(ext[q["id"]]["params"], sort_keys=True)

        def eslots(q: dict) -> list[str]:
            return sorted(ext[q["id"]]["params"])

        S_ext = ext_masked[qi] @ ext_masked[ai].T
        e_same_params = np.array([[ekey(q) == ekey(a) for a in anchors] for q in queries])
        e_same_slots = np.array([[eslots(q) == eslots(a) for a in anchors] for q in queries])
        # The refilled template is right only if the query's own values were
        # extracted right; the cached entry contributes only its template.
        params_right = np.array([ekey(q) == key(q) for q in queries])
        designs["split_full_extracted"] = (S_ext, e_same_slots & e_same_params, same_sql)
        designs["split_template_extracted"] = (
            S_ext,
            e_same_slots,
            same_intent & params_right[:, None],
        )
        # Template-slot scoring: the refilled SQL uses only the slots its
        # template has, so an extra value ("top 1" on "biggest single
        # purchase") cannot change it. Missing or wrong template values can.
        slots_right = np.array(
            [
                all(ext[q["id"]]["params"].get(s) == q["params"][s] for s in q["slots"])
                for q in queries
            ]
        )
        designs["split_template_extracted_slots"] = (
            S_ext,
            e_same_slots,
            same_intent & slots_right[:, None],
        )
        calibrate_from = {
            "split_full_extracted": "split_full",
            "split_template_extracted": "split_template",
            "split_template_extracted_slots": "split_template",
        }

        # ── Guarded designs (README section 15) ──
        # Negation guard: a cue in both questions or in neither, and a
        # question with a cue must have a named value to exclude.
        cue_q = np.array([has_negation_cue(q["text"]) for q in queries])
        cue_a = np.array([has_negation_cue(a["text"]) for a in anchors])
        ok_q = np.array([negation_consistent(q["text"], ext[q["id"]]["params"]) for q in queries])
        ok_a = np.array([negation_consistent(a["text"], ext[a["id"]]["params"]) for a in anchors])
        neg_guard = (cue_q[:, None] == cue_a[None, :]) & ok_q[:, None] & ok_a[None, :]
        correct_slots = same_intent & slots_right[:, None]
        designs["split_template_negguard"] = (S_ext, e_same_slots & neg_guard, correct_slots)
        calibrate_from["split_template_negguard"] = "split_template"
        if all("flow" in (ext[q["id"]].get("signature") or {}) for q in questions):
            # Signature guard: the extractor's own (operation, excludes, flow)
            # must match. Similarity only shortlists, at the fixed 0.50.
            sq = [signature_key(ext[q["id"]]["signature"]) for q in queries]
            sa = [signature_key(ext[a["id"]]["signature"]) for a in anchors]
            sig_eq = np.array([[x is not None and x == y for y in sa] for x in sq])
            designs["split_template_guarded"] = (
                S_ext,
                e_same_slots & neg_guard & sig_eq,
                correct_slots,
            )
            fixed_thresholds["split_template_guarded"] = GUARD_SHORTLIST_THRESHOLD
        if domain in GOLD_SIGNATURES:
            # Upper bound: the same guards given the author's signatures.
            gs = GOLD_SIGNATURES[domain]
            gold_eq = np.array(
                [[gs[q["intent"]] == gs[a["intent"]] for a in anchors] for q in queries]
            )
            designs["split_template_guarded_goldsig"] = (
                S_ext,
                e_same_slots & neg_guard & gold_eq,
                correct_slots,
            )
            fixed_thresholds["split_template_guarded_goldsig"] = GUARD_SHORTLIST_THRESHOLD
        if all("measure" in (ext[q["id"]].get("signature") or {}) for q in questions):
            # Full signature (README section 18): the measure and grouping too,
            # so similarity only breaks ties between same-intent templates.
            fq = [full_signature_key(ext[q["id"]]["signature"]) for q in queries]
            fa = [full_signature_key(ext[a["id"]]["signature"]) for a in anchors]
            full_eq = np.array([[x is not None and x == y for y in fa] for x in fq])
            designs["split_template_fullsig"] = (
                S_ext,
                e_same_slots & neg_guard & full_eq,
                correct_slots,
            )
            fixed_thresholds["split_template_fullsig"] = GUARD_SHORTLIST_THRESHOLD
            gf = GOLD_FULL_SIGNATURES[domain]
            gold_full_eq = np.array(
                [[gf[q["intent"]] == gf[a["intent"]] for a in anchors] for q in queries]
            )
            designs["split_template_fullsig_gold"] = (
                S_ext,
                e_same_slots & neg_guard & gold_full_eq,
                correct_slots,
            )
            fixed_thresholds["split_template_fullsig_gold"] = GUARD_SHORTLIST_THRESHOLD
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

    # Calibration happens once, on the full oracle run, as it would in a lab;
    # the bootstrap then varies only the traffic the threshold meets.
    thresholds = {
        name: _zero_threshold(routed[src][1], routed[src][2])
        for name, src in calibrate_from.items()
    }
    thresholds |= fixed_thresholds

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
            if name in thresholds:
                reused = np.isfinite(best) & (best >= thresholds[name])
                n_re = float((w_q * reused).sum())
                wrong = float((w_q * (reused & ~ok)).sum())
                out[name]["calibrated_reuse"] = n_re / total
                out[name]["calibrated_correct_reuse"] = (n_re - wrong) / total
                out[name]["calibrated_false_share"] = wrong / n_re if n_re else 0.0
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

    # The guarded designs at other shortlist floors. Uses no randomness, so
    # it changes no other number in a report.
    shortlist_sweep = {}
    for name in (
        "split_template_guarded",
        "split_template_guarded_goldsig",
        "split_template_fullsig",
        "split_template_fullsig_gold",
    ):
        if name not in routed:
            continue
        _, best, ok, _ = routed[name]
        rows = []
        for t in GUARD_SHORTLIST_SWEEP:
            reused = np.isfinite(best) & (best >= (-np.inf if t is None else t))
            n_re, n_ok = int(reused.sum()), int((reused & ok).sum())
            rows.append(
                {
                    "floor": t,
                    "correct_reuse_rate": round(n_ok / Q, 4),
                    "false_reuses": n_re - n_ok,
                    "false_reuse_share": round((n_re - n_ok) / n_re, 4) if n_re else 0.0,
                }
            )
        shortlist_sweep[name] = rows

    # Why each false reuse at the calibrated threshold was false: the wrong
    # template, the wrong extracted values, or both.
    causes = {}
    for name, t in thresholds.items():
        nn, best, ok, _ = routed[name]
        bad = np.flatnonzero(np.isfinite(best) & (best >= t) & ~ok)
        wrong_intent = ~same_intent[bad, nn[bad]]
        if name == "split_full_extracted":
            # Full-SQL reuse is wrong when the gold parameters differ, whoever
            # extracted them as equal.
            wrong_values = ~same_params[bad, nn[bad]]
        elif name == "split_template_extracted":
            wrong_values = ~params_right[bad]
        else:
            # Template-slot scoring: the slots and guarded designs.
            wrong_values = ~slots_right[bad]
        causes[name] = {
            "threshold": round(float(t), 4),
            "false_reuses": int(bad.size),
            "wrong_template_only": int((wrong_intent & ~wrong_values).sum()),
            "wrong_values_only": int((~wrong_intent & wrong_values).sum()),
            "both": int((wrong_intent & wrong_values).sum()),
        }

    # One row per query and extracted design, so two extractors run on the
    # same queries can be compared pairwise (evaluate.py --compare).
    per_query = {
        name: [
            {
                "id": q["id"],
                "group": q["group"],
                "sim": round(float(routed[name][1][i]), 6)
                if np.isfinite(routed[name][1][i])
                else None,
                "reused": bool(np.isfinite(routed[name][1][i]) and routed[name][1][i] >= t),
                "ok": bool(routed[name][2][i]),
            }
            for i, q in enumerate(queries)
        ]
        for name, t in thresholds.items()
    }

    # Can similarity tell a value error from a correct extraction? Among
    # queries routed to an entry of the right intent, compare the similarity
    # of those whose template values were extracted wrong with those
    # extracted right. AUC 0.5 means it carries no signal at all.
    separability = {}
    if ext is not None:
        nn, best, _, _ = routed["split_template_extracted_slots"]
        right_intent = np.isfinite(best) & same_intent[np.arange(Q), nn]
        separability = _auc_by_group(
            best[right_intent], ~slots_right[right_intent], group[right_intent], A, rng, n_boot
        )
    return {
        "n_cached": A,
        "n_queries": Q,
        "holdout": holdout,
        "designs": result,
        "calibrated": causes,
        "separability": separability,
        "per_query": per_query,
        "curves": curves,
        "shortlist_sweep": shortlist_sweep,
    }


def _auc_by_group(
    score: np.ndarray,
    positive: np.ndarray,
    group: np.ndarray,
    n_groups: int,
    rng: np.random.Generator,
    n_boot: int,
) -> dict:
    """P(score of a positive > score of a negative), ties counted half, with a
    cluster-bootstrap interval over query groups."""
    pos, neg = np.flatnonzero(positive), np.flatnonzero(~positive)
    if pos.size == 0 or neg.size == 0:
        return {"n_positive": int(pos.size), "n_negative": int(neg.size), "auc": None}
    sp, sn = score[pos][:, None], score[neg][None, :]
    C = (sp > sn) + 0.5 * (sp == sn)

    def auc(w: np.ndarray) -> float:
        wp, wn = w[group[pos]], w[group[neg]]
        den = wp.sum() * wn.sum()
        return float(wp @ C @ wn / den) if den else float("nan")

    point = auc(np.ones(n_groups))
    boots = [
        auc(np.bincount(rng.integers(0, n_groups, n_groups), minlength=n_groups))
        for _ in range(n_boot)
    ]
    return {
        "n_positive": int(pos.size),
        "n_negative": int(neg.size),
        "auc": round(point, 4),
        "auc_ci95": ci(boots),
        "positive_sim_median": round(float(np.median(score[pos])), 4),
        "negative_sim_median": round(float(np.median(score[neg])), 4),
    }


def _zero_threshold(best: np.ndarray, ok: np.ndarray) -> float:
    """The threshold _zero_and_budget uses at budget 0: the lowest similarity
    strictly above the highest-scoring false match. inf if nothing qualifies."""
    finite = np.isfinite(best)
    b, o = best[finite], ok[finite]
    if not (~o).any():
        return float(b.min()) if b.size else float("inf")
    above = b[b > b[~o].max()]
    return float(above.min()) if above.size else float("inf")


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


def study_path(p: Path) -> str:
    """A path inside this folder, relative to it, so a report is the same
    wherever the study is checked out (README section 22)."""
    try:
        return p.resolve().relative_to(HERE.resolve()).as_posix()
    except ValueError:
        return p.as_posix()


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
    ab = report["pairs"].get("ab")
    if ab:
        lines += [
            "",
            "A: same-wording period swap ≥ best reworded correct question. "
            "B: ≥ best one-span, date-free correct rewording.",
            "",
            "| Comparison | n | rate | 95% CI |",
            "|---|---:|---:|---|",
        ]
        lines += [f"| {k} | {v['n']} | {v['rate']} | {v['ci95']} |" for k, v in ab.items()]
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
    ]
    if report["cache"].get("calibrated"):
        lines += [
            "## D. Real extraction at the oracle-calibrated threshold",
            "",
            "| Design | threshold | reuse | correct reuse [CI] | false share of reuses [CI] "
            "| false reuses | wrong template only | wrong values only | both |",
            "|---|---:|---:|---|---|---:|---:|---:|---:|",
        ]
        for name, c in report["cache"]["calibrated"].items():
            m = des[name]
            lines.append(
                f"| {name} | {c['threshold']} | {m['calibrated_reuse']['value']} | "
                f"{m['calibrated_correct_reuse']['value']} {m['calibrated_correct_reuse']['ci95']} | "
                f"{m['calibrated_false_share']['value']} {m['calibrated_false_share']['ci95']} | "
                f"{c['false_reuses']} | {c['wrong_template_only']} | {c['wrong_values_only']} | "
                f"{c['both']} |"
            )
        sep = report["cache"].get("separability") or {}
        if sep.get("auc") is not None:
            lines += [
                "",
                "Similarity as a detector of value errors (right-intent matches): "
                f"AUC {sep['auc']} {sep['auc_ci95']}, {sep['n_positive']} with a template "
                f"value wrong vs {sep['n_negative']} right; median similarity "
                f"{sep['positive_sim_median']} vs {sep['negative_sim_median']}. "
                "0.5 = no signal.",
            ]
        lines += [""]
    lines += [
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


def compare(paths: list[Path], n_boot: int, seed: int) -> None:
    """Paired comparison of two extracted runs on the same queries.

    For each extracted design, the false share of reuses at the calibrated
    threshold in A and in B, and B - A, with one cluster bootstrap that
    redraws the same query groups for both — so the interval reflects the
    difference between extractors, not the sampling of questions twice.
    """
    a, b = (json.loads(p.read_text(encoding="utf-8")) for p in paths)
    rng = np.random.default_rng(seed)
    print(f"A = {paths[0]}\nB = {paths[1]}\n")
    print("| Design | A false share | B false share | B - A [95% CI] | A reuse | B reuse |")
    print("|---|---:|---:|---|---:|---:|")
    for name in a["cache"]["per_query"]:
        ra = {r["id"]: r for r in a["cache"]["per_query"][name]}
        rb = {r["id"]: r for r in b["cache"]["per_query"].get(name, [])}
        if set(ra) != set(rb):
            raise SystemExit(f"{name}: the two runs do not cover the same queries")
        ids = sorted(ra)
        gids = sorted({ra[i]["group"] for i in ids})
        gpos = {g: k for k, g in enumerate(gids)}
        g = np.array([gpos[ra[i]["group"]] for i in ids])

        def arr(r: dict, f: str, ids: list[str] = ids) -> np.ndarray:
            return np.array([r[i][f] for i in ids], dtype=bool)

        reA, okA, reB, okB = arr(ra, "reused"), arr(ra, "ok"), arr(rb, "reused"), arr(rb, "ok")

        def share(w: np.ndarray, re: np.ndarray, ok: np.ndarray) -> float:
            n = (w * re).sum()
            return float((w * (re & ~ok)).sum() / n) if n else 0.0

        ones = np.ones(len(ids))
        fa, fb = share(ones, reA, okA), share(ones, reB, okB)
        diffs = []
        for _ in range(n_boot):
            w = np.bincount(rng.integers(0, len(gids), len(gids)), minlength=len(gids))[g]
            diffs.append(share(w, reB, okB) - share(w, reA, okA))
        print(
            f"| {name} | {fa:.4f} | {fb:.4f} | {fb - fa:+.4f} {ci(diffs)} | "
            f"{reA.mean():.3f} | {reB.mean():.3f} |"
        )


def summarize_extraction(extraction_dir: Path) -> None:
    rows = []
    for rp in sorted(extraction_dir.glob("*/*/report.json")):
        r = json.loads(rp.read_text(encoding="utf-8"))
        des = r["cache"]["designs"]
        if "split_template_extracted_slots" not in des:
            raise SystemExit(f"{rp} predates template-slot scoring; rerun it")
        acc = json.loads((rp.parent.parent / "accuracy.json").read_text(encoding="utf-8"))

        def v(name: str, m: str, des: dict = des) -> str:
            x = des[name][m]
            return f"{x['value']:.4f} {x['ci95']}"

        rows.append(
            f"| {acc['extractor']} | {r['embedder']} | {acc['frame_accuracy']:.3f} "
            f"| {v('split_template_extracted', 'calibrated_false_share')} "
            f"| {v('split_template_extracted_slots', 'calibrated_false_share')} "
            f"| {v('split_template_extracted', 'calibrated_correct_reuse')} "
            f"| {v('split_template_extracted', 'correct_reuse_at_false_0.01')} "
            f"| {v('raw_global', 'correct_reuse_at_false_0.01')} "
            f"| {v('split_full_extracted', 'calibrated_false_share')} |"
        )
    header = [
        "| Extractor | Embedder | frame acc. | template: false share @calibrated (strict) "
        "| template: false share (template slots) "
        "| template: correct reuse @calibrated | template: correct reuse @≤1% "
        "| raw_global: correct reuse @≤1% | full-SQL: false share @calibrated |",
        "|---|---|---:|---|---|---|---|---|---|",
    ]
    out = "\n".join(header + rows) + "\n"
    (extraction_dir / "SUMMARY.md").write_text(out, encoding="utf-8")
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
    ap.add_argument("--location", default="us-central1", help="Vertex location")
    ap.add_argument("--region", default=None, help="AWS region for Bedrock")
    ap.add_argument("--dimensions", type=int, default=None)
    ap.add_argument("--task-type", default=None)
    ap.add_argument("--bootstrap", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--summarize", action="store_true")
    ap.add_argument(
        "--extracted",
        type=Path,
        default=None,
        help="extracted.jsonl from extract.py: rerun the split designs on its parameters",
    )
    ap.add_argument("--summarize-extraction", action="store_true")
    ap.add_argument(
        "--holdout",
        action="store_true",
        help="dataset v2: simulate only queries worded with a template no cached entry uses",
    )
    ap.add_argument(
        "--compare",
        type=Path,
        nargs=2,
        metavar=("REPORT_A", "REPORT_B"),
        help="paired comparison of two --extracted report.json files on the same queries",
    )
    args = ap.parse_args()
    # Windows consoles default to cp1252, which cannot print the report's "≥".
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.summarize:
        summarize(args.out)
        return
    if args.summarize_extraction:
        summarize_extraction(args.out / "extraction")
        return
    if args.compare:
        compare(args.compare, args.bootstrap, args.seed)
        return

    questions, pairs, manifest = load(args.data)
    label = (
        args.embedder
        + (f" prefix={args.prefix!r}" if args.prefix else "")
        + (f" task_type={args.task_type}" if args.task_type else "")
        + (f" dims={args.dimensions}" if args.dimensions else "")
    )
    report_label = label + (" holdout" if args.holdout else "")
    # Embeddings stay cached beside the embedder's own report either way.
    emb_dir = args.out / slug(label)
    out_dir = args.out / slug(report_label)

    ext = None
    if args.extracted:
        with args.extracted.open(encoding="utf-8") as f:
            ext = {r["id"]: r for r in map(json.loads, f) if r}
        if set(ext) != {q["id"] for q in questions}:
            raise SystemExit(f"{args.extracted} does not cover exactly the dataset's questions")
        out_dir = args.extracted.parent / slug(report_label)

    texts = {q["text"] for q in questions} | {q["masked_text"] for q in questions}
    if ext:
        texts |= {e["masked_text"] for e in ext.values()}
    texts = sorted(texts)
    tindex = {t: i for i, t in enumerate(texts)}
    vecs = embed(texts, args, emb_dir)
    raw = vecs[[tindex[q["text"]] for q in questions]]
    masked = vecs[[tindex[q["masked_text"]] for q in questions]]
    ext_masked = vecs[[tindex[ext[q["id"]]["masked_text"]] for q in questions]] if ext else None
    qidx = {q["id"]: i for i, q in enumerate(questions)}

    rng = np.random.default_rng(args.seed)
    report = {
        "embedder": report_label,
        "dataset_sha256_pairs": manifest["sha256"]["pairs.jsonl"],
        "generator_version": manifest.get("generator_version"),
        "bootstrap": args.bootstrap,
        "pairs": pair_analysis(pairs, qidx, raw, rng, args.bootstrap),
        "cache": cache_simulation(
            questions,
            raw,
            masked,
            rng,
            args.bootstrap,
            ext=ext,
            ext_masked=ext_masked,
            holdout=args.holdout,
            domain=manifest.get("domain", "finance"),
        ),
    }
    report["pairs"]["ab"] = ab_comparisons(pairs, qidx, raw, args.seed + 1, args.bootstrap)
    if args.extracted:
        report["extracted"] = study_path(args.extracted)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    write_markdown(report, out_dir / "report.md")
    print((out_dir / "report.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
