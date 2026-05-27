class CertificatesApi:
    def __init__(self, transport):
        self.transport = transport


class UsersApi:
    def __init__(self, transport):
        self.transport = transport


class GostRAClient:
    def __init__(self, transport):
        self.transport = transport
        self.certificates = CertificatesApi(transport)
        self.users = UsersApi(transport)
