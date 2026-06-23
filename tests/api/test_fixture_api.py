def test_cert_requests_list(client):

    result = client.cert_requests.list()

    assert len(result.items) > 0


def test_certificates_list(client):

    result = client.certificates.list()

    assert len(result.items) > 0


def test_certificates_iter_all(client):

    certs = list(client.certificates.iter_all())

    assert len(certs) > 0


def test_users_list(client):

    result = client.users.list()

    assert len(result.items) > 0


def test_certificate_detail(client, serial):

    cert = client.certificates.get_by_serial(serial)

    assert cert.subject
    assert cert.issuer

    assert cert.x509.issuer
    assert cert.x509.not_valid_after_utc
    assert cert.x509.not_valid_before_utc
    assert cert.x509.public_key_algorithm_oid
    assert cert.x509.serial_number
    assert cert.x509.signature
    assert cert.x509.signature_algorithm_oid
    assert cert.x509.subject
    assert cert.x509.tbs_certificate_bytes
    assert cert.x509.version
