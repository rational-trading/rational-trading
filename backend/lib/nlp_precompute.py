from lib.polygon_api import PolygonAPI, TickerArticle

import pickle


def precompute(N: int = 10) -> list[float]:
    tickers = ["AAPL", "MSFT", "AMZN,", "NVDA", "GOOGL", "TSLA", "BRK.B", "GOOG",
               "XOM", "UNH", "JNJ", "JPM", "META", "V", "PG", "HD", "MA", "CVX", "MRK", "LLY"]
    p = PolygonAPI()
    articles = p.get_recent_news(N, tickers)
    articles.sort(key=lambda x: x.score)
    return list(map(lambda x: x.score, articles))


def final_nlp_score(ticker: str) -> float:
    api = PolygonAPI()
    N = 20  # Number of news articles to base NLP score off
    news = api.get_news(ticker, N)
    nlp_score = sum(
        map(lambda x: x.score, normalise_nlp_scores(news)))/len(news)
    return nlp_score


def normalise_nlp_scores(articles: list[TickerArticle]) -> list[TickerArticle]:
    f = open("lib/precomputed_result", "rb")
    pre = pickle.load(f)
    f.close()
    ret = articles.copy()

    def rank(article: TickerArticle) -> float:
        # Normalises a singular article
        # Naive linear scan
        for i, rank_score in enumerate(pre):
            if article.score < rank_score:
                return i/len(pre)
        return 1

    for article in ret:
        article.score = rank(article)

    return ret


if __name__ == "__main__":
    pre = precompute(100)
    with open("lib/precomputed_result", 'wb') as f:
        pickle.dump(pre, f)
    print("Precomputed list dumped to file: lib/precomputed_result")

    api = PolygonAPI()
    news = normalise_nlp_scores(api.get_news("AAPL", 10))
    print("List of TickerArticles, with normalised scores:")
    for a in news:
        print(a)
