from typing import Dict


# these are the ratios we are gonna use and their weights(0-1)
ratios_weights = {
    "current_ratio": 0.5,
    "roic": 0.9,
    "debt_to_equity": 0.7
    }

max_score = sum(ratios_weights.values())

def normaliseValue(value: float, mapping: Dict[float, float]):
    score = -1
    for key in mapping:
        if key > value:
            score = mapping[key]
            return score
    raise Exception("Should be impossible.")

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


def scoring(current_ratio: float, roic: float, debt_to_equity: float) -> float:
    # input: ratios and their values
    # output: a score between 0 and 1
    score = 0
    score += evaluate_current_ratio(current_ratio) * ratios_weights["current_ratio"]
    score += evaluate_roic(roic) * ratios_weights["roic"]
    score += evaluate_debt_to_equity(debt_to_equity) * ratios_weights["debt_to_equity"]
    return(score / max_score)


def main():

    # make use of polygon API to get the variable values
    current_assets = 1
    current_liabilities = 1
    net_income = 1
    dividends = 1
    debt = 1
    equity = 1
    total_liabilities = 1
    # calculate ratios
    current_ratio = current_assets / current_liabilities
    roic = (net_income - dividends) / (debt + equity)
    debt_to_equity = total_liabilities / equity

    # use the scoring system
    print(scoring(current_ratio, roic, debt_to_equity))


if __name__ == "__main__":
    main()