<script lang="ts">
    import api from "$lib/api";
    import { defaultWatchlist, userWatchlist, user } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;
    export let onClick: (stock: Stock) => void;

    const newRequest = () => api.user().watchlist_add({ ticker: stock.ticker });

    function click() {
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
        onClick(stock);
    }
</script>

{#if stock.name === "Loading..."}
    <div
        style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
        <p>Loading...</p>
    </div>
{:else}
    <tr style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-left">{stock.name}</td>
        <td class="has-text-right">{stock.exchange}</td>
    </tr>
{/if}
