from functools import lru_cache

from gostra.api.client import GostRAClient
from gostra.application.cert_request_service import CertRequestService
from gostra.application.certificate_service import CertificateService
from gostra.application.search_service import SearchService
from gostra.application.user_service import UserService
from gostra.config.enums import TransportMode
from gostra.config.paths import FIXTURES_DIR
from gostra.config.settings import Settings
from gostra.infrastructure.fixtures.router import FixtureRouter
from gostra.infrastructure.fixtures.store import FixtureStore
from gostra.infrastructure.transport.cryptopro_curl import \
    CryptoProCurlTransport
from gostra.infrastructure.transport.fixture_transport import FixtureTransport


class Container:
    def __init__(self):
        self._settings = Settings()
        self._transport = self._build_transport()
        self._client = GostRAClient(self._transport)

    def _build_transport(self):
        match self._settings.transport:
            case TransportMode.FIXTURE:
                store = FixtureStore(FIXTURES_DIR)
                router = FixtureRouter(store)
                return FixtureTransport(router)

            case TransportMode.CURL:
                return CryptoProCurlTransport(self._settings)

            case _:
                raise ValueError(
                    f"Unsupported transport: " f"{self._settings.transport}"
                )

    def certificate_service(self):
        return CertificateService(self._client)

    def cert_request_service(self):
        return CertRequestService(self._client)

    def user_service(self):
        return UserService(self._client)

    def search_service(self):
        return SearchService(self._client)


@lru_cache
def get_container() -> Container:
    return Container()
