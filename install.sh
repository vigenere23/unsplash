SCRIPT_FOLDER="$(dirname $(readlink -f $0))"
INSTALLATION_DIR="$HOME/.unsplash"

if [ -d $INSTALLATION_DIR ]; then
    echo "Unsplash wallpaper is already installed in $INSTALLATION_DIR"
    exit 0
fi

echo "Installing unsplash wallpaper in $INSTALLATION_DIR"

mkdir "$INSTALLATION_DIR"
mkdir "$INSTALLATION_DIR/current"
mkdir "$INSTALLATION_DIR/saved"

cp "$SCRIPT_FOLDER/unsplash" "$INSTALLATION_DIR/"
cp "$SCRIPT_FOLDER/unsplash.desktop" "$INSTALLATION_DIR/"
cp "$SCRIPT_FOLDER/uninstall.sh" "$INSTALLATION_DIR/"

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
