from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest
from models.models import ArticleModel

router = Router()


class ArticleSchema(Schema):
    article_id: str
    publisher: str
    url: str
    title: str
    description: str
    date: int
    tickers: list[str]
    objectivity: float
    text_score: float

    @staticmethod
    def from_model(model: ArticleModel) -> 'ArticleSchema':
        return ArticleSchema(
            article_id=model.article_id,
            publisher=model.publisher.name,
            url=model.url,
            title=model.title,
            description=model.description,
            date=model.published.timestamp(),
            tickers=[stock.ticker for stock in model.stocks.all()],
            objectivity=model.objectivity,
            text_score=model.text_score)


@router.get("/news/", response=list[ArticleSchema])
def news(request: HttpRequest, ticker: str, n: int = 20) -> list[ArticleSchema]:
    """
    Gets the list of the n most objective articles about ticker.
    """
    articles = list(ArticleModel.objects.filter(
        stocks__in=[ticker]))  # get articles from database

    # get all articles from database, but only return n most objective
    articles.sort(key=lambda x: x.objectivity, reverse=True)

    return [ArticleSchema.from_model(article) for article in articles[:n]]
