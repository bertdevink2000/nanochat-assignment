$env:PYTHONUTF8 = "1"
$env:TORCH_COMPILE_DISABLE = "1"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root
try {
    & ".\.venv\Scripts\python.exe" -m scripts.task4_samples
    if ($LASTEXITCODE -ne 0) { throw "Task 4 sampling failed" }
}
finally {
    Pop-Location
}
