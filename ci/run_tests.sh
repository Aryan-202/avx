#!/usr/bin/env bash
set -e

echo "Running tests..."
pytest tests/

echo "Linting..."
flake8 avx/ tests/
mypy avx/

echo "All CI checks passed."
