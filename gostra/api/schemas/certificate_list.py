from datetime import datetime

from pydantic import Field

from gostra.api.schemas.base import APIModel
from gostra.api.schemas.name_attributes import NameAttributes


class Certificate(APIModel):
    id: str
    name_attributes: NameAttributes = Field(validation_alias="nameAttributes")

    serial_number: str = Field(validation_alias="serialNumber")
    thumbprint: str

    not_before: datetime = Field(validation_alias="notBefore")
    not_after: datetime = Field(validation_alias="notAfter")
    key_not_after: datetime = Field(validation_alias="keyNotAfter")
    created_when: datetime = Field(validation_alias="createdWhen")

    status: str
