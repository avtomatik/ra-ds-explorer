from pathlib import Path

from gostra.data.loader import FixtureLoader
from gostra.data.reports import ReportService
from gostra.data.repository import Repository


def test_report_generation():
    loader = FixtureLoader(Path("gostra/fixtures"))
    repo = Repository(loader.load())
    service = ReportService(repo)

    report = service.expiring_certificates_report(365)

    assert report.name.startswith("expiring")
    assert report.data is not None
