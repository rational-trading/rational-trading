"""
Precomputing numerical scores in order to normalise the given score based on its rank in the list
"""


import lib.scoring

numerical_results = [0.747, 0.465, 0.812, 0.753, 0.753, 0.506, 
           0.694, 0.812, 0.7, 0.8, 0.718, 0.676, 0.753, 
           0.688, 0.876, 0.841, 0.994, 0.876, 0.976, 0.794, 
           0.865, 0.876, 0.924, 0.694, 0.459, 0.759, 0.953, 0.788, 
           0.812, 0.618, 0.824, 0.694, 0.976, 0.694, 0.818, 0.818, 
           0.6, 0.718, 0.959, 0.929, 0.988, 0.665, 0.871, 0.982, 0.918, 
           0.459, 0.976, 0.718, 0.953]

def main() -> None:
    tickers50 = ["AAPL", "AMZN", "AMD", "KO", "A", "ALL", "NVDA", "ABT", "WMT", "ACN", 
               "NFLX", "AMGN", "ADI", "ADP", "GOOG", "XOM", "INTC", "META", "ACGL", "MCD",
               "VZ", "HD", "CVX", "ARE", "GE", "AON", "AIG", "AEE", "AME", "ABC", 
               "AEP", "APTV", "AFL", "TSLA", "JNJ", "MSFT", "ABBV", "ADBE", "BAC", "AMAT", 
               "ALB", "DIS", "AA", "PFE", "CSCO", "AMT", "ADM", "AJG", "AMP", "GME"]
               
    score_list = []
    count = 0          
    for t in tickers50:
        print(count)
        print(score_list)
        score = lib.scoring.numerical_scoring(t)
        score_list.append(round(score, 3))
        count+=1
    
    

if __name__ == "__main__":
    main()