import {
    readable, writable, type Readable, type Writable,
} from "svelte/store";
import type { Stock } from "$lib/types";

export const authenticated = writable(false);

export const watchlist: Writable<Stock[]> = writable([
    {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    },
    {
        ticker: "TSLA",
        name: "Tesla, Inc.",
        exchange: "NASDAQ",
    },
]);

export const currentStock: Writable<Stock> = writable({ ticker: "AAPL", name: "Apple Inc", exchange: "NASDAQ" });

export const stocks: Readable<Stock[]> = readable([
    {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    },
    {
        ticker: "JPM",
        name: "JP Morgan Chase & Co.",
        exchange: "NYSE",
    },
    {
        ticker: "KO",
        name: "Coca-Cola Company (The)",
        exchange: "NYSE",
    },
    {
        ticker: "SBUX",
        name: "Starbucks Corporation",
        exchange: "NASDAQ",
    },
    {
        ticker: "TSLA",
        name: "Tesla, Inc.",
        exchange: "NASDAQ",
    },
]);
