from gostra.api.endpoints import (CERT_REQUESTS, CERTIFICATES, USERS,
                                  certificate_by_serial)
from gostra.api.pagination import paginate
from gostra.api.parsers import (parse_cert_request, parse_cert_requests,
                                parse_certificate_detail, parse_certificates,
                                parse_user, parse_users)
from gostra.application.exceptions import APIContractError


class CertificatesApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(CERTIFICATES)

        try:
            return parse_certificates(response.json_data)
        except Exception:
            raise APIContractError("Unexpected Response for Certificate Model")

    def _fetch_href(self, href: str):
        response = self.transport.get(href)

        try:
            return parse_certificates(response.json_data)
        except Exception:
            raise APIContractError("Unexpected Response for Certificate Model")

    def iter_all(self):
        first_page = self.list()
        yield from paginate(first_page, self._fetch_href)

    def list_all(self):
        return list(self.iter_all())

    def get_by_serial(self, serial: str):
        response = self.transport.get(certificate_by_serial(serial))

        try:
            return parse_certificate_detail(response.json_data)
        except Exception:
            raise APIContractError(
                "Unexpected Response for Certificate Detail Model"
            )

    def search(self, query):
        response = self.transport.get(CERTIFICATES, params={"search": query})

        try:
            return parse_certificates(response.json_data)
        except Exception:
            raise APIContractError("Unexpected Response for Certificate Model")


class UsersApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(USERS)

        try:
            return parse_users(response.json_data)
        except Exception:
            raise APIContractError("Unexpected Response for User Model")

    def get(self, user_id):
        response = self.transport.get(f"{USERS}/{user_id}")

        try:
            return parse_user(response.json_data)
        except Exception:
            raise APIContractError("Unexpected Response for User Model")


class CertRequestsApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(CERT_REQUESTS)

        try:
            return parse_cert_requests(response.json_data)
        except Exception:
            raise APIContractError(
                "Unexpected Response for Certificate Request Model"
            )

    def get(self, cert_request_id):
        response = self.transport.get(f"{CERT_REQUESTS}/{cert_request_id}")

        try:
            return parse_cert_request(response.json_data)
        except Exception:
            raise APIContractError(
                "Unexpected Response for Certificate Request Model"
            )


class GostRAClient:

    def __init__(self, transport):
        self.transport = transport

        self.certificates = CertificatesApi(transport)

        self.users = UsersApi(transport)

        self.cert_requests = CertRequestsApi(transport)
