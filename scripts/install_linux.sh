#!/bin/bash

set -e # Exit on error

function step {
    bold=$(tput bold)
    normal=$(tput sgr0)
    printf "\n $bold$1$normal\n\n"
}

timestamp="$(date +%s)"
REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/main.zip"
TEMP_REPO_ZIP_FILE="/tmp/unsplash-$timestamp.zip"
TEMP_REPO_DIR="/tmp/unsplash-$timestamp"
INSTALLATION_DIR="$HOME/.unsplash"
BINARY_DIR="$HOME/.local/bin"

if [ -d $INSTALLATION_DIR ]; then
    rm -rf $INSTALLATION_DIR
fi

step "⬇️  Downloading content..."

curl -L -o $TEMP_REPO_ZIP_FILE $REPO_ZIP_URL
unzip -o $TEMP_REPO_ZIP_FILE -d $TEMP_REPO_DIR
mv -f -v $TEMP_REPO_DIR/* $INSTALLATION_DIR

step "🐍 Setuping Python environment..."

python3 -m venv "$INSTALLATION_DIR/.venv"
source "$INSTALLATION_DIR/.venv/bin/activate" && \
pip install --upgrade pip && \
pip install -r "$INSTALLATION_DIR/requirements.txt"

step "🛠  Creating executables..."

if [ ! -d $BINARY_DIR ]; then
    mkdir "$BINARY_DIR"
fi

ln -f -s -v "$INSTALLATION_DIR/bin/unsplash_linux.sh" "$BINARY_DIR/unsplash"
ln -f -s -v "$INSTALLATION_DIR/resources/unsplash.desktop" "$HOME"/.config/autostart/
grep -qxF 'export PATH="'$BINARY_DIR':$PATH"' "$HOME/.bashrc" || echo 'export PATH="'$BINARY_DIR':$PATH"' >> "$HOME/.bashrc"


step "⚙️  Configuring..."

printf "Screen resolution (2880x1800): "
read screen_res

printf "Keywords (aerial): "
read keywords

"$BINARY_DIR/unsplash" config set resolution $screen_res
"$BINARY_DIR/unsplash" config set keywords $keywords

step "🖼️  Setting first wallpaper..."

"$BINARY_DIR/unsplash" set

step "🎉 DONE! Use 'unsplash --help' for more commands."
