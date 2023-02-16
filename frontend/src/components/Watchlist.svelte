<script lang="ts">
    import {
        displaySymbol,
        displayCompany,
        displayExchange,
    } from "$lib/stores";

    interface Watchlist {
        symbol: string;
        last: number;
        chg: number;
        percentChg: number;
    }

    export let data: Watchlist;

    const color = data.chg >= 0 ? "success" : "warning";
    $: selected = data.symbol == $displaySymbol;

    function click() {
        displaySymbol.set(data.symbol);
        //would need an api method to get name of company and exchange based on stock symbol
        //displayCompany.set(data.company);
        //displayExchange.set(data.exchange);
    }
</script>

<tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-right">{data.last}</td>
    <td class="has-text-right has-text-{color}">{data.chg}</td>
    <td class="has-text-right has-text-{color}">{data.percentChg}%</td>
</tr>
