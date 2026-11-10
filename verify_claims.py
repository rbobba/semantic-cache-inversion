"""Recomputes the numbers the study log cites from the files on disk, and
checks that the study log still says them.

  python verify_claims.py              every check
  python verify_claims.py --only 21    one study-log section (or "integrity")
  python verify_claims.py --deep       also resolve every saved raw.jsonl again
                                       and byte-compare (a few minutes)

Each check prints PASS, FAIL or SKIP. SKIP means an input is not on disk: the
results_md reports and every cached vector are gitignored, and REPRODUCE.md
says how to rebuild them. This script never computes an embedding and never
calls an API; it reads only what is already on disk. Exit status is 1 if any
check fails.

A table check finds the study-log row by its first cells, takes every number
in the rest of the row, and requires the recomputed values to appear among
them in order, each equal to the study log's number within the rounding it
shows (0.469 matches 0.4688; 15.5 matches 15.53). The study log is
hand-written, so this tolerates its formatting while still catching a changed
value.

Covered: the integrity of the data, pre-registrations, reports and verdict
files; and the results tables of sections 7, 8, 10, 12, 13, 19 and 21 with
their headline sentences. Not covered: numbers quoted in prose elsewhere, and
section 19's per-domain H-S and signature tables (md_verdicts.py prints them).
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
README = (HERE / "STUDY_LOG.md").read_text(encoding="utf-8").replace("\r\n", "\n")

OPEN4 = {
    "MiniLM": ("st:sentence-transformers/all-MiniLM-L6-v2", ""),
    "mpnet": ("st:sentence-transformers/all-mpnet-base-v2", ""),
    "bge": ("st:BAAI/bge-base-en-v1.5", ""),
    "e5": ("st:intfloat/e5-base-v2", "query: "),
}
# Section 8's 15 configurations: study-log row label -> (embedder, prefix, task type).
ALL15 = {
    "all-MiniLM-L6-v2": ("st:sentence-transformers/all-MiniLM-L6-v2", "", None),
    "all-mpnet-base-v2": ("st:sentence-transformers/all-mpnet-base-v2", "", None),
    "e5-base-v2": ("st:intfloat/e5-base-v2", "query: ", None),
    "bge-base-en-v1.5": ("st:BAAI/bge-base-en-v1.5", "", None),
    "text-embedding-3-small": ("openai:text-embedding-3-small", "", None),
    "text-embedding-3-large": ("openai:text-embedding-3-large", "", None),
    "mxbai-embed-large-v1": ("st:mixedbread-ai/mxbai-embed-large-v1", "", None),
    "snowflake-arctic-embed-l-v2.0": (
        "st:Snowflake/snowflake-arctic-embed-l-v2.0",
        "query: ",
        None,
    ),
    "text-embedding-004": ("vertex:text-embedding-004", "", None),
    "text-embedding-004, SEMANTIC_SIMILARITY": (
        "vertex:text-embedding-004",
        "",
        "SEMANTIC_SIMILARITY",
    ),
    "voyage-3-large": ("voyage:voyage-3-large", "", None),
    "voyage-3.5": ("voyage:voyage-3.5", "", None),
    "gemini-embedding-001": ("vertex:gemini-embedding-001", "", None),
    "Qwen3-Embedding-0.6B": ("st:Qwen/Qwen3-Embedding-0.6B", "", None),
    "voyage-4": ("voyage:voyage-4", "", None),
}
DOMAINS = ("finance", "retail", "healthcare", "it_support")


def label(emb: str, prefix: str = "", task: str | None = None) -> str:
    return emb + (f" prefix={prefix!r}" if prefix else "") + (f" task_type={task}" if task else "")


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")


class Missing(Exception):
    """An input is not on disk."""


def load(path: Path) -> dict:
    if not path.exists():
        raise Missing(str(path.relative_to(HERE)))
    return json.loads(path.read_text(encoding="utf-8"))


# ── Study-log access ─────────────────────────────────────────────────────


def section(n: int, text: str | None = None) -> str:
    text = (README if text is None else text).replace("\r\n", "\n")
    start = text.index(f"\n## {n}. ") + 1
    end = text.find("\n## ", start)
    return text[start : end if end > 0 else None]


NUM = re.compile(r"(?<![\w.])[-+]?\d+(?:,\d{3})*(?:\.\d+)?")


def numbers(s: str) -> list[tuple[float, int]]:
    s = s.replace("−", "-").replace("**", "")
    out = []
    for m in NUM.findall(s):
        frac = m.split(".")[1] if "." in m else ""
        out.append((float(m.replace(",", "")), len(frac)))
    return out


def close(v: float, tok: tuple[float, int]) -> bool:
    t, d = tok
    return abs(v - t) <= 0.5 * 10**-d + 1e-9


def find_row(sec: str, cells: tuple[str, ...], after: str | None = None) -> str | None:
    lines = sec.splitlines()
    i = 0
    if after:
        i = next((k for k, line in enumerate(lines) if after in line), len(lines))
    for line in lines[i:]:
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if line.startswith("|") and tuple(parts[: len(cells)]) == cells:
            return " | ".join(parts[len(cells) :])
    return None


# ── checks ───────────────────────────────────────────────────────────────


class Checks:
    def __init__(self) -> None:
        self.counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    def emit(self, status: str, what: str, detail: str = "") -> None:
        self.counts[status] += 1
        print(f"{status}  {what}" + (f"  — {detail}" if detail else ""), flush=True)

    def row(self, sec_n: int, cells, values, src: str, after: str | None = None) -> None:
        cells = (cells,) if isinstance(cells, str) else tuple(cells)
        what = f"§{sec_n} row {' / '.join(c or '·' for c in cells)}"
        line = find_row(section(sec_n), cells, after)
        if line is None:
            self.emit("FAIL", what, "row not found in study log")
            return
        toks = numbers(line)
        i = 0
        for v in values:
            while i < len(toks) and not close(v, toks[i]):
                i += 1
            if i == len(toks):
                self.emit("FAIL", what, f"{v:.4g} not on the row (from {src}): {line}")
                return
            i += 1
        self.emit("PASS", what)

    def says(self, sec_n: int, phrase: str, src: str) -> None:
        norm = " ".join(section(sec_n).replace("**", "").split())
        ok = " ".join(phrase.split()) in norm
        self.emit("PASS" if ok else "FAIL", f"§{sec_n} says “{phrase}”", "" if ok else src)

    def equal(self, what: str, got, want, src: str = "") -> None:
        ok = got == want
        self.emit(
            "PASS" if ok else "FAIL", what, "" if ok else f"got {got!r}, expected {want!r} {src}"
        )

    def guard(self, what: str, fn) -> None:
        """Run a group of checks; a missing input skips the group."""
        try:
            fn()
        except Missing as m:
            self.emit("SKIP", what, f"not on disk: {m}")


def rate_ci(x: dict, rate="strong_rate", ci="strong_ci95") -> list[float]:
    return [x[rate], *x[ci]]


def val_ci(x: dict) -> list[float]:
    return [x["value"], *x["ci95"]]


# ── integrity ────────────────────────────────────────────────────────────

# Frozen sections: the commit that froze each, and the hash it records, if any.
FROZEN = {9: "c79d064", 11: "7888f1c", 14: "46270aa", 15: "13add93", 16: "69dce45", 18: "b520b83"}
RECORDED = {11: "544f3d7e", 16: "8d2c8f51", 18: "af42f97e"}


def git_show(commit: str, path: str) -> str | None:
    r = subprocess.run(
        ["git", "show", f"{commit}:./{path}"],
        cwd=HERE,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return r.stdout if r.returncode == 0 else None


def integrity(c: Checks) -> None:
    # Dataset manifests: every listed file hashes to its recorded SHA-256.
    for m in sorted(HERE.glob("data*/**/manifest.json")):
        man = json.loads(m.read_text(encoding="utf-8"))
        bad = [
            f
            for f, h in (man.get("sha256") or {}).items()
            if hashlib.sha256((m.parent / f).read_bytes()).hexdigest() != h
        ]
        n = len(man.get("sha256") or {})
        rel = m.relative_to(HERE).as_posix()
        c.emit("FAIL" if bad else "PASS", f"data {rel}: {n} file hashes", ", ".join(bad))

    # Recorded section hashes: heading to the end of the commands block.
    # Section 11's was taken with the newline after the block; 16 and 18 without.
    for n, rec in RECORDED.items():
        t = section(n)
        i = t.index("### Commands")
        k = t.index("```", t.index("```", i) + 3) + 3
        hashes = {hashlib.sha256(x.encode()).hexdigest()[:8] for x in (t[:k], t[:k] + "\n")}
        c.emit("PASS" if rec in hashes else "FAIL", f"§{n} hash {rec}… recomputes")

    # Every frozen section is unchanged since the commit that froze it. A
    # trailing "---" added with the next section is ignored. Section 14's
    # Addendum A (commit ab5fc6b) is the one disclosed addition.
    for n, commit in FROZEN.items():
        old = git_show(commit, "README.md")
        if old is None:
            c.emit("SKIP", f"§{n} unchanged since {commit}", "commit not in this repository")
            continue

        def norm(s: str) -> str:
            return re.sub(r"\n+---\s*$", "", s.rstrip()).rstrip()

        now = norm(section(n))
        if n == 14:
            a = now.index("### Addendum A")
            now = now[:a].rstrip() + "\n\n" + now[now.index("\n### ", a + 1) + 1 :]
        same = norm(section(n, old)) == now
        note = " (Addendum A excepted)" if n == 14 else ""
        c.emit("PASS" if same else "FAIL", f"§{n} unchanged since {commit}{note}")

    # results_md reports, which are gitignored, against their recorded hashes.
    recs = (HERE / "results_md" / "REPORTS_SHA256.txt").read_text().split("\n")
    recs = [line.split("  ", 1) for line in recs if line.strip()]
    rows = [(h, p) for h, p in recs if (HERE / p).exists()]
    bad = [p for h, p in rows if hashlib.sha256((HERE / p).read_bytes()).hexdigest() != h]
    if not rows:
        c.emit("SKIP", "results_md reports", "none on disk; rebuild them (REPRODUCE.md)")
    else:
        c.emit(
            "FAIL" if bad else "PASS",
            f"results_md reports: {len(rows)} of {len(recs)} present, hashes match",
            ", ".join(bad[:3]),
        )

    # The committed verdict and detail files are what the scripts produce now.
    def run(*args: str) -> str:
        r = subprocess.run(
            [sys.executable, *args],
            cwd=HERE,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return r.stdout

    try:
        load(
            HERE / "results_md/finance/extraction/gemini-rel_gemini-3.1-flash-lite_r1/"
            "st_BAAI_bge-base-en-v1.5/report.json"
        )
        c.equal(
            "results_md/VERDICTS.txt is current",
            run("md_verdicts.py"),
            (HERE / "results_md/VERDICTS.txt").read_text(encoding="utf-8"),
        )
    except Missing as m:
        c.emit("SKIP", "results_md/VERDICTS.txt is current", f"not on disk: {m}")
    human = []
    for suffix in ("", "-yearfix"):
        for ex in ("", "--exclude=copied", "--exclude=meaning"):
            args = [
                "human_verdicts.py",
                *([f"--suffix={suffix}"] if suffix else []),
                *([ex] if ex else []),
            ]
            human.append(run(*args) + "\n")
    c.equal(
        "results_human/VERDICTS.txt is current",
        "".join(human),
        (HERE / "results_human/VERDICTS.txt").read_text(encoding="utf-8"),
    )


# ── section 7 and 8: dataset v1, results/ ───────────────────────────────


def v1_report(lbl: str) -> dict:
    return load(HERE / "results" / slug(lbl) / "report.json")


def s7(c: Checks) -> None:
    rows = {
        "all-MiniLM-L6-v2": label(*OPEN4["MiniLM"]),
        "all-mpnet-base-v2": label(*OPEN4["mpnet"]),
        "bge-base-en-v1.5": label(*OPEN4["bge"]),
        "e5-base-v2 (`query: `)": label(*OPEN4["e5"]),
        "text-embedding-004 (production configuration)": "vertex:text-embedding-004",
        "text-embedding-004, `SEMANTIC_SIMILARITY`": label(
            "vertex:text-embedding-004", "", "SEMANTIC_SIMILARITY"
        ),
        "TF-IDF (lexical control)": "tfidf",
    }
    for cell, lbl in rows.items():

        def one(cell=cell, lbl=lbl) -> None:
            inv = v1_report(lbl)["pairs"]["inversion"]["param_near_miss"]
            c.row(7, cell, rate_ci(inv), f"results/{slug(lbl)}")

        c.guard(f"§7 row {cell}", one)


def ab_from_vectors(lbl: str, prefix: str, task: str | None) -> dict:
    """Comparison A/B as evaluate.py computes it, from the cached vectors."""
    import evaluate

    questions, pairs, _ = evaluate.load(HERE / "data")
    texts = sorted({q["text"] for q in questions} | {q["masked_text"] for q in questions})
    key = hashlib.sha256(("\n".join(texts) + prefix + str(task)).encode()).hexdigest()[:16]
    path = HERE / "results" / slug(lbl) / f"embeddings_{key}.npy"
    if not path.exists():
        raise Missing(str(path.relative_to(HERE)))
    vecs = np.load(path)
    tindex = {t: i for i, t in enumerate(texts)}
    raw = vecs[[tindex[q["text"]] for q in questions]]
    qidx = {q["id"]: i for i, q in enumerate(questions)}
    return evaluate.ab_comparisons(pairs, qidx, raw, 8, 1000)


def s8(c: Checks) -> None:
    possible = set()
    for cell, (emb, prefix, task) in ALL15.items():
        lbl = label(emb, prefix, task)

        def main_row(cell=cell, lbl=lbl) -> None:
            r = v1_report(lbl)
            inv = r["pairs"]["inversion"]["param_near_miss"]
            des = r["cache"]["designs"]
            z = [
                des[d]["correct_reuse_at_false_0"]["value"]
                for d in ("raw_global", "raw_oracle_entry", "split_full")
            ]
            possible.add(round(des["raw_global"]["possible"]["value"], 3))
            c.row(8, cell, [*rate_ci(inv), *z], f"results/{slug(lbl)}", after="| Model | Year |")

        def ab_row(cell=cell, lbl=lbl, prefix=prefix, task=task) -> None:
            # Section 8's A/B came from session code that was never committed;
            # ab_comparisons was added later (7888f1c). Its point estimates
            # reproduce exactly, its intervals to within 0.015 (section 22).
            ab = ab_from_vectors(lbl, prefix, task)
            line = find_row(section(8), (cell,), after="| Model | A: swap") or ""
            a, alo, ahi, b, blo, bhi = (t for t, _ in numbers(line))
            c.row(
                8,
                cell,
                [ab["A"]["rate"], ab["B"]["rate"]],
                "cached vectors",
                after="| Model | A: swap",
            )
            gap = max(
                abs(x - y)
                for x, y in zip(
                    [alo, ahi, blo, bhi], [*ab["A"]["ci95"], *ab["B"]["ci95"]], strict=True
                )
            )
            c.emit(
                "PASS" if gap <= 0.015 else "FAIL",
                f"§8 A/B intervals {cell} within 0.015",
                f"gap {gap:.3f}",
            )

        c.guard(f"§8 row {cell}", main_row)
        c.guard(f"§8 A/B row {cell}", ab_row)
    if possible:
        c.equal("§8 correct reuse is possible for 0.532 in every row", possible, {0.532})


# ── section 10: real extraction on v1 ───────────────────────────────────


def s10(c: Checks) -> None:
    def decision() -> None:
        false = []
        for cell, (emb, prefix) in OPEN4.items():
            r = load(
                HERE
                / "results/extraction/gemini_gemini-3.1-flash-lite"
                / slug(label(emb, prefix))
                / "report.json"
            )
            des, cal = r["cache"]["designs"], r["cache"]["calibrated"]["split_template_extracted"]
            t = des["split_template_extracted"]["correct_reuse_at_false_0.01"]["value"]
            g = des["raw_global"]["correct_reuse_at_false_0.01"]["value"]
            f = [100 * x for x in val_ci(des["split_template_extracted"]["calibrated_false_share"])]
            c.row(10, cell, [t, g, *f], "results/extraction/gemini_gemini-3.1-flash-lite")
            false.append((cal["false_reuses"], cal["wrong_template_only"] + cal["both"]))
        c.says(
            10,
            f"all {min(f for f, _ in false)}–{max(f for f, _ in false)} false reuses were caused by wrong extracted values",
            "calibrated counts",
        )
        c.equal("§10 none of those came from a wrong template", {w for _, w in false}, {0})

    def accuracy() -> None:
        for cell, run in (
            ("gemini-3.5-flash", "gemini_gemini-3.5-flash"),
            ("**gemini-3.1-flash-lite** (primary)", "gemini_gemini-3.1-flash-lite"),
            ("Duckling + entity oracle", "duckling"),
        ):
            a = load(HERE / "results/extraction" / run / "accuracy.json")
            c.row(
                10,
                cell,
                [a["frame_accuracy"], *a["frame_accuracy_ci95"], a["slot_micro"]["f1"]],
                f"results/extraction/{run}",
            )

    c.guard("§10 decision table", decision)
    c.guard("§10 extraction accuracy", accuracy)


# ── section 12: dataset v2 ──────────────────────────────────────────────


def s12(c: Checks) -> None:
    for cell, (emb, prefix) in OPEN4.items():

        def one(cell=cell, emb=emb, prefix=prefix) -> None:
            base = HERE / "results_v2" / slug(label(emb, prefix))
            r = load(base / "report.json")
            ab, inv = r["pairs"]["ab"], r["pairs"]["inversion"]["param_near_miss"]
            c.row(
                12,
                cell,
                [
                    *rate_ci(ab["A"], "rate", "ci95"),
                    *rate_ci(ab["B"], "rate", "ci95"),
                    *rate_ci(inv),
                ],
                "results_v2",
                after="| Model | A [95% CI]",
            )
            h = load(HERE / "results_v2" / (slug(label(emb, prefix)) + "_holdout") / "report.json")
            z = [
                h["cache"]["designs"][d]["correct_reuse_at_false_0"]["value"]
                for d in ("raw_global", "split_full", "split_template")
            ]
            c.row(12, cell, z, "results_v2 holdout", after="| Model | raw_global @0")

        c.guard(f"§12 {cell}", one)


# ── section 13: relative-date arm ───────────────────────────────────────


def compare(a: Path, b: Path, design: str) -> list[float]:
    """evaluate.py --compare, as the study log ran it (1,000 resamples, seed 7)."""
    import evaluate

    for p in (a, b):
        load(p)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        evaluate.compare([a, b], 1000, 7)
    line = next(x for x in buf.getvalue().splitlines() if x.startswith(f"| {design} |"))
    return [100 * v for v, _ in numbers(line.split("|")[4])]


def period_errors(acc: dict) -> int:
    return sum(
        1
        for e in acc["errors"]
        if (e["gold"] or {}).get("period") != (e["pred"] or {}).get("period")
    )


def s13(c: Checks) -> None:
    for cell, (emb, prefix) in OPEN4.items():

        def part1(cell=cell, emb=emb, prefix=prefix) -> None:
            s = slug(label(emb, prefix))
            a = HERE / "results/extraction/gemini_gemini-3.1-flash-lite" / s / "report.json"
            b = HERE / "results/extraction/gemini-rel_gemini-3.1-flash-lite" / s / "report.json"
            fa, fb = (
                100
                * load(p)["cache"]["designs"]["split_template_extracted_slots"][
                    "calibrated_false_share"
                ]["value"]
                for p in (a, b)
            )
            c.row(
                13,
                cell,
                [fa, fb, *compare(a, b, "split_template_extracted_slots")],
                "results/extraction",
                after="| Embedder | Absolute |",
            )

        def part2b(cell=cell, emb=emb, prefix=prefix) -> None:
            s = slug(label(emb, prefix)) + "_holdout"
            a = HERE / "results_v2/extraction/gemini_gemini-3.1-flash-lite" / s / "report.json"
            b = HERE / "results_v2/extraction/gemini-rel_gemini-3.1-flash-lite" / s / "report.json"
            ra, rb = load(a), load(b)
            if not ra["cache"]["designs"]["split_template_extracted_slots"]["calibrated_reuse"][
                "value"
            ]:
                c.says(
                    13,
                    f"| {cell} | 0.000 | (nothing reused) | (nothing reused) | — |",
                    "nothing reused",
                )
                return
            fa, fb = (
                100
                * r["cache"]["designs"]["split_template_extracted_slots"]["calibrated_false_share"][
                    "value"
                ]
                for r in (ra, rb)
            )
            c.row(
                13,
                cell,
                [fa, fb, *compare(a, b, "split_template_extracted_slots")],
                "results_v2/extraction holdout",
                after="| Embedder | Reuse |",
            )

        c.guard(f"§13 part 1 {cell}", part1)
        c.guard(f"§13 part 2b {cell}", part2b)

    def periods() -> None:
        got = [
            period_errors(load(HERE / d / "extraction" / run / "accuracy.json"))
            for d, run in (
                ("results", "gemini_gemini-3.1-flash-lite"),
                ("results", "gemini-rel_gemini-3.1-flash-lite"),
                ("results_v2", "gemini_gemini-3.1-flash-lite"),
                ("results_v2", "gemini-rel_gemini-3.1-flash-lite"),
            )
        ]
        c.row(13, "Period wrong", got, "accuracy.json errors")

    c.guard("§13 period errors", periods)


# ── section 19: four domains ────────────────────────────────────────────


def verdict_lines(text: str) -> dict[str, str]:
    """'H-S verdict: PARTIALLY (1/4)' -> {'H-S': 'Partially (1/4)'}."""
    out = {}
    for m in re.finditer(
        r"^(\S+) verdict(?: \(new domains\))?: ([A-Z ]+) \((\d+/\d+)\)", text, re.M
    ):
        out[m.group(1)] = f"{m.group(2).strip().capitalize()} ({m.group(3)})"
    for m in re.finditer(
        r"G2 verdict: ([A-Z ]+) \((\d+/\d+)\);\s+G3 verdict: ([A-Z ]+) \((\d+/\d+)\)", text
    ):
        out["G2"] = f"{m.group(1).strip().capitalize()} ({m.group(2)})"
        out["G3"] = f"{m.group(3).strip().capitalize()} ({m.group(4)})"
    return out


def s19(c: Checks) -> None:
    v = verdict_lines((HERE / "results_md/VERDICTS.txt").read_text(encoding="utf-8"))
    for vid in ("G1", "G2", "G3", "G4", "H-N", "H-S", "H-N-O", "H-S-O"):
        line = find_row(section(19), (vid,)) or ""
        words, frac = v[vid].rsplit(" ", 1)
        ok = words.lower() in line.lower().replace("**", "") and frac.strip("()") in line
        c.emit("PASS" if ok else "FAIL", f"§19 verdict {vid}: {v[vid]}", "" if ok else line)

    def g1() -> None:
        rates, lows = [], []
        for d in DOMAINS:
            for emb, prefix, task in ALL15.values():
                a = load(HERE / "results_md" / d / slug(label(emb, prefix, task)) / "report.json")[
                    "pairs"
                ]["ab"]["A"]
                rates.append(a["rate"])
                lows.append((a["ci95"][0], d, emb))
        lo = min(lows)
        c.says(
            19,
            f"comparison A runs from {min(rates):.2f} to {max(rates):.2f}, and its lowest 95% lower bound is {lo[0]:.2f}",
            "results_md inversion reports",
        )
        c.equal(
            "§19 the lowest lower bound is voyage-3-large in finance",
            lo[1:],
            ("finance", "voyage:voyage-3-large"),
        )

    def g3() -> None:
        cells = {
            "finance": "finance",
            "retail": "retail",
            "healthcare": "healthcare",
            "it_support": "IT support",
        }
        for d, cell in cells.items():
            negs = [
                next(
                    iter(
                        load(
                            HERE
                            / "results_md"
                            / d
                            / "extraction"
                            / f"gemini-rel_gemini-3.1-flash-lite_{t}"
                            / "accuracy.json"
                        )["negation"].values()
                    )
                )
                for t in ("r1", "r2", "r3")
            ]
            ex = sorted({int(n["excluded_wrong"].split("/")[0]) for n in negs})
            inc = sorted({int(n["included_wrong"].split("/")[0]) for n in negs})
            c.row(
                19,
                cell,
                [ex[0], *ex[1:][-1:], int(negs[0]["excluded_wrong"].split("/")[1]), inc[0]],
                "results_md accuracy.json",
                after="| Domain | Excluded value dropped | Included",
            )

    c.guard("§19 G1 range", g1)
    c.guard("§19 G3 table", g3)


# ── section 21: human-written questions ─────────────────────────────────


HUMAN_ARMS = {
    ("gemini", "relfull"): "gemini-relfull_gemini-3.1-flash-lite",
    ("openai", "relfull"): "openai-relfull_gpt-6-luna",
}


def human_cells(d: str, arm: str, suffix: str = "") -> dict[str, list]:
    out = {"c": [], "x": [], "w": [], "t": []}
    for t in ("r1", "r2", "r3"):
        for emb, prefix in OPEN4.values():
            r = load(
                HERE
                / "results_human"
                / d
                / "extraction"
                / f"{arm}_{t}{suffix}"
                / slug(label(emb, prefix))
                / "report.json"
            )
            des, cal = r["cache"]["designs"], r["cache"]["calibrated"]["split_template_fullsig"]
            out["c"].append(des["split_template_fullsig"]["calibrated_correct_reuse"]["value"])
            out["x"].append(des["split_full_extracted"]["calibrated_correct_reuse"]["value"])
            out["w"].append(cal["false_reuses"])
            out["t"].append(cal["wrong_template_only"] + cal["both"])
    return out


def span(xs: list[float]) -> list[float]:
    return [min(xs)] if round(min(xs), 2) == round(max(xs), 2) else [min(xs), max(xs)]


def s21(c: Checks) -> None:
    v = (HERE / "results_human/VERDICTS.txt").read_text(encoding="utf-8")
    reg = v.split("### exclude=copied")[0]
    for vid, pattern in (("HQ-P", r"^HQ-P: (.+)$"), ("HQ-D", r"^HQ-D: (.+)$")):
        m = re.search(pattern, reg, re.M)
        word = "holds" if m.group(1) == "HOLDS" else "does not hold"
        line = (find_row(section(21), (vid,)) or "").replace("**", "").lower()
        c.emit("PASS" if line.startswith(word) else "FAIL", f"§21 verdict {vid}: {word}")
    hqc = "DOES NOT HOLD" in re.search(r"== HQ-C: .*$", reg, re.M).group(0)
    line = (find_row(section(21), ("HQ-C",)) or "").replace("**", "").lower()
    c.emit("PASS" if hqc == line.startswith("does not hold") else "FAIL", "§21 verdict HQ-C")
    names = {
        "finance": "finance",
        "retail": "retail",
        "healthcare": "healthcare",
        "it_support": "it support",
    }
    for vid in ("HQ-S", "HQ-F"):
        table = "### Verdicts, as registered"
        line = find_row(section(21), (f"**{vid}**",), table) or find_row(section(21), (vid,), table)
        line = (line or "").replace("**", "").lower()
        for vendor, name in (("gemini", "flash-lite"), ("openai", "gpt-6-luna")):
            word = re.search(rf"^{vid} {vendor}: ([A-Z ]+) \(", reg, re.M).group(1).strip().lower()
            block = reg.split(f"== {vid}:")[1].split("\n== ")[0]
            held = [names[d] for d in DOMAINS if re.search(rf"-> {vendor} {d}: HOLDS", block)]
            # The study log names the domains that hold: "partially (finance, retail)".
            seg = line.split(name, 1)[1].split(";")[0] if name in line else ""
            listed = [n for n in names.values() if n in seg]
            ok = seg.strip().startswith(word) and listed == held
            c.emit(
                "PASS" if ok else "FAIL",
                f"§21 verdict {vid} {name}: {word} {held}",
                "" if ok else seg,
            )

    def hqp() -> None:
        for cell, key in (
            ("all-MiniLM-L6-v2", "MiniLM"),
            ("all-mpnet-base-v2", "mpnet"),
            ("bge-base-en-v1.5", "bge"),
            ("e5-base-v2", "e5"),
        ):
            r = load(HERE / "results_human/similarity" / slug(label(*OPEN4[key])) / "report.json")
            p = r["pooled"]
            c.row(
                21,
                cell,
                [p["auc"], *p["ci95"], *(r[d]["auc"] for d in DOMAINS)],
                "results_human/similarity",
                after="| Embedder | AUC [95% CI]",
            )
        sec = []
        for emb, prefix, task in ALL15.values():
            if (emb, prefix) in OPEN4.values():
                continue
            sec.append(
                load(
                    HERE
                    / "results_human/similarity"
                    / slug(label(emb, prefix, task))
                    / "report.json"
                )["pooled"]
            )
        c.says(
            21,
            f"The 11 secondary configurations agree: {min(x['auc'] for x in sec):.2f}–{max(x['auc'] for x in sec):.2f}, upper bounds {min(x['ci95'][1] for x in sec):.2f}–{max(x['ci95'][1] for x in sec):.2f}",
            "secondary similarity reports",
        )

    def hqf() -> None:
        names = {
            "finance": "finance",
            "retail": "retail",
            "healthcare": "healthcare",
            "it_support": "IT support",
        }
        for (vendor, _), arm in HUMAN_ARMS.items():
            head = "fullsig, flash-lite" if vendor == "gemini" else "fullsig, gpt-6-luna"
            for i, d in enumerate(DOMAINS):
                h = human_cells(d, arm)
                cells = (head, names[d]) if i == 0 else ("", names[d])
                vals = [*span(h["c"]), *span(h["x"]), *span(h["w"]), *span(h["t"])]
                c.row(21, cells, vals, f"results_human/{d} {arm}", after=f"| {head} |")

    def yearfix() -> None:
        reg_c, fix_c = [], []
        for d in DOMAINS:
            reg_c += human_cells(d, HUMAN_ARMS[("openai", "relfull")])["c"]
            fix_c += human_cells(d, HUMAN_ARMS[("openai", "relfull")], "-yearfix")["c"]
        c.row(
            21,
            "HQ-F correct reuse",
            [min(reg_c), max(reg_c), min(fix_c), max(fix_c)],
            "results_human openai relfull",
            after="| gpt-6-luna, `-yearfix` |",
        )

    def details() -> None:
        md = (HERE / "results_human/DETAILS.md").read_text(encoding="utf-8")
        part = md.split("## Every wrong reuse")[1].split("## Per writer")[0]
        rows = [r.split(" | ") for r in part.splitlines() if r.startswith("| ") and "_s" in r]
        tmpl = {r[2] for r in rows if "template" in r[4]}
        import csv

        with (HERE / "data_human/meaning_check.csv").open(encoding="utf-8") as f:
            changed = {r["id"] for r in csv.DictReader(f) if r["same_meaning (Y/N)"] == "N"}
        c.equal(
            "§21 wrong-template reuses are hA_s001 and hA_s003 only", tmpl, {"hA_s001", "hA_s003"}
        )
        c.equal("§21 both are meaning-check N", tmpl <= changed, True)
        c.says(
            21,
            f"On the {480 - len(changed)} questions that keep their spec's meaning, it made no wrong-template reuse",
            "DETAILS.md",
        )

    c.guard("§21 HQ-P table", hqp)
    c.guard("§21 HQ-F table", hqf)
    c.guard("§21 year-fix table", yearfix)
    c.guard("§21 wrong reuses", details)


def deep(c: Checks) -> None:
    """Resolve every saved raw.jsonl again with the current extract.py, into a
    temporary folder, and byte-compare: earlier runs with their committed
    output, and the human runs with their -yearfix folders (section 20)."""
    import tempfile

    def data_for(run: Path) -> Path:
        top, *rest = run.relative_to(HERE).parts
        sub = rest[0] if top in ("results_md", "results_human") else ""
        return (
            HERE
            / {"results": "data", "results_v2": "data_v2"}.get(top, top.replace("results", "data"))
            / sub
        )

    with tempfile.TemporaryDirectory() as tmp:
        for raw in sorted(HERE.glob("results*/**/raw.jsonl")):
            run = raw.parent
            kind, model, *tag = run.name.split("_")
            human = run.relative_to(HERE).parts[0] == "results_human"
            new_tag = "_".join(tag) + ("-yearfix" if human else "")
            out = Path(tmp) / run.relative_to(HERE).parent
            cmd = [sys.executable, "extract.py", "--data", str(data_for(run)), "--out", str(out)]
            cmd += ["--extractor", f"{kind}:{model}", "--from-raw", str(run)]
            cmd += ["--tag", new_tag] if new_tag else []
            r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, encoding="utf-8")
            new = out / (f"{kind}_{model}" + (f"_{new_tag}" if new_tag else ""))
            want = run.parent / new.name
            what = f"re-resolve {run.relative_to(HERE).as_posix()}"
            if r.returncode or not (new / "extracted.jsonl").exists():
                c.emit("FAIL", what, r.stderr[-300:])
                continue
            # Five early accuracy files predate two keys the scorer added later
            # (negation, domain); their extractions and every old value match.
            files = ["extracted.jsonl"] + (
                []
                if run.relative_to(HERE).parts[0] in ("results", "results_v2")
                else ["accuracy.json"]
            )
            same = all((new / f).read_bytes() == (want / f).read_bytes() for f in files)
            c.emit("PASS" if same else "FAIL", what + (" = -yearfix" if human else ""))


def same_values(old: Path, new: Path) -> None:
    """Every value in a committed report against a regenerated one. Newer code
    adds fields (comparison A/B, later cache designs); the values the old
    report holds must be unchanged. The "extracted" path is ignored."""

    def flat(o, p=""):
        if isinstance(o, dict):
            for k, v in o.items():
                yield from flat(v, f"{p}/{k}")
        else:
            yield p, o

    a, b = (dict(flat(json.loads(x.read_text(encoding="utf-8")))) for x in (old, new))
    for d in (a, b):
        d.pop("/extracted", None)
    missing = sorted(set(a) - set(b))
    differ = sorted(k for k in set(a) & set(b) if a[k] != b[k])
    print(
        f"{len(a)} values in {old}: {len(differ)} differ, {len(missing)} missing; "
        f"{len(set(b) - set(a))} new in {new}"
    )
    for k in (differ + missing)[:20]:
        print(f"  {k}: {a.get(k)!r} -> {b.get(k, '(missing)')!r}")
    sys.exit(1 if differ or missing else 0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument(
        "--same-values",
        nargs=2,
        type=Path,
        metavar=("COMMITTED", "REGENERATED"),
        help="check that every value of a committed report is unchanged in a regenerated one",
    )
    ap.add_argument("--only", help='a study-log section number, or "integrity"')
    ap.add_argument(
        "--deep",
        action="store_true",
        help="also resolve every raw.jsonl again and byte-compare (a few minutes)",
    )
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if a.same_values:
        same_values(*a.same_values)
    sys.path.insert(0, str(HERE))
    groups = {
        "integrity": integrity,
        "7": s7,
        "8": s8,
        "10": s10,
        "12": s12,
        "13": s13,
        "19": s19,
        "21": s21,
    }
    if a.deep or a.only == "deep":
        groups["deep"] = deep
    c = Checks()
    for name, fn in groups.items():
        if a.only in (None, name):
            print(f"\n== {name}")
            fn(c)
    print(f"\n{c.counts['PASS']} passed, {c.counts['FAIL']} failed, {c.counts['SKIP']} skipped")
    sys.exit(1 if c.counts["FAIL"] else 0)


if __name__ == "__main__":
    main()
