<script lang="ts">
    import api from "$lib/api";
    import { stocks } from "$lib/stores";
    import type { Stock } from "$lib/types";
    import { browser } from "$app/environment";

    export let selected: boolean;
    export let onClick: (stock: Stock) => void;
    export let ticker: string;
    const stock = $stocks.get(ticker);

    let request = api.pendingRequest<{
        last: number;
        change: number;
        percentChange: number;
        color: "success" | "warning";
    }>();

    $: newRequest = () => api
        .price(stock.ticker)
        .recent()
        .then((response) => {
            const last = response.close;
            const change = last - response.open;
            const percentChange = (change / response.open) * 100;
            const color: "success" | "warning" =
                    change >= 0 ? "success" : "warning";
            return {
                last,
                change,
                percentChange,
                color,
            };
        });

    $: if (browser) request = newRequest();
</script>

{#await request}
    <tr
        class:is-selected={selected}
        style="cursor: pointer;"
        on:click={() => onClick(stock)}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">-</td>
        <td class="has-text-right has-text-grey">-</td>
        <td class="has-text-right has-text-grey">-</td>
    </tr>
{:then data}
    <tr
        class:is-selected={selected}
        style="cursor: pointer;"
        on:click={() => onClick(stock)}>
        <th class="has-text-left">{stock.ticker}</th>
        <td class="has-text-right">{data.last.toFixed(2)}</td>
        <td class="has-text-right has-text-{data.color}"
            >{data.change.toFixed(2)}</td>
        <td class="has-text-right has-text-{data.color}"
            >{data.percentChange.toFixed(2)}%</td>
    </tr>
{:catch}
    <tr
        class:is-selected={selected}
        style="cursor: pointer;"
        on:click={() => onClick(stock)}>
        <th class="has-text-left">-</th>
        <td class="has-text-right">-</td>
        <td class="has-text-right has-text-grey">-</td>
        <td class="has-text-right has-text-grey">-</td>
    </tr>
{/await}
