from ninja import Schema


class ErrorResponse(Schema):
    error: str


class FriendlyClientException(Exception):
    pass


class FriendlyInternalException(Exception):
    pass
