import subprocess
from os import path
from pathlib import Path

from commands.upgrade.upgrade_command import UpgradeCommand


class UpgradeCommandLinux(UpgradeCommand):

    def execute(self):
        script = path.join(Path.home(), '.unsplash', 'scripts', 'upgrade_linux.sh')
        subprocess.call(['/bin/bash', f'{script}'])
