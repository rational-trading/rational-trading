<script lang="ts">
    import api from "$lib/api";
    import type { Holding } from "$lib/api/portfolio";

    import { browser } from "$app/environment";

    let ticker = "AAPL";

    let request = api.pendingRequest<Holding[]>();

    const newRequest = () => api.portfolio().holdings();

    $: if (browser) request = newRequest();
</script>

<h3 class="title is-3">Portolio Holdings</h3>
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
    {#each response as holding}
        <div class="box has-background-grey">
            <p>Ticker: {holding.ticker}</p>
            <p>Units: {holding.units}</p>
            <p>Value: {holding.value}</p>
            <p>Unrealised Gain: {holding.unrealised_gain}</p>
        </div>
    {/each}
{:catch error}
    <p>{error.message}</p>
{/await}
