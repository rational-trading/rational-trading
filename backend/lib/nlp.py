"""
Testing NLP libraries to perform sentiment analysis on financial news headlines/descriptions.
"""

from textblob import TextBlob
from lib.polygon_api import PolygonAPI, TickerArticle


def get_ticker_text_score(ticker: str) -> float:
    """
    Returns the overall text-based NLP score for a given ticker, as a float between 0 and 1,
    but more likely, a very small number (will need to normalise)
    """
    # Get the N most recent articles about this ticker
    N = 20
    polygon = PolygonAPI()
    articles = polygon.get_news(ticker=ticker, max_items=N)
    return sum([get_text_score(a) for a in articles])/N


def get_text_score(ta: TickerArticle) -> float:
    """
    Returns our text-based NLP score for a given article
    """
    t = TextBlob(" ".join([ta.title, ta.description]))
    score = t.polarity * t.subjectivity
    assert isinstance(score, float)
    return score


if __name__ == "__main__":
    text_score = get_ticker_text_score("AAPL")
    print(text_score)
