<script lang="ts">
    import type { Stock } from "$lib/types";
    import NewsTile from "$components/NewsTile.svelte";

    export let close: () => void;
    const stock: Stock = {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    };

    let buy = true;
    let units: number;
    let totalValue: number;

    let lowPrice = 153.22;
    let highPrice = 152.98;

    // eslint-disable-next-line no-restricted-globals
    $: validUnits = !isNaN(units);
    $: validTotalValue = !isNaN(totalValue);
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
                style="height: 75vh; border-right: 1px solid #4a4a4a;">
                <header class="title is-3 mb-0">
                    {stock.exchange}:{stock.ticker}
                </header>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block" style="height: 55%">
                    <div class="buttons has-addons is-centered mb-2">
                        <button
                            class="button is-large {buy
                                ? 'is-info is-selected'
                                : ''}"
                            on:click={() => (buy = true)}
                            style="height: 8vh; width: 50%; justify-content: left; text-align: left">
                            <div>
                                <p class="title is-4">Buy</p>
                                <p class="subtitle is-5">153.22</p>
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
                                <p class="subtitle is-5">152.94</p>
                            </div>
                        </button>
                    </div>

                    <!-- units -->
                    <div class="field" style="height: 30%">
                        <label class="label">Units</label>
                        <div class="control">
                            <input
                                class="input {validUnits ? '' : 'is-danger'}"
                                type="text"
                                placeholder="Units"
                                bind:value={units}
                                on:input={() =>
                                    (totalValue = units * lowPrice)} />
                        </div>
                        {#if !validUnits}
                            <p class="help is-danger">
                                Please enter a valid number.
                            </p>
                        {/if}
                    </div>

                    <div
                        class="mb-5"
                        style="width: 100%; height: 15px; border-bottom: 1px solid #4a4a4a; text-align: center">
                        <span
                            style="color: #4a4a4a; background-color: #363636; padding: 0 10px;">
                            or
                        </span>
                    </div>

                    <!-- total value -->

                    <div class="field" style="height: 30%">
                        <label class="label">Total value</label>
                        <div class="control">
                            <input
                                class="input {validTotalValue
                                    ? ''
                                    : 'is-danger'}"
                                type="text"
                                placeholder="Units"
                                bind:value={totalValue}
                                on:input={() =>
                                    (units = totalValue / lowPrice)} />
                        </div>
                        {#if !validUnits}
                            <p class="help is-danger">
                                Please enter a valid number.
                            </p>
                        {/if}
                    </div>
                </div>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block" style="height: 20%">
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
                            <strong>-</strong>
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
            </div>

            <!-- state the reason -->
            <div class="column">
                <div class="block mr-5" style="height: 45%;">
                    <header class="title is-5">
                        Did some news articles push you towards making this
                        trade? (Click to select)
                    </header>
                    <div
                        class="tile is-ancestor"
                        style="height: 90%; overflow-y: auto;">
                        <div class="tile is-vertical is-8">
                            <div class="tile">
                                <div class="tile is-parent is-vertical">
                                    <NewsTile />
                                    <NewsTile />
                                </div>
                                <div class="tile is-parent">
                                    <NewsTile />
                                </div>
                            </div>
                            <div class="tile is-parent">
                                <NewsTile />
                            </div>
                        </div>
                        <div class="tile is-parent">
                            <NewsTile />
                        </div>
                    </div>
                </div>

                <div class="block mr-5">
                    <header class="title is-5">
                        ...or was it something else?
                    </header>

                    <textarea
                        class="textarea"
                        placeholder="3 lines of textarea"
                        rows="3" />
                </div>

                <div class="block mr-5">
                    <button
                        class="button is-large is-info"
                        style="width: 100%"
                        disabled={!validUnits}>
                        <strong
                            >{buy ? "Buy" : "Sell"}
                            {validUnits ? units : ""}
                            {stock.exchange}:{stock.ticker}</strong>
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .modal-content {
        width: 80vw;
        height: 80vh;
        overflow-x: hidden;
        overflow-y: hidden;
        background: #363636;
        border-radius: 7px;
    }
</style>
