from platform import system

from commands.upgrade.upgrade_command_mac import UpgradeCommandMac
from commands.upgrade.upgrade_command_linux import UpgradeCommandLinux

class UpgradeCommandProvider:

    def provide(self):
        os = system()

        if os == 'Linux':
            return UpgradeCommandLinux()
        elif os == 'Darwin':
            return UpgradeCommandMac()
