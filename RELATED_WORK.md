# Related work and positioning (checked 2026-10-29)

**How this was checked.** Every entry below was read on 2026-10-29 from its
arXiv abstract page, its arXiv HTML full text, the ACL Anthology, or the
publisher's page. Numbers are each paper's own reported figures. Where a
detail could not be confirmed from the source, it is left out.

**How complete it is.** About a dozen web searches; the queries are listed at
the end. This is **not** a systematic review. Before submission, repeat the
search in Google Scholar and Semantic Scholar, search VLDB, SIGMOD and CIDR
proceedings directly, and check every paper that cites the two closest works
(Bindschaedler 2026 and Rathore et al. 2026).

---

## 1. The closest work

### Bindschaedler 2026: exact intent signatures for OLAP

*Semantic Caching for OLAP via LLM-Based Query Canonicalization (Extended
Version)*. L. Bindschaedler. arXiv:2602.19811, 23 Feb 2026. Extended version
of a short paper at DOLAP 2026 (with EDBT/ICDT 2026).

What it does:
- Maps both SQL and natural language to an "OLAP Intent Signature": measures,
  grouping levels, filters and time windows.
- **Reuse needs an exact match.** No approximate matching is used.
- An LLM (GPT-4o-mini at temperature 0; Claude-3.5-haiku also compared)
  produces the signature as strict JSON, with a 0–1 confidence score.
  Low-confidence signatures bypass the cache.

What it reports:
- 82% hit rate with zero false hits on 1,395 queries (TPC-DS, SSB, NYC TLC),
  against 28% for text keys and 56% for AST keys.
- The NL queries are 10 manually authored paraphrases per intent (450), plus
  150 BIRD dev questions.
- On 63 adversarial queries, 28 signatures were correct. Time references
  were wrong in 10 of 12, and "last month" without the current date was
  right in only 2 of 12.

What it does not do:
- It does not run an embedding cache. It argues, without measuring, that
  GPTCache-style caches "cannot distinguish" total from average revenue.
- Its error categories do not include exclusion or negation.

**Relation to this study.** Its design is our exact-key design
(`split_full_extracted`), and its time-reference failures agree with our
absolute-date arm. We add:
- the measurement it does not make (comparison A);
- the template cache between exact keys and raw similarity;
- negation fragility;
- held-out wording, four domains, two extractor vendors and pre-registration.

### Rathore et al. 2026: COGNI, a gated cache in production BI

*Conversational Query Engine for Mixed-Modality Heterogeneous Enterprise Data
Sources*. D. Rathore, V. Kumar, V. Singal, A. V. Singh, A. Moitra.
arXiv:2606.28370, 15 Jun 2026. Agent4IR at KDD 2026.

What it does:
- The cache gates a hit on "conjunctive checks on embedding similarity,
  entity overlap, intent, polarity, and freshness". Similarity is a
  "necessary but insufficient pre-filter".
- It names four failure classes: entity substitution, intent variation,
  polarity reversal and temporal staleness.

What it reports:
- It states that queries differing only in period ("MAU in Q1 2024" against
  "Q1 2025") "often exceed 0.95 cosine similarity under
  text-embedding-3-large". This is **asserted; no measurement is given.**
- Zero false hits on 200 queries built adversarially from 50 hand-curated
  seeds. The authors say this is not evidence about production traffic, and
  that they "have not run GPTCache as a direct baseline".

**Relation to this study.**
- **The guarded cache (section 15) is the same idea as COGNI's gating.** It
  is not a new design, and the paper must say so.
- Comparison A measures what COGNI asserts, in 15 embedding configurations.
- H-S and H-S-O test whether such gates hold with real extractors, on
  held-out wording, in four domains and with two vendors. COGNI reports
  zero false hits on its own constructed set only.

### Singh 2026: the source of our thresholds (NL to pandas, not SQL)

*Semantic Caching and Intent-Driven Context Optimization for Multi-Agent
Natural Language to Code Systems*. H. Singh. arXiv:2601.11687, 16 Jan 2026.

What it reports:
- A production multi-agent system that turns analytics questions into
  **pandas code, not SQL**, over 10,000+ queries.
- A dual threshold:
  - similarity ≥ 0.995 returns the cached result directly;
  - 0.50 to 0.995 injects it as a reference;
  - below 0.50 generates fresh.
- "Cached returns have highest accuracy (98.7%)", and a 67% hit rate.

**Relation to this study.**
- It is the source of our 1% false-share bar (section 9) and of the 0.50
  shortlist floor (section 15).
- **Both sections call it an "NL-to-SQL cache"; that is wrong.** It is
  natural language to code for the same kind of analytics questions. The
  numbers we took from it are unaffected. See README section 17.

### Brukau, Rudolph and Bhat 2026: AWS parameterized SQL templates

*Reducing Text2SQL latency with parameterized query templates*. AWS
Architecture Blog, 12 Aug 2026. Industry practice, not peer-reviewed.

What it describes:
- Cached SQL templates are matched by embedding similarity "above a
  confidence threshold", with an optional reranker. No model and no
  threshold value are given.
- Values are extracted by NER (a small model such as Amazon Nova 2 Lite, or
  a custom one) and checked against the format each placeholder expects.
- Results are checked, with a fallback to full generation.

What it reports:
- An 80% latency reduction, over 50% fewer tokens, and about a 60% hit rate.
- **No accuracy or false-match rate.**

**Relation to this study.** This is our template cache
(`split_template_extracted`) as deployed in industry. We measure the
false-reuse rate it does not report.

---

## 2. Semantic caching in general

| Work | What it says that matters here |
|---|---|
| GPTCache. F. Bang. NLP-OSS 2023 (ACL), pp. 212–218, doi:10.18653/v1/2023.nlposs-1.24 | The open-source raw-similarity cache: embed, search, reuse above a threshold. Reports a 2–10× speed-up on hits. This is our `raw_global` design. |
| MeanCache. W. Gill et al. IPDPS 2025. arXiv:2403.02694 | Existing caches give "unacceptable false hit-and-miss rates". Adds context chains for follow-up questions. |
| vCache. L. G. Schroeder et al. ICLR 2026. arXiv:2502.03771 | "Static thresholds do not give formal correctness guarantees." Learns a threshold per cached prompt, with user-set error bounds. |
| Krites. A. K. Singh et al. arXiv:2602.13165, Feb 2026 | An asynchronous LLM judge approves near-threshold matches; up to 3.9× more curated answers served. |
| Category-aware caching. C. Wang et al. arXiv:2510.26835, Oct 2025 (position paper) | "Fixed thresholds cause false positives in dense spaces"; proposes per-category thresholds. |
| Domain-specific cache embeddings. W. Gill et al. (Redis). arXiv:2504.02268, Apr 2025 | Small fine-tuned embedders beat larger general ones on cache precision and recall. |
| Operational gap. A. Baral et al. EMNLP 2026 Industry Track. arXiv:2606.19719 | "Models with the highest PR-AUC are often the worst in operation." Fixed-threshold metrics are what matter. |
| CacheAttack. Z. Zhang et al. ICML 2026. arXiv:2601.23088 | Similarity locality conflicts with collision resistance; 86% hijack rate. |
| Similarity Is Not Validity. Z. Zhang et al. arXiv:2609.35908, Sep 2026 | Argues, with a proof, that query embeddings can discard the information needed to tell valid hits from invalid ones. |

**How these bear on our results:**
- **vCache and category thresholds.** Our oracle per-entry threshold is an
  upper bound on any per-entry threshold method. On finance v1, even with
  perfect knowledge of each entry, it allows only 6.4–16.8% correct reuse at
  zero false reuse, against 53.2% possible (section 8). So a better threshold
  alone cannot fix the period problem.
- **Baral et al.** support reporting correct reuse at fixed false-reuse
  budgets, as we do, rather than AUC alone.
- **Similarity Is Not Validity** makes the theoretical argument in an
  adversarial setting. Our results are the same failure in ordinary,
  non-adversarial traffic.

---

## 3. Known blind spots of embeddings

- **Negation blindness.** H. Cao. *Semantic Adapter for Universal Text
  Embeddings: Diagnosing and Mitigating Negation Blindness to Enhance
  Universality*. ECAI 2025. arXiv:2504.00584. Universal text embeddings show
  "a significant lack of negation awareness" and treat negated pairs as
  similar.
- **Relation to this study.** Our exclusion results ("everything except X")
  are this blind spot in a caching setting. We also find the extraction
  side is fragile: excluded values are dropped far more often than included
  ones.

---

## 4. Text-to-SQL and slot filling (metric conventions)

| Work | Used for |
|---|---|
| Spider. T. Yu et al. EMNLP 2018. arXiv:1809.08887 | Context: text-to-SQL generation benchmark. We measure reuse, not generation. |
| BIRD. J. Li et al. NeurIPS 2023. arXiv:2305.03111 | Context; Bindschaedler draws 150 questions from its dev set. |
| Snips Voice Platform. A. Coucke et al. arXiv:1805.10190, 2018 | Slot-filling evaluation (slot F1, frame accuracy), which our extraction scoring follows. |

ATIS (Hemphill et al., 1990) was **not** checked this session. Verify it
before citing.

---

## 5. What is and is not new in this study

**Not new; cite, don't claim:**
- That embedding similarity confuses near-identical questions with different
  parameters. COGNI asserts it; Bindschaedler, MeanCache and Similarity Is
  Not Validity argue it.
- Gating reuse on extracted structure: COGNI's conjunctive checks,
  Bindschaedler's exact signatures, and AWS's value validation.
- Adaptive, per-entry thresholds (vCache).

**New, as far as this search found:**
1. **A measurement of the near-miss problem.** Comparison A is rank-based,
   pre-registered, and covers 15 configurations, 9 publishers and 4 domains.
   The closest work asserts it (COGNI) or argues it (Bindschaedler). The
   oracle per-entry bound shows that no per-entry threshold rescues it.
2. **The industry template cache measured with real extractors.** We report
   its false-reuse rate, and show that similarity barely signals extraction
   errors (AUC 0.36–0.41).
3. **Negation asymmetry in extraction.** Excluded values are dropped far more
   often than included ones. This is not in the error categories of the
   works found.
4. **Relative-time labels remove period errors**, with zero errors in the
   relative arm. The fix is quantified where Bindschaedler documents the
   failure.
5. **Gated designs tested on held-out wording, across domains and two
   extractor vendors, under pre-registered rules, with a cost break-even.**
   Earlier gated designs report zero false hits on their own constructed
   sets (200 queries; 1,395 queries).
6. **Method.** Pre-registration with recorded hashes, and corrections kept in
   place.

**Framing that follows.** The paper is an empirical, pre-registered study of
when semantic caching is safe for text-to-SQL, and a test of the gating
designs practitioners are already adopting. It does **not** propose a new
guarded cache.

---

## Search queries used (2026-10-29)

- semantic cache text-to-SQL LLM arXiv
- semantic caching LLM false positive hits embedding similarity threshold arXiv 2025
- sentence embeddings fail negation numbers temporal expressions benchmark arXiv
- NL2SQL query template reuse cache parameterized SQL natural language interface database
- semantic cache wrong answer entity number date mismatch correctness verification LLM judge arXiv 2026
- GPTCache open-source semantic cache LLM applications NLP-OSS 2023 paper
- text-to-SQL caching reuse previous SQL similar questions few-shot retrieval risk wrong filter aggregation
- semantic cache benchmark near-duplicate queries different entity number false hit rate embedding models evaluation
