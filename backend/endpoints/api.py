from ninja import NinjaAPI, Schema
from ninja.errors import AuthenticationError, ValidationError
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from ninja.security import HttpBearer
from django.contrib.auth.hashers import make_password, check_password

import jwt
import datetime
from config.env import env
from django.conf import settings

from endpoints.error import FriendlyException

from .demo.route import router as demo_router
from .hello.route import router as hello_router
from .auth.route import router as auth_router
from .maths.route import router as maths_router
from .price.route import router as price_router
from .portfolio.route import router as portfolio_router
from .financials.route import router as financials_router
from .trades.route import router as trades_router

from models.models import UserModel

api = NinjaAPI()

api.add_router("/auth/", auth_router)
api.add_router("/price/", price_router)
api.add_router("/portfolio/", portfolio_router)
api.add_router("/financials/", financials_router)
api.add_router("/trades/", trades_router)


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


@api.exception_handler(FriendlyException)
def friendly_exception(request: HttpRequest, e: FriendlyException) -> HttpResponse:
    return api.create_response(
        request,
        {
            "error": str(e)
        },
        status=500
    )


@api.exception_handler(Exception)
def exception(request: HttpRequest, e: Exception) -> HttpResponse:
    print(e)
    return api.create_response(
        request,
        {"error": str(
            e) if settings.DEBUG else "Something went wrong! Check logs for more details."},
        status=500
    )
