from gostra.domain.models.search import SearchResult
from gostra.infrastructure.transport.base import BaseTransport


class SearchService:
    def __init__(self, transport: BaseTransport):
        self.transport = transport

    def search(self, query: str):
        resp = self.transport.get("/search", params={"q": query})
        data = resp.json_data
        return SearchResult(
            query=data["query"],
            items=data["items"],
        )
