from pathlib import Path

from gostra.application.demo_flow import DemoFlow
from gostra.container.container import get_container
from gostra.data.export.xlsx import XLSXExporter
from gostra.data.loader import FixtureLoader
from gostra.data.reports import ReportService
from gostra.data.repository import Repository


def main():
    container = get_container()

    loader = FixtureLoader(Path("gostra/fixtures"))

    repo = Repository(loader.load())

    reports = ReportService(repo)

    flow = DemoFlow(
        certificate_service=container.certificate_service(),
        user_service=container.user_service(),
        cert_request_service=container.cert_request_service(),
        exporter=XLSXExporter(),
        reports=reports,
    )

    flow.run()


if __name__ == "__main__":
    main()
