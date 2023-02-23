from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest

from endpoints.auth import AuthBearer

from lib.polygon_api import PolygonAPI, TickerArticle

router = Router(auth=AuthBearer())

class NewsResponseSchema(Schema):
    news: list[TickerArticle]
    authenticated_user: str

@dataclass
class NewsResponse:
    news: list[TickerArticle]
    authenticated_user: str

class AuthenticatedRequest(HttpRequest):
    auth: str

@router.get("/news/}", response=NewsResponseSchema)
def news(request: AuthenticatedRequest, ticker: str = "AAPL", n=20) -> NewsResponse:
    """
    /news/ticker=?n=? 
    Gets the n most recent articles about ticker, as a list of TickerArticles
    """
    api = PolygonAPI()
    news = api.get_news(ticker, n)
    return NewsResponse(news=news, authenticated_user=request.auth)

