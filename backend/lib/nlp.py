"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
Scroll to bottom to see usage and testing.
"""

from textblob import TextBlob


def get_text_score(text: str) -> float:
    """
    Returns our text-based NLP score for a given article, between -1 and 1,
    but more likely a very small number near 0
    """
    t = TextBlob(text)
    score = t.polarity * (1 - t.subjectivity)
    assert isinstance(score, float)
    return score
