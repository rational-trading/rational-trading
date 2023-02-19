import { get } from "../request";

interface TickerPrice {
    time: number,
    open: number,
    low: number,
    high: number,
    close: number,
}

class PriceRoute {
    ticker: string;

    constructor(ticker: string) {
        this.ticker = ticker;
    }

    recent(): Promise<TickerPrice> {
        return get<TickerPrice>({ endpoint: "/price/recent", queryString: `ticker=${this.ticker}` });
    }

    history(): Promise<TickerPrice[]> {
        return get<TickerPrice[]>({ endpoint: "/price/history", queryString: `ticker=${this.ticker}` });
    }
}

export { PriceRoute, type TickerPrice };
