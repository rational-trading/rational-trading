<script lang="ts">
    import api from "$lib/api";
    import { currentStock } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;

    const newRequest = () => api.price(stock.ticker).recent();
    let request = newRequest();

    const last = 100.3;
    const chg = 1;
    const percentChg = 0.1;

    $: color = chg >= 0 ? "success" : "warning";
    $: selected = stock.ticker == $currentStock.ticker;

    function click() {
        currentStock.set(stock);
    }
</script>

<tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{stock.ticker}</th>
    {#await request}
        <td class="has-text-right">-</td>
        <td class="has-text-right has-text-{color}">-</td>
        <td class="has-text-right has-text-{color}">-</td>
    {:then response}
        <td class="has-text-right">{response.close}</td>
        <td class="has-text-right has-text-{color}">{chg}</td>
        <td class="has-text-right has-text-{color}">{percentChg}%</td>
    {:catch error}
        <p>{error.message}</p>
    {/await}
</tr>
