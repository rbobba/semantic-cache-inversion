# Runs every Gemini extraction pre-registered in README section 14.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   .\run_extractions.ps1                       # everything (about $50)
#   .\run_extractions.ps1 -SkipFlash            # flash-lite only (about $16)
#
# -Tags replay1 writes a separately tagged replay and never touches r1-r3
# (REPRODUCE.md).
#
# Safe to stop and rerun: each run resumes from its own raw.jsonl, and a run
# that is already complete makes no API calls.

param(
    [string[]]$Tags = @("r1", "r2", "r3"),
    [string]$Project = "financial-insights-967",
    [int]$Workers = 2,
    [switch]$SkipFlash
)

$ErrorActionPreference = "Stop"
$domains = @("finance", "retail", "healthcare", "it_support")

function Invoke-Extraction([string]$Domain, [string]$Extractor, [string]$Tag) {
    $common = @(
        "extract.py", "--data", "data_md/$Domain", "--out", "results_md/$Domain/extraction",
        "--extractor", $Extractor, "--tag", $Tag, "--project", $Project, "--workers", $Workers
    )
    for ($attempt = 1; $attempt -le 3; $attempt++) {
        Write-Host "== $Domain  $Extractor  $Tag  (attempt $attempt)"
        python @common
        if ($LASTEXITCODE -eq 0) { return }
        Write-Host "   incomplete; resuming in 30s"
        Start-Sleep -Seconds 30
    }
    throw "$Domain $Extractor $Tag did not complete after 3 attempts; rerun this script to resume"
}

foreach ($d in $domains) {
    foreach ($t in $Tags) {
        Invoke-Extraction $d "gemini:gemini-3.1-flash-lite" $t
        Invoke-Extraction $d "gemini-rel:gemini-3.1-flash-lite" $t
    }
    if (-not $SkipFlash) {
        Invoke-Extraction $d "gemini-rel:gemini-3.5-flash" $($Tags[0])
    }
}
Write-Host "All extractions complete."
