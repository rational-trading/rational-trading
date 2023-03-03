<script lang="ts">
    import Activity from "$components/Activity.svelte";
    import Asset from "$components/Asset.svelte";
    import { stocksDetails } from "$lib/stores";

    import api from "$lib/api";
    import type { Holding, PortfolioStats } from "$lib/api/portfolio";
    import type { Trade } from "$lib/api/trades";
    import { calculatePercentage, convertValueToMoney } from "$lib/functions";
    import { browser } from "$app/environment";

    let requestHoldings = api.pendingRequest<Holding[]>();
    const newRequestHoldings = () => api.portfolio().holdings();

    let requestTrades = api.pendingRequest<Trade[]>();
    const newRequestTrades = () => api.trades().personal();

    let requestStats = api.pendingRequest<PortfolioStats>();
    const newRequestStats = () => api.portfolio().stats();

    $: if (browser) {
        requestHoldings = newRequestHoldings();
        requestTrades = newRequestTrades();
        requestStats = newRequestStats();
    }

    function getCompanyNameFromTicker(ticker: string) {
        const stockDetail = $stocksDetails.get(ticker);
        if (stockDetail !== undefined) return stockDetail.company_name;
        throw new Error(`Company name not found for ticker ${ticker}`);
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
            style="height: 85%; overflow-y: auto;"
        >
            {#await requestStats}
                <p>Retrieving your portfolio summary...</p>
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
                            <p class="subtitle has-text-success">
                                {convertValueToMoney(response.unrealised_gain)}
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
            style="height: 85%; overflow-y: auto;"
        >
            {#await requestTrades}
                <p>Fetching your trades ...</p>
            {:then response}
                <table class="table is-fullwidth is-dark">
                    <thead>
                        <tr>
                            <th class="has-text-left">Time</th>
                            <th class="has-text-left">Symbol</th>
                            <th class="has-text-left">Side</th>
                            <th class="has-text-left"
                                ><abbr title="Quantity">Qty</abbr></th
                            >
                            <th>Price</th>
                            <th>Total value</th>
                            <th class="has-text-left">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each response as trade}
                            <Activity
                                data={{
                                    time: trade.time,
                                    symbol: trade.ticker,
                                    quantity_bought: trade.units_change,
                                    price: trade.balance_change,
                                    status: "Filled",
                                }}
                            />
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
        style="height: 85%; overflow-y: auto;"
    >
        {#await requestHoldings}
            <p>Fetching your portfolio ...</p>
        {:then response}
            {#each response as holding, i}
                <Asset
                    data={{
                        company: getCompanyNameFromTicker(holding.ticker),
                        symbol: holding.ticker,
                        qty: holding.units,
                        currentVal: holding.value,
                        glToday: 0,
                        glOverall: holding.unrealised_gain,
                    }}
                />
                {#if i < response.length - 1}
                    <hr style="background: #4a4a4a;" />
                {/if}
            {/each}
        {:catch error}
            <p>{error.message}</p>
        {/await}
    </div>
</div>
