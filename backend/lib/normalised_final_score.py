
from typing import List
import lib.scoring
import lib.numerical_precompute

from lib.polygon_api import PolygonAPI, normalise_scores


def normalised_numerical_scoring(ticker: str, numerical_pre_results: List[float]) -> float:
    result = lib.scoring.numerical_scoring(ticker)
    score = 0.
    for x in numerical_pre_results:
        if result > x:
            score += 0.02
    return score


def final_scoring(ticker: str) -> float:
    numerical_score = normalised_numerical_scoring(
        ticker, lib.numerical_precompute.numerical_results)
    api = PolygonAPI()

    N = 20  # Number of news articles to base NLP score off
    nlp_score = sum(
        map(lambda x: x.score, normalise_scores(api.get_news(ticker, N))))/N
    return 0.5 * numerical_score + 0.5 * nlp_score

