"""
Gets annotated news articles for stocks. Uses TextBlob to perform sentiment analysis.
Scroll to bottom to see usage and testing.
"""

import math
from django.utils import timezone
from scipy.stats import norm
import numpy as np

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

    weights = np.array([current_article_relevance(article)
                       for article in articles])
    weights /= np.sum(weights)

    impact = np.array([article.normalised_sentiment for article in articles])

    weighted_average = np.sum(impact * weights)

    # Here we estimate the number of samples that contributed to the average. For example, [0, 0.5, 0.5] should give 2, [0.333, 0.333, 0.333] should give 3, and [0.2, 0.4, 0.4] should give somewhere in between 2 and 3. For reference, see when q=1 on https://en.wikipedia.org/wiki/Diversity_index
    effective_samples = math.exp(-np.sum(weights *
                                 np.log(weights + 0.0000001)))

    # This is the std_dev of the normal distribution approximating the average of n samples from U(-1, 1). We use effective_n instead of the actual n.
    std_dev = np.sqrt(1 / (3 * effective_samples))

    left_cdf = norm.cdf(-1, loc=0, scale=std_dev)
    right_cdf = norm.cdf(1, loc=0, scale=std_dev)
    missed = 1 - (right_cdf - left_cdf)

    # uniformly distributed the x < -1 and 1 < x parts of the cdf
    normalised = norm.cdf(weighted_average, loc=0, scale=std_dev) - \
        left_cdf + missed * (weighted_average+1)/2

    assert isinstance(normalised, float)

    # Have visualised with matplotlib and it seems to work shockingly well for any effective_n over around 3

    return 2 * normalised - 1
