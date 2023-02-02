from ninja import Router

from auth.bearer import AuthBearer

router = Router(auth=AuthBearer())


@router.get("/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b, "authenticated_user": request.auth}