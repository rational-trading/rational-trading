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


class DailyChangeSchema(Schema):
    price: float
    percentage: float


@router.get("/change", response=DailyChangeSchema)
def daily_change(request: HttpRequest, ticker: str) -> DailyChangeSchema:
    api = PolygonAPI()
    prev_close = api.previous_daily_price(ticker).close
    current = api.recent_price(ticker).close
    price_change = current - prev_close
    percentage_change = 100 * price_change / prev_close
    return DailyChangeSchema(price=price_change, percentage=percentage_change)


@router.get("/history", response=List[PriceSchema])
def price_history(request: HttpRequest, ticker: str) -> List[TickerPrice]:
    api = PolygonAPI()
    prices = api.price_history(ticker)
    return prices
