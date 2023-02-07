from ninja import Router, Schema
from django.http.request import HttpRequest

router = Router()


@router.get("/")
def hello_get(request: HttpRequest, name: str = "world") -> str:
    print(request.user)
    msg = "You can specify your name by appending \'?name=\' to the url."
    return f"Hello {name}! {msg if name == 'world'  else ''}"


class HelloRequest(Schema):
    name: str = "world"


@router.post("/")
def hello_post(request: HttpRequest, data: HelloRequest) -> str:
    return f"Hello {data.name}"
