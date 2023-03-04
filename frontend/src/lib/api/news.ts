import { get } from "../request";

interface Article {
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
    about(ticker: string, n: number): Promise<Article[]> {
        return get<Article[]>({ endpoint: "/news/about", queryString: `ticker=${ticker}&n=${n}` });
    }

    articles(articleIds: string[]): Promise<Article[]> {
        const queryString = articleIds.map((id) => `article_ids=${id}`).join("&");
        return get<Article[]>({ endpoint: "/news/articles", queryString });
    }
}

export { NewsRoute, type Article };
