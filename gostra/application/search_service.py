class SearchService:

    def __init__(self, repository):
        self.repository = repository

    def certificates(self, query: str):
        return self.repository.search_certificates(query)

    def users(self, query: str):
        return self.repository.search_users(query)
