from gostra.infrastructure.transport.exceptions import (HttpError,
                                                        JsonParseError)


def ensure_success(response):

    if not response.ok:
        raise HttpError(response.status_code, response.body)

    return response


def ensure_json(response):

    if response.json_data is None:
        raise JsonParseError(response.body)

    return response.json_data
