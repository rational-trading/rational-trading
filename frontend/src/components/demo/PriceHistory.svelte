<script lang="ts">
    import api from "$lib/api";
    import type { TickerPrice } from "$lib/api/price";
    import { browser } from "$app/environment";

    let ticker = "AAPL";

    let request = api.pendingRequest<TickerPrice[]>();

    const newRequest = () => api.price(ticker).history();

    $: if (browser) request = newRequest();
</script>

<h3 class="title is-3">Price History</h3>
<p>
    <input class="input" bind:value={ticker} placeholder="Ticker" />
</p>
<br />
<p>
    <button class="button is-info" on:click={() => (request = newRequest())}
        >Send</button>
</p>
<br />
{#await request}
    <p>Waiting...</p>
{:then response}
    {#each response as price}
        <div class="box has-background-grey">
            <p>Time: {new Date(price.time * 1000).toLocaleString()}</p>
            <p>Open: {price.open}</p>
            <p>Low: {price.low}</p>
            <p>High: {price.high}</p>
            <p>Close: {price.close}</p>
        </div>
    {/each}
{:catch error}
    <p>{error.message}</p>
{/await}
