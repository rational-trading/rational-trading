from ninja import Schema


class ErrorResponse(Schema):
    error: str


class FriendlyException(Exception):
    pass
