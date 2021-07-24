from abc import ABC, abstractmethod

class PostInstaller(ABC):
    def install(self):
        self._create_cli_alias_with_permissions()
        self._create_auto_setter()

    @abstractmethod
    def _create_cli_alias_with_permissions(self):
        raise NotImplementedError()

    @abstractmethod
    def _create_auto_setter(self):
        raise NotImplementedError()
