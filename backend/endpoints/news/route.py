from typing import List
from ninja import Query, Router, Schema
from django.http.request import HttpRequest
from pydantic import conlist
from lib.exceptions import FriendlyClientException
from lib.nlp.scoring import current_article_recency, current_article_relevance, current_article_reputation
from models.models import ArticleModel

router = Router()


class ArticleSchema(Schema):
    article_id: str
    publisher: str
    url: str
    title: str
    description: str
    date: int
    tickers: List[str]
    normalised_sentiment: float
    reputation: float
    recency: float

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
            normalised_sentiment=model.normalised_sentiment,
            reputation=current_article_reputation(model),
            recency=current_article_recency(model))


@router.get("/about", response=List[ArticleSchema])
def about_ticker(request: HttpRequest, ticker: str, n: int = 20) -> List[ArticleSchema]:
    """
    Gets the list of the n most objective articles about ticker.
    """
    articles = list(ArticleModel.objects.filter(
        stocks__in=[ticker]))  # get articles from database

    # get all articles from database, but only return n most relevant
    articles.sort(key=lambda x: current_article_relevance(x), reverse=True)

    return [ArticleSchema.from_model(article) for article in articles[:n]]


@router.get("/articles", response=List[ArticleSchema])
def articles(request: HttpRequest, article_ids: List[str] = Query([])) -> List[ArticleSchema]:
    articles = ArticleModel.objects.filter(article_id__in=article_ids)
    print([ArticleSchema.from_model(model) for model in articles])
    return [ArticleSchema.from_model(model) for model in articles]
