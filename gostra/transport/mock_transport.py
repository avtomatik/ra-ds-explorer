from typing import Any, Mapping, Optional

from gostra.transport.config import Settings
from gostra.transport.response import HttpResponse


class MockTransport:

    def __init__(self, settings: Settings):
        self.settings = settings

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Mapping[str, Any]] = None,
        json_data: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> HttpResponse: ...
