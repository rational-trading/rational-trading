from typing import List
from models.models import HoldingModel, UserModel, StockModel, TradeModel, PublisherModel, ArticleModel
from django.contrib import admin


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin[UserModel]):
    list_display = ['username', 'password', 'balance']


@admin.register(StockModel)
class StockAdmin(admin.ModelAdmin[StockModel]):
    list_display = ['ticker']


@admin.register(HoldingModel)
class HoldingAdmin(admin.ModelAdmin[HoldingModel]):
    list_display = ['user', 'stock', 'units']


@admin.register(TradeModel)
class TradeAdmin(admin.ModelAdmin[TradeModel]):
    def articles(self, trade: TradeModel) -> List[str]:
        return [article.title for article in trade.article_evidence.all()]
    list_display = ['user', 'stock', 'units_change', 'balance_change',
                    'time', 'text_evidence', 'articles']


@admin.register(PublisherModel)
class PublisherAdmin(admin.ModelAdmin[PublisherModel]):
    list_display = ['name', 'reputation']


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin[ArticleModel]):
    def all_stocks(self, article: ArticleModel) -> List[str]:
        return [stock.ticker for stock in article.stocks.all()]

    list_display = ['article_id', 'publisher',
                    'url', 'title', 'description', 'published', 'all_stocks']
