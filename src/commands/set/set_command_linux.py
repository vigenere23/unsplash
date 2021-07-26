import subprocess
from os import path
from pathlib import Path

from commands.config.config_repository import ConfigRepository
from commands.set.set_command import SetCommand


class SetCommandLinux(SetCommand):
    def __init__(self, config_repo: ConfigRepository):
        super().__init__(path.join(Path.home(), 'Pictures', 'unsplash', 'current'), config_repo)

    def _set_new_wallpaper(self, image_path: str):
        subprocess.call(['/usr/bin/gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{image_path}'])
