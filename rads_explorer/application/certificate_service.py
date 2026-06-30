class CertificateService:

    def __init__(self, api_client):
        self.api = api_client

    def list_certificates(self):
        return self.api.certificates.list()

    def get_certificate(self, serial: str):
        return self.api.certificates.get_by_serial(serial)

    def search(self, query: str):
        return self.api.certificates.search(query)
