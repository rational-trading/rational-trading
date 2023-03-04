<script lang="ts">
    import { browser } from "$app/environment";
    import NewsTile from "$components/news/NewsTile.svelte";
    import api from "$lib/api";
    import type { Article } from "$lib/api/news";
    import type { MakeTrade } from "$lib/api/trades";
    import { stepUrl } from "./Steps.svelte";

    export let initialState: MakeTrade;

    $: ({ side, ticker, text_evidence, amount, article_evidence, type } =
        initialState);

    let articlesRequest = api.pendingRequest<Article[]>();
    $: if (browser) articlesRequest = api.news().articles(article_evidence);
</script>

<div class="block mr-5">
    <div class="columns">
        <div class="column" />
        <div class="column is-two-thirds">
            <h2 class="title is-2">Order Summary</h2>
            <br />
            <div class="box has-background-grey-dark">
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Side</p>
                            <p class="title">{side}</p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Amount</p>
                            <p class="title">{amount}</p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Type</p>
                            <p class="title">
                                {type === "PRICE" ? "$" : "UNITS"}
                            </p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Ticker</p>
                            <p class="title">{ticker}</p>
                        </div>
                    </div>
                </nav>
            </div>
            <br />
            <h3 class="title is-4">Articles</h3>
            <div class="block">
                <div class="tile is-ancestor">
                    {#await articlesRequest}
                        <div
                            style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                            <p>Loading...</p>
                        </div>
                    {:then responses}
                        <div class="tile is-parent is-vertical">
                            {#each responses as response}
                                <NewsTile
                                    light
                                    toggleArticle={null}
                                    data={response}
                                    description={false} />
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
            <br />
            <h3 class="title is-4">Justification</h3>
            <div class="box has-background-grey-dark content">
                <p>{text_evidence}</p>
            </div>
            <div class="block">
                <div class="columns">
                    <div class="column" style="text-align:right;">
                        <a
                            href={stepUrl(5, initialState)}
                            class="button is-info">Continue</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="column" />
    </div>
</div>
