#!/usr/bin/env bash
set -e

echo "==========================================="
echo "Installing AVX globally..."
echo "==========================================="

if command -v uv &> /dev/null; then
    echo "Using 'uv' for fast installation..."
    uv tool install . --force
    echo ""
    echo "AVX installed successfully via uv!"
    echo "You can now use the 'avx' command anywhere."
    exit 0
fi

if command -v pipx &> /dev/null; then
    echo "Using 'pipx' for isolated installation..."
    pipx install . --force
    echo ""
    echo "AVX installed successfully via pipx!"
    echo "You can now use the 'avx' command anywhere."
    exit 0
fi

echo "'uv' or 'pipx' not found. Falling back to standard pip..."
pip install .
echo ""
echo "AVX installed successfully!"
echo "You can now use the 'avx' command anywhere."
