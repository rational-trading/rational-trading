from typing import Dict


# these are the ratios we are gonna use and their weights(0-1)
ratios_weights = {
    "current_ratio": 0.5,
    # (cannot use roic becasue of the API) "roic": 0.9,
    "debt_to_equity": 0.7,
    "eps": 0.5
}

max_score = sum(ratios_weights.values())


def normaliseValue(value: float, mapping: Dict[float, float]) -> float:
    keysGreaterThanValue = filter(
        lambda k: k > value, mapping.keys())
    return mapping[min(keysGreaterThanValue)]


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


def evaluate_eps(value: float) -> float:
    # input: value in usd
    # output: a score between 0 and 1, 0.5 is considered okay
    if value < 0:
        return 0
    elif value > 10:
        return 1
    else:
        return (value / 10)

# (cannot use roic becasue of the API) roic: float,


def scoring(current_ratio: float, debt_to_equity: float, eps: float) -> float:
    # input: ratios and their values
    # output: a score between 0 and 1
    weighted_scores = [
        evaluate_current_ratio(current_ratio) *
        ratios_weights["current_ratio"],
        # (cannot use roic becasue of the API) evaluate_roic(roic) *
        # (cannot use roic becasue of the API) ratios_weights["roic"],
        evaluate_debt_to_equity(debt_to_equity) *
        ratios_weights["debt_to_equity"],
        evaluate_eps(eps) *
        ratios_weights["eps"]
    ]
    return sum(weighted_scores) / max_score


if __name__ == "__main__":

    # make use of polygon API to get the variable values

    # dividendV3:
    dividends = 1

    # BS:
    current_assets = 1
    current_liabilities = 1
    liabilities = 1
    debt = 0.8 * liabilities
    equity = 1

    # IS:
    # (cannot use roic becasue of the API) net_income = 1
    # basic_earnings_per_share in IS:
    eps = 1

    # calculate ratios
    current_ratio = current_assets / current_liabilities
    # (cannot use roic becasue of the API) roic = (net_income - dividends) / (debt + equity)
    debt_to_equity = debt / equity

    # use the scoring system
    # (cannot use roic becasue of the API)
    print(scoring(current_ratio, debt_to_equity, eps))
