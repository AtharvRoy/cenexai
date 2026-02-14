#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python}"
VENV_DIR="${VENV_DIR:-.venv}"

echo "[1/4] Creating virtual environment at ${VENV_DIR}..."
"${PYTHON_BIN}" -m venv "${VENV_DIR}"

# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

echo "[2/4] Upgrading pip..."
python -m pip install --upgrade pip

echo "[3/4] Installing dependencies from requirements.txt..."
python -m pip install -r requirements.txt

echo "[4/4] Running unit tests..."
python -m unittest discover -s tests -p 'test_*.py'

echo "Done. Start API with: source ${VENV_DIR}/bin/activate && uvicorn app.main:app --reload"
