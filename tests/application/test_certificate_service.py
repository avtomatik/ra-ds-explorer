from gostra.application.certificate_service import CertificateService
from gostra.infrastructure.transport.mock_transport import MockTransport


def test_get_certificate():
    transport = MockTransport()
    service = CertificateService(transport)
    response = service.get_certificate("dummy_id")
    assert response.id == "dummy"
    assert response.owner == "test-user"
