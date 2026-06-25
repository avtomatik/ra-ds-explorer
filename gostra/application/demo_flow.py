from pathlib import Path


class DemoFlow:

    def __init__(
        self,
        certificate_service,
        user_service,
        cert_request_service,
        exporter,
        reports,
    ):
        self.certificates = certificate_service
        self.users = user_service
        self.requests = cert_request_service
        self.exporter = exporter
        self.reports = reports

    def run(self):
        print("=" * 70)
        print("GOST RA CLIENT DEMO")
        print("=" * 70)

        # =====================================================================
        # A — Certificates
        # =====================================================================
        certificates = self.certificates.list_certificates()

        print("[A] Certificates")
        print("Count:", len(certificates.items))

        for cert in certificates.items[:5]:
            print("=" * 54)
            print(
                f"""
                CN:
                    {cert.name_attributes.common_name}
                SNILS:
                    {cert.name_attributes.snils}
                Serial:
                    {cert.serial_number}
                Status:
                    {cert.status}
                Valid:
                    {cert.not_before}
                    -
                    {cert.not_after}"""
            )
            print("=" * 54)

        # =====================================================================
        # B — Detail
        # =====================================================================
        first = certificates.items[0]

        detail = self.certificates.get_certificate(first.serial_number)

        print("[B] Certificate detail")
        print("Subject:", detail.subject)
        print("Issuer:", detail.issuer)
        print("X509:", detail.x509.subject)

        # =====================================================================
        # C — Reports
        # =====================================================================
        print("[C] Reports")

        expiring = self.reports.expiring_certificates_report(365)

        if len(expiring.data) > 0:
            print("Expiring:", len(expiring.data))

            issuer = self.reports.issuer_report()

            print("Issuers:", issuer.data)

        # =====================================================================
        # D — Export
        # =====================================================================
        print("[D] XLSX Export")

        output = Path("/tmp/gostra-demo.xlsx")

        self.exporter.export(expiring, output)

        print("Created:", output)
        print("DEMO COMPLETE")
