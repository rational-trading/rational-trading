from lib.polygon_api import PolygonAPI, normalise

import pickle

def precompute(N: int = 10) -> list[float]:
    tickers = ["AAPL", "MSFT", "AMZN,", "NVDA", "GOOGL", "TSLA", "BRK.B", "GOOG", "XOM", "UNH", "JNJ", "JPM", "META", "V", "PG", "HD", "MA", "CVX", "MRK", "LLY"]
    p = PolygonAPI()
    articles = p.get_recent_news(N, tickers)
    articles.sort(key=lambda x: x.score)
    return list(map(lambda x: x.score, articles))

if __name__ == "__main__":
    pre = precompute(100)
    with open("lib/precomputed_result", 'wb') as f:
        pickle.dump(pre, f)
    print("Precomputed list dumped to file: lib/precomputed_result")

    api = PolygonAPI()
    news = normalise(api.get_news("AAPL", 10))
    print("List of TickerArticles, with normalised scores:")
    for a in news:
        print(a)