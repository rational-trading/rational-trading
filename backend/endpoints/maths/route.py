from ninja import Router, Schema
from django.http.request import HttpRequest

from endpoints.auth import AuthBearer

router = Router(auth=AuthBearer())


class MathsResponse(Schema):
    add: int
    multiply: int
    authenticated_user: str

    def __init__(self, add: int, multiple: int, authenticated_user: str):
        self.add = add
        self.multiple = multiple
        self.authenticated_user = authenticated_user


class AuthenticatedRequest(HttpRequest):
    auth: str


@router.get("/{a}and{b}", response=MathsResponse)
def maths(request: AuthenticatedRequest, a: int, b: int) -> MathsResponse:
    print(type(request))
    return MathsResponse(add=a + b, multiple=a * b, authenticated_user=request.auth)
