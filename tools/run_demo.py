import logging

from rads_explorer.application.demo_flow import DemoFlow
from rads_explorer.config.paths import FIXTURES_DIR
from rads_explorer.container.container import get_container
from rads_explorer.data.export.xlsx import XLSXExporter
from rads_explorer.data.loader import FixtureLoader
from rads_explorer.data.reports import ReportService
from rads_explorer.data.repository import Repository
from rads_explorer.shared.logging import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()

    container = get_container()

    loader = FixtureLoader(FIXTURES_DIR)

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
