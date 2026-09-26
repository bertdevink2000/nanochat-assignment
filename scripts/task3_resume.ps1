$env:PYTHONUTF8 = "1"
$env:TORCH_COMPILE_DISABLE = "1"
$env:WANDB_MODE = "offline"

$root = Split-Path $PSScriptRoot -Parent
Push-Location $root
try {
    $python = ".\.venv\Scripts\python.exe"

    & $python -m scripts.chat_eval -i sft -g task3-midtrain -a "ARC-Easy|ARC-Challenge|GSM8K" --output-file=report/task3_midtrain.json
    if ($LASTEXITCODE -ne 0) { throw "Mid-training evaluation failed" }

    & $python -m scripts.chat_sft --stage=sft --model-tag=task3-midtrain --output-tag=task3-sft --eval-every=100 --eval-tokens=1048576 --chatcore-every=-1 --run=task3-sft
    if ($LASTEXITCODE -ne 0) { throw "SFT failed" }
    & $python -m scripts.chat_eval -i sft -g task3-sft -a "ARC-Easy|ARC-Challenge|GSM8K" --output-file=report/task3_sft.json
    if ($LASTEXITCODE -ne 0) { throw "SFT evaluation failed" }
}
finally {
    Pop-Location
}
