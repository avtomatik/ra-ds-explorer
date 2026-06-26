from functools import lru_cache

from rads_explorer.api.client import RADSClient
from rads_explorer.application.cert_request_service import CertRequestService
from rads_explorer.application.certificate_service import CertificateService
from rads_explorer.application.search_service import SearchService
from rads_explorer.application.user_service import UserService
from rads_explorer.config.enums import TransportMode
from rads_explorer.config.paths import FIXTURES_DIR
from rads_explorer.config.settings import Settings
from rads_explorer.infrastructure.fixtures.router import FixtureRouter
from rads_explorer.infrastructure.fixtures.store import FixtureStore
from rads_explorer.infrastructure.transport.cryptopro_curl import \
    CryptoProCurlTransport
from rads_explorer.infrastructure.transport.fixture_transport import \
    FixtureTransport


class Container:
    def __init__(self):
        self._settings = Settings()
        self._transport = self._build_transport()
        self._client = RADSClient(self._transport)

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
