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

step "⚙️ Creating executables..."

ln -f -s "$INSTALLATION_DIR/bin/unsplash_mac.sh" /usr/local/bin/unsplash

step "Configuring..."

printf "\nScreen resolution (2880x1800): "
read screen_res

printf "Keywords (mountains): "
read keywords

unsplash config resolution --value $screen_res
unsplash config keywords --value $keywords

step "✨ Setting first wallpaper..."

unsplash set

step "✨ DONE!"
