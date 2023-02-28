<script lang="ts">
    import api from "$lib/api";
    import type { News } from "$lib/api/news";

    import { browser } from "$app/environment";

    let ticker = "AAPL";
    let n = 5;

    let request = api.pendingRequest<News[]>();

    const newRequest = () => api.news().get(ticker, n);

    $: if (browser) request = newRequest();
</script>

<h3 class="title is-3">Related News</h3>
<p>
    <input class="input" bind:value={ticker} placeholder="Ticker" />
    <input
        class="input"
        bind:value={n}
        placeholder="Number of articles required" />
</p>
<br />
<p>
    <button class="button is-info" on:click={() => (request = newRequest())}
        >Send</button>
</p>
<br />
{#await request}
    <p>Waiting...</p>
{:then responses}
    {#each responses as response}
        <div class="box has-background-grey">
            <p>article_id: {response.article_id}</p>
            <p>publisher: {response.publisher}</p>
            <p>url: {response.url}</p>
            <p>title: {response.title}</p>
            <p>description: {response.description}</p>
            <p>date: {new Date(response.date * 1000).toLocaleString()}</p>
            <p>tickers: {response.tickers}</p>
            <p>normalised_sentiment: {response.normalised_sentiment}</p>
            <p>reputation: {response.reputation}</p>
            <p>recency: {response.recency}</p>
        </div>
    {/each}
{:catch error}
    <p>{error.message}</p>
{/await}
