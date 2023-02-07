import typing


# these are the rotios we are gonna use and their weights(0-1)
ratios_weights = {
    "current_ratio": 0.5,
    "roic": 0.9,
    "debt_to_equity": 0.7
    }

max_score = 0

for key in ratios_weights:
    max_score += ratios_weights[key]



def evaluate_current_ratio(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    # 0.4-0.7: 0.3
    scoring_dic = {
        float("-inf"): 0,
        0.1: 0,
        0.4: 0.1,
        0.7: 0.3,
        1: 0.5,
        1.2: 0.7,
        1.5: 0.9,
        float("inf"): 1
        }
    score = -1
    for key in scoring_dic:
        if key > value:
            score = scoring_dic[key]
            break
    
    return score

def evaluate_roic(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    scoring_dic = {
        float("-inf"): 0,
        2: 0,
        5: 0.3,
        10: 0.5,
        20: 0.7,
        30: 0.9,
        float("inf"): 1
        }
    score = -1
    for key in scoring_dic:
        if key > value:
            score = scoring_dic[key]
            break
    
    return score

def evaluate_debt_to_equity(value: float) -> float:
    # input: ratio value
    # output: a score between 0 and 1, 0.5 is considered okay
    scoring_dic = {
        float("-inf"): 1,
        1: 1,
        1.5: 0.9,
        2: 0.7,
        3: 0.5,
        5: 0.1,
        7: 0,
        float("inf"): 0
        }
    score = -1
    for key in scoring_dic:
        if key > value:
            score = scoring_dic[key]
            break
    
    return score



def scoring(ratios: typing.Dict[str, float]) -> float:
    # input: ratios and their values
    # output: a score between 0 and 1
    score = 0
    score += evaluate_current_ratio(ratios["current_ratio"]) * ratios_weights["current_ratio"]
    score += evaluate_roic(ratios["roic"]) * ratios_weights["roic"]
    score += evaluate_debt_to_equity(ratios["debt_to_equity"]) * ratios_weights["debt_to_equity"]
    return(score / max_score)




def main():



        
    # initialise ratios to -1
    ratios = {}
    for key in ratios_weights:
        ratios[key] = -1
    # make use of polygon API to get the variable values
    current_assets = 1
    current_liabilities = 1
    net_income = 1
    dividends = 1
    debt = 1
    equity = 1
    total_liabilities = 1
    # calculate ratios
    ratios["current_ratio"] = current_assets / current_liabilities
    ratios["roic"] = (net_income - dividends) / (debt + equity)
    ratios["debt_to_equity"] = total_liabilities / equity

    # use the scoring system
    print(scoring(ratios))


    

if __name__ == "__main__":
    main()
