from src.commands.config.config_repository import ConfigRepository
from src.commands.set.set_command import SetCommand
from src.commands.set.set_command_macos import SetCommandMacOS


class SetCommandProvider:
    def __init__(self, config_repo: ConfigRepository):
        self.__config_repo = config_repo

    def provide(self) -> SetCommand:
        # TODO switch case for each OS
        return SetCommandMacOS(self.__config_repo)
