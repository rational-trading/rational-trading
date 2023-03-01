import { get } from "../request";

interface TickerDetails {
    ticker: string,
    company_name: string,
    exchange: string
}

class StocksRoute {
    all(): Promise<TickerDetails[]> {
        return get<TickerDetails[]>({ endpoint: "/stocks/all" });
    }
}

export { StocksRoute, type TickerDetails };
