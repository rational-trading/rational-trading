<script lang="ts">
    import api from "$lib/api";
    import type { TickerPrice } from "$lib/api/price";

    import { browser } from "$app/environment";

    let ticker = "AAPL";

    let request = api.pendingRequest<TickerPrice>();

    const newRequest = () => api.price(ticker).recent();

    $: if (browser) request = newRequest();
</script>

<h3 class="title is-3">Price Recent</h3>
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
    <div class="box has-background-grey">
        <p>Time: {new Date(response.time * 1000).toLocaleString()}</p>
        <p>Open: {response.open}</p>
        <p>Low: {response.low}</p>
        <p>High: {response.high}</p>
        <p>Close: {response.close}</p>
    </div>
{:catch error}
    <p>{error.message}</p>
{/await}
