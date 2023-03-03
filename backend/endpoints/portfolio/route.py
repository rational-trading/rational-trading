from decimal import ROUND_DOWN
from typing import List

from ninja import Router, Schema
from django.db import transaction

from lib.polygon_api import PolygonAPI
from endpoints.auth import AuthBearer, AuthenticatedRequest
from models.models import HoldingModel, TradeModel, UserModel

router = Router(auth=AuthBearer())


class PortfolioStatsSchema(Schema):
    cash_balance: float
    holdings_value: float
    unrealised_gain: float


def calculate_unrealised_gain(holding: HoldingModel, sale_price: float) -> float:
    trades = TradeModel.objects.filter(user=holding.user, stock=holding.stock)

    cost_basis = 0.
    current_holding = 0.

    for trade in trades:
        if trade.units_change > 0 and trade.balance_change < 0:
            # BUY
            cost_basis += -float(trade.balance_change)
            current_holding += float(trade.units_change)
        elif trade.units_change < 0 and trade.balance_change >= 0:
            # SELL
            # we will use average cost, but FIFO cost is often sometimes used
            cost_basis_per_share = cost_basis / current_holding
            # subtract the cost basis of the units just sold from the running total
            cost_basis -= -float(trade.units_change) * cost_basis_per_share
            current_holding += float(trade.units_change)
        else:
            raise ValueError("Invalid trade!")

    unrealised_gain = (current_holding * sale_price) - cost_basis
    return unrealised_gain


@router.get("/stats", response=PortfolioStatsSchema)
@transaction.atomic
def stats(request: AuthenticatedRequest) -> PortfolioStatsSchema:
    user = UserModel.objects.get(username=request.auth)
    holdings = HoldingModel.objects.filter(user=user)

    api = PolygonAPI()

    current_prices = [(holding, api.recent_price(holding.stock.ticker).low)
                      for holding in holdings]

    current_value = sum(
        [float(holding.units) * price for (holding, price) in current_prices], start=0.)

    unrealised_gains = [calculate_unrealised_gain(
        holding, price) for (holding, price) in current_prices]

    return PortfolioStatsSchema(
        cash_balance=user.balance,
        holdings_value=current_value,
        unrealised_gain=sum(unrealised_gains))


class HoldingSchema(Schema):
    ticker: str
    units: float
    value: float
    unrealised_gain: float

    @staticmethod
    def from_model(model: HoldingModel) -> 'HoldingSchema':
        current_price = PolygonAPI().recent_price(model.stock.ticker).low
        return HoldingSchema(
            ticker=model.stock.ticker,
            units=float(model.units),
            value=round(current_price * float(model.units), 2),
            unrealised_gain=round(
                calculate_unrealised_gain(model, current_price), 2))


@router.get("/holdings", response=List[HoldingSchema])
@transaction.atomic
def holdings(request: AuthenticatedRequest) -> List[HoldingSchema]:
    user = UserModel.objects.get(username=request.auth)
    holdings = HoldingModel.objects.filter(user=user)
    return [HoldingSchema.from_model(holding) for holding in holdings]
