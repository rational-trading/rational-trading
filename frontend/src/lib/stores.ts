import { writable } from "svelte/store";

export const displaySymbol = writable("AAPL");
export const displayCompany = writable("Apple Inc");
export const displayExchange = writable("NASDAQ");

export const watchSymbols = writable(["AAPL"]);
