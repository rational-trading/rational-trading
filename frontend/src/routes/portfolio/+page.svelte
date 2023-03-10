<script lang="ts">
    import Activity from "$components/Activity.svelte";
    import Asset from "$components/Asset.svelte";

    import api from "$lib/api";
    import type { Holding, PortfolioStats } from "$lib/api/portfolio";
    import type { Trade } from "$lib/api/trades";
    import { calculatePercentage, convertValueToMoney } from "$lib/functions";
    import { stocks, user } from "$lib/stores";
    import { browser } from "$app/environment";
    import { goto } from "$app/navigation";

    let requestHoldings = api.pendingRequest<Holding[]>();
    const newRequestHoldings = () => api.portfolio().holdings();

    let requestTrades = api.pendingRequest<Trade[]>();
    const newRequestTrades = () => api.trades().personal();

    let requestStats = api.pendingRequest<PortfolioStats>();
    const newRequestStats = () => api.portfolio().stats();

    $: if (browser && $user === false) goto("/");

    $: if (browser) {
        requestHoldings = newRequestHoldings();
        requestTrades = newRequestTrades();
        requestStats = newRequestStats();
    }
</script>

<div class="block mt-5 ml-5">
    <h1 class="title is-2">Portfolio</h1>
</div>

<div class="columns mt-5" style="height: 17rem; width: calc(100vw + 12px);">
    <div class="column is-two-fifths">
        <h2 class="title is-5 ml-5">Summary</h2>
        <div
            class="box mx-5 has-background-grey-darker"
            style="height: 85%; overflow-y: auto;">
            {#await requestStats}
                <div
                    style="height: 20%; display: flex; justify-content: center; align-items: center;">
                    <p>Retrieving your portfolio summary...</p>
                </div>
            {:then response}
                <div>
                    <p class="heading">Current value</p>
                    <p class="title">
                        {convertValueToMoney(response.holdings_value)}
                    </p>
                </div>
                <div class="block" style="height: 20%" />
                <div class="columns">
                    <div class="column">
                        <div>
                            <p class="heading">Today's gain/loss</p>
                            <p class="subtitle has-text-success">TODO</p>
                        </div>
                    </div>
                    <div class="column">
                        <div>
                            <p class="heading">Overall gain/loss</p>
                            <p
                                class="subtitle has-text-{response.unrealised_gain >=
                                0 ?
                                    'success' :
                                    'warning'}">
                                {response.unrealised_gain >= 0 ? "" : "-"}
                                {convertValueToMoney(
                                    Math.abs(response.unrealised_gain),
                                )}
                                (
                                {calculatePercentage(
                                    response.unrealised_gain,
                                    response.holdings_value,
                                )})
                            </p>
                        </div>
                    </div>
                </div>
            {:catch error}
                console.log({error.message});
            {/await}
        </div>
    </div>

    <div class="column px-0">
        <h2 class="title is-5 ml-5">Recent Activities</h2>
        <div
            class="box mx-5 py-2 has-background-grey-darker"
            style="height: 85%; overflow-y: auto;">
            {#await requestTrades}
                <div
                    class="mt-3"
                    style="height: 20%; display: flex; justify-content: center; align-items: center;">
                    <p>Fetching your trades...</p>
                </div>
            {:then response}
                <table class="table is-fullwidth is-dark">
                    <thead>
                        <tr>
                            <th class="has-text-left">Time</th>
                            <th class="has-text-left">Symbol</th>
                            <th class="has-text-left">Side</th>
                            <th class="has-text-left"
                                ><abbr title="Quantity">Qty</abbr></th>
                            <th>Price</th>
                            <th>Total value</th>
                            <th class="has-text-left">Feedback</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each response as trade}
                            <Activity data={trade} />
                        {/each}
                    </tbody>
                </table>
            {:catch error}
                <p>{error.message}</p>
            {/await}
        </div>
    </div>
</div>

<div class="block mt-5">
    <h2 class="title is-5 ml-5">Details</h2>
    <div
        class="box mx-5 has-background-grey-darker"
        style="height: 85%; overflow-y: auto;">
        {#await requestHoldings}
            <div
                style="height: 20%; display: flex; justify-content: center; align-items: center;">
                <p>Fetching your portfolio...</p>
            </div>
        {:then response}
            {#each response as holding, i}
                <Asset
                    data={{
                        company: $stocks.get(holding.ticker).name,
                        symbol: holding.ticker,
                        qty: holding.units,
                        currentVal: holding.value,
                        glToday: 0,
                        glOverall: holding.unrealised_gain,
                    }} />
                {#if i < response.length - 1}
                    <hr style="background: #4a4a4a;" />
                {/if}
            {/each}
        {:catch error}
            <p>{error.message}</p>
        {/await}
    </div>
</div>
