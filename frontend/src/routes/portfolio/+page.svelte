<script lang="ts">
    import Activity from "$components/Activity.svelte";
    import Asset from "$components/Asset.svelte";

    import { Status } from "$types/status";

    const activities = [
        {
            time: "2023-02-08 21:09:19",
            symbol: "AAPL",
            side: "Buy",
            qty: 10,
            price: 151.66,
            totalVal: 1516.63,
            status: Status.Pending,
        },
        {
            time: "2023-02-08 21:09:19",
            symbol: "AAPL",
            side: "Buy",
            qty: 10,
            price: 151.66,
            totalVal: 1516.63,
            status: Status.Filled,
        },
        {
            time: "2023-02-08 21:09:19",
            symbol: "AAPL",
            side: "Buy",
            qty: 10,
            price: 151.66,
            totalVal: 1516.63,
            status: Status.Rejected,
        },
    ];
    const assets = [
        {
            company: "Tesla, Inc.",
            symbol: "TSLA",
            qty: 10,
            currentVal: 1996.82,
            glToday: -53.28,
            glOverall: -18.02,
        },
        {
            company: "Apple, Inc.",
            symbol: "AAPL",
            qty: 10,
            currentVal: 1996.82,
            glToday: 53.28,
            glOverall: 18.02,
        },
    ];
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
            <div>
                <p class="heading">Current value</p>
                <p class="title">£13,267.39</p>
            </div>
            <div class="block" style="height: 20%" />
            <div class="columns">
                <div class="column">
                    <div>
                        <p class="heading">Today's gain/loss</p>
                        <p class="subtitle has-text-success">£28.27 (1.50%)</p>
                    </div>
                </div>
                <div class="column">
                    <div>
                        <p class="heading">Overall gain/loss</p>
                        <p class="subtitle has-text-success">
                            £1,937.25 (14.60%)
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="column px-0">
        <h2 class="title is-5 ml-5">Recent Activities</h2>
        <div
            class="box mx-5 py-2 has-background-grey-darker"
            style="height: 85%; overflow-y: auto;">
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
                        <th class="has-text-left">Status</th>
                    </tr>
                </thead>
                <tbody>
                    {#each activities as item}
                        <Activity data={item} />
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
</div>

<div class="block mt-5">
    <h2 class="title is-5 ml-5">Details</h2>
    <div
        class="box mx-5 has-background-grey-darker"
        style="height: 85%; overflow-y: auto;">
        {#each assets as item, i}
            <Asset data={item} />
            {#if i < assets.length - 1}
                <hr style="background: #4a4a4a;" />
            {/if}
        {/each}
    </div>
</div>
