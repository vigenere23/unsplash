#!/bin/bash

INSTALLER_SCRIPT="https://raw.githubusercontent.com/vigenere23/unsplash/main/installers/install_linux.sh"

bash <(curl -L -o- "$INSTALLER_SCRIPT")
