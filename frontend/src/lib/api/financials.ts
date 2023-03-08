import { get } from "../request";

interface Financials {
    price_earning_ratio: number,
    earnings_per_share: number,
    debt_to_equity: number,
    current_ratio: number,
    score: number
}

class FinancialsRoute {
    get(ticker: string): Promise<Financials> {
        return get<Financials>({ endpoint: "/financials/", queryString: `ticker=${ticker}` });
    }
}

export { FinancialsRoute, type Financials };
