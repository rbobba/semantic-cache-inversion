"""Applies the frozen rules of README sections 14 (G1-G4), 15 (H-N, H-S) and
16 (H-N-O, H-S-O, floor sweep) to the reports on disk. Prints every number a
verdict rests on, so each verdict can be checked by hand. Section 19 reports
the verdicts. The reports under results_md are gitignored; see REPRODUCE.md.

  python md_verdicts.py [g1 g23 g4 hn hs hno hso sweep indep]"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
R = ROOT / "results_md"
DOMAINS = ("finance", "retail", "healthcare", "it_support")
NEW = ("retail", "healthcare", "it_support")
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
SHORT = {e: e.split("_", 1)[1][:28] for e in PRIMARY + SECONDARY}
REL = "gemini-rel_gemini-3.1-flash-lite"
SIG = "gemini-relsig_gemini-3.1-flash-lite"


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def verdict(n_hold: int, n: int) -> str:
    if n_hold == n:
        return "GENERALISES"
    return "PARTIALLY" if n_hold else "DOES NOT GENERALISE"


def g1() -> None:
    print("\n== G1: comparison A, 95% CI lower bound > 0.5 in all four primary embedders")
    held = 0
    for d in DOMAINS:
        ok_all = True
        for e in PRIMARY + SECONDARY:
            rep = load(R / d / e / "report.json")
            if rep is None:
                print(f"  {d:11s} {SHORT[e]:28s} MISSING")
                ok_all &= e not in PRIMARY
                continue
            a, b = rep["pairs"]["ab"]["A"], rep["pairs"]["ab"]["B"]
            tag = "primary" if e in PRIMARY else "secondary"
            if e in PRIMARY:
                ok_all &= a["ci95"][0] > 0.5
            print(
                f"  {d:11s} {SHORT[e]:28s} {tag:9s} A={a['rate']:.3f} [{a['ci95'][0]:.3f},"
                f"{a['ci95'][1]:.3f}] n={a['n']}  B={b['rate']:.3f} [{b['ci95'][0]:.3f},{b['ci95'][1]:.3f}]"
            )
        print(f"  -> {d}: {'HOLDS' if ok_all else 'does not hold'}")
        held += ok_all and d in NEW
    print(f"G1 verdict (new domains): {verdict(held, 3)} ({held}/3)")


def period_errors(acc: dict) -> int:
    return sum(
        1
        for e in acc["errors"]
        if (e["gold"] or {}).get("period") != (e["pred"] or {}).get("period")
    )


def g2_g3() -> None:
    print("\n== G2: relative arm period-slot errors <= 0.5% of questions, each of r1-r3")
    print("== G3: excluded-minus-included error rate, 95% CI lower bound > 0, in >= 2 of r1-r3")
    g2_held = g3_held = 0
    for d in DOMAINS:
        g2_ok, g3_n = True, 0
        for t in RUNS:
            acc = load(R / d / "extraction" / f"{REL}_{t}" / "accuracy.json")
            if acc is None:
                print(f"  {d} {t} MISSING")
                g2_ok = False
                continue
            pe, n = period_errors(acc), acc["n_questions"]
            g2_ok &= pe / n <= 0.005
            (neg,) = acc["negation"].values()
            g3 = neg["difference_ci95"][0] > 0
            g3_n += g3
            print(
                f"  {d:11s} {t} period errors {pe}/{n} = {pe / n:.4%}   negation: excluded "
                f"{neg['excluded_wrong']} included {neg['included_wrong']} diff "
                f"{neg['difference']:.3f} [{neg['difference_ci95'][0]:.3f},{neg['difference_ci95'][1]:.3f}]"
                f" {'>0' if g3 else ''}"
            )
        print(
            f"  -> {d}: G2 {'HOLDS' if g2_ok else 'does not hold'}; G3 "
            f"{'HOLDS' if g3_n >= 2 else 'does not hold'} ({g3_n}/3)"
        )
        if d in NEW:
            g2_held += g2_ok
            g3_held += g3_n >= 2
    print(
        f"G2 verdict: {verdict(g2_held, 3)} ({g2_held}/3);  G3 verdict: {verdict(g3_held, 3)} ({g3_held}/3)"
    )
    print("\n  absolute arm period errors and 3.5-flash negation (reported, no rule):")
    for d in DOMAINS:
        for arm in (
            "gemini_gemini-3.1-flash-lite_r1",
            "gemini_gemini-3.1-flash-lite_r2",
            "gemini_gemini-3.1-flash-lite_r3",
            "gemini-rel_gemini-3.5-flash_r1",
        ):
            acc = load(R / d / "extraction" / arm / "accuracy.json")
            if acc is None:
                continue
            (neg,) = acc["negation"].values()
            print(
                f"  {d:11s} {arm:34s} period errors {period_errors(acc)}/{acc['n_questions']}"
                f"  negation excl {neg['excluded_wrong']} incl {neg['included_wrong']}"
            )


def design(rep: dict, name: str) -> tuple[float, float]:
    x = rep["cache"]["designs"][name]
    return x["calibrated_false_share"]["value"], x["calibrated_correct_reuse"]["value"]


def per_run(arm: str, d: str, t: str, e: str, hold: bool):
    return load(
        R / d / "extraction" / f"{arm}_{t}" / (e + ("_holdout" if hold else "")) / "report.json"
    )


def g4() -> None:
    print(
        "\n== G4: F_slots (non-held-out, calibrated) > 1% in all four embedders, in >= 2 of r1-r3"
    )
    held = 0
    for d in DOMAINS:
        n_runs = 0
        for t in RUNS:
            vals = []
            for e in PRIMARY:
                rep = per_run(REL, d, t, e, False)
                vals.append(
                    None if rep is None else design(rep, "split_template_extracted_slots")[0]
                )
            ok = all(v is not None and v > 0.01 for v in vals)
            n_runs += ok
            print(
                f"  {d:11s} {t} F_slots "
                + "  ".join("MISSING" if v is None else f"{v:.4f}" for v in vals)
                + ("  all >1%" if ok else "")
            )
        print(f"  -> {d}: {'HOLDS' if n_runs >= 2 else 'does not hold'} ({n_runs}/3)")
        held += n_runs >= 2 and d in NEW
    print(f"G4 verdict: {verdict(held, 3)} ({held}/3)")


def h_n(arm: str, label: str, domains) -> None:
    print(
        f"\n== {label}: negguard F_slots <= 1% AND correct reuse >= slots-only - 0.02, "
        "held-out and non-held-out, all four embedders, >= 2 of r1-r3"
    )
    held = 0
    for d in domains:
        n_runs = 0
        for t in RUNS:
            ok = True
            cells = []
            for e in PRIMARY:
                for hold in (False, True):
                    rep = per_run(arm, d, t, e, hold)
                    if rep is None:
                        ok = False
                        cells.append("MISSING")
                        continue
                    f, c = design(rep, "split_template_negguard")
                    _, c0 = design(rep, "split_template_extracted_slots")
                    good = f <= 0.01 and c >= c0 - 0.02
                    ok &= good
                    cells.append(
                        f"{'H' if hold else 'N'} F={f:.3f} c={c:.3f}/{c0:.3f}{'' if good else ' X'}"
                    )
            n_runs += ok
            print(f"  {d:11s} {t} " + " | ".join(cells))
        print(f"  -> {d}: {'HOLDS' if n_runs >= 2 else 'does not hold'} ({n_runs}/3)")
        held += n_runs >= 2
    print(f"{label} verdict: {verdict(held, len(domains))} ({held}/{len(domains)})")


def h_s(arm: str, label: str) -> None:
    print(
        f"\n== {label}: guarded, held-out: F_slots <= 1% AND correct reuse >= exact-key + 0.10, "
        "all four embedders, >= 2 of r1-r3"
    )
    held = 0
    for d in DOMAINS:
        n_runs = 0
        for t in RUNS:
            ok = True
            cells = []
            for e in PRIMARY:
                rep = per_run(arm, d, t, e, True)
                if rep is None:
                    ok = False
                    cells.append("MISSING")
                    continue
                f, c = design(rep, "split_template_guarded")
                _, cx = design(rep, "split_full_extracted")
                good = f <= 0.01 and c >= cx + 0.10
                ok &= good
                cells.append(f"F={f:.3f} c={c:.3f} exact={cx:.3f}{'' if good else ' X'}")
            n_runs += ok
            print(f"  {d:11s} {t} " + " | ".join(cells))
        print(f"  -> {d}: {'HOLDS' if n_runs >= 2 else 'does not hold'} ({n_runs}/3)")
        held += n_runs >= 2
    print(f"{label} verdict: {verdict(held, 4)} ({held}/4)")


OAI = "openai-relsig_gpt-6-luna"


def hs_domain_holds(arm: str, d: str) -> bool:
    n_runs = 0
    for t in RUNS:
        ok = True
        for e in PRIMARY:
            rep = per_run(arm, d, t, e, True)
            if rep is None:
                return False
            f, c = design(rep, "split_template_guarded")
            _, cx = design(rep, "split_full_extracted")
            ok &= f <= 0.01 and c >= cx + 0.10
        n_runs += ok
    return n_runs >= 2


def sweep(arm: str, label: str) -> None:
    print(
        f"\n== Floor sweep, {label}: split_template_guarded false share <= 1% at every floor, "
        "every embedder, >= 2 of r1-r3"
    )
    for hold in (True, False):
        print(f"  [{'held-out' if hold else 'non-held-out'}]")
        for d in DOMAINS:
            n_runs = 0
            worst: dict = {}
            for t in RUNS:
                ok = True
                for e in PRIMARY:
                    rep = per_run(arm, d, t, e, hold)
                    if rep is None:
                        ok = False
                        continue
                    for row in rep["cache"]["shortlist_sweep"]["split_template_guarded"]:
                        fl = row["floor"]
                        worst[fl] = max(worst.get(fl, 0), row["false_reuse_share"])
                        ok &= row["false_reuse_share"] <= 0.01
                n_runs += ok
            w = "  ".join(f"{'none' if k is None else k}:{v:.4f}" for k, v in worst.items())
            print(
                f"    {d:11s} robust={'YES' if n_runs >= 2 else 'no '} ({n_runs}/3)  worst false share by floor: {w}"
            )


if __name__ == "__main__":
    which = sys.argv[1:] or ["g1", "g23", "g4", "hn", "hs", "hno", "hso", "sweep", "indep"]
    if "g1" in which:
        g1()
    if "g23" in which:
        g2_g3()
    if "g4" in which:
        g4()
    if "hn" in which:
        h_n(REL, "H-N", NEW)
    if "hs" in which:
        h_s(SIG, "H-S")
    if "hno" in which:
        h_n(OAI, "H-N-O", NEW)
    if "hso" in which:
        h_s(OAI, "H-S-O")
    if "sweep" in which:
        sweep(SIG, "gemini")
        sweep(OAI, "openai")
    if "indep" in which:
        print("\n== Extractor-independent (H-S holds for both vendors):")
        for d in DOMAINS:
            g, o = hs_domain_holds(SIG, d), hs_domain_holds(OAI, d)
            print(f"  {d:11s} gemini {g}  openai {o}  -> {'YES' if g and o else 'no'}")
