from typing import List
from ninja import Router, Schema
from django.http.request import HttpRequest
from endpoints.auth import AuthBearer

from lib.polygon_api import PolygonAPI, TickerPrice
from models.models import StockModel, UserModel, WatchlistModel


router = Router(auth=AuthBearer())


class AuthenticatedRequest(HttpRequest):
    auth: str


class PriceSchema(Schema):
    time: int
    open: float
    low: float
    high: float
    close: float


class WhoamiSchema(Schema):
    username: str


class WatchListSchema(Schema):
    tickers: List[str]


class TickerSchema(Schema):
    ticker: str


@router.get("/whoami", response=WhoamiSchema)
def whoami(request: AuthenticatedRequest) -> WhoamiSchema:
    return WhoamiSchema(username=request.auth)


@router.post("/watchlist/add")
def add_to_watchlist(request: AuthenticatedRequest, data: TickerSchema) -> bool:
    try:
        stock = StockModel.objects.get(ticker=data.ticker)
        user = UserModel.objects.get(username=request.auth)
        WatchlistModel.create_typed(
            user=user, stock=stock)
        return True
    except StockModel.DoesNotExist:
        raise ValueError("No such stock exists")


@router.post("/watchlist/remove")
def remove_from_watchlist(request: AuthenticatedRequest, data: TickerSchema) -> bool:
    try:
        stock = StockModel.objects.get(ticker=data.ticker)
        user = UserModel.objects.get(username=request.auth)
        item = WatchlistModel.objects.get(user=user, stock=stock)
        item.delete()
        return True
    except WatchlistModel.DoesNotExist:
        raise ValueError("Item in watchlist not found")


@router.get("/watchlist", response=WatchListSchema)
def watchlist(request: AuthenticatedRequest) -> WatchListSchema:
    items = WatchlistModel.objects.filter(user=request.auth)
    stockList = [i.stock.ticker for i in items]
    return WatchListSchema(tickers=stockList)


"""
@router.get("/watchlist", response=WatchListSchema)
@router.get("/watchlist-t", response=TickersSchema)
@router.get("/watchlist/add")
@router.get("/watchlist/remove")
@router.get("/recent", response=PriceSchema)
def recent_price(request: HttpRequest, ticker: str) -> TickerPrice:
    api = PolygonAPI()
    price = api.recent_price(ticker)
    return price


@router.get("/history", response=List[PriceSchema])
def price_history(request: HttpRequest, ticker: str) -> List[TickerPrice]:
    api = PolygonAPI()
    prices = api.price_history(ticker)
    return prices
"""
