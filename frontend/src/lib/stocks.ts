import api from "./api";
import { stocksDetails } from "./stores";

async function loadTickerDetails() {
    const tickerDetails = await api.stocks().all();
    stocksDetails.set(new Map(tickerDetails.map((x) => [x.ticker, { ticker: x.ticker, name: x.company_name, exchange: x.exchange }])));
}

export { loadTickerDetails };
