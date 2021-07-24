INSTALLATION_FOLDER="$(dirname $(readlink -f $0))"

rm "$HOME"/.local/bin/unsplash
rm "$HOME"/.config/autostart/unsplash.desktop

rm -r "$INSTALLATION_FOLDER"
