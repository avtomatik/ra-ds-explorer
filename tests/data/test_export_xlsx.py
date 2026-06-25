from gostra.data.export.xlsx import XLSXExporter
from gostra.data.loader import FixtureLoader
from gostra.data.reports import ReportService
from gostra.data.repository import Repository


def test_xlsx_export(fixtures_dir, tmp_path):
    loader = FixtureLoader(fixtures_dir)
    repo = Repository(loader.load())
    service = ReportService(repo)

    report = service.expiring_certificates_report(365)

    exporter = XLSXExporter()
    out = tmp_path / "report.xlsx"

    exporter.export(report, out)

    assert out.exists()
    assert out.stat().st_size > 0
