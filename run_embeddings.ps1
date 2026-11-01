# Runs the commercial embedding models on all four domains (README section 14,
# addendum A). Secondary to G1-G4. Open models are run locally.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   $env:OPENAI_API_KEY = "..."; $env:VOYAGE_API_KEY = "..."
#   .\run_embeddings.ps1
#
# Each run caches its vectors under results_md\<domain>\<model>\, so a rerun
# skips what is already embedded. Total cost is cents.

param(
    [string]$Project = "",  # your GCP project ID
    [switch]$SkipOpenAI,
    [switch]$SkipVoyage
)

$ErrorActionPreference = "Stop"
$domains = @("finance", "retail", "healthcare", "it_support")

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

foreach ($d in $domains) {
    foreach ($r in $runs) {
        Write-Host "== $d  $($r[1]) $($r[2..($r.Length - 1)] -join ' ')"
        # Full run (inversion, A/B, cache), then the held-out cache from the same vectors.
        python evaluate.py --data "data_md/$d" --out "results_md/$d" @r | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "$d $($r[1]) failed; rerun to resume" }
        python evaluate.py --data "data_md/$d" --out "results_md/$d" --holdout @r | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "$d $($r[1]) holdout failed; rerun to resume" }
    }
}
Write-Host "All commercial embeddings complete."
