import json
from pathlib import Path

from gostra.api.parsers import (parse_cert_requests, parse_certificates,
                                parse_users)
from gostra.data.models import Dataset


class FixtureLoader:
    def __init__(self, root: Path):
        self.root = root

    def load(self) -> Dataset:
        cert_requests = parse_cert_requests(
            json.loads((self.root / "cert_requests.json").read_text())
        )

        certificates = parse_certificates(
            json.loads((self.root / "certificates.json").read_text())
        )

        users = parse_users(json.loads((self.root / "users.json").read_text()))

        return Dataset(
            cert_requests=cert_requests.items,
            certificates=certificates.items,
            users=users.items,
        )
