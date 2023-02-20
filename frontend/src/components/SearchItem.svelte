<script lang="ts">
    import type { Stock } from "$lib/types";
    import { currentStock } from "$lib/stores";

    export let data: Stock;
    export let active = true;

    function click() {
        currentStock.set(data);
        active = false;
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.ticker}</th>
    <td class="has-text-left">{data.name}</td>
    <td class="has-text-right">{data.exchange}</td>
</tr>
