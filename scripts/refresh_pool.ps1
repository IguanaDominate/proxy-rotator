# Windows helper: refresh the proxy pool on a schedule
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}
& ".venv\Scripts\Activate.ps1"
pip install -q -r requirements.txt

python -m proxy_rotator.bootstrap.cli generate --limit 300 --output proxy_output/pool.txt
Write-Host "Pool refreshed at $(Get-Date -Format o)"