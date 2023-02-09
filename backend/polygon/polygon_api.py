from polygon import RESTClient
import config #contains API_KEY
import json

def main():
    client = RESTClient(api_key=config.API_KEY)
    ticker = "GOOG"

    news = client.list_ticker_news(ticker=ticker, limit=2)
    print([n for n in news])

if __name__ == "__main__":
    main()