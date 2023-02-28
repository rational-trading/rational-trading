<script lang="ts">
    import type { Stock } from "$lib/types";

    export let close: () => void;
    const stock: Stock = {
        ticker: "AAPL",
        name: "Apple Inc",
        exchange: "NASDAQ",
    };

    let buy = true;
    let units: number;

    // eslint-disable-next-line no-restricted-globals
    $: validNumber = !isNaN(units);
    $: validValue = !(units < 0.01);
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

                <div class="block" style="height: 30%">
                    <div class="buttons has-addons is-centered">
                        <button
                            class="button is-large {buy ?
                                'is-info is-selected' :
                                ''}"
                            on:click={() => (buy = true)}
                            style="height: 8vh; width: 50%; justify-content: left; text-align: left">
                            <div>
                                <p class="title is-4">Buy</p>
                                <p class="subtitle is-5">153.22</p>
                            </div>
                        </button>
                        <button
                            class="button is-large {buy ?
                                '' :
                                'is-info is-selected'}"
                            on:click={() => (buy = false)}
                            style="height: 8vh; width: 50%; justify-content: right; text-align: right">
                            <div>
                                <p class="title is-4">Sell</p>
                                <p class="subtitle is-5">152.94</p>
                            </div>
                        </button>
                    </div>

                    <input
                        class="input {validNumber && validValue ?
                            '' :
                            'is-danger'}"
                        type="text"
                        placeholder="Units"
                        bind:value={units} />

                    {#if !validNumber}
                        <p class="has-text-danger">
                            Please enter a valid number.
                        </p>
                    {:else if !validValue}
                        <p class="has-text-danger">
                            Specified value is less than the minimum of 0.01.
                        </p>
                    {/if}
                </div>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block" style="height: 30%">
                    <header class="title is-6">Order info</header>

                    <div style="display: flex; justify-content: space-between;">
                        <div style="vertical-align: baseline; ">Units</div>
                        <div style="vertical-align: baseline; ">
                            <strong
                                >{validNumber && validValue ?
                                    units :
                                    "-"}</strong>
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
                            Trade value
                        </div>
                        <div style="vertical-align: baseline; ">
                            <strong>-</strong>
                        </div>
                    </div>
                </div>

                <hr style="background: #4a4a4a; height: 1px" />

                <div class="block">
                    <button
                        class="button is-large"
                        style="width: 100%"
                        disabled>
                        <strong
                            >{buy ? "Buy" : "Sell"}
                            {validNumber && validValue ? units : ""}
                            {stock.exchange}:{stock.ticker}</strong>
                    </button>
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

<style>
    .modal-content {
        width: 80vw;
        height: 80vh;
        overflow-x: hidden;
        background: #363636;
        border-radius: 7px;
    }
</style>
