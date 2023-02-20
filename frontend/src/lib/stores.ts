import { readable, writable } from "svelte/store";
import type { Stock } from "$lib/types";

export const watchlist: writable<Stock[]> = writable([
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

export const currentStock: writable<Stock> = writable({ ticker: "AAPL", name: "Apple Inc", exchange: "NASDAQ" });

export const stocks: readable<Stock[]> = readable([
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
