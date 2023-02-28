"""
Precomputing numerical scores in order to normalise the given score based on its rank in the list
"""


from typing import List
from lib.financials.scoring import Financials


def main() -> None:
    tickers50 = ["AAPL", "AMZN", "AMD", "KO", "A", "ALL", "NVDA", "ABT", "WMT", "ACN",
                 "NFLX", "AMGN", "ADI", "ADP", "GOOG", "XOM", "INTC", "META", "ACGL", "MCD",
                 "VZ", "HD", "CVX", "ARE", "GE", "AON", "AIG", "AEE", "AME", "ABC",
                 "AEP", "APTV", "AFL", "TSLA", "JNJ", "MSFT", "ABBV", "ADBE", "BAC", "AMAT",
                 "ALB", "DIS", "AA", "PFE", "CSCO", "AMT", "ADM", "AJG", "AMP", "GME"]

    score_list: List[float] = []
    count = 0
    for t in tickers50:
        score = Financials.create(
            t, normalise_score=False).score
        score_list.append(round(score, 3))
        count += 1
    print(count)
    print(score_list)


if __name__ == "__main__":
    main()
