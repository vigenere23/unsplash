import subprocess
from os import path
from pathlib import Path

from commands.config.config_repository import ConfigRepository
from commands.set.set_command import SetCommand


class SetCommandMacOS(SetCommand):
    def __init__(self, config_repo: ConfigRepository):
        super().__init__(
            path.join(Path.home(), 'Pictures', 'unsplash', 'current'),
            path.join(Path.home(), 'Pictures', 'unsplash', 'saved'),
            config_repo
        )

    def _set_new_wallpaper(self, image_path: str):
        subprocess.call(['osascript', '-e', f'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'])
        subprocess.call(['/usr/bin/killall', 'Dock'])
