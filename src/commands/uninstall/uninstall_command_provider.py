from platform import system

from commands.uninstall.uninstall_command_linux import UninstallCommandLinux
from commands.uninstall.uninstall_command_mac import UninstallCommandMac
from commands.uninstall.uninstall_command import UninstallCommand


class UninstallCommandProvider:
    def provide(self) -> UninstallCommand:
        os = system()

        if os == 'Linux':
            return UninstallCommandLinux()
        elif os == 'Darwin':
            return UninstallCommandMac()
