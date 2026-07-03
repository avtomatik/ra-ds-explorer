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

    def _get_certificates(self):
        return self.certificate_service.list_certificates().items

    def _get_mapped_certificates(self, certificates):
        return [self.mapper.map(c) for c in certificates]

    def certificates_inventory_report(self):
        certificates = self._get_certificates()

        mapped = self._get_mapped_certificates(certificates)

        return Report(
            name="certificates_inventory",
            generated_at=datetime.now(timezone.utc),
            data=mapped,
        )

    def expiring_certificates_report(self, days: int):
        certificates = self._get_certificates()

        threshold = datetime.now(timezone.utc) + timedelta(days=days)

        filtered = [c for c in certificates if c.not_after <= threshold]

        mapped = [self.mapper.map(c) for c in filtered]

        return Report(
            name=f"expiring_{days}_days",
            generated_at=datetime.now(timezone.utc),
            data=mapped,
        )
