from models.models import StockModel, ArticleModel
from lib.polygon_api import PolygonAPI, normalise_scores
from time import sleep
from threading import Thread

WAIT_TIME_SECONDS = 600 
NUM_ARTICLES_TO_GET = 20

def main():
    t = Thread(target=fetch_task)
    t.start()

def fetch_task():
    while True():
        api = PolygonAPI()
        tickers = StockModel.objects.all() # get supported tickers from database
        for t in tickers:
            news = normalise_scores(api.get_news(t.ticker, NUM_ARTICLES_TO_GET))
            for article in news:
                entry = ArticleModel()
                entry.article_id = article.article_id
                entry.publisher = article.publisher
                entry.url = article.url
                entry.title = article.title
                entry.description = article.description
                entry.published = article.date
                entry.stocks = article.tickers
                entry.objectivity - article.objectivity
                ArticleModel.objects.get_or_create(entry)
        sleep(WAIT_TIME_SECONDS)

if __name__ == "__main__":
    main()