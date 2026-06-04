from gostra.api.endpoints import certificate_by_id


class CertificatesApi:
    def __init__(self, transport):
        self.transport = transport

    def get(self, cert_id: str):
        return self.transport.get(certificate_by_id(cert_id))


class UsersApi:
    def __init__(self, transport):
        self.transport = transport


class GostRAClient:
    def __init__(self, transport):
        self.transport = transport
        self.certificates = CertificatesApi(transport)
        self.users = UsersApi(transport)
