<script lang="ts">
    import NewsTile from "$components/NewsTile.svelte";
    import api from "$lib/api";
    import type { TickerPrice } from "$lib/api/price";
    import type { News } from "$lib/api/news";
    import { stocks } from "$lib/stores";
    import { browser } from "$app/environment";

    export let close: () => void;

    let buy = true;

    let useUnits = true;
    let units: number;
    let totalValue: number;

    // eslint-disable-next-line no-restricted-globals
    $: validUnits = units !== undefined && !isNaN(units) && units > 0;

    $: validTotalValue =
        // eslint-disable-next-line no-restricted-globals
        totalValue !== undefined && !isNaN(totalValue) && totalValue > 0;

    export let ticker: string;
    $: stock = $stocks.get(ticker);

    let priceRequest = api.pendingRequest<TickerPrice>();
    $: newPriceRequest = () => api.price(stock.ticker).recent();
    $: if (browser) priceRequest = newPriceRequest();

    let newsRequest = api.pendingRequest<News[]>();
    $: newNewsRequest = () => api.news().get(stock.ticker, 20);
    $: if (browser) newsRequest = newNewsRequest();

    let articles: string[] = [];
    let textEvidence = "";
    async function submit() {
        try {
            await api.trades().make({
                ticker: stock.ticker,
                side: buy ? "BUY" : "SELL",
                type: useUnits ? "UNITS" : "PRICE",
                amount: useUnits ? units : totalValue,
                text_evidence: textEvidence,
                article_evidence: articles,
            });
            alert("Trade succeeded.");
            close();
        } catch {
            alert("Oops! Something went wrong.");
        }
    }
</script>

<div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={close} />
    <div class="modal-content">
        <div style="display: flex; justify-content: right;">
            <button class="button is-ghost" on:click={close}>
                <span class="icon is-large">
                    <i class="fas fa-xmark" />
                </span>
            </button>
        </div>

        <div class="columns">
            <!-- trading stats -->
            <div
                class="column is-one-third ml-5"
                style="height: 85vh; border-right: 1px solid #4a4a4a;">
                <header class="title is-3 mb-0">
                    {stock.exchange}:{stock.ticker}
                </header>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block" style="height: 30vh">
                    <div class="buttons has-addons is-centered mb-2">
                        <button
                            class="button is-large {buy
                                ? 'is-info is-selected'
                                : ''}"
                            on:click={() => (buy = true)}
                            style="height: 8vh; width: 50%; justify-content: left; text-align: left">
                            <div>
                                <p class="title is-4">Buy</p>
                                <p class="subtitle is-5">
                                    {#await priceRequest}
                                        -
                                    {:then price}
                                        {price.high}
                                    {/await}
                                </p>
                            </div>
                        </button>
                        <button
                            class="button is-large {buy
                                ? ''
                                : 'is-info is-selected'}"
                            on:click={() => (buy = false)}
                            style="height: 8vh; width: 50%; justify-content: right; text-align: right">
                            <div>
                                <p class="title is-4">Sell</p>
                                <p class="subtitle is-5">
                                    {#await priceRequest}
                                        -
                                    {:then price}
                                        {price.low}
                                    {/await}
                                </p>
                            </div>
                        </button>
                    </div>

                    <div class="select mb-4">
                        <select bind:value={useUnits}>
                            <option value={true}>Units</option>
                            <option value={false}>Total value</option>
                        </select>
                    </div>

                    {#if useUnits}
                        <!-- units -->
                        <div class="field" style="height: 25%">
                            <div class="control">
                                <input
                                    class="input {validUnits
                                        ? ''
                                        : 'is-danger'}"
                                    type="text"
                                    placeholder="Units"
                                    bind:value={units}
                                    on:input={async () => {
                                        const price = await priceRequest;
                                        totalValue =
                                            units *
                                            (buy ? price.high : price.low);
                                    }} />
                            </div>
                            {#if !validUnits}
                                <p class="help is-danger">
                                    Please enter a valid number.
                                </p>
                            {/if}
                        </div>
                    {:else}
                        <!-- total value -->
                        <div class="field" style="height: 25%">
                            <div class="control">
                                <input
                                    class="input {validTotalValue
                                        ? ''
                                        : 'is-danger'}"
                                    type="text"
                                    placeholder="Total value"
                                    bind:value={totalValue}
                                    on:input={async () => {
                                        const price = await priceRequest;
                                        units =
                                            totalValue /
                                            (buy ? price.high : price.low);
                                    }} />
                            </div>
                            {#if !validTotalValue}
                                <p class="help is-danger">
                                    Please enter a valid number.
                                </p>
                            {/if}
                        </div>
                    {/if}
                </div>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block" style="height: 20vh">
                    <header class="title is-6">Order info</header>

                    <div style="display: flex; justify-content: space-between;">
                        <div style="vertical-align: baseline; ">Units</div>
                        <div style="vertical-align: baseline; ">
                            <strong>{validUnits ? units : "-"}</strong>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between;">
                        <div style="vertical-align: baseline; ">
                            Per-unit value
                        </div>
                        <div style="vertical-align: baseline; ">
                            <strong>
                                {#await priceRequest}
                                    -
                                {:then price}
                                    {buy ? price.high : price.low}
                                {/await}
                            </strong>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between;">
                        <div style="vertical-align: baseline; ">
                            Total value
                        </div>
                        <div style="vertical-align: baseline; ">
                            <strong
                                >{validTotalValue ? totalValue : "-"}</strong>
                        </div>
                    </div>
                </div>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block">
                    <!-- force refresh button label -->
                    {#key units}
                        <button
                            class="button is-large is-info mb-5"
                            style="width: 100%"
                            on:click={submit}
                            disabled={!validUnits}>
                            <strong
                                >{buy ? "Buy" : "Sell"}
                                {validUnits ? units : ""}
                                {stock.exchange}:{stock.ticker}</strong>
                        </button>
                    {/key}
                </div>
            </div>

            <!-- state the reason -->
            <div class="column" style="height: 85vh;">
                <div class="block mr-5" style="height: 50vh;">
                    <header class="title is-5">
                        Did some news articles push you towards making this
                        trade? (Click to select)
                    </header>
                    <div
                        class="block"
                        style="height: 85%; overflow-x: hidden; overflow-y: auto;">
                        <div class="tile is-ancestor">
                            {#await newsRequest}
                                <div
                                    style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                                    <p>Loading...</p>
                                </div>
                            {:then responses}
                                <div class="tile is-parent is-vertical">
                                    {#each responses.filter((_element, index) => index % 2 === 0) as response}
                                        <NewsTile
                                            data={response}
                                            bind:articles />
                                    {/each}
                                </div>
                                <div class="tile is-parent is-vertical">
                                    {#each responses.filter((_element, index) => index % 2 === 1) as response}
                                        <NewsTile
                                            data={response}
                                            bind:articles />
                                    {/each}
                                </div>
                            {:catch error}
                                <div
                                    style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                                    <p>{error.message}</p>
                                </div>
                            {/await}
                        </div>
                    </div>
                </div>

                <div class="block mr-5">
                    <header class="title is-5">
                        And did any financial stats play into this?
                    </header>

                    <div class="columns">
                        <div class="column">
                            <label class="checkbox">
                                <input type="checkbox" />
                                Remember me
                            </label>
                        </div>
                        <div class="column">
                            <label class="checkbox">
                                <input type="checkbox" />
                                Remember me
                            </label>
                        </div>
                        <div class="column">
                            <label class="checkbox">
                                <input type="checkbox" />
                                Remember me
                            </label>
                        </div>
                        <div class="column">
                            <label class="checkbox">
                                <input type="checkbox" />
                                Remember me
                            </label>
                        </div>
                    </div>
                </div>

                <div class="block mr-5">
                    <header class="title is-5">
                        ...or was it something else?
                    </header>

                    <textarea
                        class="textarea"
                        placeholder="Share your insights..."
                        rows="3"
                        bind:value={textEvidence} />
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .modal-content {
        width: 90vw;
        height: 90vh;
        overflow-x: hidden;
        background: #363636;
        border-radius: 7px;
    }
</style>
