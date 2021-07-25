from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    resolution: str
    keywords: List[str]
