from dataclasses import dataclass
from datetime import datetime, timezone

from rads_explorer.data.repository import Repository


@dataclass
class Report:
    name: str
    generated_at: datetime
    data: object


class ReportService:
    def __init__(self, repo: Repository):
        self.repo = repo

    def expiring_certificates_report(self, days: int):
        return Report(
            name=f"expiring_{days}_days",
            generated_at=datetime.now(timezone.utc),
            data=self.repo.certificates_expiring_before(days),
        )

    def issuer_report(self):
        return Report(
            name="issuer_distribution",
            generated_at=datetime.now(timezone.utc),
            data=self.repo.issuer_distribution(),
        )
