from fastapi import APIRouter

from rads_explorer.config.paths import EXPORTS_DIR, FIXTURES_DIR
from rads_explorer.container.container import get_container
from rads_explorer.data.export.xlsx import XLSXExporter
from rads_explorer.data.loader import FixtureLoader
from rads_explorer.data.reports import ReportService
from rads_explorer.data.repository import Repository

router = APIRouter()

loader = FixtureLoader(FIXTURES_DIR)
dataset = loader.load()
repo = Repository(dataset)
report_service = ReportService(repo)
exporter = XLSXExporter()


@router.get("/certificates")
def certificates():
    container = get_container()
    service = container.certificate_service()
    return service.list_certificates().model_dump(by_alias=True)


@router.get("/certificates/{serial}")
def get_certificate(serial: str):
    container = get_container()
    service = container.certificate_service()
    return service.get_certificate(serial)


@router.get("/users")
def users():
    container = get_container()
    service = container.user_service()
    return service.list_users().model_dump(by_alias=True)


@router.get("/certRequests")
def cert_requests():
    container = get_container()
    service = container.cert_request_service()
    return service.list_requests().model_dump(by_alias=True)


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/search/certificates")
def search_certificates(q: str):
    return repo.search_certificates(q)


@router.get("/reports/expiring")
def expiring(days: int = 30):
    return report_service.expiring_certificates_report(days).data


@router.get("/reports/issuer")
def issuer_report():
    return report_service.issuer_report().data


@router.get("/export/expiring.xlsx")
def export_expiring(days: int = 30):
    report = report_service.expiring_certificates_report(days)
    path = EXPORTS_DIR / "expiring.xlsx"
    exporter.export(report, path)
    return {"file": str(path)}
