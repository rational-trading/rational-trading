import { stocksDetails } from "$lib/stores";
import { get } from "../request";

interface TickerDetails {
    ticker: string,
    company_name: string,
    exchange: string
}

async function getStocksDetails(): Promise<void> {
    const tickersDetails = await get<TickerDetails[]>({ endpoint: "/stocks/all" });
    const stocksDetailsMap = new Map<string, TickerDetails>();
    for (let i = 0; i < tickersDetails.length; i += 1) {
        stocksDetailsMap.set(tickersDetails[i].ticker, tickersDetails[i]);
    }
    stocksDetails.set(stocksDetailsMap);
}

class StocksRoute {

}

export { StocksRoute, type TickerDetails, getStocksDetails };
