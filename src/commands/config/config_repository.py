from abc import ABC, abstractmethod

from src.commands.config.config import Config

class ConfigRepository(ABC):
    @abstractmethod
    def get(self) -> Config:
        raise NotImplementedError()

    def save(self, config: Config) -> None:
        raise NotImplementedError()
