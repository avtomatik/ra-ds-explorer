from gostra.api.schemas.cert_request import CertificateRequest
from gostra.api.schemas.certificate import Certificate
from gostra.api.schemas.responses import (CertificatesResponse,
                                          CertRequestsResponse, UsersResponse)
from gostra.api.schemas.user import User


def parse_cert_requests(data: dict) -> CertRequestsResponse:
    return CertRequestsResponse.model_validate(data)


def parse_certificates(data: dict) -> CertificatesResponse:
    return CertificatesResponse.model_validate(data)


def parse_users(data: dict) -> UsersResponse:
    return UsersResponse.model_validate(data)


def parse_cert_request(data: dict) -> CertificateRequest:
    return CertificateRequest.model_validate(data)


def parse_certificate_detail(data: dict) -> Certificate:
    return Certificate.model_validate(data)


def parse_cert_request_detail(data: dict) -> CertificateRequest:
    return CertificateRequest.model_validate(data)


def parse_certificate(data: dict) -> Certificate:
    return Certificate.model_validate(data)


def parse_user(data: dict) -> User:
    return User.model_validate(data)
