"""Applies section 18's frozen rules (HQ-P, HQ-D, HQ-C, HQ-S, HQ-F) to the
reports in results_human. Prints every number a verdict rests on.

  python human_verdicts.py [--exclude copied|meaning] [--suffix -yearfix]

--suffix reads the runs tagged r1<suffix> etc. (section 20, exploratory).
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).parent
R = ROOT / "results_human"
DOMAINS = ("finance", "retail", "healthcare", "it_support")
RUNS = ("r1", "r2", "r3")
PRIMARY = (
    "st_sentence-transformers_all-MiniLM-L6-v2",
    "st_sentence-transformers_all-mpnet-base-v2",
    "st_BAAI_bge-base-en-v1.5",
    "st_intfloat_e5-base-v2_prefix_query",
)
SECONDARY = (
    "st_Qwen_Qwen3-Embedding-0.6B",
    "st_Snowflake_snowflake-arctic-embed-l-v2.0_prefix_query",
    "st_mixedbread-ai_mxbai-embed-large-v1",
    "vertex_text-embedding-004",
    "vertex_text-embedding-004_task_type_SEMANTIC_SIMILARITY",
    "vertex_gemini-embedding-001",
    "openai_text-embedding-3-small",
    "openai_text-embedding-3-large",
    "voyage_voyage-3-large",
    "voyage_voyage-3.5",
    "voyage_voyage-4",
)
SHORT = {e: e.split("_", 1)[1][:24] for e in PRIMARY + SECONDARY}
ARMS = {
    ("gemini", "relsig"): "gemini-relsig_gemini-3.1-flash-lite",
    ("gemini", "relfull"): "gemini-relfull_gemini-3.1-flash-lite",
    ("openai", "relsig"): "openai-relsig_gpt-6-luna",
    ("openai", "relfull"): "openai-relfull_gpt-6-luna",
}


def verdict(n_hold: int, n: int) -> str:
    if n_hold == n:
        return "GENERALISES"
    return "PARTIALLY" if n_hold else "DOES NOT GENERALISE"


def rep(arm, d, t, e, ex, suffix):
    # Gemini's -yearfix extractions are byte-identical to its registered ones
    # (checked), so its registered reports stand for them.
    if arm.startswith("gemini"):
        suffix = ""
    name = e + (f"_excl_{ex}" if ex else "")
    p = R / d / "extraction" / f"{arm}_{t}{suffix}" / name / "report.json"
    return json.loads(p.read_text(encoding="utf-8"))


def hq_p(ex):
    print(
        "\n== HQ-P: raw-similarity AUC (rewording vs period change), pooled; holds if CI upper < 0.80"
    )
    ok = True
    for e in PRIMARY + SECONDARY:
        name = e + (f"_excl_{ex}" if ex else "")
        r = json.loads((R / "similarity" / name / "report.json").read_text(encoding="utf-8"))
        p = r["pooled"]
        prim = e in PRIMARY
        if prim:
            ok &= p["ci95"][1] < 0.80
        per = " ".join(f"{d[:4]}={r[d]['auc']:.2f}" for d in DOMAINS)
        print(
            f"  {SHORT[e]:24s} {'primary  ' if prim else 'secondary'} AUC={p['auc']:.3f} "
            f"[{p['ci95'][0]:.3f},{p['ci95'][1]:.3f}] n+={p['n_rewordings']} n-={p['n_period_changes']}  {per}"
        )
    print(f"HQ-P: {'HOLDS' if ok else 'DOES NOT HOLD'}")


def hq_d(ex, suffix):
    print(
        "\n== HQ-D: period errors <= 0.5% of the writers' questions, each of r1-r3, both relfull runs"
    )
    ok = True
    for v in ("gemini", "openai"):
        for t in RUNS:
            n = err = 0
            for d in DOMAINS:
                r = rep(ARMS[(v, "relfull")], d, t, PRIMARY[0], ex, suffix)
                n += r["n_human"]
                err += r["period_errors"]["n"]
            good = err <= 0.005 * n
            ok &= good
            print(f"  {v:6s} {t}: {err}/{n} = {err / n:.4f} {'' if good else 'X'}")
    print(f"HQ-D: {'HOLDS' if ok else 'DOES NOT HOLD'}")


def hq_c(ex, suffix):
    caught = nx = false = no = 0
    for d in DOMAINS:
        c = rep(ARMS[("gemini", "relfull")], d, "r1", PRIMARY[0], ex, suffix)["negation_cue"]
        caught += c["caught"]
        nx += c["of_excluding"]
        false += c["false_cues"]
        no += c["of_other"]
    ok = caught >= 0.95 * nx and false <= 0.01 * no
    print(
        f"\n== HQ-C: caught {caught}/{nx} = {caught / nx:.3f} (>= 0.95); "
        f"false cues {false}/{no} = {false / no:.4f} (<= 0.01) -> {'HOLDS' if ok else 'DOES NOT HOLD'}"
    )


def guarded(label, arm_kind, design, ex, suffix, gold=None):
    print(
        f"\n== {label}: {design} on {arm_kind}: F <= 1% and correct >= exact-key + 0.10, "
        "all four embedders, >= 2 of r1-r3; per domain and vendor"
    )
    held = {}
    for v in ("gemini", "openai"):
        arm = ARMS[(v, arm_kind)]
        n_dom = 0
        for d in DOMAINS:
            n_runs = 0
            for t in RUNS:
                ok, cells = True, []
                for e in PRIMARY:
                    r = rep(arm, d, t, e, ex, suffix)
                    x = r["cache"]["designs"][design]
                    f, c = (
                        x["calibrated_false_share"]["value"],
                        x["calibrated_correct_reuse"]["value"],
                    )
                    cx = r["cache"]["designs"]["split_full_extracted"]["calibrated_correct_reuse"][
                        "value"
                    ]
                    cal = r["cache"]["calibrated"][design]
                    good = f <= 0.01 and c >= cx + 0.10
                    ok &= good
                    g = ""
                    if gold:
                        gx = r["cache"]["designs"][gold]
                        g = f" gold={gx['calibrated_correct_reuse']['value']:.2f}/{gx['calibrated_false_share']['value']:.3f}"
                    n_re = round(x["calibrated_reuse"]["value"] * r["cache"]["n_queries"])
                    cells.append(
                        f"F={cal['false_reuses']}/{n_re}={f:.4f} c={c:.2f} ex={cx:.2f} [tmpl {cal['wrong_template_only']}"
                        f" val {cal['wrong_values_only']} both {cal['both']}]{g}{'' if good else ' X'}"
                    )
                n_runs += ok
                print(f"  {v:6s} {d:10s} {t} " + " | ".join(cells))
            hold = n_runs >= 2
            held[(v, d)] = hold
            n_dom += hold
            print(f"  -> {v} {d}: {'HOLDS' if hold else 'does not hold'} ({n_runs}/3)")
        print(f"{label} {v}: {verdict(n_dom, 4)} ({n_dom}/4)")
    both = [d for d in DOMAINS if held[("gemini", d)] and held[("openai", d)]]
    print(f"{label} extractor-independent in: {both or 'none'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exclude", choices=("copied", "meaning"))
    ap.add_argument("--suffix", default="")
    a = ap.parse_args()
    print(f"### exclude={a.exclude} runs=r1{a.suffix}..r3{a.suffix}")
    if not a.suffix:
        hq_p(a.exclude)
    hq_d(a.exclude, a.suffix)
    hq_c(a.exclude, a.suffix)
    guarded("HQ-S", "relsig", "split_template_guarded", a.exclude, a.suffix)
    guarded(
        "HQ-F",
        "relfull",
        "split_template_fullsig",
        a.exclude,
        a.suffix,
        gold="split_template_fullsig_gold",
    )


if __name__ == "__main__":
    main()
