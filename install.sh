#!/usr/bin/env bash
set -e

echo "==========================================="
echo "Installing AVX..."
echo "==========================================="

OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    ARCH="arm64"
fi

if [ "$OS" = "linux" ] || [ "$OS" = "darwin" ]; then
    BINARY_URL="https://github.com/Aryan-202/avx/releases/latest/download/avx-${OS}-${ARCH}"
else
    echo "Unsupported OS: $OS"
    exit 1
fi

INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

echo "Downloading AVX for $OS ($ARCH) from $BINARY_URL..."
curl -fsSL "$BINARY_URL" -o "$INSTALL_DIR/avx"
chmod +x "$INSTALL_DIR/avx"

echo ""
echo "AVX installed successfully to $INSTALL_DIR/avx"
echo "Make sure $INSTALL_DIR is in your PATH."
echo "You can now use the 'avx' command anywhere."
