import pytest

from rads_explorer.application.cert_request_service import CertRequestService
from rads_explorer.application.certificate_service import CertificateService
from rads_explorer.application.user_service import UserService
from rads_explorer.data.export.xlsx import XLSXExporter
from tests.helpers.demo_flow import DemoFlow


@pytest.mark.real
def test_list_certificates(): ...
@pytest.mark.real
def test_get_certificate_by_serial(): ...
@pytest.mark.real
def test_list_users(): ...
@pytest.mark.real
def test_list_cert_requests(): ...


@pytest.mark.real
def test_real_api_flow_runs(client, report_service):
    flow = DemoFlow(
        certificate_service=CertificateService(client),
        cert_request_service=CertRequestService(client),
        user_service=UserService(client),
        exporter=XLSXExporter(),
        reports=report_service,
    )

    flow.run()
