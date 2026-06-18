import pytest

from gostra.application.certificate_service import CertificateService


@pytest.mark.skip
def test_get_certificate():
    transport = ""
    service = CertificateService(transport)
    response = service.get_certificate("dummy_id")
    assert response.id == "dummy"
    assert response.owner == "test-user"
