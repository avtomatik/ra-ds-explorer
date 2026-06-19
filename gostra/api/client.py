from gostra.api.endpoints import (CERT_REQUESTS, CERTIFICATES, USERS,
                                  certificate_by_serial)
from gostra.api.pagination import paginate
from gostra.api.parsers import (parse_cert_requests, parse_certificate_detail,
                                parse_certificates, parse_users)


class CertificatesApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(CERTIFICATES)
        return parse_certificates(response.json_data)

    def _fetch_href(self, href: str):
        response = self.transport.get(href)
        return parse_certificates(response.json_data)

    def iter_all(self):

        first_page = self.list()

        yield from paginate(first_page, self._fetch_href)

    def list_all(self):
        return list(self.iter_all())

    def get_by_serial(self, serial: str):
        response = self.transport.get(certificate_by_serial(serial))
        return parse_certificate_detail(response.json_data)


class UsersApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(USERS)
        return parse_users(response.json_data)


class CertRequestsApi:

    def __init__(self, transport):
        self.transport = transport

    def list(self):
        response = self.transport.get(CERT_REQUESTS)
        return parse_cert_requests(response.json_data)


class GostRAClient:

    def __init__(self, transport):
        self.transport = transport

        self.certificates = CertificatesApi(transport)

        self.users = UsersApi(transport)

        self.cert_requests = CertRequestsApi(transport)
