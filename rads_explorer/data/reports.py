from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from rads_explorer.application.certificate_mapper import CertificateMapper
from rads_explorer.application.x509_inspector import X509Inspector


@dataclass
class Report:
    name: str
    generated_at: datetime
    data: object


class ReportService:
    def __init__(self, certificate_service):
        self.certificate_service = certificate_service
        self.mapper = CertificateMapper(inspector=X509Inspector())

    def expiring_certificates_report(self, days: int):
        certificates = self.certificate_service.list_certificates().items

        threshold = datetime.now(timezone.utc) + timedelta(days=days)

        filtered = [c for c in certificates if c.not_after <= threshold]

        mapped = [self.mapper.map(c) for c in filtered]

        return Report(
            name=f"expiring_{days}_days",
            generated_at=datetime.now(timezone.utc),
            data=mapped,
        )

    def issuer_report(self):
        certificates = self.certificate_service.list_certificates().items

        result = {}
        for c in certificates:
            result[c.issuer] = result.get(c.issuer, 0) + 1

        return Report(
            name="issuer_distribution",
            generated_at=datetime.now(timezone.utc),
            data=result,
        )
