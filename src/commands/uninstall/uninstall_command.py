from abc import ABC, abstractmethod


class UninstallCommand(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
