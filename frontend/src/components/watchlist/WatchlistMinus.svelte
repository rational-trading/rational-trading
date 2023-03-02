<script lang="ts">
    import api from "$lib/api";
    import {
        user, userWatchlist, defaultWatchlist, stocks,
    } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let currentStock: Stock;
    export let setCurrentStock: (stock: Stock) => void;

    const newRequest = () => api.user().watchlist_remove({ ticker: currentStock.ticker });

    function minus() {
        if ($user) {
            userWatchlist.update((tickers: string[]) => {
                const index = tickers.indexOf(currentStock.ticker);
                if (index !== -1) {
                    newRequest();
                    tickers.splice(index, 1);
                    setCurrentStock(
                        $stocks.get(
                            $userWatchlist.length === 0 ?
                                "AAPL" :
                                $userWatchlist[0],
                        ),
                    );
                }
                return tickers;
            });
        } else {
            defaultWatchlist.update((tickers: string[]) => {
                const index = tickers.indexOf(currentStock.ticker);
                if (index !== -1) {
                    tickers.splice(index, 1);
                    setCurrentStock(
                        $stocks.get(
                            $defaultWatchlist.length === 0 ?
                                "AAPL" :
                                $defaultWatchlist[0],
                        ),
                    );
                }
                return tickers;
            });
        }
    }
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a on:click={minus}><i class="fas fa-minus" /></a>
</span>
