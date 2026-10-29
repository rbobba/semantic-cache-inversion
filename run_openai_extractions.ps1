# Runs the second-vendor signature extractions (README section 16):
# openai-relsig on gpt-6-luna, r1-r3, in all four domains.
#
#   cd research\semantic-cache-inversion
#   .venv\Scripts\activate
#   $env:OPENAI_API_KEY = "<key>"
#   .\run_openai_extractions.ps1 -SmokeOnly     # 20 questions, prints the projected cost
#   .\run_openai_extractions.ps1                # the full 12 runs
#
# Independent of the Gemini scripts, so it can run alongside them.
# Safe to stop and rerun: each run resumes from its own raw.jsonl, and the
# smoke test's 20 responses are reused by finance r1.

param(
    [string]$Model = "gpt-6-luna",
    [int]$Workers = 4,
    [switch]$SmokeOnly
)

$ErrorActionPreference = "Stop"
if (-not $env:OPENAI_API_KEY) { throw "Set `$env:OPENAI_API_KEY first" }

$extractor = "openai-relsig:$Model"
$smokeDir = "results_md/finance/extraction/openai-relsig_${Model}_r1"

python extract.py --data data_md/finance --out results_md/finance/extraction `
    --extractor $extractor --tag r1 --limit 20 --workers $Workers
if ($LASTEXITCODE -ne 0) { throw "smoke test failed; see the error above" }

# Projected cost of all 12 runs from the smoke test's own token counts, at
# the price on OpenAI's pricing page on 2026-10-29 ($0.10 in, $0.50 out per
# 1M tokens; reasoning tokens bill as output).
python -c @"
import json, statistics as s
u = [json.loads(l)['usage'] for l in open('$smokeDir/raw.jsonl', encoding='utf-8') if json.loads(l).get('response')]
p, o, t = (s.mean(x[k] or 0 for x in u) for k in ('prompt', 'output', 'thinking'))
calls = 3 * (1295 + 1241 + 1399 + 1202)
print(f'per call: {p:.0f} input, {o:.0f} output, {t:.0f} reasoning tokens')
print(f'projected for 12 runs ({calls} calls): about USD {calls * (p * 0.10 + (o + t) * 0.50) / 1e6:.2f}')
"@
if ($SmokeOnly) { return }

foreach ($d in @("finance", "retail", "healthcare", "it_support")) {
    foreach ($t in @("r1", "r2", "r3")) {
        $args_ = @(
            "extract.py", "--data", "data_md/$d", "--out", "results_md/$d/extraction",
            "--extractor", $extractor, "--tag", $t, "--workers", $Workers
        )
        $done = $false
        for ($attempt = 1; $attempt -le 3 -and -not $done; $attempt++) {
            Write-Host "== $d  openai-relsig  $t  (attempt $attempt)"
            python @args_
            if ($LASTEXITCODE -eq 0) { $done = $true } else { Start-Sleep -Seconds 30 }
        }
        if (-not $done) { throw "$d openai-relsig $t did not complete; rerun this script to resume" }
    }
}
Write-Host "All OpenAI extractions complete."
