import subprocess
from os import path
from pathlib import Path

from commands.upgrade.upgrade_command import UpgradeCommand


class UpgradeCommandMac(UpgradeCommand):

    def execute(self):
        script = path.join(Path.home(), '.unsplash', 'scripts', 'upgrade_mac.sh')
        subprocess.call(['/bin/bash', f'{script}'])
