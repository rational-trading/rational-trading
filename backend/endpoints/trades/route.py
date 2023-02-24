from typing import List, Literal, Tuple
from decimal import ROUND_DOWN, ROUND_UP, Decimal

from ninja import Schema, Router
from django.utils import timezone
from django.db import transaction

from models.models import ArticleModel, HoldingModel, StockModel, TradeModel
from models.models import UserModel
from endpoints.auth import AuthBearer, AuthenticatedRequest
from endpoints.error import FriendlyClientException
from lib.polygon_api import PolygonAPI


router = Router(auth=AuthBearer())


class TradeSchema(Schema):
    ticker: str
    units_change: float
    balance_change: float
    time: int
    text_evidence: str
    article_evidence: List[str]

    @staticmethod
    def from_model(model: TradeModel) -> 'TradeSchema':
        return TradeSchema(
            ticker=model.stock.ticker,
            units_change=model.units_change,
            balance_change=model.balance_change,
            time=int(model.time.timestamp()),
            text_evidence=model.text_evidence,
            article_evidence=[article.article_id for article in model.article_evidence.all()])


@router.get("/personal", response=List[TradeSchema])
@transaction.atomic
def personal_trades(request: AuthenticatedRequest) -> List[TradeSchema]:
    user = UserModel.objects.get(username=request.auth)
    trades = TradeModel.objects.filter(user=user)

    return [TradeSchema.from_model(trade) for trade in trades]


class AddTradeSchema(Schema):
    ticker: str
    side: Literal['BUY'] | Literal['SELL']
    type: Literal['UNITS'] | Literal['PRICE']
    amount: Decimal
    text_evidence: str
    article_evidence: List[str]

    def balance_units_changes(self) -> Tuple[Decimal, Decimal]:
        if self.amount <= 0:
            raise FriendlyClientException(
                "Trade amount must be greater than 0!")

        BUY = self.side == 'BUY'

        current_price = PolygonAPI().recent_price(self.ticker)
        deal_price = Decimal(current_price.high if BUY else current_price.low)

        if self.type == 'UNITS':
            balance_change = deal_price * self.amount
            units_change = self.amount
        else:
            balance_change = self.amount
            units_change = balance_change / deal_price

        balance_change = balance_change.quantize(
            Decimal('0.01'), rounding=ROUND_UP if BUY else ROUND_DOWN)
        units_change = units_change.quantize(
            Decimal('0.000001'), rounding=ROUND_DOWN if BUY else ROUND_UP)

        if units_change < Decimal('0.000001'):
            print(balance_change, units_change)
            raise FriendlyClientException("Amount too small!")

        if BUY:
            if balance_change < Decimal('0.01'):
                print(balance_change, units_change)
                raise FriendlyClientException("Amount too small!")
            return (balance_change * -1, units_change)
        else:
            return (balance_change, units_change * -1)


@router.post("/add")
@transaction.atomic
def add_trade(request: AuthenticatedRequest, order: AddTradeSchema) -> TradeSchema:
    user = UserModel.objects.get(username=request.auth)
    articles = [ArticleModel.objects.get(
        article_id=id) for id in set(order.article_evidence)]
    stock = StockModel.objects.get(ticker=order.ticker)

    time = timezone.now()
    (balance_change, units_change) = order.balance_units_changes()

    try:
        holding = HoldingModel.objects.get(user=user, stock=stock)
    except HoldingModel.DoesNotExist:
        holding = HoldingModel.create_typed(user, stock, 0)

    user.balance += Decimal(balance_change)
    holding.units += Decimal(units_change)

    if user.balance < 0:
        raise FriendlyClientException('Current balance is too small!')
    if holding.units < 0:
        raise FriendlyClientException('Current holding is too small!')

    trade = TradeModel.create_typed(
        user=user, stock=stock, units_change=units_change, balance_change=balance_change, time=time, text_evidence=order.text_evidence, article_evidence=articles)

    user.save()
    trade.save()

    if holding.units == 0:
        holding.delete()
    else:
        holding.save()

    return TradeSchema.from_model(trade)
