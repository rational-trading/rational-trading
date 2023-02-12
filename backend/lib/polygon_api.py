"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs/stocks/
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from http.client import HTTPResponse
from typing import Iterator, Optional
from polygon import RESTClient
from polygon.rest.models import StockFinancial
from polygon.rest.models import TickerNews

from config.env import env


class TickerArticle():
    def __init__(self, title: str, description: str, url: str, published: str) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.published = published

    def __repr__(self) -> str:
        return (f"TickerArticle Object ({self.title[:20]}...)")


class TickerFinancials():
    def __init__(self) -> None:
        # Simon: add in relevant fields @Trevor
        pass


class PolygonAPI():
    def __init__(self) -> None:
        # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        POLYGON_API_KEY = env("POLYGON_API_KEY")
        self.client = RESTClient(api_key=POLYGON_API_KEY)  # type: ignore

    def get_financials(self, ticker: str) -> TickerFinancials:
        financials: Iterator[StockFinancial] | HTTPResponse = self.client.vx.list_stock_financials(
            ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        f = TickerFinancials()
        return f

    def get_news(self, ticker: str, max_items: int) -> list[TickerArticle]:
        news_generator: Iterator[TickerNews] | HTTPResponse = self.client.list_ticker_news(
            ticker=ticker, limit=1)
        articles = []
        for _ in range(max_items):
            n = news_generator.__next__()
            # We only get bytes if calling list_ticker_news with raw=True, so can assert TickerNews
            assert isinstance(n, TickerNews)

            assert n.title is not None
            assert n.description is not None
            assert n.article_url is not None
            assert n.published_utc is not None

            article = TickerArticle(n.title, n.description,
                                    n.article_url, n.published_utc)
            articles.append(article)
        return articles


# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    n = api.get_news("AAPL", 1)
    f = api.get_financials("AAPL")
    print(n)
    print(f)
