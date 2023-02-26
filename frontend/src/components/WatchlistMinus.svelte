<script lang="ts">
    import { currentStock, watchlist } from "$lib/stores";
    import type { Stock } from "$lib/types";

    function minus() {
        watchlist.update((stocks: Stock[]) => {
            let index = stocks.indexOf($currentStock);
            if (index !== -1) {
                stocks.splice(index, 1);
            }
            return stocks;
        });
    }
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a on:click={minus}><i class="fas fa-minus" /></a>
</span>
