from typing import List
from ninja import Router, Schema
from django.http.request import HttpRequest

from lib.polygon_api import PolygonAPI, TickerPrice

router = Router()


class PriceSchema(Schema):
    time: int
    open: float
    low: float
    high: float
    close: float


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
