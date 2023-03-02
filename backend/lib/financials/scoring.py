
from dataclasses import dataclass
from lib.financials.core import evaluate_current_ratio, evaluate_debt_to_equity, evaluate_equity_risk, evaluate_pe

from lib.polygon_api import PolygonAPI

"""
Create a function such that when given a ticker,
it returns a numerical score for the financial data using 
the Stock Financials VX in Polygon API.
Mainly use P/E ratio to see if the stock is overpriced or not,
also use other ratios to evaluate liquidity, capital structure and risk

As the Stock Financials VX in Polygon API is experimental, 
some of the detailed information in the financial statements is missing, 
including “debt” under “liabilities” and “net_income_loss” in “income_statement”.

According to what we have discussed with our client, we decided to estimate the value.
Once the features are upgraded, we can replace the estimation with the real value 
and activate the ratios we cannot use now.

"""


precomputed_dist = [0.767, 0.552, 0.695, 0.767, 0.771, 0.571, 0.581, 0.819, 0.79,
                    0.857, 0.743, 0.648, 0.771, 0.705, 0.933, 0.971, 0.981, 0.886,
                    0.905, 0.705, 0.862, 0.829, 0.971, 0.771, 0.529, 0.733, 0.933,
                    0.795, 0.819, 0.571, 0.776, 0.724, 0.952, 0.724, 0.838, 0.838,
                    0.605, 0.743, 0.952, 0.914, 0.962, 0.714, 0.581, 0.971, 0.905,
                    0.538, 0.952, 0.743, 0.914, 0.562]


def normalise_financials_score(score: float) -> float:
    return len([x for x in precomputed_dist if score > x]) / len(precomputed_dist)


# these are the ratios we are gonna use and their weights(0-1)
ratios_weights = {
    "equity_risk": 0.4,
    "current_ratio": 0.2,
    # (cannot use roic becasue of the API) "roic": 0.9,
    "debt_to_equity": 0.5,
    "pe": 1
}

max_score = sum(ratios_weights.values())


# (cannot use roic becasue of the API) roic: float,

def scoring(current_ratio: float, debt_to_equity: float, pe: float, equity: float) -> float:
    # input: ratios and their values
    # output: a score between 0 and 1
    weighted_scores = [
        evaluate_current_ratio(current_ratio) *
        ratios_weights["current_ratio"],
        # (cannot use roic becasue of the API) evaluate_roic(roic) *
        # (cannot use roic becasue of the API) ratios_weights["roic"],
        evaluate_debt_to_equity(debt_to_equity) *
        ratios_weights["debt_to_equity"],
        evaluate_pe(pe) *
        ratios_weights["pe"],
        evaluate_equity_risk(equity) *
        ratios_weights["equity_risk"]
    ]
    return sum(weighted_scores) / max_score


@dataclass
class Financials:
    price_earning_ratio: float
    earnings_per_share: float
    debt_to_equity: float
    current_ratio: float
    score: float

    @staticmethod
    def create(ticker: str, normalise_score: bool = True) -> 'Financials':
        api = PolygonAPI()

        # dividendV3: (this is the most recent dividend, not for a year, but won't be used for now)
        # dividends = api.get_dividend(ticker).cash_amount

        price = api.recent_price(ticker).high

        # BS:
        financials = api.get_financials(ticker)

        current_assets = financials.current_assets
        current_liabilities = financials.current_liabilities
        nc_liabilities = financials.nc_liabilities
        # estimation to be replaced:
        debt = 0.6 * nc_liabilities
        equity = financials.equity

        # IS:
        # (cannot use roic becasue of the API) net_income = 1
        # basic_earnings_per_share in IS:
        eps = financials.basic_earnings_per_share

        # calculate ratios
        current_ratio = current_assets / current_liabilities

        # (cannot use roic becasue of the API) roic = (net_income - dividends) / (debt + equity)
        debt_to_equity = debt / equity
        pe = price / eps

        score = scoring(current_ratio, debt_to_equity, pe, equity)

        # (cannot use roic becasue of the API)
        return Financials(price_earning_ratio=pe,
                          earnings_per_share=eps,
                          debt_to_equity=debt_to_equity,
                          current_ratio=current_ratio,
                          score=normalise_financials_score(
                              score) if normalise_score else score
                          )
