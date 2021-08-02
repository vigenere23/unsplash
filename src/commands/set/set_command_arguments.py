from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

@dataclass
class SetCommandArguments:
    type: Optional[str] = None
    resolution: Optional[str] = None
    keywords: Optional[List[str]] = None

class SetCommandType(Enum):
    NEW = auto(),
    SAVED = auto()

    @staticmethod
    def parse(value: str):
        if value == 'new':
            return SetCommandType.NEW
        elif value == 'saved':
            return SetCommandType.SAVED
        else:
            raise ValueError(f'Invalid value {value} for SetCommandType.')

    def print(self) -> str:
        return self.name.lower()
