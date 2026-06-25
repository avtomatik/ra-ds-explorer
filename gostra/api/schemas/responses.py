from pydantic import Field

from .base import APIModel
from .cert_request import CertificateRequest
from .certificate import Certificate
from .pages import Links
from .user import User


class CertRequestsResponse(APIModel):
    items: list[CertificateRequest]
    links: Links = Field(validation_alias="_links")


class CertificatesResponse(APIModel):
    items: list[Certificate]
    links: Links = Field(validation_alias="_links")


class UsersResponse(APIModel):
    items: list[User]
    links: Links = Field(validation_alias="_links")
