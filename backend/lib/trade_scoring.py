"""Takes a MakeTradeSchema and returns 3 values: evidence, controversy, financial risk"""
from datetime import datetime
from decimal import Decimal
import math
from typing import List
from models.models import StockModel, TradeModel, UserModel
from lib.financials.scoring import Financials
from models.models import ArticleModel
from lib.nlp.scoring import current_article_relevance, current_media_sentiment


def trade_score_evidence(text_evidence: str, article_evidence: list[ArticleModel]) -> float:
    """
    Evidence score, on an arbitrary positive scale
    """

    # NO. SELECTED ARTICLES
    num_articles = len(article_evidence)
    # Score between 0 and 1 (close to 1 at above 4)
    num_articles_score = 1 - math.exp(-0.5 * num_articles)

    # RELEVANCE OF SELECTED ARTICLES
    relevance = 0.
    for article in article_evidence:
        relevance += (current_article_relevance(article) / num_articles)

    # USER PROVIDED EVIDENCE
    user_evidence_len = len(text_evidence)
    # Score between 0 and 1 (close to 1 at above 25 chars)
    len_score = 1 - math.exp(-0.1 * user_evidence_len)

    return (num_articles_score + relevance + len_score) / 3


def trade_score_controversy(ticker: str, buy: bool) -> float:
    """
    Controversy score, between 0 and 1.
    0 is very uncontroversial, 1 is controversial
    """
    sentiment = current_media_sentiment(StockModel.objects.get(ticker=ticker))
    if buy:
        return (1 - sentiment)/2
    else:
        return (1 + sentiment)/2


def trade_score_financial_risk(ticker: str, buy: bool) -> float:
    """
    Financial risk score, between 0 and 1
    """
    financials = Financials.create(ticker)
    """
    Low numerical score => Low RISK for sell, High RISK for buy
        1 - numerical score = High risk score (correct for buy)
        numerical score = Low risk score (correct for sell)
    
    High numerical score => High RISK for sell, Low RISK for buy
        1 - numerical score = Low risk score (correct for buy)
        numerical score = High risk score (correct for sell)
    """
    return 1-financials.score if buy else financials.score


def create_trade(user: UserModel, stock: StockModel, units_change: Decimal, balance_change: Decimal, time: datetime, text_evidence: str, article_evidence: List[ArticleModel]) -> TradeModel:
    trade = TradeModel.objects.create(
        user=user,
        stock=stock,
        units_change=units_change,
        balance_change=balance_change,
        time=time,
        text_evidence=text_evidence,
        controversy=trade_score_controversy(stock.ticker, buy=units_change > 0), evidence=trade_score_evidence(text_evidence, article_evidence),
        financial_risk=trade_score_financial_risk(stock.ticker, buy=units_change > 0))

    trade.article_evidence.set(article_evidence)
    return trade
