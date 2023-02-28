from dataclasses import dataclass
import pickle
from typing import List

from .core import AnalysisResult
from lib.polygon_api import PolygonAPI, TickerArticle


with open("lib/nlp/precomputed_result", "rb") as f:
    precomputed_dist: List[float] = pickle.load(f)


@dataclass
class NormalisedAnalysisResult:
    objectivity: float
    normalised_sentiment: float

    @staticmethod
    def from_article(article: TickerArticle) -> 'NormalisedAnalysisResult':
        result = AnalysisResult.from_article(article)
        num_smaller_samples = len(
            [sample for sample in precomputed_dist if result.sentiment > sample])
        normalised_sentiment = 2 * \
            (num_smaller_samples / len(precomputed_dist)) - 1
        return NormalisedAnalysisResult(result.objectivity, normalised_sentiment)


def precompute(N: int = 10) -> list[float]:
    tickers = ["AAPL", "MSFT", "AMZN,", "NVDA", "GOOGL", "TSLA", "BRK.B", "GOOG",
               "XOM", "UNH", "JNJ", "JPM", "META", "V", "PG", "HD", "MA", "CVX", "MRK", "LLY"]
    p = PolygonAPI()
    articles = p.get_recent_news(N, tickers)
    sentiments = [AnalysisResult.from_article(
        article).sentiment for article in articles]
    return list(sentiments)


if __name__ == "__main__":
    pre = precompute(100)
    with open("lib/nlp/precomputed_result", 'wb') as fw:
        pickle.dump(pre, fw)
    print("Precomputed list dumped to file: lib/precomputed_result")

    api = PolygonAPI()
    news = api.get_news("AAPL", 10)
    print("List of TickerArticles, with normalised scores:")
    for a in news:
        print(NormalisedAnalysisResult.from_article(a).normalised_sentiment)
