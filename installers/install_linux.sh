#!/bin/bash

set -e # Exit on error

function step {
    bold=$(tput bold)
    normal=$(tput sgr0)
    printf "\n $bold$1$normal\n"
}

timestamp="$(date +%s)"
REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/main.zip"
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

python3 -m venv "$INSTALLATION_DIR/.venv"
source "$INSTALLATION_DIR/.venv/bin/activate" && \
pip install --upgrade pip && \
pip install -r "$INSTALLATION_DIR/requirements.txt"

step "⚙️ Creating config and executables..."

ln -f -s "$INSTALLATION_DIR/bin/unsplash_linux.sh" "$HOME/.local/bin/unsplash"
ln -f -s "$INSTALLATION_DIR/installers/unsplash.desktop" "$HOME"/.config/autostart

step "✨ DONE!"

printf "\nBefore starting:\n"
echo "  1. Adjust your resolution with 'unsplash config resolution --value <value>'"
echo "  2. Set your random keywords selection with with 'unsplash config keywords --value <value>'"
echo "  3. Get your first wallpaper with 'unsplash set'"
echo "  4. Like it? Save it with 'unsplash save'!"
echo "  5. Display help with 'unsplash --help'"
