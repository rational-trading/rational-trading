import datetime
from ninja import Schema, Router
from ninja.errors import AuthenticationError
from django.contrib.auth.hashers import make_password, check_password
from django.http.request import HttpRequest
import jwt

from models.models import UserModel
from config.env import env

router = Router()


class TokenSchema(Schema):
    access_token: str


class UserInput(Schema):
    username: str
    password: str


class SignupSuccess(Schema):
    success: bool


@router.post("/signup", auth=None)
def signup(request: HttpRequest, data: UserInput) -> TokenSchema:

    try:
        UserModel.objects.get(username=data.username)
        raise AuthenticationError("Username has been taken.")
    except UserModel.DoesNotExist:
        UserModel.create_typed(
            username=data.username, password=make_password(data.password), balance=0.)
        return TokenSchema(access_token=create_token(data.username))


@router.post("/login", auth=None, response=TokenSchema)
def auth(request: HttpRequest, data: UserInput) -> TokenSchema:
    try:
        pwdHash = UserModel.objects.get(username=data.username).password
        if (check_password(data.password, pwdHash)):

            token = create_token(data.username)
            return TokenSchema(access_token=token)
        else:
            raise AuthenticationError()
    except UserModel.DoesNotExist:
        raise AuthenticationError()


def create_token(username: str) -> str:

    JWT_SIGNING_KEY: str = env("JWT_SIGNING_KEY")
    JWT_ACCESS_EXPIRY: int = env("JWT_ACCESS_EXPIRY")
    access_expire = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(minutes=int(JWT_ACCESS_EXPIRY))
    encoded_access_jwt = jwt.encode(
        {"sub": username, "exp": access_expire}, JWT_SIGNING_KEY, algorithm="HS256")
    return encoded_access_jwt


"""example
@api.get("/something", auth=AuthBearer())
def something(request):
    ...

"""
