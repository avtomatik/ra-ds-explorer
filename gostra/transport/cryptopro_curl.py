import json
import subprocess
from typing import Any, Mapping, Optional
from urllib.parse import urlencode

from gostra.transport.config import Settings
from gostra.transport.response import HttpResponse


class CryptoProCurlTransport:

    def __init__(self, settings: Settings):
        self.settings = settings

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Mapping[str, Any]] = None,
        json_data: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> HttpResponse:
        url = self.build_url(path, params)

        cmd = [
            self.settings.curl_path,
            "-s",
            "-k",
            "--cert",
            self.settings.cert_thumbprint,
            "-i",
            "-w",
            "\nHTTP_STATUS:%{http_code}",
            url,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        raw, status_part = result.stdout.rsplit("HTTP_STATUS", 1)

        status_code = int(status_part.strip())

        try:
            headers, body = raw.split("\r\n\r\n", 1)
        except ValueError:
            headers = ""
            body = raw

        try:
            parsed_json = json.loads(body) if body else None
        except json.JSONDecodeError:
            parsed_json = None

        return HttpResponse(
            status_code=status_code,
            headers={},
            body=body,
            json_data=parsed_json,
        )

    def get(self, path, params=None, headers=None) -> HttpResponse:
        return self.request(
            method="GET", path=path, params=params, headers=headers
        )

    def build_url(self, path: str, params=None) -> str:

        base = self.settings.api_base_url.rstrip("/")
        path = path.lstrip("/")

        url = f"{base}/{path}"

        if params:
            url += "?" + urlencode(params)

        return url
