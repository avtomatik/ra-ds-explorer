import json
from pathlib import Path


class FixtureStore:

    def __init__(self, root: Path):
        self.root = root

    def load(self, name: str) -> dict:
        path = self.root / f"{name}.json"

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
