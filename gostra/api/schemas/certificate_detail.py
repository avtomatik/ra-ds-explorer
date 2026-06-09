import base64
from functools import cached_property

from cryptography import x509
from pydantic import Field

from .certificate_base import CertificateBase
from .extension import Extension


class CertificateDetail(CertificateBase):
    cert_request_id: str = Field(validation_alias="certRequestId")
    subject: str
    issuer: str
    user_id: str = Field(validation_alias="userId")

    version: int = 3

    public_key: str = Field(validation_alias="publicKey")
    public_key_parameters: str = Field(validation_alias="publicKeyParameters")
    public_key_oid: str = Field(validation_alias="publicKeyOid")
    public_key_oid_description: str = Field(
        validation_alias="publicKeyOidDescription"
    )

    extensions: list[Extension]

    signature: str
    signature_oid: str = Field(validation_alias="signatureOid")
    signature_oid_description: str = Field(
        validation_alias="signatureOidDescription"
    )

    raw_certificate: str = Field(validation_alias="rawCertificate")

    folder: str

    @cached_property
    def x509(self) -> x509.Certificate:
        return x509.load_der_x509_certificate(
            base64.b64decode(self.raw_certificate)
        )
