from fastapi import APIRouter

from gostra.container.container import get_container

router = APIRouter()


@router.get("/certificates/{cert_id}")
def get_certificate(cert_id: str):
    container = get_container()
    service = container.certificate_service()
    return service.get_certificate(cert_id)


@router.get("/health")
def health():
    return {"status": "ok"}
