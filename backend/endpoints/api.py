from ninja import NinjaAPI, Schema
from ninja.errors import AuthenticationError, ValidationError
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.conf import settings

from lib.exceptions import FriendlyClientException, FriendlyInternalException

from .auth.route import router as auth_router
from .price.route import router as price_router
from .portfolio.route import router as portfolio_router
from .financials.route import router as financials_router
from .trades.route import router as trades_router
from .user.route import router as user_router
from .stocks.route import router as stocks_router
from .news.route import router as news_router

api = NinjaAPI()

api.add_router("/auth/", auth_router)
api.add_router("/price/", price_router)
api.add_router("/portfolio/", portfolio_router)
api.add_router("/user/", user_router)
api.add_router("/financials/", financials_router)
api.add_router("/trades/", trades_router)
api.add_router("/stocks/", stocks_router)
api.add_router("/news/", news_router)


class ErrorResponse(Schema):
    error: str


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


@api.exception_handler(FriendlyClientException)
def friendly_client_exception(request: HttpRequest, e: FriendlyClientException) -> HttpResponse:
    print(e)
    return api.create_response(
        request,
        {
            "error": str(e)
        },
        status=400
    )


@api.exception_handler(FriendlyInternalException)
def friendly_internal_exception(request: HttpRequest, e: FriendlyInternalException) -> HttpResponse:
    print(e)
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
