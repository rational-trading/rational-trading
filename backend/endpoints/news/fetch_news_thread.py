from models.models import StockModel, ArticleModel
from lib.polygon_api import PolygonAPI, normalise_scores
from time import sleep
from threading import Thread

WAIT_TIME_SECONDS = 600 
NUM_ARTICLES_TO_GET = 20

def main() -> None:
    t = Thread(target=fetch_task)
    t.start()

def fetch_task() -> None:
    while True:
        api = PolygonAPI()
        tickers = list(StockModel.objects.all()) # get supported tickers from database
        for t in tickers:
            news = normalise_scores(api.get_news(t.ticker, NUM_ARTICLES_TO_GET))
            
            for article in news:
                try:
                    ArticleModel.objects.get(article_id=article.article_id)
                except ArticleModel.DoesNotExist:
                    ArticleModel.objects.create(
                        article_id = article.article_id,
                        publisher = article.publisher,
                        url = article.url,
                        title = article.title,
                        description = article.description,
                        published = article.date,
                        stocks = [StockModel(t) for t in article.tickers],
                        objectivity = article.objectivity,
                        text_score = article.score
                    )
        sleep(WAIT_TIME_SECONDS)

if __name__ == "__main__":
    main()