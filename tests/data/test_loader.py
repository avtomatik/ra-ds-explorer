from gostra.data.loader import FixtureLoader


def test_fixture_loader(fixtures_dir):
    loader = FixtureLoader(fixtures_dir)
    ds = loader.load()

    assert len(ds.certificates) > 0
    assert len(ds.users) > 0
    assert len(ds.cert_requests) > 0
