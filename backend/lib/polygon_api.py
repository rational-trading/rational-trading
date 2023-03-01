"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
import pickle
from dataclasses import dataclass
from datetime import datetime, timedelta
from http.client import HTTPResponse
from typing import Iterator, List
from polygon import RESTClient

from polygon.rest.models import Sort, TickerNews, Agg

from config.env import env
from lib.nlp import get_text_score
from lib.utils import guardNone


class TickerDividend():
    def __init__(self, cash_amount: float) -> None:
        self.cash_amount = cash_amount


@dataclass
class TickerFinancials():

    # in this class, we provide:
    # BS:
    equity: float
    current_assets: float
    current_liabilities: float
    nc_liabilities: float

    # IS:
    revenues: float
    # basic_earnings_per_share in IS:
    basic_earnings_per_share: float


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
        return f"{self.score:>6.3f} | {self.date[5:7]}/{self.date[8:10]} {self.date[11:16]} | {self.publisher[:8]:<8}... {self.title[:40]}..."


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


@dataclass
class TickerDetails():
    ticker: str
    company_name: str
    exchange: str


class PolygonAPI():
    def __init__(self) -> None:
        # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        POLYGON_API_KEY = env("POLYGON_API_KEY")
        self.client = RESTClient(api_key=POLYGON_API_KEY)

    def get_ticker_details(self, ticker: str) -> TickerDetails:
        ticker_details = self.client.get_ticker_details(ticker)
        return TickerDetails(ticker=ticker_details.ticker, company_name=ticker_details.name, exchange=ticker_details.primary_exchange)

    def get_dividend(self, ticker: str) -> TickerDividend:
        dividends = self.client.list_dividends(
            ticker=ticker, limit=1)
        assert not isinstance(dividends, HTTPResponse)

        cash_amount = next(dividends).cash_amount
        assert isinstance(cash_amount, float)

        f = TickerDividend(cash_amount)
        return f

    def get_financials(self, ticker: str) -> TickerFinancials:
        financials = self.client.vx.list_stock_financials(
            ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        assert not isinstance(financials, HTTPResponse)

        latest = next(financials).financials
        assert latest is not None

        assert latest.balance_sheet is not None
        assert latest.income_statement is not None

        f = TickerFinancials(
            equity=guardNone(
                latest.balance_sheet["equity"].value),
            current_assets=guardNone(
                latest.balance_sheet["current_assets"].value),
            current_liabilities=guardNone(
                latest.balance_sheet["current_liabilities"].value),
            nc_liabilities=guardNone(
                latest.balance_sheet["noncurrent_liabilities"].value),
            revenues=guardNone(guardNone(
                latest.income_statement.revenues).value),
            basic_earnings_per_share=guardNone(guardNone(
                latest.income_statement.basic_earnings_per_share).value)

        )
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
        news_generator: Iterator[TickerNews] | HTTPResponse = self.client.list_ticker_news(
            sort="published_utc")
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


def normalise_scores(articles: list[TickerArticle]) -> list[TickerArticle]:
    f = open("lib/precomputed_result", "rb")
    pre = pickle.load(f)
    f.close()
    ret = articles.copy()

    def rank(article: TickerArticle) -> float:
        # Normalises a singular article
        # Naive linear scan
        for i, rank_score in enumerate(pre):
            if article.score < rank_score:
                return i/len(pre)
        return 1

    for article in ret:
        article.score = rank(article)

    return ret


# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    # news = api.get_news("AAPL", 10)
    # for n in news:
    #    print(
    #        f"{n.score:.2f} || {n.publisher} - {n.title[:40]}... \n\t\t -> {n.url[:40]}...")
    # print()
    p = list.pop(api.price_history("AAPL"))
    print(f"{p.time} {p.low} {p.high}")
    # print(api.get_financials("AAPL"))
