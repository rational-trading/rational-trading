"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from http.client import HTTPResponse
from typing import Iterator, List
from polygon import RESTClient
from polygon.rest.models import Sort, StockFinancial, TickerNews, Agg

from config.env import env
from lib.nlp import get_text_score


class TickerArticle():
    def __init__(self, title: str, description: str, url: str, date: str, publisher: str) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.date = date
        self.publisher = publisher
        self.score = get_text_score(" ".join([title, description]))

    def __repr__(self) -> str:
        return (f"TickerArticle({self.title[:20]}...)")


class TickerFinancials():
    def __init__(self) -> None:
        # Simon: add in relevant fields @Trevor
        pass


@dataclass
class TickerPrice():
    time: int
    open: float
    low: float
    high: float
    close: float

    @staticmethod
    def from_agg(agg: Agg) -> 'TickerPrice':
        assert isinstance(agg, Agg)

        assert agg.timestamp is not None
        assert agg.open is not None
        assert agg.low is not None
        assert agg.high is not None
        assert agg.close is not None

        return TickerPrice(time=agg.timestamp // 1000, open=agg.open, low=agg.low, high=agg.high, close=agg.close)


class PolygonAPI():
    def __init__(self) -> None:
        # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        POLYGON_API_KEY = env("POLYGON_API_KEY")
        self.client = RESTClient(api_key=POLYGON_API_KEY)

    def get_financials(self, ticker: str) -> TickerFinancials:
        financials: Iterator[StockFinancial] | HTTPResponse = self.client.vx.list_stock_financials(
            ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        f = TickerFinancials()
        return f

    def get_news(self, ticker: str, max_items: int) -> list[TickerArticle]:
        """
        Returns a list of N annotated news articles (i.e. 'TickerArticle's)
        """
        news_generator: Iterator[TickerNews] | HTTPResponse = self.client.list_ticker_news(
            ticker=ticker, limit=1)
        articles = []

        for _ in range(max_items):
            n = news_generator.__next__()
            # We only get bytes if calling list_ticker_news with raw=True, so can assert TickerNews
            assert isinstance(n, TickerNews)

            assert isinstance(n.title, str)
            assert isinstance(n.article_url, str)
            assert isinstance(n.published_utc, str)

            desc = n.description if n.description else ""

            assert n.publisher is not None
            assert isinstance(n.publisher.name, str)

            article = TickerArticle(n.title, desc, n.article_url,
                                    n.published_utc, n.publisher.name)
            articles.append(article)

        return articles

    def recent_price(self, ticker: str) -> TickerPrice:
        # Set quite long, as trading closes on weekends, holidays etc
        from_ = datetime.utcnow() - timedelta(days=7)
        to = datetime.utcnow()
        aggs = self.client.get_aggs(
            ticker=ticker, multiplier=1, timespan="minute", from_=from_, to=to, sort=Sort.DESC, limit=1)

        assert not isinstance(aggs, HTTPResponse)

        return TickerPrice.from_agg(aggs[0])

    def price_history(self, ticker: str) -> List[TickerPrice]:
        from_ = datetime.utcnow() - timedelta(days=365*5)
        to = datetime.utcnow()
        aggs = self.client.get_aggs(
            ticker=ticker, multiplier=1, timespan="day", from_=from_, to=to, sort=Sort.ASC)

        assert not isinstance(aggs, HTTPResponse)

        prices = list(map(TickerPrice.from_agg, aggs))
        return prices


# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    news = api.get_news("AAPL", 10)
    for n in news:
        print(
            f"{n.score:.2f} || {n.publisher} - {n.title[:40]}... \n\t\t -> {n.url[:40]}...")
    print()
    prices = api.price_history("AAPL")
    for p in prices:
        print(f"{p.time} {p.low} {p.high}")
