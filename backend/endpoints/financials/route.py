from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest

from lib.scoring import get_financial_endpoints

router = Router()

class FinancialsResponseSchema(Schema):
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float
        
@dataclass
class FinancialsResponse:
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float


@router.get("/", response=FinancialsResponseSchema)
def maths(request: HttpRequest, ticker: str) -> FinancialsResponse:
    print(type(request))
    end_dict = get_financial_endpoints(ticker)
    return FinancialsResponse(price_earning_ratio=end_dict["price_earning_ratio"],
                                    earnings_per_share=end_dict["earnings_per_share"],
                                    debt_to_equity=end_dict["debt_to_equity"],
                                    current_ratio=end_dict["current_ratio"])
