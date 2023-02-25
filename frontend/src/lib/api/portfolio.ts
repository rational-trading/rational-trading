import { get } from "$lib/request";

interface PortfolioStats {
    cash_balance: number,
    holdings_value: number,
    unrealised_gain: number,
}

interface Holding {
    ticker: string,
    units: number,
    value: number,
    unrealised_gain: number,
}


class PortfolioRoute {
    stats(): Promise<PortfolioStats> {
        return get<PortfolioStats>({ endpoint: "/portfolio/stats", authenticated: true });
    }

    holdings(): Promise<Holding[]> {
        return get<Holding[]>({ endpoint: "/portfolio/holdings", authenticated: true });
    }
}

export { PortfolioRoute, type PortfolioStats, type Holding };
