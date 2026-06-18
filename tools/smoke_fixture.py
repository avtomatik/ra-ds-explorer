from pathlib import Path

from gostra.api.client import GostRAClient
from gostra.application.certificate_service import CertificateService
from gostra.infrastructure.fixtures.router import FixtureRouter
from gostra.infrastructure.fixtures.store import FixtureStore
from gostra.infrastructure.transport.fixture_transport import FixtureTransport

store = FixtureStore(Path("gostra/fixtures"))

router = FixtureRouter(store)

transport = FixtureTransport(router)

client = GostRAClient(transport)

response = client.certificates.list()

print(response)
print()
print(response.items[0].id)
print(response.items[0].thumbprint)
print(response.items[0].name_attributes.common_name)


service = CertificateService(client)

certs = service.list_certificates()

print(len(certs.items))
