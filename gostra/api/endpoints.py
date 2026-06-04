API_PREFIX = "/api/ra"

CERTIFICATES = f"{API_PREFIX}/certificates"
USERS = f"{API_PREFIX}/users"
CERT_REQUESTS = f"{API_PREFIX}/certRequests"
TEMPLATES = f"{API_PREFIX}/templates"


def certificate_by_id(cert_id: str) -> str:
    return f"{CERTIFICATES}/{cert_id}"
