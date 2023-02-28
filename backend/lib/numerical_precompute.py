"""
Precomputing numerical scores in order to normalise the given score based on its rank in the list
"""


from typing import List
import lib.numerical_scoring

numerical_results = [0.767, 0.552, 0.695, 0.767, 0.771, 0.571, 0.581, 0.819, 0.79, 
                     0.857, 0.743, 0.648, 0.771, 0.705, 0.933, 0.971, 0.981, 0.886, 
                     0.905, 0.705, 0.862, 0.829, 0.971, 0.771, 0.529, 0.733, 0.933, 
                     0.795, 0.819, 0.571, 0.776, 0.724, 0.952, 0.724, 0.838, 0.838, 
                     0.605, 0.743, 0.952, 0.914, 0.962, 0.714, 0.581, 0.971, 0.905, 
                     0.538, 0.952, 0.743, 0.914, 0.562]


def main() -> None:
    tickers50 = ["AAPL", "AMZN", "AMD", "KO", "A", "ALL", "NVDA", "ABT", "WMT", "ACN",
                 "NFLX", "AMGN", "ADI", "ADP", "GOOG", "XOM", "INTC", "META", "ACGL", "MCD",
                 "VZ", "HD", "CVX", "ARE", "GE", "AON", "AIG", "AEE", "AME", "ABC",
                 "AEP", "APTV", "AFL", "TSLA", "JNJ", "MSFT", "ABBV", "ADBE", "BAC", "AMAT",
                 "ALB", "DIS", "AA", "PFE", "CSCO", "AMT", "ADM", "AJG", "AMP", "GME"]

    score_list: List[float] = []
    count = 0
    for t in tickers50:
        score = lib.numerical_scoring.get_financial_endpoints(t)["score"]
        score_list.append(round(score, 3))
        count += 1
    print(count)
    print(score_list)


if __name__ == "__main__":
    main()
