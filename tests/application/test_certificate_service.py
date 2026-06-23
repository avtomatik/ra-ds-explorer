def test_get_certificate(client, serial):

    cert = client.certificates.get_by_serial(serial)

    assert cert.id == "019e25e7-75ee-42fc-9046-aeed792aec4b"
    assert cert.user_id == "019e25e7-5dac-4aac-b5d5-7bf83a396f9f"
    # assert cert.subject == ""
    # assert cert.issuer == ""
