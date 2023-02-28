from typing import Dict


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
