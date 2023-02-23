<script lang="ts">
    import type { Stock } from "$lib/types";

    export let close: () => void;
    let stock: Stock = {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    };

    let buy = true;
    let units: number;
    $: validUnits = !((units !== undefined && isNaN(units)) || units < 0.01);
</script>

<div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={close} />
    <div class="modal-content">
        <div class="is-flex is-flex-direction-column">
            <div class="is-align-self-flex-end">
                <button class="button is-ghost" on:click={close}>
                    <span class="icon is-large">
                        <i class="fas fa-xmark" />
                    </span>
                </button>
            </div>

            <div class="columns">
                <!-- trading stats -->
                <div
                    class="column is-one-third ml-3"
                    style="height: 75vh; border-right: 1px solid #4a4a4a;">
                    <header class="title is-3 mb-0">
                        {stock.exchange}:{stock.ticker}
                    </header>

                    <hr style="background: #4a4a4a; height: 1px" />

                    <div class="buttons has-addons is-centered">
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

                    <div class="block">
                        <input
                            class="input {validUnits ? '' : 'is-danger'}"
                            type="text"
                            placeholder="Units"
                            bind:value={units} />

                        {#if units !== undefined && isNaN(units)}
                            <p class="has-text-danger">
                                Please enter a valid number.
                            </p>
                        {:else if units < 0.01}
                            <p class="has-text-danger">
                                Specified value is less than the minimum of
                                0.01.
                            </p>
                        {/if}

                        <hr style="background: #4a4a4a; height: 1px" />

                        <header class="title is-6">Order info</header>

                        <div
                            style="display: flex; justify-content: space-between;">
                            <div style="vertical-align: baseline; ">Units</div>
                            <div style="vertical-align: baseline; ">
                                <strong>{validUnits ? units : "-"}</strong>
                            </div>
                        </div>

                        <div
                            style="display: flex; justify-content: space-between;">
                            <div style="vertical-align: baseline; ">
                                Per unit value
                            </div>
                            <div style="vertical-align: baseline; ">
                                <strong>-</strong>
                            </div>
                        </div>

                        <div
                            style="display: flex; justify-content: space-between;">
                            <div style="vertical-align: baseline; ">
                                Trade value
                            </div>
                            <div style="vertical-align: baseline; ">
                                <strong>-</strong>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- state the reason -->
                <div class="column">
                    <p>Random placeholder</p>
                    {#if buy}
                        <p>Buy</p>
                    {:else}
                        <p>Sell</p>
                    {/if}
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .modal-content {
        width: 80vw;
        height: 80vh;
        background: #363636;
        border-radius: 7px;
    }
</style>
