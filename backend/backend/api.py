from ninja import NinjaAPI, Schema
from ninja.security import HttpBearer

api = NinjaAPI()


@api.get("/hello")
def hello(request, name="world"):
    print(request.user)
    return f"Hello {name}! You can specify your name by appending '?name=' to the url."


class HelloSchema(Schema):
    name: str = "world"


@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        # Auth stuff (e.g. JWT) can go here.
        if token == "supersecret":
            return "user123"


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"user": request.auth}
