def test_search_certificates(client, serial):
    results = client.certificates.search(serial[:5])
    assert results.items
