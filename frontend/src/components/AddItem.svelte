<script lang="ts">
    import { watchlist, currentStock } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;
    export let active = true;

    function click() {
        watchlist.update((stocks: Stock[]) => {
            if (stocks.indexOf(stock) == -1) {
                return [...stocks, stock];
            } else {
                return stocks;
            }
        });
        currentStock.set(stock);
        active = false;
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{stock.ticker}</th>
    <td class="has-text-left">{stock.name}</td>
    <td class="has-text-right">{stock.exchange}</td>
</tr>
