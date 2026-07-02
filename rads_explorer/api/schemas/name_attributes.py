from typing import Any

from pydantic import ConfigDict, Field

from .base import APIModel
from .oids import OID


class NameAttributes(APIModel):
    model_config = ConfigDict(extra="allow")

    common_name: str | None = Field(None, validation_alias=OID.CN)
    surname: str | None = Field(None, validation_alias=OID.SN)
    given_name: str | None = Field(None, validation_alias=OID.GIVEN_NAME)
    country_name: str | None = Field(None, validation_alias=OID.C)
    locality_name: str | None = Field(None, validation_alias=OID.L)
    organization_name: str | None = Field(None, validation_alias=OID.O)
    organizational_unit_name: str | None = Field(None, validation_alias=OID.OU)

    inn: str | None = Field(None, validation_alias=OID.INN)
    guid: str | None = Field(None, validation_alias=OID.GUID)
    snils: str | None = Field(None, validation_alias=OID.SNILS)
    email: str | None = Field(None, validation_alias=OID.EMAIL_ADDRESS)
    upn: str | None = Field(None, validation_alias=OID.USER_PRINCIPAL_NAME)

    def raw(self) -> dict[str, Any]:
        return self.model_extra or {}
