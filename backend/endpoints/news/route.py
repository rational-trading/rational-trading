from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest
from models.models import ArticleModel

from lib.polygon_api import PolygonAPI, normalise_scores

router = Router()

class ArticleSchema(Schema):
    article_id: str 
    publisher: str
    url: str
    title: str
    description: str
    date: str
    tickers: list[str]
    objectivity: float
    text_score: float

    @staticmethod
    def from_model(model: ArticleModel) -> 'ArticleSchema':
        return ArticleSchema(
            article_id = model.article_id,
            publisher = model.publisher,
            url = model.url,
            title = model.title,
            description = model.description,
            date = model.published,
            tickers = model.stocks,
            objectivity = model.objectivity,
            text_score = model.text_score)
    

# What's this used for?
@dataclass
class ArticleDataclass:
    article_id: str 
    publisher: str
    url: str
    title: str
    description: str
    date: str
    tickers: list[str]
    objectivity: float
    text_score: float

@router.get("/news/", response=list[ArticleSchema])
def news(request: HttpRequest, ticker: str, n:int=20) -> list[ArticleSchema]:
    """
    Gets the list of the n most recent articles about ticker.
    """
    articles = list(ArticleModel.objects.filter(stocks__in=[ticker])) # get articles from database

    # get all articles from database, but only return n most objective
    articles.sort(key=lambda x: x.objectivity, reverse=True)

    return [ArticleSchema.from_model(article) for article in articles[:n]]



