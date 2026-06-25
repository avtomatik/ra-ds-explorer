from dataclasses import dataclass

from rads_explorer.api.schemas.cert_request import CertificateRequest
from rads_explorer.api.schemas.certificate import Certificate
from rads_explorer.api.schemas.user import User


@dataclass
class Dataset:
    cert_requests: list[CertificateRequest]
    certificates: list[Certificate]
    users: list[User]
