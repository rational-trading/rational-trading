
from typing import List
import lib.numerical_scoring
import lib.numerical_precompute

from lib.polygon_api import PolygonAPI, normalise_scores


def normalised_numerical_scoring(ticker: str, numerical_pre_results: List[float]) -> float:
    result = lib.numerical_scoring.get_financial_endpoints(ticker)["score"]
    score = 0.
    for x in numerical_pre_results:
        if result > x:
            score += 0.02
    return score

def final_numerical_rank(ticker: str) -> float:
    numerical_rank = normalised_numerical_scoring(
        ticker, lib.numerical_precompute.numerical_results)
    return numerical_rank

def final_nlp_score(ticker: str) -> float:
    api = PolygonAPI()
    N = 20  # Number of news articles to base NLP score off
    nlp_score = sum(
        map(lambda x: x.score, normalise_scores(api.get_news(ticker, N))))/N
    return nlp_score
