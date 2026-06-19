from fastapi import APIRouter

from gostra.container.container import get_container

router = APIRouter()


@router.get("/certificates")
def certificates():
    container = get_container()
    service = container.certificate_service()
    return service.list_certificates()


@router.get("/certificates/{serial}")
def get_certificate(serial: str):
    container = get_container()
    service = container.certificate_service()
    return service.get_certificate(serial)


@router.get("/users")
def users(): ...


@router.get("/certRequests")
def certRequests(): ...


@router.get("/health")
def health():
    return {"status": "ok"}
