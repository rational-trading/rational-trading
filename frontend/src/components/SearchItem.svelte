<script lang="ts">
    import type { Stock } from "$lib/types";
    import { currentStock } from "$lib/stores";

    export let stock: Stock;

    export let onClick: () => void;

    function click() {
        currentStock.set(stock);
        onClick();
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{stock.ticker}</th>
    <td class="has-text-left">{stock.name}</td>
    <td class="has-text-right">{stock.exchange}</td>
</tr>
