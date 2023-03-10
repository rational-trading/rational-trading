"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from http.client import HTTPResponse
from typing import Generator, Iterator, List
from polygon import RESTClient
from polygon.rest.models import Sort, TickerNews, Agg, Order, PreviousCloseAgg

from config.env import env
from lib.exceptions import FriendlyClientException
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


@dataclass
class TickerArticle():
    article_id: str
    title: str
    description: str
    url: str
    date: str
    publisher: str
    tickers: list[str]


@dataclass
class TickerPrice():
    time: int
    open: float
    low: float
    high: float
    close: float

    @staticmethod
    def from_agg(agg: Agg | PreviousCloseAgg) -> 'TickerPrice':
        assert agg.timestamp is not None
        assert agg.open is not None
        assert agg.low is not None
        assert agg.high is not None
        assert agg.close is not None

        return TickerPrice(time=int(agg.timestamp) // 1000, open=agg.open, low=agg.low, high=agg.high, close=agg.close)


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

        assert isinstance(ticker_details.ticker, str)
        assert isinstance(ticker_details.name, str)
        assert isinstance(ticker_details.primary_exchange, str)

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

        try:
            latest = next(financials).financials
        except Exception as e:
            raise FriendlyClientException("Financials not found!")

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

    def get_recent_news(self, ticker: str, max_items: int) -> Generator[TickerArticle, None, None]:
        """
        Returns a generator that yeilds at most "max_items" `TickerArticle`s.
        """
        news_generator: Iterator[TickerNews] | HTTPResponse = self.client.list_ticker_news(
            ticker=ticker,
            sort="published_utc", limit=max_items, order=Order.DESC)

        for _ in range(max_items):
            n = news_generator.__next__()
            # We only get bytes if calling list_ticker_news with raw=True, so can assert TickerNews
            assert isinstance(n, TickerNews)
            assert isinstance(n.id, str)
            assert isinstance(n.title, str)
            assert isinstance(n.article_url, str)
            assert isinstance(n.published_utc, str)
            desc = n.description if n.description else ""
            assert n.publisher is not None
            assert isinstance(n.publisher.name, str)
            assert n.tickers is not None

            article = TickerArticle(article_id=n.id, title=n.title, description=desc, url=n.article_url,
                                    date=n.published_utc, publisher=n.publisher.name, tickers=n.tickers)
            yield article

    def search_all_recent_news(self, N: int, tickers: list[str]) -> list[TickerArticle]:
        """
        Searches for the N most recent news articles that talk about any of the stocks in tickers
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
            assert isinstance(n.id, str)
            assert isinstance(n.title, str)
            assert isinstance(n.article_url, str)
            assert isinstance(n.published_utc, str)
            desc = n.description if n.description else ""
            assert n.publisher is not None
            assert isinstance(n.publisher.name, str)

            article = TickerArticle(article_id=n.id, title=n.title, description=desc, url=n.article_url,
                                    date=n.published_utc, publisher=n.publisher.name, tickers=n.tickers)
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

    def previous_daily_price(self, ticker: str) -> TickerPrice:
        # The library type annotations are actually wrong for this function!
        aggs: List[PreviousCloseAgg] | HTTPResponse = self.client.get_previous_close_agg(
            ticker)  # type: ignore
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
    # news = api.get_news("AAPL", 10)
    # for n in news:
    #    print(
    #        f"{n.score:.2f} || {n.publisher} - {n.title[:40]}... \n\t\t -> {n.url[:40]}...")
    # print()
    p = list.pop(api.price_history("AAPL"))
    print(f"{p.time} {p.low} {p.high}")
    # print(api.get_financials("AAPL"))
