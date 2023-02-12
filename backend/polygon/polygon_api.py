"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs/stocks/
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from http.client import HTTPResponse
from typing import Iterator
from polygon import RESTClient
from polygon.rest.models import StockFinancial
from polygon.rest.models import TickerNews
import config


class PolygonAPI():
    def __init__(self) -> None:
        self.client = RESTClient(api_key=config.API_KEY)  # type: ignore

    def get_financials(self, ticker: str) -> Iterator[StockFinancial] | HTTPResponse:
        financials = self.client.vx.list_stock_financials(
            ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        return financials

    def get_news(self, ticker: str) -> Iterator[TickerNews] | HTTPResponse:
        news = self.client.list_ticker_news(ticker=ticker, limit=1)
        return news  # use next(news) to iterate over
