REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/main.zip"
TEMP_REPO_ZIP_FILE="/tmp/unsplash-$(uuidgen).zip"
INSTALLATION_DIR="$HOME/.unsplash"

if [ -d $INSTALLATION_DIR ]; then
    echo "Unsplash wallpaper is already installed in $INSTALLATION_DIR"
    exit 0
fi

echo "Downloading content"

wget -O $TEMP_REPO_ZIP_FILE $REPO_ZIP_URL
unzip -j $TEMP_REPO_ZIP_FILE -d $INSTALLATION_DIR

echo "Installing unsplash wallpaper in $INSTALLATION_DIR"

mkdir "$INSTALLATION_DIR/current"
mkdir "$INSTALLATION_DIR/saved"

chmod +x "$INSTALLATION_DIR/unsplash"
chmod +x "$INSTALLATION_DIR/unsplash.desktop"
chmod +x "$INSTALLATION_DIR/uninstall.sh"

if [ ! -e "$HOME"/.local/bin/unsplash ]; then
    ln -s "$INSTALLATION_DIR/unsplash" "$HOME"/.local/bin/unsplash
fi

if [ ! -e "$HOME"/.config/autostart ]; then
    ln -s "$INSTALLATION_DIR/unsplash.desktop" "$HOME"/.config/autostart
fi


"$INSTALLATION_DIR/unsplash" set mountains
