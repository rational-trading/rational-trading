from typing import List
from ninja import Router, Schema
from django.http.request import HttpRequest

from endpoints.auth import AuthBearer, AuthenticatedRequest
from endpoints.api import FriendlyClientException
from lib.polygon_api import PolygonAPI, TickerPrice
from models.models import StockModel, UserModel, WatchlistItemModel


router = Router(auth=AuthBearer())


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
        WatchlistItemModel.create_typed(
            user=user, stock=stock)
        return True
    except StockModel.DoesNotExist:
        raise ValueError("No such stock exists")


@router.post("/watchlist/remove")
def remove_from_watchlist(request: AuthenticatedRequest, data: TickerSchema) -> bool:
    try:
        stock = StockModel.objects.get(ticker=data.ticker)
        user = UserModel.objects.get(username=request.auth)
        item = WatchlistItemModel.objects.get(user=user, stock=stock)
        item.delete()
        return True
    except WatchlistItemModel.DoesNotExist:
        raise FriendlyClientException("Item in watchlist not found")


@router.get("/watchlist", response=WatchListSchema)
def watchlist(request: AuthenticatedRequest) -> WatchListSchema:
    items = WatchlistItemModel.objects.filter(user=request.auth)
    stockList = [i.stock.ticker for i in items]
    return WatchListSchema(tickers=stockList)
