from dataclasses import dataclass
from typing import Any, Mapping


@dataclass
class HTTPResponse:
    status_code: int
    headers: Mapping[str, str]
    body: str
    json_data: Any | None

    @property
    def ok(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def content_type(self) -> str | None:
        for k, v in self.headers.items():
            if k.lower() == "content-type":
                return v

        return None
