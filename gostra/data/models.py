from dataclasses import dataclass

from gostra.api.schemas.cert_request import CertificateRequest
from gostra.api.schemas.certificate import Certificate
from gostra.api.schemas.user import User


@dataclass
class Dataset:
    cert_requests: list[CertificateRequest]
    certificates: list[Certificate]
    users: list[User]
