from functools import lru_cache

from gostra.application.certificate_service import CertificateService
from gostra.application.search_service import SearchService
from gostra.config.settings import Settings
from gostra.infrastructure.transport.cryptopro_curl import \
    CryptoProCurlTransport


class Container:
    def __init__(self):
        self._settings = Settings()
        self._transport = CryptoProCurlTransport(self._settings)

    def certificate_service(self):
        return CertificateService(self._transport)

    def search_service(self):
        return SearchService(self._transport)


@lru_cache
def get_container() -> Container:
    return Container()
