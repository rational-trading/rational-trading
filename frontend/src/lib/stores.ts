import { writable, type Writable } from "svelte/store";
import type { Stock } from "$lib/types";

export const user: Writable<{ username: string } | null> = writable(null);

export const currentStock: Writable<Stock> = writable({ ticker: "AAPL", name: "Apple Inc.", exchange: "XNAS" });

export const stocksDetails: Writable<Map<string, Stock> | null> = writable(null);

export const defaultWatchlist: Writable<string[]> = writable(["AAPL", "TSLA"]);

export const userWatchlist: Writable<string[]> = writable([]);
