"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
Scroll to bottom to see usage and testing.
"""

from textblob import TextBlob
from lib.polygon_api import PolygonAPI, TickerArticle

def get_text_score(tickerArticle: TickerArticle) -> float:
    """
    Returns our text-based NLP score for a given article, between -1 and 1,
    but more likely a very small number near 0
    """
    t = TextBlob(" ".join([tickerArticle.title, tickerArticle.description]))
    score = t.polarity * t.subjectivity
    assert isinstance(score, float)
    return score