from functools import lru_cache

from gostra.api.client import GostRAClient
from gostra.application.certificate_service import CertificateService
from gostra.config.settings import Settings
from gostra.infrastructure.transport.cryptopro_curl import \
    CryptoProCurlTransport


class Container:
    def __init__(self):
        self._settings = Settings()
        transport = CryptoProCurlTransport(self._settings)
        self._client = GostRAClient(transport)

    def certificate_service(self):
        return CertificateService(self._client)


@lru_cache
def get_container() -> Container:
    return Container()
