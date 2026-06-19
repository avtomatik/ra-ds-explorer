from gostra.infrastructure.fixtures.store import FixtureStore


class FixtureRouter:

    def __init__(self, store: FixtureStore):
        self.store = store

    def resolve(self, method: str, path: str) -> dict:

        if path == "/api/ra/users":
            return self.store.load("users")

        if path == "/api/ra/certRequests":
            return self.store.load("cert_requests")

        if path == "/api/ra/certificates":
            return self.store.load("certificates")

        if path.startswith("/api/ra/certificates/serialNumber/"):
            serial = path.rsplit("/", 1)[1]
            return self.store.load_detail(serial)

        raise KeyError(f"No fixture for {method} {path}")
