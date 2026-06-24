from pydantic import Field

from .base import APIModel
from .cert_request_list import CertRequest
from .certificate_list import Certificate
from .pages import Links
from .user_list import User


class CertRequestsResponse(APIModel):
    items: list[CertRequest]
    links: Links = Field(validation_alias="_links")


class CertificatesResponse(APIModel):
    items: list[Certificate]
    links: Links = Field(validation_alias="_links")


class UsersResponse(APIModel):
    items: list[User]
    links: Links = Field(validation_alias="_links")
