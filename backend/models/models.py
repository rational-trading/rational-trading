from django.db import models
from django.db.models import Model


class UserModel(Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=11, decimal_places=2)


class StockModel(Model):
    ticker = models.CharField(max_length=255, primary_key=True)


class PublisherModel(Model):
    name = models.CharField(max_length=255, primary_key=True)
    reputation = models.FloatField()


class ArticleModel(Model):  # type: ignore
    article_id = models.CharField(max_length=255, primary_key=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    url = models.TextField()
    title = models.TextField()
    description = models.TextField()
    published = models.DateTimeField()
    stocks = models.ManyToManyField(StockModel)


class HoldingModel(Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'stock'], name='no_duplicate_holdings')
        ]


class TradeModel(Model):  # type: ignore
    """
    Type ignore required until https://github.com/typeddjango/django-stubs/issues/64 is resolved.
    """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=15, decimal_places=6)
    total_cost = models.DecimalField(max_digits=11, decimal_places=2)
    time = models.DateTimeField()
    text_evidence = models.TextField()
    article_evidence = models.ManyToManyField(ArticleModel)
    pass
