<script lang="ts">
    import type { Stock } from "$lib/types";
    import { currentStock } from "$lib/stores";

    export let stock: Stock;

    export let onClick: () => void;

    function click() {
        if ($currentStock !== stock) {
            currentStock.set(stock);
        }
        onClick();
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
