from typing import List
from ninja import Router, Schema
from django.db import transaction
from django.http.request import HttpRequest

from lib.polygon_api import PolygonAPI, TickerDetails

router = Router()


class TickerDetailsSchema(Schema):
    ticker: str
    company_name: str
    exchange: str


@router.get("/all", response=List[TickerDetailsSchema])
@transaction.atomic
def all_stocks(request: HttpRequest) -> List[TickerDetails]:
    companies_ticker = ["AAPL", "META", "ADBE"]
    api = PolygonAPI()

    stocks_details = []
    for company_ticker in companies_ticker:
        stocks_details.append(api.get_ticker_details(company_ticker))
    return stocks_details
