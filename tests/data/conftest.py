import pytest

from rads_explorer.data.loader import FixtureLoader
from rads_explorer.data.reports import ReportService
from rads_explorer.data.repository import Repository


@pytest.fixture
def report_service(fixtures_dir) -> ReportService:
    loader = FixtureLoader(fixtures_dir)
    repo = Repository(loader.load())
    return ReportService(repo)
