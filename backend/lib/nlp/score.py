"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
Scroll to bottom to see usage and testing.
"""

from django.utils import timezone

from models.models import ArticleModel, StockModel


def calculate_ticker_sentiment(ticker: str) -> float:
    stock = StockModel.objects.get(ticker=ticker)
    articles = ArticleModel.objects.filter(
        stocks__in=[stock]).order_by('-published')
    weeks_ago = [(timezone.now() - article.published).days / 7
                 for article in articles]

    # weight sentiments by 1/weeks ago
    weights = [1/min(1., weeks) for weeks in weeks_ago]
    normalised_sentiments = [
        article.normalised_sentiment for article in articles]
    weighted_average = sum(
        [w * s for (w, s) in zip(weights, normalised_sentiments)]) / sum(weights)

    return weighted_average
