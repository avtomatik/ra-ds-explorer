from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SearchResult:
    query: str
    items: list[dict[str, Any]]
