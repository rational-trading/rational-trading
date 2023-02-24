from datetime import datetime
from decimal import Decimal
from typing import List
from django.db import models
from django.db.models import Model


class UserModel(Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=11, decimal_places=2)

    @staticmethod
    def create_typed(username: str, password: str, balance: float) -> 'UserModel':
        return UserModel.objects.create(username=username, password=password, balance=balance)


class StockModel(Model):
    ticker = models.CharField(max_length=255, primary_key=True)

    @staticmethod
    def create_typed(ticker: str) -> 'StockModel':
        return StockModel.objects.create(ticker=ticker)


class PublisherModel(Model):
    name = models.CharField(max_length=255, primary_key=True)
    reputation = models.FloatField()

    @staticmethod
    def create_typed(name: str, reputation: float) -> 'PublisherModel':
        return PublisherModel.objects.create(name=name, reputation=reputation)


class ArticleModel(Model):  # type: ignore
    article_id = models.CharField(max_length=255, primary_key=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    url = models.TextField()
    title = models.TextField()
    description = models.TextField()
    published = models.DateTimeField()
    stocks = models.ManyToManyField(StockModel)

    @staticmethod
    def create_typed(article_id: str, publisher: PublisherModel, url: str, title: str, description: str, published: datetime, stocks: List[StockModel]) -> 'ArticleModel':
        article = ArticleModel.objects.create(article_id=article_id, publisher=publisher, url=url,
                                              title=title, description=description, published=published)
        article.stocks.set(stocks)
        return article


class HoldingModel(Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'stock'], name='no_duplicate_holdings')
        ]

    @staticmethod
    def create_typed(user: UserModel, stock: StockModel, units: float) -> 'HoldingModel':
        return HoldingModel.objects.create(user=user, stock=stock, units=units)


class TradeModel(Model):  # type: ignore
    """
    Type ignore required until https://github.com/typeddjango/django-stubs/issues/64 is resolved.
    """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    units_change = models.DecimalField(max_digits=15, decimal_places=6)
    balance_change = models.DecimalField(max_digits=11, decimal_places=2)
    time = models.DateTimeField()
    text_evidence = models.TextField()
    article_evidence = models.ManyToManyField(ArticleModel, blank=True)

    @staticmethod
    def create_typed(user: UserModel, stock: StockModel, units_change: Decimal, balance_change: Decimal, time: datetime, text_evidence: str, article_evidence: List[ArticleModel]) -> 'TradeModel':
        trade = TradeModel.objects.create(
            user=user, stock=stock, units_change=units_change, balance_change=balance_change, time=time, text_evidence=text_evidence)
        trade.article_evidence.set(article_evidence)
        return trade
