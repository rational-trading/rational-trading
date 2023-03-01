import {
    readable, writable, type Readable, type Writable,
} from "svelte/store";
import type { Stock } from "$lib/types";
import type { TickerDetails } from "./api/stocks";

export const user: Writable<{ username: string } | null> = writable(null);

export const currentStock: Writable<Stock> = writable({ ticker: "AAPL", name: "Apple Inc", exchange: "NASDAQ" });

export const stocksDetails: Writable<Map<string, TickerDetails> | null> = writable(null);

export const defaultWatchlist: Writable<string[]> = writable(["AAPL", "TSLA"]);

export const userWatchlist: Writable<string[]> = writable([]);

export const stocks: Readable<Map<string, Stock>> = readable(new Map([
    ["AAPL", {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    }],
    ["JPM", {
        ticker: "JPM",
        name: "JP Morgan Chase & Co.",
        exchange: "NYSE",
    }],
    ["KO", {
        ticker: "KO",
        name: "Coca-Cola Company (The)",
        exchange: "NYSE",
    }],
    ["SBUX", {
        ticker: "SBUX",
        name: "Starbucks Corporation",
        exchange: "NASDAQ",
    }],
    ["TSLA", {
        ticker: "TSLA",
        name: "Tesla, Inc.",
        exchange: "NASDAQ",
    }],
]));
