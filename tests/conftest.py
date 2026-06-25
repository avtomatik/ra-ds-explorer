from pathlib import Path

import pytest

from gostra.api.client import GostRAClient
from gostra.config.paths import FIXTURES_DIR
from gostra.infrastructure.fixtures.router import FixtureRouter
from gostra.infrastructure.fixtures.store import FixtureStore
from gostra.infrastructure.transport.fixture_transport import FixtureTransport


@pytest.fixture
def serial() -> str:
    return "014A99A46D4DA7FF824147754A019E25E7"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def client(fixtures_dir) -> GostRAClient:
    store = FixtureStore(fixtures_dir)
    router = FixtureRouter(store)
    transport = FixtureTransport(router)
    return GostRAClient(transport)
