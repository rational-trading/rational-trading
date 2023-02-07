from ninja import NinjaAPI
from ninja.errors import AuthenticationError

from .hello.route import router as hello_router
from .maths.route import router as maths_router

api = NinjaAPI()

api.add_router("/hello/", hello_router)
api.add_router("/maths/", maths_router)


@api.exception_handler(AuthenticationError)
def authentication_error(request, e):
    print(e)
    return api.create_response(
        request,
        {"error": "Could not authenticate. Hint: You need to add 'Authorization: Bearer supersecret;' to your HTTP headers. This can be done in Swagger UI using the lock icon in the top right of the endpoint."},
        status=401
    )
