from platform import system

from commands.config.config_repository import ConfigRepository
from commands.set.set_command import SetCommand
from commands.set.set_command_macos import SetCommandMacOS
from commands.set.set_command_macos import SetCommandLinux


class SetCommandProvider:
    def __init__(self, config_repo: ConfigRepository):
        self.__config_repo = config_repo

    def provide(self) -> SetCommand:
        os = system()

        if os == 'Linux':
            return SetCommandLinux(self.__config_repo)
        elif os == 'Darwin':
            return SetCommandMacOS(self.__config_repo)
