from dataclasses import dataclass
from typing import Any, Mapping, Optional


@dataclass
class HttpResponse:
    status_code: int
    headers: Mapping[str, str]
    body: str
    json_data: Optional[Any]

    @property
    def ok(self) -> bool:
        return 200 <= self.status_code < 300
