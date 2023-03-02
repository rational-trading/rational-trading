import type { Stock } from "./types";
import { stocksDetails } from "./stores";

export function matchAny(search: string, options: string[]): boolean {
    const searchLower = search.toLowerCase();
    return (
        options.findIndex((o) => o.toLowerCase().includes(searchLower)) !==
        -1
    );
}

export function capitalize(s: string): string {
    return s[0].toUpperCase() + s.slice(1);
}

// may need to call the wrappers more than once, triggered by change in store value
let stocksMap: Map<string, Stock> | null;
stocksDetails.subscribe((x) => { stocksMap = x; });

// wrapper method for getting stock details based on ticker
export function findTicker(ticker: string) {
    if (stocksMap === null) {
        return { ticker, name: "Loading...", exchange: "Loading..." };
    }

    return stocksMap.get(ticker);
}

// wrapper method for getting details of all supported stocks
export function getStocks() {
    if (stocksMap === null) {
        return [{ ticker: "Loading...", name: "Loading...", exchange: "Loading..." }];
    }

    return stocksMap.values();
}
