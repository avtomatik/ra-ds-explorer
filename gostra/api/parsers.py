from .schemas.certificate_detail import CertificateDetail
from .schemas.responses import (CertificatesResponse, CertRequestsResponse,
                                UsersResponse)


def parse_cert_requests(data: dict) -> CertRequestsResponse:
    return CertRequestsResponse.model_validate(data)


def parse_certificates(data: dict) -> CertificatesResponse:
    return CertificatesResponse.model_validate(data)


def parse_users(data: dict) -> UsersResponse:
    return UsersResponse.model_validate(data)


def parse_certificate_detail(data: dict) -> CertificateDetail:
    return CertificateDetail.model_validate(data)
