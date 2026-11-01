# Runs the signature extractions for the guarded hybrid cache (README
# section 15): gemini-relsig flash-lite, r1-r3, in all four domains, about $8.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   .\run_guard_extractions.ps1
#
# -Tags replay1 writes a separately tagged replay and never touches r1-r3
# (REPRODUCE.md).
#
# Safe to stop and rerun: each run resumes from its own raw.jsonl.

param(
    [string[]]$Tags = @("r1", "r2", "r3"),
    [string]$Project = "",  # your GCP project ID
    [int]$Workers = 2
)

$ErrorActionPreference = "Stop"

foreach ($d in @("finance", "retail", "healthcare", "it_support")) {
    foreach ($t in $Tags) {
        $args_ = @(
            "extract.py", "--data", "data_md/$d", "--out", "results_md/$d/extraction",
            "--extractor", "gemini-relsig:gemini-3.1-flash-lite", "--tag", $t,
            "--project", $Project, "--workers", $Workers
        )
        $done = $false
        for ($attempt = 1; $attempt -le 3 -and -not $done; $attempt++) {
            Write-Host "== $d  relsig  $t  (attempt $attempt)"
            python @args_
            if ($LASTEXITCODE -eq 0) { $done = $true } else { Start-Sleep -Seconds 30 }
        }
        if (-not $done) { throw "$d relsig $t did not complete; rerun this script to resume" }
    }
}
Write-Host "All guard extractions complete."
