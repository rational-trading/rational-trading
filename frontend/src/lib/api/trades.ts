import { get, post } from "$lib/request";

interface Trade {
    ticker: string,
    units_change: number,
    balance_change: number,
    time: number,
    text_evidence: string,
    article_evidence: string[],
    controversy: number,
    evidence: number,
    financial_risk: number,
}

interface MakeTrade {
    ticker: string,
    side: "BUY" | "SELL",
    type: "UNITS" | "PRICE",
    amount: number,
    text_evidence: string,
    article_evidence: string[],
}


class TradesRoute {
    personal(): Promise<Trade[]> {
        return get<Trade[]>({ endpoint: "/trades/personal", authenticated: true });
    }

    make(trade: MakeTrade): Promise<Trade> {
        return post<MakeTrade, Trade>({ endpoint: "/trades/make", authenticated: true, data: trade });
    }
}

export { TradesRoute, type Trade, type MakeTrade };
