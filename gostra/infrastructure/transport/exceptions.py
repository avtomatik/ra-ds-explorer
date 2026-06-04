class TransportError(Exception): ...


class CurlExecutionError(TransportError): ...


class HttpError(TransportError):
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
        super().__init__(f"HTTP {status_code}")


class JsonParseError(TransportError): ...
