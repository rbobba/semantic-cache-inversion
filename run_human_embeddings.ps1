# HQ-P's secondary embedders on the writers' questions (README section 18):
# the eight commercial configurations of section 14, addendum A, with the
# same settings. Secondary: HQ-P is decided on the four open models only.
# The three secondary open models are run locally by the agent.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   $env:OPENAI_API_KEY = "<key>"; $env:VOYAGE_API_KEY = "<key>"
#   .\run_human_embeddings.ps1
#
# Needs data_human\ (human.py). Each run caches its vectors under
# results_human\<domain>\<model>\, so a rerun skips what is already embedded.
# About 2,000 short texts per model; total cost is cents.

param(
    [string]$Project = "financial-insights-967",
    [switch]$SkipOpenAI,
    [switch]$SkipVoyage
)

$ErrorActionPreference = "Stop"
if (-not (Test-Path "data_human")) { throw "data_human\ is missing; run human.py first" }

$runs = @(
    @("--embedder", "vertex:text-embedding-004", "--project", $Project),
    @("--embedder", "vertex:text-embedding-004", "--task-type", "SEMANTIC_SIMILARITY", "--project", $Project),
    @("--embedder", "vertex:gemini-embedding-001", "--project", $Project)
)
if (-not $SkipOpenAI) {
    if (-not $env:OPENAI_API_KEY) { throw "Set OPENAI_API_KEY, or pass -SkipOpenAI" }
    $runs += , @("--embedder", "openai:text-embedding-3-small")
    $runs += , @("--embedder", "openai:text-embedding-3-large")
}
if (-not $SkipVoyage) {
    if (-not $env:VOYAGE_API_KEY) { throw "Set VOYAGE_API_KEY, or pass -SkipVoyage" }
    $runs += , @("--embedder", "voyage:voyage-3-large")
    $runs += , @("--embedder", "voyage:voyage-3.5")
    $runs += , @("--embedder", "voyage:voyage-4")
}

foreach ($r in $runs) {
    Write-Host "== $($r[1]) $($r[2..($r.Length - 1)] -join ' ')"
    foreach ($ex in @($null, "copied", "meaning")) {
        $extra = if ($ex) { @("--exclude", $ex) } else { @() }
        python human_eval.py @r @extra | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "$($r[1]) $ex failed; rerun to resume" }
    }
}
Write-Host "All human-question embeddings complete."
