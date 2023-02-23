from typing import List
from ninja import Schema, Router

from models.models import TradeModel
from models.models import UserModel
from endpoints.auth import AuthBearer, AuthenticatedRequest


router = Router(auth=AuthBearer())


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


@router.get("/trades/all", response=List[TradeSchema])
def trades(request: AuthenticatedRequest) -> List[TradeSchema]:
    user = UserModel.objects.get(username=request.auth)
    trades = TradeModel.objects.filter(user=user)

    return [TradeSchema.from_model(trade) for trade in trades]


class AddTradeSchema(Schema):
    ticker: str
    units: float
    total_cost: float
    time: int
    text_evidence: str
    article_evidence: List[str]


@router.post("/trades/add")
def add_trade(request: AuthenticatedRequest, data: AddTradeSchema) -> None:
    pass
