import json
from dataclasses import asdict
from os import path

from src.config.config import Config
from src.config.config_repository import ConfigRepository


class ConfigRepositoryJson(ConfigRepository):
    def __init__(self):
        this_file_dir = path.dirname(path.realpath(__file__))
        self.__FILE_PATH = path.join(this_file_dir, '..', '..', 'config.json')

    def get(self) -> Config:
        with open(self.__FILE_PATH, 'r') as file:
            data = json.loads(file.read())
            return Config(**data)


    def save(self, config: Config) -> None:
        data = json.dumps(asdict(config), indent=4)
        with open(self.__FILE_PATH, 'w') as file:
            file.write(data)
