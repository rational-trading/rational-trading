<script lang="ts">
    import {
        displaySymbol,
        displayCompany,
        displayExchange,
    } from "$lib/stores";

    interface SearchItem {
        symbol: string;
        company: string;
        exchange: string;
    }

    export let data: SearchItem;
    export let search = true;

    function click() {
        displaySymbol.set(data.symbol);
        displayCompany.set(data.company);
        displayExchange.set(data.exchange);
        search = false;
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-left">{data.company}</td>
    <td class="has-text-right">{data.exchange}</td>
</tr>
