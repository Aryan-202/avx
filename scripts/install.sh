#!/usr/bin/env bash
set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}Starting AVX Installation...${NC}"

OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

echo -n "Checking architecture ($ARCH)... "
sleep 0.4
echo -e "${GREEN}Done${NC}"

if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    ARCH="arm64"
fi

if [ "$OS" = "linux" ] || [ "$OS" = "darwin" ]; then
    BINARY_URL="https://github.com/Aryan-202/avx/releases/latest/download/avx-${OS}-${ARCH}"
else
    echo -e "${RED}Unsupported OS: $OS${NC}"
    exit 1
fi

INSTALL_DIR="$HOME/.local/bin"
echo -n "Preparing directory: $INSTALL_DIR... "
mkdir -p "$INSTALL_DIR"
sleep 0.4
echo -e "${GREEN}Done${NC}"

echo -e "Downloading AVX for $OS ($ARCH) from GitHub..."
curl -# -fSL "$BINARY_URL" -o "$INSTALL_DIR/avx"

echo -n "Finalizing configuration... "
chmod +x "$INSTALL_DIR/avx"
sleep 0.4
echo -e "${GREEN}Done${NC}"

cat << "EOF" | sed "s/^/$(tput setaf 6 2>/dev/null || echo '\e[0;36m')/"

    ___ _    ___  __
   /   | |  / / |/ /
  / /| | | / /|   / 
 / ___ | |/ //   |  
/_/  |_|___//_/|_|  

EOF
echo -e "${NC}"

echo -e "${GREEN}AVX installed successfully to $INSTALL_DIR/avx${NC}"
echo -e "Make sure ${YELLOW}$INSTALL_DIR${NC} is in your PATH."
echo -e "You can now use the 'avx' command anywhere.\n"
