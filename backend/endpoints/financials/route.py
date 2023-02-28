from dataclasses import dataclass
from ninja import Router, Schema
from django.http.request import HttpRequest

from lib.numerical_scoring import get_financial_endpoints
from lib.final_score_rank import final_numerical_rank


router = Router()

class FinancialsResponseSchema(Schema):
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float
    score: float
    ranked_score: float
    
        
@dataclass
class FinancialsResponse:
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float
    score: float
    ranked_score: float


@router.get("/", response=FinancialsResponseSchema)
def maths(request: HttpRequest, ticker: str) -> FinancialsResponse:
    print(type(request))
    end_dict = get_financial_endpoints(ticker)
    final_rank = final_numerical_rank(ticker)
    return FinancialsResponse(price_earning_ratio=end_dict["price_earning_ratio"],
                                    earnings_per_share=end_dict["earnings_per_share"],
                                    debt_to_equity=end_dict["debt_to_equity"],
                                    current_ratio=end_dict["current_ratio"],
                                    score=end_dict["score"],
                                    ranked_score = final_rank
    )
