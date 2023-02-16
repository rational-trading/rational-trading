from lib.polygon_api import PolygonAPI

def main() -> None:
    tickers = ["AAPL", "MSFT", "AMZN,", "NVDA", "GOOGL", "TSLA", "BRK.B", "GOOG", "XOM", "UNH", "JNJ", "JPM", "META", "V", "PG", "HD", "MA", "CVX", "MRK", "LLY"]
    p = PolygonAPI()
    N = 20
    articles = p.get_recent_news(N, tickers)
    articles.sort(key=lambda x: x.score, reverse=True)
    for a in articles:
        print(a)

if __name__ == "__main__":
    main()