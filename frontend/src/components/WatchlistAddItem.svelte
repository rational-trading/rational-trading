<script lang="ts">
    import type { Stock } from "$lib/types";

    export let stock: Stock;
    export let onClick: (stock: Stock) => void;

    function click() {
        onClick(stock);
    }
</script>

{#if stock.name === "Loading..."}
    <div
        style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
        <p>Loading...</p>
    </div>
{:else}
    <tr style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-left">{stock.name}</td>
        <td class="has-text-right">{stock.exchange}</td>
    </tr>
{/if}
