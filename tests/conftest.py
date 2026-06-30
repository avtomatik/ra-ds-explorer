from pathlib import Path

import pytest

from rads_explorer.api.client import RADSClient
from rads_explorer.application.certificate_service import CertificateService
from rads_explorer.config.paths import FIXTURES_DIR
from rads_explorer.data.reports import ReportService
from rads_explorer.infrastructure.fixtures.router import FixtureRouter
from rads_explorer.infrastructure.fixtures.store import FixtureStore
from rads_explorer.infrastructure.transport.fixture_transport import \
    FixtureTransport


@pytest.fixture
def serial() -> str:
    return "014A99A46D4DA7FF824147754A019E25E7"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def client(fixtures_dir) -> RADSClient:
    store = FixtureStore(fixtures_dir)
    router = FixtureRouter(store)
    transport = FixtureTransport(router)
    return RADSClient(transport)


@pytest.fixture
def report_service(client) -> ReportService:
    return ReportService(CertificateService(client))
