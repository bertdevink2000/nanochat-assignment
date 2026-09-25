$env:PYTHONUTF8 = "1"
$env:TORCH_COMPILE_DISABLE = "1"
$env:WANDB_MODE = "offline"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root
try {
    & ".\.venv\Scripts\python.exe" -m scripts.base_train `
        --depth=2 `
        --window-pattern=L `
        --device-batch-size=8 `
        --eval-every=100 `
        --eval-tokens=1048576 `
        --core-metric-every=-1 `
        --sample-every=-1 `
        --save-every=100 `
        --model-tag=task2-d2 `
        --run=task2-d2
}
finally {
    Pop-Location
}
