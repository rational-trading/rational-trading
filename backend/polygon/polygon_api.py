"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs/stocks/
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from polygon import RESTClient # type: ignore
import environ

class TickerArticle():
    def __init__(self, title: str, description: str, url: str, published: str) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.published = published
    
    def __repr__(self) -> str:
        return (f"TickerArticle Object ({self.title[:20]}...)")

class TickerFinancials():
    def __init__(self) -> None:
        # Simon: add in relevant fields @Trevor
        pass

class PolygonAPI():
    def __init__(self) -> None:
        env = environ.Env()
        # reading .env file
        environ.Env.read_env()

        # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        API_KEY = env("API_KEY")
        self.client = RESTClient(api_key=API_KEY) # type: ignore

    def get_financials(self, ticker: str) -> TickerFinancials:
        financials = self.client.vx.list_stock_financials(ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        f = TickerFinancials()
        return f
    
    def get_news(self, ticker: str, max_items: int) -> list[TickerArticle]:
        news = self.client.list_ticker_news(ticker=ticker, limit=1)
        ret = []
        for _ in range(max_items):
            n= next(news)
            t = TickerArticle(n.title, n.description, n.article_url, n.published_utc)
            ret.append(t)
        return ret

# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    n = api.get_news("AAPL", 1)
    print(n)
