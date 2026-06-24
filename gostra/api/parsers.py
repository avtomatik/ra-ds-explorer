from gostra.api.schemas.cert_request_detail import CertRequestDetail
from gostra.api.schemas.cert_request_list import CertRequest
from gostra.api.schemas.certificate_detail import CertificateDetail
from gostra.api.schemas.certificate_list import Certificate
from gostra.api.schemas.responses import (CertificatesResponse,
                                          CertRequestsResponse, UsersResponse)
from gostra.api.schemas.user_list import User


def parse_cert_requests(data: dict) -> CertRequestsResponse:
    return CertRequestsResponse.model_validate(data)


def parse_certificates(data: dict) -> CertificatesResponse:
    return CertificatesResponse.model_validate(data)


def parse_users(data: dict) -> UsersResponse:
    return UsersResponse.model_validate(data)


def parse_cert_request(data: dict) -> CertRequest:
    return CertRequest.model_validate(data)


def parse_certificate_detail(data: dict) -> CertificateDetail:
    return CertificateDetail.model_validate(data)


def parse_cert_request_detail(data: dict) -> CertRequestDetail:
    return CertRequestDetail.model_validate(data)


def parse_certificate(data: dict) -> Certificate:
    return Certificate.model_validate(data)


def parse_user(data: dict) -> User:
    return User.model_validate(data)
