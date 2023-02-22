
import lib.scoring
import lib.numerical_precompute



def normalised_numerical_scoring(ticker, numerical_pre_results):
    result = lib.scoring.numerical_scoring(ticker)
    score = 0
    for x in numerical_pre_results:
        if result > x: score += 0.02
    return score



def final_scoring(ticker: str) -> float:
    numerical_score = normalised_numerical_scoring(ticker, lib.numerical_precompute.numerical_results)
    # @Simon
    nlp_score = 0
    return 0.5 * numerical_score + 0.5 * nlp_score

print(final_scoring("AAPL"))