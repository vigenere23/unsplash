from os import path
from pathlib import Path

class LogsCommand:
    def execute(self):
        log_path = path.join(Path.home(), '.unsplash', 'unsplash.log')

        try:
            with open(log_path, 'r') as log_file:
                print(log_file.read())
        except OSError:
            print('No logs found.')
