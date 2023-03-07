import { writable, type Writable } from "svelte/store";
import type { Stock } from "$lib/types";

export const user: Writable<{ username: string } | null | false> = writable(null);

export const stocks: Writable<{ get: (ticker: string) => Stock, all: Stock[] }> = writable({
    get: (ticker) => ({
        ticker,
        name: "Loading...",
        exchange: "Loading...",
    }),
    all: [],
});

export const defaultWatchlist: Writable<string[]> = writable(["AAPL", "TSLA"]);

export const userWatchlist: Writable<string[]> = writable([]);
