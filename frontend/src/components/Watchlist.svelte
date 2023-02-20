<script lang="ts">
    import api from "$lib/api";
    import { currentStock } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;

    let last: number;
    let chg: number;
    let percentChg: number;

    const fetchData = async () => {
        const response = await api.price(stock.ticker).recent();
        // TODO: this is the wrong way to calculate the values
        // need an api endpoint for accessing the prices on the previous market day
        last = response.close;
        chg = last - response.open;
        percentChg = (chg / response.open) * 100;
        return response;
    };

    let response = fetchData();

    $: color = chg >= 0 ? "success" : "warning";
    $: selected = stock.ticker == $currentStock.ticker;

    function click() {
        currentStock.set(stock);
    }
</script>

{#await response}
    <tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">-</td>
        <td class="has-text-right has-text-{color}">-</td>
        <td class="has-text-right has-text-{color}">-</td>
    </tr>
{:then}
    <tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">{last.toFixed(2)}</td>
        <td class="has-text-right has-text-{color}">{chg.toFixed(2)}</td>
        <td class="has-text-right has-text-{color}"
            >{percentChg.toFixed(2)}%</td>
    </tr>
{:catch error}
    <p>{error.message}</p>
{/await}
