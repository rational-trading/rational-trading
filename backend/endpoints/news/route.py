from dataclasses import dataclass
from ninja import Router
from django.http.request import HttpRequest

from lib.polygon_api import PolygonAPI, normalise_scores

router = Router()

@dataclass
class TickerArticleDataclass:
    title: str
    description: str
    url: str
    date: str
    publisher: str
    score: float
    tickers: list[str]

@dataclass
class NewsResponse:
    news: list[TickerArticleDataclass]

@router.get("/news/", response=NewsResponse)
def news(request: HttpRequest, ticker: str, n=20) -> NewsResponse:
    """
    Gets the list of the n most recent articles about ticker
    """
    api = PolygonAPI()
    news = normalise_scores(api.get_news(ticker, n))
    response = []
    for n in news:
        response.append(TickerArticleDataclass(n.title, n.description, n.url, n.date, n.publisher, n.score, n.tickers))
    return NewsResponse(news=response)

