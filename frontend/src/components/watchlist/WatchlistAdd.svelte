<script lang="ts">
    import { defaultWatchlist, user, userWatchlist } from "$lib/stores";
    import type { Stock } from "$lib/types";
    import api from "$lib/api";
    import SearchPane from "../search/SearchPane.svelte";

    export let currentStock: Stock;
    export let onAdd: (stock: Stock) => void;

    function onSelected(stock: Stock) {
        const newRequest = () => api.user().watchlist_add({ ticker: stock.ticker });

        if ($user) {
            userWatchlist.update((tickers: string[]) => {
                if (tickers.indexOf(stock.ticker) === -1) {
                    newRequest();
                    return [...tickers, stock.ticker];
                }
                return tickers;
            });
        } else {
            defaultWatchlist.update((tickers: string[]) => {
                if (tickers.indexOf(stock.ticker) === -1) {
                    return [...tickers, stock.ticker];
                }
                return tickers;
            });
        }

        onAdd(stock);
    }

    let text = currentStock.ticker;

    let active = false;
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a
        on:click={() => {
            if (
                ($user && $userWatchlist.includes(currentStock.ticker)) ||
                (!$user && $defaultWatchlist.includes(currentStock.ticker))
            ) {
                text = "";
            } else {
                text = currentStock.ticker;
            }
            active = true;
        }}><i class="fas fa-plus" /></a>
</span>

{#if active}
    <SearchPane
        {onSelected}
        {text}
        exit={() => {
            active = false;
        }} />
{/if}
