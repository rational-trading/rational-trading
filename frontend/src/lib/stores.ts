import { writable } from "svelte/store";
import type { Stock } from "$lib/types";

export const displaySymbol = writable("AAPL");
export const displayCompany = writable("Apple Inc");
export const displayExchange = writable("NASDAQ");

export const watchSymbols = writable(["AAPL"]);

export const currentStock: writable<Stock> = writable({ ticker: "AAPL", name: "Apple Inc", exchange: "NASDAQ" });
