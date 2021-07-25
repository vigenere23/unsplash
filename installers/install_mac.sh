#!/bin/bash

set -e # Exit on error

function step {
    bold=$(tput bold)
    normal=$(tput sgr0)
    printf "\n $bold$1$normal\n"
}

timestamp="$(date +%s)"
REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/v2.zip"
TEMP_REPO_ZIP_FILE="/tmp/unsplash-$timestamp.zip"
TEMP_REPO_DIR="/tmp/unsplash-$timestamp"
INSTALLATION_DIR="$HOME/.unsplash"

if [ -d $INSTALLATION_DIR ]; then
    rm -rf $INSTALLATION_DIR
fi

step "⬇️ Downloading content..."

curl -L -o $TEMP_REPO_ZIP_FILE $REPO_ZIP_URL
unzip -o $TEMP_REPO_ZIP_FILE -d $TEMP_REPO_DIR
mv -f -v $TEMP_REPO_DIR/* $INSTALLATION_DIR

step "🐍 Setuping Python environment..."

python3 -m venv .venv
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r "$INSTALLATION_DIR"/requirements.txt

step "⚙️ Creating config and executables..."

if [ ! -e "$HOME"/.local/bin/unsplash ]; then
    ln -f -s "$INSTALLATION_DIR/unsplash" /usr/local/bin/unsplash
fi

step "✨ DONE!\n"

unsplash --help
