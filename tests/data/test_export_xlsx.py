from rads_explorer.data.export.xlsx import XLSXExporter


def test_xlsx_export(report_service, tmp_path):
    report = report_service.expiring_certificates_report(365)

    exporter = XLSXExporter()
    out = tmp_path / "report.xlsx"

    exporter.export(report, out)

    assert out.exists()
    assert out.stat().st_size > 0
