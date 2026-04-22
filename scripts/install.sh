#!/bin/bash
set -e

echo "=================================================="
echo "          Installing AVX CLI                      "
echo "=================================================="

REPO_URL="git+https://github.com/Aryan-202/avx.git"

if command -v pipx &> /dev/null; then
    echo "📦 Found pipx! Installing avx using pipx (Recommended)..."
    pipx install $REPO_URL
    echo "✅ AVX installed successfully!"
elif command -v uv &> /dev/null; then
    echo "📦 Found uv! Installing avx using uv..."
    uv tool install $REPO_URL
    echo "✅ AVX installed successfully!"
elif command -v pip &> /dev/null; then
    echo "📦 Found pip! Installing avx using pip..."
    pip install --user $REPO_URL
    echo "✅ AVX installed successfully!"
    echo "⚠️  Note: Make sure your Python user site-packages bin directory is in your PATH."
else
    echo "Error: Python package manager (pipx, uv, or pip) not found."
    echo "Please install Python from https://www.python.org/downloads/ and try again."
    exit 1
fi

echo ""
echo "You can now run 'avx --help' to get started!"
