"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs/stocks/
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from polygon import RESTClient
import config #contains API_KEY

class PolygonAPI():
    def __init__(self) -> None:
        self.client = RESTClient(api_key=config.API_KEY) #type:ignore

    def get_financials(self, ticker: str) -> object:
        financials = self.client.vx.list_stock_financials(ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        return financials
    
    def get_news(self, ticker: str) -> object:
        news = self.client.list_ticker_news(ticker=ticker, limit=1)
        return news  # use next(news) to iterate over