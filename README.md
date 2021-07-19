# Unsplash Bash CLI

Small Unsplash CLI for changing your desktop background on Ubuntu with Gnome.

## Installation

```sh
curl -L -o- https://raw.githubusercontent.com/vigenere23/unsplash/main/install.sh | bash
```

Make sure to add `~/.local/bin` to your `PATH` by adding `export PATH=$PATH:~/.local/bin` to your `.bashrc` / `.zshrc` / `*rc` file.

## Usage

### Change the wallpaper

```sh
unsplash set <keywords>
```

will set the wallpaper with a random image using the <keywords> keywords.

### Save the current wallpaper for later

```sh
unsplash save
```

will save the current wallpaper to `~/.unsplash/saved` for your future usage.

### Uninstall

```sh
unsplash uninstall
```
