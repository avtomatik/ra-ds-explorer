from pathlib import Path

from fastapi import APIRouter

from gostra.container.container import get_container
from gostra.data.export.xlsx import XLSXExporter
from gostra.data.loader import FixtureLoader
from gostra.data.reports import ReportService
from gostra.data.repository import Repository

router = APIRouter()

loader = FixtureLoader(Path("gostra/fixtures"))
dataset = loader.load()
repo = Repository(dataset)
reports = ReportService(repo)
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
    return reports.expiring_certificates_report(days).data


@router.get("/reports/issuer")
def issuer_report():
    return reports.issuer_report().data


@router.get("/export/expiring.xlsx")
def export_expiring(days: int = 30):
    report = reports.expiring_certificates_report(days)
    path = Path("/tmp/expiring.xlsx")
    exporter.export(report, path)
    return {"file": str(path)}
