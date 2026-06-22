from pathlib import Path

from gostra.data.loader import FixtureLoader
from gostra.data.repository import Repository


def setup_repo():
    loader = FixtureLoader(Path("gostra/fixtures"))
    return Repository(loader.load())


def test_search_certificates():
    repo = setup_repo()
    results = repo.search_certificates("ivan")

    assert isinstance(results, list)


def test_expiring_certificates():
    repo = setup_repo()
    results = repo.certificates_expiring_before(365)

    assert isinstance(results, list)
