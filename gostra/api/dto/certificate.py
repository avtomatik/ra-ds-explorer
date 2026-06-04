from pydantic import BaseModel


class CertificateDTO(BaseModel):
    id: str
    owner: str
