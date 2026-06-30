from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass
class Report:
    name: str
    generated_at: datetime
    data: object


class ReportService:
    def __init__(self, certificate_service):
        self.certificate_service = certificate_service

    def expiring_certificates_report(self, days: int):
        certificates = self.certificate_service.list_certificates().items

        threshold = datetime.now(timezone.utc) + timedelta(days=days)

        expiring = [c for c in certificates if c.not_after <= threshold]

        return Report(
            name=f"expiring_{days}_days",
            generated_at=datetime.now(timezone.utc),
            data=expiring,
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
