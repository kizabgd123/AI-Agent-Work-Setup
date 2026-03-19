#!/usr/bin/env bash
set -euo pipefail

# Setup script for AI-Agent-Work-Setup
# Usage:
#   ./setup.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# Create virtual environment
if [[ ! -d ".venv" ]]; then
  echo "Creating Python virtual environment..."
  python3 -m venv .venv
fi

# Activate venv
# shellcheck source=/dev/null
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install python dependencies
if [[ -f requirements.txt ]]; then
  echo "Installing Python dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "No requirements.txt found; skipping dependency install."
fi

# Ensure .env exists
if [[ ! -f ".env" ]]; then
  if [[ -f ".env.example" ]]; then
    echo "Creating .env from .env.example (you must fill in API keys)..."
    cp .env.example .env
  else
    echo "No .env or .env.example found; create a .env with your API keys." >&2
  fi
fi

echo "Setup complete. Activate the virtual environment with:\n  source .venv/bin/activate"