import { get } from "../request";

interface News {
    article_id: string,
    publisher: string,
    url: string,
    title: string,
    description: string,
    date: number,
    tickers: string[],
    normalised_sentiment: number,
    reputation: number,
    recency: number
}

class NewsRoute {
    get(ticker: string, n: number): Promise<News[]> {
        return get<News[]>({ endpoint: "/news/get", queryString: `ticker=${ticker}&n=${n}` });
    }
}

export { NewsRoute, type News };
