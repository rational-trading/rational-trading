from dataclasses import dataclass
from typing import List
from ninja import Router, Schema
from lib.polygon_api import PolygonAPI

from endpoints.auth import AuthBearer, AuthenticatedRequest
from models.models import ArticleModel, HoldingModel, TradeModel, UserModel

router = Router(auth=AuthBearer())


class StatsResponseSchema(Schema):
    current_value: float


@router.get("/stats", response=StatsResponseSchema)
def stats(request: AuthenticatedRequest) -> StatsResponseSchema:
    user = UserModel.objects.get(username=request.auth)
    holdings = HoldingModel.objects.filter(user=user)

    api = PolygonAPI()

    current_value = sum([api.recent_price(holding.stock.ticker).low * float(holding.units)
                        for holding in holdings])

    return StatsResponseSchema(current_value=current_value)


class HoldingSchema(Schema):
    ticker: str
    units: float

    @staticmethod
    def from_model(model: HoldingModel) -> 'HoldingSchema':
        return HoldingSchema(ticker=model.stock.ticker, units=float(model.units))


@router.get("/holdings", response=List[HoldingSchema])
def holdings(request: AuthenticatedRequest) -> List[HoldingSchema]:
    user = UserModel.objects.get(username=request.auth)
    holdings = HoldingModel.objects.filter(user=user)
    return [HoldingSchema.from_model(holding) for holding in holdings]

