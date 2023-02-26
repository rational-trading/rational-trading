<script lang="ts">
    import api from "$lib/api";
    import {
        currentStock,
        user,
        userWatchlist,
        defaultWatchlist,
    } from "$lib/stores";

    const newRequest = () => api.user().watchlist_remove({ ticker: $currentStock.ticker });

    function minus() {
        if ($user) {
            userWatchlist.update((tickers: string[]) => {
                const index = tickers.indexOf($currentStock.ticker);
                if (index !== -1) {
                    newRequest();
                    tickers.splice(index, 1);
                }
                return tickers;
            });
        } else {
            defaultWatchlist.update((tickers: string[]) => {
                const index = tickers.indexOf($currentStock.ticker);
                if (index !== -1) {
                    tickers.splice(index, 1);
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
