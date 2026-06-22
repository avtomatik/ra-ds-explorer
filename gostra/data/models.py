from dataclasses import dataclass

from gostra.api.schemas.cert_request import CertRequest
from gostra.api.schemas.certificate import Certificate
from gostra.api.schemas.user import User


@dataclass
class Dataset:
    cert_requests: list[CertRequest]
    certificates: list[Certificate]
    users: list[User]
