"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from http.client import HTTPResponse
from typing import Iterator, Optional
from polygon import RESTClient
from polygon.rest.models import StockFinancial
from polygon.rest.models import TickerNews

from config.env import env

from lib.nlp import get_text_score


class TickerArticle():
    def __init__(self, title: str, description: str, url: str, date: str, publisher: str, tickers: list[str]) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.date = date
        self.publisher = publisher
        self.score = get_text_score(" ".join([title, description]))
        self.tickers = tickers

    def __repr__(self) -> str:
        return f"{self.score:>6.3f} || {self.publisher[:8]:<8}... {self.title[:40]}..."


class TickerFinancials():
    def __init__(self) -> None:
        # Simon: add in relevant fields @Trevor
        pass


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
            assert n.tickers is not None

            article = TickerArticle(n.title, desc, n.article_url,
                                    n.published_utc, n.publisher.name, n.tickers)
            articles.append(article)
        
        return articles

    def get_recent_news(self, N: int, tickers: list[str]) -> list[TickerArticle]:
        """
        Gets the N most recent news articles that talk about any of the stocks in tickers
        """
        news_generator: Iterator[TickerNews] | HTTPResponse = self.client.list_ticker_news(sort="published_utc")
        articles: list[TickerArticle] = []

        while len(articles) < N:
            n = news_generator.__next__()
            # We only get bytes if calling list_ticker_news with raw=True, so can assert TickerNews
            assert isinstance(n, TickerNews)
            
            assert n.tickers is not None
            if len(set(n.tickers).intersection(set(tickers))) == 0:
                continue
            assert isinstance(n.title, str)
            assert isinstance(n.article_url, str)
            assert isinstance(n.published_utc, str)
            desc = n.description if n.description else ""
            assert n.publisher is not None
            assert isinstance(n.publisher.name, str)

            article = TickerArticle(n.title, desc, n.article_url,
                                    n.published_utc, n.publisher.name, n.tickers)
            articles.append(article)

            print(f"{len(articles)} articles collected.")
        return articles


# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    news = api.get_news("AAPL", 10)
    for n in news:
        print(f"{n.score:.2f} || {n.publisher} - {n.title[:40]}... \n\t\t -> {n.url[:40]}...")
