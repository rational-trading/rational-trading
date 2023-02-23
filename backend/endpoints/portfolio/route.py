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


class TradeSchema(Schema):
    ticker: str
    units: float
    total_cost: float
    time: int
    text_evidence: str
    article_evidence: List[str]

    @staticmethod
    def from_model(model: TradeModel) -> 'TradeSchema':
        return TradeSchema(
            ticker=model.stock.ticker,
            units=float(model.units),
            total_cost=float(model.total_cost),
            time=int(model.time.timestamp()),
            text_evidence=model.text_evidence,
            article_evidence=[article.article_id for article in model.article_evidence.all()])


@router.get("/trades", response=List[TradeSchema])
def trades(request: AuthenticatedRequest) -> List[TradeSchema]:
    user = UserModel.objects.get(username=request.auth)
    trades = TradeModel.objects.filter(user=user)

    return [TradeSchema.from_model(trade) for trade in trades]
