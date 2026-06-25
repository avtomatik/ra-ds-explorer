import base64
from datetime import datetime
from functools import cached_property

from cryptography import x509
from pydantic import Field

from .base import APIModel
from .extension import Extension
from .name_attributes import NameAttributes


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

    # =========================================================================
    # Detailed Fields
    # =========================================================================
    cert_request_id: str | None = Field(None, validation_alias="certRequestId")
    subject: str | None = None
    issuer: str | None = None
    user_id: str | None = Field(None, validation_alias="userId")

    version: int | None = None

    public_key: str | None = Field(None, validation_alias="publicKey")
    public_key_parameters: str | None = Field(
        None, validation_alias="publicKeyParameters"
    )
    public_key_oid: str | None = Field(None, validation_alias="publicKeyOid")
    public_key_oid_description: str | None = Field(
        None, validation_alias="publicKeyOidDescription"
    )

    extensions: list[Extension] | None = None

    signature: str | None = None
    signature_oid: str | None = Field(None, validation_alias="signatureOid")
    signature_oid_description: str | None = Field(
        None, validation_alias="signatureOidDescription"
    )

    raw_certificate: str | None = Field(
        None, validation_alias="rawCertificate"
    )

    folder: str | None = None

    @cached_property
    def x509(self) -> x509.Certificate:
        return x509.load_der_x509_certificate(
            base64.b64decode(self.raw_certificate)
        )
