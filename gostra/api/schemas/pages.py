from .base import APIModel


class NextLink(APIModel):
    href: str


class Links(APIModel):
    next: NextLink | None = None
