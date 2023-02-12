from models.models import User, Stock, Trade
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin[User]):
    list_display = ['username', 'password', 'balance']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin[Stock]):
    list_display = ['ticker']


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin[Trade]):
    list_display = ['user', 'stock', 'units', 'total_cost']
