<script lang="ts">
    import { browser } from "$app/environment";
    import api from "$lib/api";
    import { currentStock } from "$lib/stores";
    import type { Stock } from "$lib/types";

    export let stock: Stock;

    let request = api.pendingRequest<{
        last: number;
        change: number;
        percentChange: number;
        color: "success" | "warning";
    }>();

    $: newRequest = () =>
        api
            .price(stock.ticker)
            .recent()
            .then((response) => {
                let last = response.close;
                let change = last - response.open;
                let percentChange = (change / response.open) * 100;
                let color: "success" | "warning" =
                    change >= 0 ? "success" : "warning";
                return {
                    last,
                    change,
                    percentChange,
                    color,
                };
            });

    $: if (browser) request = newRequest();

    $: selected = stock.ticker == $currentStock.ticker;

    function click() {
        currentStock.set(stock);
    }
</script>

{#await request}
    <tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">-</td>
        <td class="has-text-right has-text-grey">-</td>
        <td class="has-text-right has-text-grey">-</td>
    </tr>
{:then data}
    <tr class:is-selected={selected} style="cursor: pointer;" on:click={click}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">{data.last.toFixed(2)}</td>
        <td class="has-text-right has-text-{data.color}"
            >{data.change.toFixed(2)}</td>
        <td class="has-text-right has-text-{data.color}"
            >{data.percentChange.toFixed(2)}%</td>
    </tr>
{:catch error}
    <p>{error.message}</p>
{/await}
