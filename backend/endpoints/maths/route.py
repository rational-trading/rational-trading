from ninja import Router, Schema

from endpoints.auth import AuthBearer

router = Router(auth=AuthBearer())


class MathsResponse(Schema):
    add: int
    multiply: int
    authenticated_user: str


@router.get("/{a}and{b}", response=MathsResponse)
def maths(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b, "authenticated_user": request.auth}
