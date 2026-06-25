from enum import StrEnum


class OID(StrEnum):
    CN = "2.5.4.3"
    SN = "2.5.4.4"
    GIVEN_NAME = "2.5.4.42"

    C = "2.5.4.6"
    L = "2.5.4.7"
    O = "2.5.4.10"  # NOQA: E741
    OU = "2.5.4.11"

    INN = "1.2.643.3.131.1.1"
    GUID = "1.2.643.3.168.7"
    SNILS = "1.2.643.100.3"

    EMAIL_PKCS = "1.2.840.113549.1.9.1"

    USER_PRINCIPAL_NAME = "1.3.6.1.4.1.311.20.2.3"
