# Extraction runs on the writers' questions (README section 18): both vendors,
# the section 15 signature and the full signature, r1-r3, all four domains.
# Each run also re-extracts the domain's cached questions, so a cache entry and
# a query are always read by the same run.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   .\run_human_extractions.ps1 -Vendor gemini                 # about $3
#   $env:OPENAI_API_KEY = "<key>"; .\run_human_extractions.ps1 -Vendor openai   # about $1.50
#
# -Tags replay1 writes a separately tagged replay and never touches r1-r3
# (REPRODUCE.md).
#
# Needs data_human\ (human.py). The two vendors can run at the same time in
# separate windows. Safe to stop and rerun: each run resumes from its raw.jsonl.

param(
    [Parameter(Mandatory = $true)][ValidateSet("gemini", "openai")][string]$Vendor,
    [string]$Project = "financial-insights-967",
    [int]$Workers = 0,
    [string[]]$Tags = @("r1", "r2", "r3")
)

$ErrorActionPreference = "Stop"
if (-not (Test-Path "data_human")) { throw "data_human\ is missing; run human.py first" }
if ($Vendor -eq "gemini") {
    $arms = @("gemini-relsig:gemini-3.1-flash-lite", "gemini-relfull:gemini-3.1-flash-lite")
    $extra = @("--project", $Project)
    if (-not $Workers) { $Workers = 2 }
} else {
    if (-not $env:OPENAI_API_KEY) { throw "Set `$env:OPENAI_API_KEY first" }
    $arms = @("openai-relsig:gpt-6-luna", "openai-relfull:gpt-6-luna")
    $extra = @()
    if (-not $Workers) { $Workers = 4 }
}

foreach ($d in @("finance", "retail", "healthcare", "it_support")) {
    foreach ($arm in $arms) {
        foreach ($t in $Tags) {
            $done = $false
            for ($attempt = 1; $attempt -le 3 -and -not $done; $attempt++) {
                Write-Host "== $d  $arm  $t  (attempt $attempt)"
                python extract.py --data "data_human/$d" --out "results_human/$d/extraction" `
                    --extractor $arm --tag $t --workers $Workers @extra
                if ($LASTEXITCODE -eq 0) { $done = $true } else { Start-Sleep -Seconds 30 }
            }
            if (-not $done) { throw "$d $arm $t did not complete; rerun this script to resume" }
        }
    }
}
Write-Host "All human-question extractions complete for $Vendor."
