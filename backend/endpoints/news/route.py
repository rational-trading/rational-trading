from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest
from models.models import ArticleModel

from lib.polygon_api import PolygonAPI, normalise_scores

router = Router()

class ArticleSchema(Schema):
    title: str
    description: str
    url: str
    date: str
    publisher: str
    score: float
    tickers: list[str]

    @staticmethod
    def from_model(model: ArticleModel) -> 'ArticleSchema':
        return ArticleSchema(
            title = model.title,
            description = model.description,
            url = model.url,
            date = model.published,
            publisher = model.publisher,
            tickers = model.stocks)
    
@dataclass
class TickerArticleDataclass:
    title: str
    description: str
    url: str
    date: str
    publisher: str
    score: float
    tickers: list[str]

@router.get("/news/", response=list[ArticleSchema])
def news(request: HttpRequest, ticker: str, n:int=20, sort:str="recent") -> list[ArticleSchema]:
    """
    Gets the list of the n most recent articles about ticker.
    """
    articles = ArticleModel.objects.filter(stocks=ticker) # get articles from database

    if sort == "recent":
        # todo: return sorted list by recency
        return []
    elif sort == "objectivity":
        # todo: return sorted list by objectivity
        return []
    
    # Simon - currently trying to understand how to interact with database system
    return [ArticleSchema.from_model(article) for article in articles]



