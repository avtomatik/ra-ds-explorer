from gostra.infrastructure.transport.response import HttpResponse


class MockTransport:

    def request(
        self,
        method: str,
        path: str,
        params=None,
        json_data=None,
        headers=None,
    ) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            headers={},
            body="",
            json_data={
                "id": "dummy",
                "owner": "test-user",
            },
        )

    def get(self, path, params=None, headers=None):
        return self.request(
            "GET",
            path,
            params=params,
            headers=headers,
        )
