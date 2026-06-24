from functools import cached_property

from pydantic import Field

from gostra.api.schemas.cert_request_list import CertRequest
from gostra.api.schemas.extension import Extension


class CertRequestDetail(CertRequest):
    user_id: str = Field(validation_alias="userId")
    subject: str

    creator_id: str = Field(validation_alias="creatorId")
    creator_name: str = Field(validation_alias="creatorName")
    creator_login: str = Field(validation_alias="creatorLogin")

    resolver_id: str = Field(validation_alias="resolverId")
    resolver_name: str = Field(validation_alias="resolverName")
    resolver_login: str = Field(validation_alias="resolverLogin")

    version: int = 1

    public_key: str = Field(validation_alias="publicKey")
    public_key_parameters: str = Field(validation_alias="publicKeyParameters")
    public_key_oid: str = Field(validation_alias="publicKeyOid")
    public_key_oid_description: str = Field(
        validation_alias="publicKeyOidDescription"
    )

    signature: str
    signature_oid: str = Field(validation_alias="signatureOid")
    signature_oid_description: str = Field(
        validation_alias="signatureOidDescription"
    )

    template_oid: str = Field(validation_alias="templateOid")
    template_name: str = Field(validation_alias="templateName")
    template_display_name: str = Field(validation_alias="templateDisplayName")

    extensions: list[Extension]

    raw_request: str = Field(validation_alias="rawRequest")

    folder: str

    certificate_id: str = Field(validation_alias="certificateId")

    @cached_property
    def pkcs7_blob(self):
        raise NotImplementedError("PKCS#7 parsing not implemented yet.")
