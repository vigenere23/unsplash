import subprocess
from os import path
from pathlib import Path
from appscript import app, mactypes

from src.commands.config.config_repository import ConfigRepository
from src.commands.set.set_command import SetCommand


class SetCommandMacOS(SetCommand):
    def __init__(self, config_repo: ConfigRepository):
        # TODO inject
        super().__init__(path.join(Path.home(), 'Pictures', 'unsplash', 'current'), config_repo)

    def _set_new_wallpaper(self, image_path: str):
        app('Finder').desktop_picture.set(mactypes.File(image_path))
        subprocess.call(['/usr/bin/killall', 'Dock'])
