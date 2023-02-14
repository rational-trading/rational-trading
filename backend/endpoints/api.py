from ninja import NinjaAPI
from ninja.errors import AuthenticationError, ValidationError
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from ninja.security import HttpBearer

import jwt
import datetime
import os
from dotenv import load_dotenv

from .hello.route import router as hello_router
from .maths.route import router as maths_router

api = NinjaAPI()

api.add_router("/hello/", hello_router)
api.add_router("/maths/", maths_router)


@api.exception_handler(AuthenticationError)
def authentication_error(request: HttpRequest, e: AuthenticationError) -> HttpResponse:
    print(e)
    return api.create_response(
        request,
        {"error": "Could not authenticate. Hint: You need to add 'Authorization: Bearer supersecret;' to your HTTP headers. This can be done in Swagger UI using the lock icon in the top right of the endpoint."},
        status=401
    )


@api.exception_handler(ValidationError)
def validation_error(request: HttpRequest, e: ValidationError) -> HttpResponse:
    print(e)
    return api.create_response(
        request,
        {"error": "Request validation failed. Please use the correct input format."},
        status=422
    )


class TokenSchema(Schema):

    access_token: str
    

@api.post("/login", auth=None, response={200, TokenSchema})
def auth(request, username: str, password: str):
    #check username 
    # check password
    create_token(username)

def create_token(username):
    load_dotenv()
    JWT_SIGNING_KEY = os.getenv('JWT_SIGNING_KEY')
    JWT_ACCESS_EXPIRY = os.getenv('JWT_ACCESS_EXPIRY')
    #JWT_SIGNING_KEY = getattr(settings, "JWT_SIGNING_KEY", None)        # add attributes to settings
    #JWT_ACCESS_EXPIRY = getattr(settings, "JWT_ACCESS_EXPIRY", "60") # 60 minutes expiration
    to_encode_access = {"sub": username}
    access_expire = datetime.utcnow() + datetime.timedelta(minutes=JWT_ACCESS_EXPIRY)
    to_encode_access.update({"exp": access_expire})
    encoded_access_jwt = jwt.encode(to_encode_access, JWT_SIGNING_KEY, algorithm="HS256")
    return encoded_access_jwt

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            #JWT secret key is set up in .env
            load_dotenv()
            JWT_SIGNING_KEY = os.getenv(JWT_SIGNING_KEY)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None
        return username


"""example
@api.get("/something", auth=AuthBearer())
def something(request):
    ...

"""