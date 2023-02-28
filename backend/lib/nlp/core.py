from textblob import TextBlob
from dataclasses import dataclass

from lib.polygon_api import TickerArticle


@dataclass
class AnalysisResult:
    """
    Objectivity ranges from 0 to 1.
    Sentiment is weighted by objectivity, and 
    """
    objectivity: float
    sentiment: float

    @staticmethod
    def from_text(text: str) -> 'AnalysisResult':
        t = TextBlob(text)

        objectivity = 1-t.subjectivity
        assert isinstance(objectivity, float)

        sentiment = t.polarity * objectivity
        assert isinstance(sentiment, float)

        return AnalysisResult(objectivity, sentiment)

    @staticmethod
    def from_article(article: TickerArticle) -> 'AnalysisResult':
        return AnalysisResult.from_text(" ".join([article.title, article.description]))
