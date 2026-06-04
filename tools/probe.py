import argparse
import json

from gostra.config.settings import Settings
from gostra.infrastructure.transport.cryptopro_curl import \
    CryptoProCurlTransport


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("path")
    parser.add_argument("--param", action="append", default=[])

    args = parser.parse_args()

    params = {}

    for item in args.param:
        key, value = item.split("=", 1)
        params[key] = value

    settings = Settings()

    transport = CryptoProCurlTransport(settings)

    response = transport.get(args.path, params=params)

    print(f"HTTP {response.status_code}")

    if response.json_data is not None:
        print(json.dumps(response.json_data, indent=2, ensure_ascii=False))
    else:
        print(response.body)


if __name__ == "__main__":
    main()
