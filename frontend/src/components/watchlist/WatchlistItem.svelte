<script lang="ts">
    import api from "$lib/api";
    import { stocks } from "$lib/stores";
    import type { Stock } from "$lib/types";
    import { browser } from "$app/environment";
    import type { DailyChange } from "$lib/api/price";

    export let selected: boolean;
    export let onClick: (stock: Stock) => void;
    export let ticker: string;
    const stock = $stocks.get(ticker);

    let recentPriceRequest = api.pendingRequest<number>();
    let changeRequest = api.pendingRequest<DailyChange & { color: string }>();

    $: newRecentPriceRequest = () =>
        api
            .price(stock.ticker)
            .recent()
            .then((response) => response.close);

    $: newChangeRequest = () =>
        api
            .price(stock.ticker)
            .daily_change()
            .then((change) => {
                return {
                    ...change,
                    color: change.price >= 0 ? "success" : "warning",
                };
            });

    $: if (browser) recentPriceRequest = newRecentPriceRequest();
    $: if (browser) changeRequest = newChangeRequest();
</script>

<tr
    class:is-selected={selected}
    style="cursor: pointer;"
    on:click={() => onClick(stock)}>
    <th class="has-text-left">{stock.ticker}</th>
    {#await recentPriceRequest}
        <td class="has-text-right">-</td>
    {:then price}
        <td class="has-text-right">{price.toFixed(2)}</td>
    {:catch}
        <td class="has-text-right">-</td>
    {/await}
    {#await changeRequest}
        <td class="has-text-right has-text-grey">-</td>
        <td class="has-text-right has-text-grey">-</td>
    {:then change}
        <td class="has-text-right has-text-{change.color}"
            >{change.price.toFixed(2)}</td>
        <td class="has-text-right has-text-{change.color}"
            >{change.percentage.toFixed(2)}%</td>
    {:catch}
        <td class="has-text-right has-text-grey">-</td>
        <td class="has-text-right has-text-grey">-</td>
    {/await}
</tr>
