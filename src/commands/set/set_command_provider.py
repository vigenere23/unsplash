from src.commands.set.set_command import SetCommand
from src.commands.set.set_command_macos import SetCommandMacOS


class SetCommandProvider:
    def provide(self) -> SetCommand:
        # TODO switch case for each OS
        return SetCommandMacOS()
