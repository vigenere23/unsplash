from commands.uninstall.uninstall_command_mac import UninstallCommandMac
from commands.uninstall.uninstall_command import UninstallCommand


class UninstallCommandProvider:
    def provide(self) -> UninstallCommand:
        return UninstallCommandMac()
