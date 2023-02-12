"""
Polygon API class to get stock financials and news articles
https://polygon.io/docs/stocks/
https://polygon-api-client.readthedocs.io/en/latest/index.html
"""
from polygon import RESTClient # type: ignore
import environ

class PolygonAPI():
    def __init__(self) -> None:
        env = environ.Env()
        # reading .env file
        environ.Env.read_env()

        # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        API_KEY = env("API_KEY")
        self.client = RESTClient(api_key=API_KEY) # type: ignore

    def get_financials(self, ticker: str) -> object:
        financials = self.client.vx.list_stock_financials(ticker=ticker, limit=1, timeframe="annual", include_sources=True)
        return financials
    
    def get_news(self, ticker: str) -> object:
        news = self.client.list_ticker_news(ticker=ticker, limit=1)
        return news  # use next(news) to iterate over

# Testing
if __name__ == "__main__":
    api = PolygonAPI()
    f = api.get_financials("AAPL")
    print(next(f))
