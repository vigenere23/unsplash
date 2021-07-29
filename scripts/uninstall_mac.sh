#!/bin/bash

INSTALLATION_DIR="$HOME/.unsplash"

sudo rm "$HOME"/Library/LaunchAgents/ca.vigenere23.unsplash.plist
rm /usr/local/bin/unsplash

rm -r "$INSTALLATION_DIR"
