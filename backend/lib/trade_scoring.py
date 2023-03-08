"""Takes a MakeTradeSchema and returns 3 values: evidence, controversy, financial risk"""
import math
import statistics
from typing import Literal
from models.models import StockModel
from lib.financials.scoring import Financials
from models.models import ArticleModel
from endpoints.trades.route import MakeTradeSchema
from lib.nlp.scoring import current_article_relevance, current_media_sentiment

def trade_score_evidence(text_evidence: str, article_evidence: list[str]) -> float:
    """
    Evidence score, on an arbitrary positive scale
    """

    # NO. SELECTED ARTICLES
    num_articles = len(article_evidence)
    num_articles_score = 1 - math.exp(-0.5 * num_articles) # Score between 0 and 1 (close to 1 at above 4)

    
    # RELEVANCE OF SELECTED ARTICLES
    relevance = 0.
    for id in article_evidence:
        article = ArticleModel.objects.get(article_id=id)
        relevance += (current_article_relevance(article) / num_articles)
    
    # USER PROVIDED EVIDENCE
    user_evidence_len = len(text_evidence)
    len_score = 1 - math.exp(-0.1 * user_evidence_len) # Score between 0 and 1 (close to 1 at above 25 chars)

    return (num_articles_score + relevance + len_score) / 3

def trade_score_controversy(ticker: str, buy: True) -> float:
    """
    Controversy score, between 0 and 1.
    0 is very uncontroversial, 1 is controversial
    """
    sentiment = current_media_sentiment(StockModel.objects.get(ticker=ticker))
    if buy:
        return (1 - sentiment)/2
    else:
        return abs(-1 - sentiment)/2


def trade_score_financial_risk(ticker: str) -> float:
    """
    Financial risk score, between 0 and 1
    """
    financials = Financials.create(ticker)

    # High financial score = low risk score
    return 1-financials.score