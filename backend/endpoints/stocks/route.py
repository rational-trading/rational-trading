from typing import List
from ninja import Router, Schema
from django.db import transaction
from django.http.request import HttpRequest
from models.models import StockModel

from lib.polygon_api import PolygonAPI, TickerDetails

router = Router()


class TickerDetailsSchema(Schema):
    ticker: str
    company_name: str
    exchange: str


@router.get("/all", response=List[TickerDetailsSchema])
@transaction.atomic
def all_stocks(request: HttpRequest) -> List[TickerDetails]:
    api = PolygonAPI()
    stocks = StockModel.objects.all()

    stocks_details = []
    for stock in stocks:
        if (stock.company_name == "" or stock.exchange == ""):
            tickerDetails = api.get_ticker_details(stock.ticker)

            stock.company_name = tickerDetails.company_name
            stock.exchange = tickerDetails.exchange
            stock.save()

            stocks_details.append(tickerDetails)
        else:
            stocks_details.append(TickerDetails(
                ticker=stock.ticker, company_name=stock.company_name, exchange=stock.exchange))
    return stocks_details
