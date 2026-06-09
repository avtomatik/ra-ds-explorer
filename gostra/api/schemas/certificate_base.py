from datetime import datetime

from pydantic import Field

from .base import APIModel
from .name_attributes import NameAttributes


class CertificateBase(APIModel):
    id: str
    name_attributes: NameAttributes = Field(validation_alias="nameAttributes")
    serial_number: str = Field(validation_alias="serialNumber")
    thumbprint: str
    not_before: datetime = Field(validation_alias="notBefore")
    not_after: datetime = Field(validation_alias="notAfter")
    key_not_after: datetime = Field(validation_alias="keyNotAfter")
    created_when: datetime = Field(validation_alias="createdWhen")
    status: str
