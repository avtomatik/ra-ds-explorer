import json

from gostra.infrastructure.fixtures.router import FixtureRouter
from gostra.infrastructure.transport.response import HttpResponse


class FixtureTransport:

    def __init__(self, router: FixtureRouter):
        self.router = router

    def request(
        self,
        method,
        path,
        params=None,
        json_data=None,
        headers=None,
    ):

        payload = self.router.resolve(
            method,
            path,
        )

        return HttpResponse(
            status_code=200,
            headers={},
            body=json.dumps(payload),
            json_data=payload,
        )

    def get(
        self,
        path,
        params=None,
        headers=None,
    ):
        return self.request(
            "GET",
            path,
            params=params,
            headers=headers,
        )
