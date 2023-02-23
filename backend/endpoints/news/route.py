from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest
from endpoints.auth import AuthBearer

from lib.polygon_api import PolygonAPI, normalise_scores

router = Router(auth=AuthBearer())

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
    authenticated_user: str

class AuthenticatedRequest(HttpRequest):
    auth: str

@router.get("/news/", response=NewsResponse)
def news(request: AuthenticatedRequest, ticker: str, n=20) -> NewsResponse:
    """
    /news/ticker=?n=? 
    Gets the n most recent articles about ticker, as a list of TickerArticles
    """
    api = PolygonAPI()
    news = normalise_scores(api.get_news(ticker, n))
    response = []
    for n in news:
        response.append(TickerArticleDataclass(n.title, n.description, n.url, n.date, n.publisher, n.score, n.tickers))
    return NewsResponse(news=response, authenticated_user=request.auth)

