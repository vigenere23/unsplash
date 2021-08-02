from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ConfigCommandArguments:
    type: Optional[str] = None
    resolution: Optional[str] = None
    keywords: Optional[List[str]] = None
