"""Takes a MakeTradeSchema and returns 3 values: evidence, controversy, financial risk"""

# class MakeTradeSchema(Schema):
#     ticker: str
#     side: Literal['BUY'] | Literal['SELL']
#     type: Literal['UNITS'] | Literal['PRICE']
#     amount: Decimal
#     text_evidence: str
#     article_evidence: List[str] (List of article_id)

import math
from typing import Literal
from lib.financials.scoring import normalise_financials_score
from models.models import ArticleModel
from endpoints.trades.route import MakeTradeSchema
from lib.nlp.scoring import current_article_relevance, current_media_sentiment

def trade_score_evidence(trade: MakeTradeSchema) -> float:
    """
    Evidence score, on an arbitrary positive scale

    """

    # NO. SELECTED ARTICLES
    num_articles = len(trade.article_evidence)
    num_articles_score = 1 - math.exp(-0.5 * num_articles) # Score between 0 and 1 (close to 1 at above 4)

    
    # RELEVANCE OF SELECTED ARTICLES
    relevance = 0
    for id in trade.article_evidence:
        article = ArticleModel.objects.get(article_id=id)
        relevance += (current_article_relevance(article) / num_articles)
    
    # USER PROVIDED EVIDENCE
    user_evidence_len = len(trade.text_evidence)
    len_score = 1 - math.exp(-0.1 * user_evidence_len) # Score between 0 and 1 (close to 1 at above 25 chars)

    return (num_articles_score + relevance + len_score) / 3

def trade_score_controversy(trade: MakeTradeSchema) -> float:
    """
    Controversy score, on an arbitrary positive scale
    """
    return 0

def trade_score_financial_risk(trade: MakeTradeSchema) -> float:
    """
    Financial risk score, on an arbitrary positive scale
    """
    financial_score = f(trade.ticker) # @Trevor - Give me the financial score of a ticker

    if (trade.side == Literal['BUY'] and financial_score >= 0.5) or (trade.side == Literal['SELL'] and financial_score < 0.5):
        # Good trade
        pass
    else:
        # Bad trade 
        pass
    return 0

def trade_score_overall(trade: MakeTradeSchema) -> tuple(int, int, int):
    """ 
    Returns a 3-tuple, (evidence, controversy, financial_risk)
    """
    return (trade_score_evidence(trade), trade_score_controversy(trade), trade_score_financial_risk(trade))


if __name__ == "__main__":
    pass