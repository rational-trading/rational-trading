from lib.polygon_api import PolygonAPI

def main() -> None:
    tickers = ["AAPL", "MSFT", "AMZN,", "NVDA", "GOOGL", "TSLA", "BRK.B", "GOOG", "XOM", "UNH", "JNJ", "JPM", "META", "V", "PG", "HD", "MA", "CVX", "MRK", "LLY"]
    p = PolygonAPI()
    N = 10
    articles = p.get_recent_news(N, tickers)
    print("By published date:")
    for a in articles:
        print(a)
    articles.sort(key=lambda x: x.score, reverse=True)
    print("By NLP score:")
    for a in articles:
        print(a)

if __name__ == "__main__":
    main()