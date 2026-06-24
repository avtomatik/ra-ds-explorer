from datetime import datetime

from pydantic import Field

from .base import APIModel
from .name_attributes import NameAttributes


class CertRequest(APIModel):
    id: str
    name_attributes: NameAttributes = Field(validation_alias="nameAttributes")

    created_when: datetime = Field(validation_alias="createdWhen")
    resolved_when: datetime | None = Field(
        None, validation_alias="resolvedWhen"
    )
    auth_replied_when: datetime | None = Field(
        None, validation_alias="authRepliedWhen"
    )

    status: str
