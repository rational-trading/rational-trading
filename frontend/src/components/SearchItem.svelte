<script lang="ts">
    import type { Stock } from "$lib/types";
    import {
        displaySymbol,
        displayCompany,
        displayExchange,
        currentStock,
    } from "$lib/stores";

    export let data: Stock;
    export let active = true;

    function click() {
        currentStock.set({
            ticker: data.ticker,
            name: data.name,
            exchange: data.exchange,
        });
        active = false;
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.ticker}</th>
    <td class="has-text-left">{data.name}</td>
    <td class="has-text-right">{data.exchange}</td>
</tr>
