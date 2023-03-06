<script lang="ts">
    import NewsTile from "$components/news/NewsTile.svelte";
    import api from "$lib/api";
    import type { Article } from "$lib/api/news";
    import type { MakeTrade } from "$lib/api/trades";
    import { ApiError } from "$lib/request";
    import { goto } from "$app/navigation";
    import { browser } from "$app/environment";
    import { stepUrl } from "./Steps.svelte";

    export let initialState: MakeTrade;
    export let currentState: MakeTrade;

    $: ({
        side,
        ticker,
        text_evidence: textEvidence,
        amount,
        article_evidence: articleEvidence,
        type,
    } = initialState);
    $: currentState = initialState;

    let articlesRequest = api.pendingRequest<Article[]>();
    $: if (browser) articlesRequest = api.news().articles(articleEvidence);

    let errorMessage = "";

    let makingTrade = false;
    async function makeTrade() {
        errorMessage = "";
        makingTrade = true;
        try {
            await api.trades().make(initialState);
        } catch (e) {
            makingTrade = false;
            if (e instanceof ApiError) {
                errorMessage = e.message;
            } else {
                errorMessage = "Something went wrong!";
            }
            return;
        }

        makingTrade = false;
        await goto(stepUrl(5, initialState));
    }
</script>

<div class="block">
    <div class="columns">
        <div class="column" />
        <div class="column is-two-thirds">
            <h2 class="title is-2">Order Summary</h2>
            <br />
            <div class="box has-background-grey-dark">
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Ticker</p>
                            <p class="title">{ticker}</p>
                        </div>
                    </div>
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
                </nav>
            </div>
            <br />
            <h3 class="title is-4">Articles</h3>
            <div class="block">
                {#await articlesRequest}
                    <div
                        style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                        <p>Loading...</p>
                    </div>
                {:then responses}
                    {#if responses.length > 0}
                        {#each responses as response}
                            <NewsTile
                                toggleArticle={null}
                                data={response}
                                description={false} />
                        {/each}
                    {:else}
                        <div class="notification is-warning">
                            You didn't provide any articles to support your
                            trade!
                        </div>
                    {/if}
                {:catch error}
                    <div
                        style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                        <p>{error.message}</p>
                    </div>
                {/await}
            </div>
            <br />
            <h3 class="title is-4">Justification</h3>
            {#if textEvidence !== ""}
                <div class="box has-background-grey-dark content">
                    <p>{textEvidence}</p>
                </div>
            {:else}
                <div class="notification is-warning">
                    You didn't provide any explanation to justify your trade!
                </div>
            {/if}
            <br />
            <div class="block">
                <div class="columns">
                    <div class="column" style="text-align:right;">
                        <button
                            class="block button is-info"
                            class:is-loading={makingTrade}
                            on:click={makeTrade}>Make Trade Now</button>
                        <p class="block has-text-danger">{errorMessage}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="column" />
    </div>
</div>
