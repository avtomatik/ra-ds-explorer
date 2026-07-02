from enum import StrEnum


class OID(StrEnum):
    # =========================================================================
    # Subject attributes
    # =========================================================================
    CN = "2.5.4.3"  # common_name
    SN = "2.5.4.4"  # surname
    GIVEN_NAME = "2.5.4.42"  # given_name
    C = "2.5.4.6"  # country_name
    L = "2.5.4.7"  # locality_name
    O = "2.5.4.10"  # organization_name      # NOQA: E741
    OU = "2.5.4.11"  # organizational_unit_name
    # =========================================================================
    # Russian subject attributes
    # =========================================================================
    INN = "1.2.643.3.131.1.1"  # inn
    SNILS = "1.2.643.100.3"  # snils
    GUID = "1.2.643.3.168.7"  # guid
    LEGAL_ENTITY_INN = "1.2.643.100.4"  # legal_entity_inn
    OGRN = "1.2.643.100.1"  # ogrn
    # =========================================================================
    # PKCS #9
    # =========================================================================
    EMAIL_ADDRESS = "1.2.840.113549.1.9.1"  # email_address
    UNSTRUCTURED_NAME = "1.2.840.113549.1.9.2"  # unstructured_name
    # =========================================================================
    # Microsoft
    # =========================================================================
    USER_PRINCIPAL_NAME = "1.3.6.1.4.1.311.20.2.3"  # user_principal_name
    CERTIFICATE_TEMPLATE = "1.3.6.1.4.1.311.21.7"  # certificate_template
    # =========================================================================
    # Russian certificate extensions
    # =========================================================================
    SIGNATURE_DEVICE = "1.2.643.100.111"  # signature_device
    ISSUER_SIGNATURE_AND_CA_TOOLS = (
        "1.2.643.100.112"  # issuer_signature_and_ca_tools
    )
    IDENTITY_VERIFICATION_METHOD = (
        "1.2.643.100.114"  # identity_verification_method
    )
    # =========================================================================
    # GOST algorithms
    # =========================================================================
    GOST3410_2012_256_PUBLIC_KEY = (
        "1.2.643.7.1.1.1.1"  # gost3410_2012_256_public_key
    )
    GOST3411_2012_256_SIGNATURE = (
        "1.2.643.7.1.1.3.2"  # gost3411_2012_256_signature
    )
    # =========================================================================
    # PKIX
    # =========================================================================
    AUTHORITY_INFORMATION_ACCESS = (
        "1.3.6.1.5.5.7.1.1"  # authority_information_access
    )
    OCSP = "1.3.6.1.5.5.7.48.1"  # ocsp
    CA_ISSUERS = "1.3.6.1.5.5.7.48.2"  # ca_issuers
    # =========================================================================
    # X.509 v3 extensions
    # =========================================================================
    SUBJECT_KEY_IDENTIFIER = "2.5.29.14"  # subject_key_identifier
    KEY_USAGE = "2.5.29.15"  # key_usage
    PRIVATE_KEY_USAGE_PERIOD = "2.5.29.16"  # private_key_usage_period
    CRL_DISTRIBUTION_POINTS = "2.5.29.31"  # crl_distribution_points
    CERTIFICATE_POLICIES = "2.5.29.32"  # certificate_policies
    AUTHORITY_KEY_IDENTIFIER = "2.5.29.35"  # authority_key_identifier
    EXTENDED_KEY_USAGE = "2.5.29.37"  # extended_key_usage
    # =========================================================================
    # Extended Key Usage (EKU)
    # =========================================================================
    SMARTCARD_LOGIN = "1.2.643.3.168.6.1"  # smartcard_login
    # =========================================================================
    # Extras
    # =========================================================================
    PARTICULAR_TEMPLATE = (
        "1.2.643.2.2.50.1.9.10425219.14382135.8474254.6866964.19296.34159"
    )
