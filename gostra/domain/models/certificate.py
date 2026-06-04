from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Certificate:
    id: str
    owner: str
    raw: dict[str, Any]
