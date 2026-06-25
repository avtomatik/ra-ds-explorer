import json
from pathlib import Path

from gostra.api.parsers import (parse_cert_request_detail, parse_cert_requests,
                                parse_certificate_detail, parse_certificates,
                                parse_users)

root = Path("gostra/fixtures")

parse_certificates(json.loads((root / "certificates.json").read_text()))

parse_users(json.loads((root / "users.json").read_text()))

parse_cert_requests(json.loads((root / "cert_requests.json").read_text()))

parse_certificate_detail(
    json.loads(
        (
            root
            / "certificate_details"
            / "014A99A46D4DA7FF824147754A019E25E7.json"
        ).read_text()
    )
)

parse_cert_request_detail(
    json.loads(
        (
            root
            / "cert_request_details"
            / "019eb692-51bc-4096-91a3-28b79508e670.json"
        ).read_text()
    )
)

print("OK")
