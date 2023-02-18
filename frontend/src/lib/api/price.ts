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

    current(): Promise<TickerPrice> {
        return get<TickerPrice>({ endpoint: "/price/current", queryString: `ticker=${this.ticker}` });
    }

    history(): Promise<TickerPrice[]> {
        return get<TickerPrice[]>({ endpoint: "/price/history", queryString: `ticker=${this.ticker}` });
    }
}

export { PriceRoute, type TickerPrice };
