# Development pilot of the full-signature prompt (README section 18), on the
# synthetic data already seen: one run per vendor, all four domains. It checks
# that every measure and grouping definition has one reading before the human
# test is frozen. Nothing here is a test result.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   .\run_fullsig_pilot.ps1 -Vendor gemini                 # about $3
#   $env:OPENAI_API_KEY = "<key>"; .\run_fullsig_pilot.ps1 -Vendor openai   # about $1
#
# -Tag names the run (default "pilot"). The second pilot, after the operation
# definitions were tightened, is -Tag pilot2; the first is kept as it was.
#
# The two vendors can run at the same time in separate windows. Safe to stop
# and rerun: each run resumes from its raw.jsonl.

param(
    [Parameter(Mandatory = $true)][ValidateSet("gemini", "openai")][string]$Vendor,
    [string]$Project = "",  # your GCP project ID
    [int]$Workers = 0,
    [string]$Tag = "pilot"
)

$ErrorActionPreference = "Stop"
if ($Vendor -eq "gemini") {
    $extractor = "gemini-relfull:gemini-3.1-flash-lite"
    $extra = @("--project", $Project)
    if (-not $Workers) { $Workers = 2 }
} else {
    if (-not $env:OPENAI_API_KEY) { throw "Set `$env:OPENAI_API_KEY first" }
    $extractor = "openai-relfull:gpt-6-luna"
    $extra = @()
    if (-not $Workers) { $Workers = 4 }
}

foreach ($d in @("finance", "retail", "healthcare", "it_support")) {
    $done = $false
    for ($attempt = 1; $attempt -le 3 -and -not $done; $attempt++) {
        Write-Host "== $d  $extractor  $Tag  (attempt $attempt)"
        python extract.py --data "data_md/$d" --out "results_md/$d/extraction" `
            --extractor $extractor --tag $Tag --workers $Workers @extra
        if ($LASTEXITCODE -eq 0) { $done = $true } else { Start-Sleep -Seconds 30 }
    }
    if (-not $done) { throw "$d $extractor did not complete; rerun this script to resume" }
}
Write-Host "Pilot $Tag complete for $Vendor."
