from abc import ABC, abstractmethod


class UpgradeCommand(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
