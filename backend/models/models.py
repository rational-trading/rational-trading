from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=11, decimal_places=2)


class Stock(models.Model):
    ticker = models.CharField(max_length=255, primary_key=True)


class Trade(models.Model):  # type: ignore
    """
    Type ignore required until https://github.com/typeddjango/django-stubs/issues/64 is resolved.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=15, decimal_places=6)
    total_cost = models.DecimalField(max_digits=11, decimal_places=2)
    time = models.DateTimeField()
