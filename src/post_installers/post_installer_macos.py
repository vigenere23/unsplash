from os import path
from pathlib import Path
from distutils.dir_util import copy_tree

from src.post_installers.post_installer import PostInstaller


class PostInstallerMacOS(PostInstaller):
    def __init__(self):
        self.__INSTALLATION_DIR = path.join(Path.home(), '.unsplash')

    def _create_cli_alias_with_permissions(self):
        pass

    def _create_auto_setter(self):
        return super()._create_auto_setter()
