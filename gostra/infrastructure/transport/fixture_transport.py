import json

from gostra.infrastructure.fixtures.router import FixtureRouter
from gostra.infrastructure.transport.response import HTTPResponse


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
        try:
            payload = self.router.resolve(method, path)
        except FileNotFoundError:
            return HTTPResponse(
                status_code=404,
                headers={},
                body="Not found",
                json_data=None,
            )

        return HTTPResponse(
            status_code=200,
            headers={},
            body=json.dumps(payload),
            json_data=payload if isinstance(payload, (dict, list)) else None,
        )

    def get(
        self,
        path,
        params=None,
        headers=None,
    ):
        return self.request("GET", path, params=params, headers=headers)
