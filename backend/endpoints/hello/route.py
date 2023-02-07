from ninja import Router, Schema

router = Router()


@router.get("/")
def hello_get(request, name="world"):
    print(request.user)
    return f"Hello {name}! You can specify your name by appending '?name=' to the url."


class HelloSchema(Schema):
    name: str = "world"


@router.post("/")
def hello_post(request, data: HelloSchema):
    return f"Hello {data.name}"
