<script lang="ts">
    import { displaySymbol } from "$lib/stores";

    interface SearchItem {
        symbol: string;
        company: string;
        exchange: string;
    }

    export let data: SearchItem;

    function click() {
        displaySymbol.set(data.symbol);
    }
</script>

<tr class:is-selected={false} style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-left">{data.company}</td>
    <td class="has-text-right">{data.exchange}</td>
</tr>
