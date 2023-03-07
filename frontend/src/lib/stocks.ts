import api from "./api";
import { stocks } from "./stores";

async function loadTickerDetails() {
    const tickerDetails = await api.stocks().all();
    const all = tickerDetails.map((x) => ({ ticker: x.ticker, name: x.company_name, exchange: x.exchange }));
    const map = new Map(all.map((x) => [x.ticker, x]));
    stocks.set({
        get: (ticker: string) => map.get(ticker) ?? { ticker, name: "Not found!", exchange: "Not found!" },
        all,
    });
}

export { loadTickerDetails };
