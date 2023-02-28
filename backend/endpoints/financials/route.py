from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest

from lib.financials import Financials


router = Router()


class FinancialsResponseSchema(Schema):
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float
    score: float


@router.get("/", response=FinancialsResponseSchema)
def financials(request: HttpRequest, ticker: str) -> Financials:
    return Financials.create(ticker)
