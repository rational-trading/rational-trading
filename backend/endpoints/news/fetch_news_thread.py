from datetime import datetime
from typing import Optional
from time import sleep
from threading import Thread
import pytz

from lib.nlp.precompute import NormalisedAnalysisResult
from models.models import StockModel, ArticleModel, PublisherModel
from lib.polygon_api import PolygonAPI

WAIT_TIME_SECONDS = 60
NUM_ARTICLES_TO_GET = 20

started = False


def start_background_thread() -> None:
    global started
    if not started:
        started = True
        t = Thread(target=fetch_task)
        t.start()


def fetch_task() -> None:
    while True:
        print("Fetching news sources...")

        api = PolygonAPI()
        # get supported tickers from database
        tickers = list(StockModel.objects.all())
        for t in tickers:
            news = api.get_news(
                t.ticker, NUM_ARTICLES_TO_GET)

            for article in news:
                try:
                    publisher = PublisherModel.objects.get(
                        name=article.publisher)
                except PublisherModel.DoesNotExist:
                    publisher = PublisherModel.create_typed(
                        name=article.publisher, reputation=1.)
                try:
                    ArticleModel.objects.get(article_id=article.article_id)
                except ArticleModel.DoesNotExist:
                    def try_get_stock(ticker: str) -> Optional[StockModel]:
                        try:
                            return StockModel.objects.get(ticker=ticker)
                        except StockModel.DoesNotExist:
                            return None

                    optional_stocks = [try_get_stock(ticker)
                                       for ticker in article.tickers]
                    stocks = [
                        stock for stock in optional_stocks if stock is not None]

                    nlp_result = NormalisedAnalysisResult.from_article(article)

                    ArticleModel.create_typed(
                        article_id=article.article_id,
                        publisher=publisher,
                        url=article.url,
                        title=article.title,
                        description=article.description,
                        published=datetime.strptime(
                            article.date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.UTC),  # article.date
                        stocks=stocks,
                        objectivity=nlp_result.objectivity,
                        normalised_sentiment=nlp_result.normalised_sentiment
                    )
        print("Completed fetching.")
        sleep(WAIT_TIME_SECONDS)
