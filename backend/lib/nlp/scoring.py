"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
Scroll to bottom to see usage and testing.
"""

import math
from django.utils import timezone

from models.models import ArticleModel, StockModel


def current_article_reputation(article: ArticleModel) -> float:
    """
    How much the article can be trusted, on an arbitrary positive scale.
    """
    return article.publisher.reputation * article.objectivity


def current_article_recency(article: ArticleModel) -> float:
    """
    Gives a score of 1 for the present, 0 for MAX_WEEKS_AGO, and a smooth curve between the values.
    """
    RECENCY_BIAS = 1.1  # negative means concave, positive means convex, 0 is straight line
    MAX_WEEKS_AGO = 52

    def f(x: float) -> float:
        return math.pow(x+1, 1-RECENCY_BIAS)

    w = max(
        0., (timezone.now() - article.published).seconds / (60 * 60 * 24 * 7))

    score = (f(w) - f(MAX_WEEKS_AGO)) / (f(0)-f(MAX_WEEKS_AGO))

    return max(score, 0)


def current_article_relevance(article: ArticleModel) -> float:
    """
    How relevant an article is, on an arbitrary positive scale determined by reputation and recency.
    """
    return current_article_reputation(article) * current_article_recency(article)


def current_article_impact(article: ArticleModel) -> float:
    """
    Define the "impact" of an article on the overall sentiment, weighted by article sentiment and relevance.
    """
    return article.normalised_sentiment * current_article_relevance(article)


def current_media_sentiment(stock: StockModel) -> float:
    """
    Returns the current media sentiment for a stock between -1 and 1, weighted on reputation, recency, and sentiment.
    """
    articles = list(ArticleModel.objects.filter(
        stocks__in=[stock]).order_by('-published'))

    # weight article sentiments by relevance and publisher
    total_impact = sum([
        current_article_impact(article) for article in articles])
    total_relevance = sum([current_article_relevance(article)
                           for article in articles])

    return total_impact / total_relevance
