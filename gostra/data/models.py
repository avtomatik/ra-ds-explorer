from dataclasses import dataclass

from gostra.api.schemas.cert_request_list import CertRequest
from gostra.api.schemas.certificate_list import Certificate
from gostra.api.schemas.user_list import User


@dataclass
class Dataset:
    cert_requests: list[CertRequest]
    certificates: list[Certificate]
    users: list[User]
