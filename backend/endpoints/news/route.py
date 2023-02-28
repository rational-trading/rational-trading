from ninja import Router, Schema
from django.http.request import HttpRequest
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
    tickers: list[str]
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


@router.get("/news", response=list[ArticleSchema])
def news(request: HttpRequest, ticker: str, n: int = 20) -> list[ArticleSchema]:
    """
    Gets the list of the n most objective articles about ticker.
    """
    articles = list(ArticleModel.objects.filter(
        stocks__in=[ticker]))  # get articles from database

    # get all articles from database, but only return n most relevant
    articles.sort(key=lambda x: current_article_relevance(x), reverse=True)

    return [ArticleSchema.from_model(article) for article in articles[:n]]
