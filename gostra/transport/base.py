from typing import Any, Mapping, Optional, Protocol

from gostra.transport.response import HttpResponse


class BaseTransport(Protocol):

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Mapping[str, Any]] = None,
        json_data: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> HttpResponse: ...

    def get(self, path, params=None, headers=None) -> HttpResponse: ...
