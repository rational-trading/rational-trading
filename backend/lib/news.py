"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
"""

from textblob import TextBlob
from lib.polygon_api import PolygonAPI, TickerArticle

def get_news(ticker: str, N: int) -> list[TickerArticle]:
    """
    Returns a list of N annotated news articles (i.e. TickerArticle.score)
    """
    poly = PolygonAPI()
    news = poly.get_news(ticker=ticker, max_items=N)
    for ta in news:
        ta.score = get_text_score(ta)
    return news


def get_text_score(ta: TickerArticle) -> float:
    """
    Returns our text-based NLP score for a given article, between -1 and 1,
    but more likely a very small number near 0
    """
    t = TextBlob(" ".join([ta.title, ta.description]))
    score = t.polarity * t.subjectivity
    assert isinstance(score, float)
    return score


if __name__ == "__main__":
    news = get_news("AAPL", 10)
    for n in news:
        print(f"{n.score} + {n.title}")
