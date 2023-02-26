<script lang="ts">
    import api from "$lib/api";
    import {
        defaultWatchlist,
        userWatchlist,
        currentStock,
        user,
    } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;
    export let onClick: () => void;

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

        if ($currentStock !== stock) {
            currentStock.set(stock);
        }
        onClick();
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{stock.ticker}</th>
    <td class="has-text-left">{stock.name}</td>
    <td class="has-text-right">{stock.exchange}</td>
</tr>
