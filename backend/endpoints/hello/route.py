from ninja import Router, Schema

router = Router()


@router.get("/")
def hello_get(request, name="world"):
    print(request.user)
    msg = "You can specify your name by appending \'?name=\' to the url."
    return f"Hello {name}! {msg if name == 'world'  else ''}"


class HelloRequest(Schema):
    name: str = "world"


@router.post("/")
def hello_post(request, data: HelloRequest):
    return f"Hello {data.name}"
