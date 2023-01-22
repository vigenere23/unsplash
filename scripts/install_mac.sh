#!/bin/bash

set -e # Exit on error

function step {
    bold=$(tput bold)
    normal=$(tput sgr0)
    printf "\n $bold$1$normal\n\n"
}

function is_agent_running {
    launch_agent_running=$(sudo launchctl list | grep $1)
    test -n "$launch_agent_running"
}

timestamp="$(date +%s)"
REPO_ZIP_URL="https://github.com/vigenere23/unsplash/archive/refs/heads/main.zip"
TEMP_REPO_ZIP_FILE="/tmp/unsplash-$timestamp.zip"
TEMP_REPO_DIR="/tmp/unsplash-$timestamp"
INSTALLATION_DIR="$HOME/.unsplash"
LAUNCH_AGENT_NAME="ca.vigenere23.unsplash"
LAUNCH_AGENT_PATH="$HOME/Library/LaunchAgents/$LAUNCH_AGENT_NAME.plist"

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

sudo ln -f -s -v "$INSTALLATION_DIR/bin/unsplash_mac.sh" /usr/local/bin/unsplash

step "⚙️  Configuring..."

printf "Screen resolution (2880x1800): "
read screen_res

printf "Keywords (aerial): "
read keywords

unsplash config set resolution $screen_res
unsplash config set keywords $keywords

cat "$INSTALLATION_DIR/resources/ca.vigenere23.unsplash.plist.template" | envsubst > "$INSTALLATION_DIR/resources/ca.vigenere23.unsplash.plist"
mv -f -v "$INSTALLATION_DIR/resources/ca.vigenere23.unsplash.plist" "$LAUNCH_AGENT_PATH"
chmod 644 "$LAUNCH_AGENT_PATH"

printf "\nThis program needs 'root' privileges to install the sheduler (will change your wallpaper at every login).\n"

sudo chown root:wheel "$LAUNCH_AGENT_PATH"

set +e
sudo launchctl unload -F "$LAUNCH_AGENT_PATH"
sudo launchctl load "$LAUNCH_AGENT_PATH"
set -e

if ! is_agent_running $LAUNCH_AGENT_NAME
then
    echo "ERROR: Could not start the launchd agent." >&2
    exit 1
else
    echo "launchd agent started successfully"
fi

step "🎉 DONE! Use 'unsplash --help' for more commands."
