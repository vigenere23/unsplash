import subprocess
from os import path
from pathlib import Path

from commands.uninstall.uninstall_command import UninstallCommand


class UninstallCommandLinux(UninstallCommand):
    def execute(self):
        script = path.join(Path.home(), '.unsplash', 'installers', 'uninstall_linux.sh')
        subprocess.call(['/bin/bash', f'{script}'])
