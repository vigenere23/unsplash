from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    type: str
    resolution: str
    keywords: List[str]

    def __getitem__(self, item):
        return getattr(self, item)
