"""
Testing NLP libraries to perform sentiment analysis on financial news headlines/descriptions.
"""

from textblob import TextBlob

def get_sentiment(text: str) -> float:
    """ 
    Returns sentiment of input string as float between 0 and 1 (0 being negative sentiment, 0.5 neutral, 1 positive)
    """
    t = TextBlob(text)
    return t.sentiment.polarity

def get_subjectivity(text: str) -> float:
    """
    Returns subjectivity of input string as float between 0 and 1 (0 being entirely objective, 1 being entirely subjective)
    """
    t = TextBlob(text)
    return t.sentiment.subjectivity

def get_average_sentiment(texts: list[str]) -> float:
    n = len(texts)
    return sum([get_sentiment(t) for t in texts]) / len(texts)

def get_average_subjectivity(texts: list[str]) -> float:
    return sum([get_subjectivity(t) for t in texts]) / len(texts)

if __name__ == "__main__":
    test = ['Wedgewood Partners Fourth Quarter 2022 Client Letter - Since World War II, 2022 has been the 4th worst year for the broad stock market. Click here to read more on our current thoughts in our Client Letter.', "Here's how — and where — Netflix has started cracking down on password sharing - Netflix once tweeted 'Love is sharing a password,' which hasn't aged so well.", "'Patience will be rewarded': Why Wall Street analysts aren't freaking out over Amazon's results and think shares are worth more - Wall Street was raising their target prices on shares of Amazon, as main street was selling. The e-commerce giant is about investing in a long game, say many analysts.", 'Tech stocks have been minting money this year, but many investors fear getting burned if they buy the rally now - These 3 tech giants have stood out in this earnings season -- with mixed market reactions.', "Big Tech’s squeeze of technology innovators is costing you more for apps and other internet services - Change intellectual property law to level the playing field or risk America's global tech leadership.", 'Apple Vs. Meta: Which Is The More Attractive Choice? - Last Thursday, both Apple and Meta presented their latest quarterly results. Read more about them here.', "Apple earnings show steepest sales decline in more than 6 years - Apple Inc.'s business came under pressure in the holiday quarter, as the company posted its largest revenue decline in more than six years.", "Apple CEO Tim Cook Says Layoffs Are Last Resort, But 'You Can Never Say Never' - As many tech giants have been executing an unprecedented level of layoffs, Apple Inc (NASDAQ: AAPL) has managed to avoid major job cuts even though it missed expectations for several of its lines of business announced during its first-quarter earnings.\nThe iPhone maker announced its first quarterly revenue, which declined for the first time in nearly four years, with revenue of $117.2 billion that missed analyst expectations of $121.1 billion.\nIn an\xa0interview\xa0with the Wall Street Journal, Apple CEO Tim Cook said there are ways to reduce costs, and that layoffs aren’t the only answer.\xa0\n“I view layoffs as a last resort kind of thing,” Cook said. “You can never say never. We want to manage ...", 'Apple is producing more. But now the worries are who will buy? - With COVID-19 supply constraints in the rear-view mirror, Apple Inc. is now inviting some concern about demand']
    print(get_average_sentiment(test), get_average_subjectivity(test))

