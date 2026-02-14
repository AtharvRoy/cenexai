param(
  [string]$PythonBin = "python",
  [string]$VenvDir = ".venv"
)

$ErrorActionPreference = "Stop"

Write-Host "[1/4] Creating virtual environment at $VenvDir..."
& $PythonBin -m venv $VenvDir

$activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
Write-Host "Activating virtual environment..."
. $activateScript

Write-Host "[2/4] Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "[3/4] Installing dependencies from requirements.txt..."
python -m pip install -r requirements.txt

Write-Host "[4/4] Running unit tests..."
python -m unittest discover -s tests -p "test_*.py"

Write-Host "Done. Start API with: .\$VenvDir\Scripts\Activate.ps1; uvicorn app.main:app --reload"
