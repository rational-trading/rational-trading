<script lang="ts">
    import api from "$lib/api";
    import type { Financials } from "$lib/api/financials";

    import { browser } from "$app/environment";

    let ticker = "AAPL";

    let request = api.pendingRequest<Financials>();

    const newRequest = () => api.financials().get(ticker);

    $: if (browser) request = newRequest();
</script>

<h3 class="title is-3">Related News</h3>
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
        <p>price_earning_ratio: {response.price_earning_ratio}</p>
        <p>earnings_per_share: {response.earnings_per_share}</p>
        <p>debt_to_equity: {response.debt_to_equity}</p>
        <p>current_ratio: {response.current_ratio}</p>
        <p>score: {response.score}</p>
    </div>
{:catch error}
    <p>{error.message}</p>
{/await}
