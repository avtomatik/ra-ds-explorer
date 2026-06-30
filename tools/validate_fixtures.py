import json
import logging

from rads_explorer.api.parsers import (parse_cert_request_detail,
                                       parse_cert_requests,
                                       parse_certificate_detail,
                                       parse_certificates, parse_users)
from rads_explorer.config.paths import FIXTURES_DIR
from rads_explorer.shared.logging import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()

    parse_certificates(
        json.loads((FIXTURES_DIR / "certificates.json").read_text())
    )

    parse_users(json.loads((FIXTURES_DIR / "users.json").read_text()))

    parse_cert_requests(
        json.loads((FIXTURES_DIR / "cert_requests.json").read_text())
    )

    parse_certificate_detail(
        json.loads(
            (
                FIXTURES_DIR
                / "certificate_details"
                / "014A99A46D4DA7FF824147754A019E25E7.json"
            ).read_text()
        )
    )

    parse_cert_request_detail(
        json.loads(
            (
                FIXTURES_DIR
                / "cert_request_details"
                / "019eb692-51bc-4096-91a3-28b79508e670.json"
            ).read_text()
        )
    )

    logger.info("OK")


if __name__ == "__main__":
    main()
