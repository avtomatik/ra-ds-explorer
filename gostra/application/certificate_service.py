from gostra.domain.models.certificate import Certificate
from gostra.infrastructure.transport.base import BaseTransport


class CertificateService:
    def __init__(self, transport: BaseTransport):
        self.transport = transport

    def get_certificate(self, cert_id: str):
        resp = self.transport.get(f"/certificates/{cert_id}")

        if not resp.ok:
            raise Exception("Failed to fetch certificate")

        data = resp.json_data
        return Certificate(
            id=data["id"],
            owner=data["owner"],
            raw=data,
        )
