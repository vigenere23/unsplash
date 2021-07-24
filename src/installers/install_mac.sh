#!/bin/bash

set -e # Exit on error

function step {
    bold=$(tput bold)
    normal=$(tput sgr0)
    printf "\n $bold$1$normal\n"
}

REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/v2.zip"
TEMP_REPO_ZIP_FILE="/tmp/unsplash-$(date +%s).zip"
INSTALLATION_DIR="$HOME/.unsplash2"

step "⬇️ Downloading content..."

curl -L -o $TEMP_REPO_ZIP_FILE $REPO_ZIP_URL
unzip -o -j $TEMP_REPO_ZIP_FILE -d $INSTALLATION_DIR

step "🐍 Setuping Python environment..."

python3 -m venv .venv
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r "$INSTALLATION_DIR"/requirements.txt

step "⚙️ Running post installation..."

"$INSTALLATION_DIR"/unsplash postinstall
