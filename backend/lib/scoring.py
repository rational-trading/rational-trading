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


from typing import Dict

from lib.polygon_api import PolygonAPI

# ————————————————————————————————————————————————————————————————

# these are the ratios we are gonna use and their weights(0-1)
ratios_weights = {
    "equity_risk": 0.1,
    "current_ratio": 0.2,
    # (cannot use roic becasue of the API) "roic": 0.9,
    "debt_to_equity": 0.4,
    "pe": 1
}

max_score = sum(ratios_weights.values())


def normaliseValue(value: float, mapping: Dict[float, float]) -> float:
    keysGreaterThanValue = filter(
        lambda k: k > value, mapping.keys())
    return mapping[min(keysGreaterThanValue)]

# ————————————————————————————————————————————————————————————————


def evaluate_equity_risk(value: float) -> float:
    # input: equity
    # output: a score between 0 and 1, 0.5 is considered okay
    # 0.4-0.7: 0.3
    mapping = {
        float("-inf"): 0,
        (0.5 * (10 ** 9)): 0.5,
        (5 * (10 ** 9)): 0.7,
        (50 * (10 ** 9)): 0.8,
        (500 * (10 ** 9)): 0.9,
        float("inf"): 1
    }
    return normaliseValue(value, mapping)


def evaluate_current_ratio(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    # 0.4-0.7: 0.3
    mapping = {
        float("-inf"): 0,
        0.1: 0,
        0.4: 0.1,
        0.7: 0.3,
        1: 0.5,
        1.2: 0.7,
        1.5: 0.9,
        float("inf"): 1
    }
    return normaliseValue(value, mapping)


# (cannot use roic becasue of the API)
def evaluate_roic(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    mapping = {
        float("-inf"): 0,
        2: 0,
        5: 0.3,
        10: 0.5,
        20: 0.7,
        30: 0.9,
        float("inf"): 1
    }
    return normaliseValue(value, mapping)


def evaluate_debt_to_equity(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    mapping = {
        float("-inf"): 1,
        1: 1,
        1.5: 0.9,
        2: 0.7,
        3: 0.5,
        5: 0.1,
        7: 0,
        float("inf"): 0
    }
    return normaliseValue(value, mapping)


def evaluate_pe(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    # 0.4-0.7: 0.3
    mapping = {
        float("-inf"): 0,
        0: 0.2,
        15: 1,
        20: 0.9,
        25: 0.8,
        30: 0.7,
        50: 0.6,
        75: 0.5,
        100: 0.4,
        float("inf"): 0.2
    }
    return normaliseValue(value, mapping)

# ————————————————————————————————————————————————————————————————

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

# ————————————————————————————————————————————————————————————————


def numerical_scoring(ticker: str) -> float:

    # make use of polygon API to get the variable values
    api = PolygonAPI()

    # dividendV3: (this is the most recent dividend, not for a year, but won't be used for now)
    # dividends = api.get_dividend(ticker).cash_amount

    price = list.pop(api.price_history(ticker)).high

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

    # use the scoring system
    # (cannot use roic becasue of the API)
    return scoring(current_ratio, debt_to_equity, pe, equity)


# numerical_scoring("AAPL")
