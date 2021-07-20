from abc import ABC, abstractmethod

from commands.arguments import SetCommandArguments


class CommandExecutor(ABC):
    @abstractmethod
    def set(self, args: SetCommandArguments) -> None:
        raise NotImplementedError()

    @abstractmethod
    def save_current(self) -> None:
        raise NotImplementedError()
