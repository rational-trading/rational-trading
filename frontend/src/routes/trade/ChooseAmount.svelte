<script lang="ts">
    import type { MakeTrade } from "$lib/api/trades";
    import api from "$lib/api";
    import type { TickerPrice } from "$lib/api/price";
    import { stocks } from "$lib/stores";
    import { browser } from "$app/environment";
    import { stepUrl } from "./Steps.svelte";
    import { goto } from "$app/navigation";

    export let initialState: MakeTrade;
    export let currentState: MakeTrade;

    $: ({ ticker, type, amount: initialAmount, side } = initialState);
    $: currentState = {
        ...initialState,
        type,
        amount,
        side,
    };

    $: stock = $stocks.get(ticker);
    $: BUY = side === "BUY";
    $: UNITS = type === "UNITS";

    $: textAmount = initialAmount === 0 ? "" : initialAmount.toString();
    $: amount = Number.isNaN(parseFloat(textAmount))
        ? 0
        : parseFloat(textAmount);
    $: validAmount =
        textAmount.match(/^\d+(\.\d+)?$/) &&
        !Number.isNaN(amount) &&
        amount > 0;

    let priceRequest = api.pendingRequest<TickerPrice>();
    $: newPriceRequest = () => api.price(stock.ticker).recent();
    $: if (browser) priceRequest = newPriceRequest();

    $: getTradePrice = (price: TickerPrice) => (BUY ? price.high : price.low);

    function onTypeChange(
        e: Event & {
            currentTarget: EventTarget & HTMLSelectElement;
        }
    ) {
        type = e.currentTarget.value as "PRICE" | "UNITS";
    }
</script>

<div class="columns">
    <div class="column" />
    <div class="column is-one-third ml-5">
        <header class="title is-3 mb-0">
            {stock.exchange} : {stock.ticker}
        </header>

        <hr style="background: #4a4a4a; height: 1px" />

        <div class="block">
            <div class="buttons has-addons is-centered mb-2">
                <button
                    class="button is-large {BUY ? 'is-info is-selected' : ''}"
                    on:click={() => (side = "BUY")}
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
                    class="button is-large {BUY ? '' : 'is-info is-selected'}"
                    on:click={() => (side = "SELL")}
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
            <br />

            <div class="field has-addons">
                <div class="control is-expanded">
                    <input
                        class="input  is-fullwidth {validAmount
                            ? ''
                            : 'is-danger'} "
                        type="text"
                        placeholder={UNITS ? "Units" : "Total Value"}
                        value={textAmount}
                        on:keyup={(e) =>
                            (textAmount = e.currentTarget.value)} />
                </div>
                <div class="control">
                    <div class="select  {validAmount ? '' : 'is-danger'}">
                        <select value={type} on:change={onTypeChange}>
                            <option value="UNITS">Units</option>
                            <option value="PRICE">Dollars</option>
                        </select>
                    </div>
                </div>
            </div>
            {#if !validAmount}
                <p class="help is-danger">
                    Please enter a valid number greater than 0.
                </p>
            {:else}
                <p class="help"><wbr /></p>
            {/if}
        </div>

        <hr style="background: #4a4a4a; height: 1px" />

        <div class="block">
            <header class="title is-6">Order info (estimated)</header>

            {#await priceRequest}
                <p>Loading...</p>
            {:then price}
                <div style="display: flex; justify-content: space-between;">
                    <div style="vertical-align: baseline; ">Units</div>

                    <div style="vertical-align: baseline; ">
                        <strong>
                            {!validAmount
                                ? "-"
                                : (UNITS
                                      ? amount
                                      : amount / getTradePrice(price)
                                  ).toFixed(6)}
                        </strong>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between;">
                    <div style="vertical-align: baseline; ">Per-unit value</div>
                    <div style="vertical-align: baseline; ">
                        <strong>
                            ${BUY ? price.high : price.low}
                        </strong>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between;">
                    <div style="vertical-align: baseline; ">Total value</div>
                    <div style="vertical-align: baseline; ">
                        <strong>
                            {!validAmount
                                ? "-"
                                : `$${(UNITS
                                      ? amount * getTradePrice(price)
                                      : amount
                                  ).toFixed(2)}`}</strong>
                    </div>
                </div>
            {/await}
        </div>

        <hr style="background: #4a4a4a; height: 1px" />
        <div class="block">
            <div class="columns">
                <div class="column" style="text-align:right;">
                    <button
                        class="button is-text"
                        on:click={() => goto(stepUrl(2, currentState))}
                        >Back (Add Evidence)</button>
                    <button
                        class="button is-info"
                        disabled={!validAmount}
                        on:click={() => goto(stepUrl(4, currentState))}
                        >Continue</button>
                </div>
            </div>
        </div>
    </div>

    <div class="column" />
</div>
