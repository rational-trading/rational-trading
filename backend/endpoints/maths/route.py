from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest

from endpoints.auth import AuthBearer

router = Router(auth=AuthBearer())


class MathsResponseSchema(Schema):
    add: int
    multiply: int
    authenticated_user: str


@dataclass
class MathsResponse:
    add: int
    multiply: int
    authenticated_user: str


class AuthenticatedRequest(HttpRequest):
    auth: str


@router.get("/{a}and{b}", response=MathsResponseSchema)
def maths(request: AuthenticatedRequest, a: int, b: int) -> MathsResponse:
    print(type(request))
    return MathsResponse(add=a + b, multiply=a * b, authenticated_user=request.auth)
