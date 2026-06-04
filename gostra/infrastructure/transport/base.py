from typing import Protocol

from gostra.infrastructure.transport.response import HttpResponse


class BaseTransport(Protocol):

    def request(
        self,
        method: str,
        path: str,
        params=None,
        json_data=None,
        headers=None,
    ) -> HttpResponse: ...

    def get(
        self,
        path: str,
        params=None,
        headers=None,
    ) -> HttpResponse: ...
