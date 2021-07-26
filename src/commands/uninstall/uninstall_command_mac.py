import subprocess
from os import path
from pathlib import Path

from commands.uninstall.uninstall_command import UninstallCommand


class UninstallCommandMac(UninstallCommand):
    def execute(self):
        script = path.join(Path.home(), '.unsplash', 'scripts', 'uninstall_mac.sh')
        subprocess.call(['/bin/bash', f'{script}'])
