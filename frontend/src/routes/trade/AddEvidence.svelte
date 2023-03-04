<script lang="ts">
    import type { MakeTrade } from "$lib/api/trades";
    import { goto } from "$app/navigation";
    import { stepUrl } from "./Steps.svelte";
    import api from "$lib/api";
    import { browser } from "$app/environment";
    import type { News } from "$lib/api/news";
    import NewsTile from "$components/news/NewsTile.svelte";

    export let initialState: MakeTrade;
    export let currentState: MakeTrade;

    let newsRequest = api.pendingRequest<News[]>();
    $: newNewsRequest = () => api.news().get(ticker, 20);
    $: if (browser) newsRequest = newNewsRequest();

    $: ({ ticker, article_evidence } = initialState);

    $: currentState = { ...initialState, article_evidence };

    function toggleArticle(id: string) {
        const index = article_evidence.indexOf(id);
        if (index === -1) {
            article_evidence.push(id);
        } else {
            article_evidence.splice(index, 1);
        }
        article_evidence = article_evidence;
    }

    $: console.log(currentState);
</script>

<div class="block mr-5">
    <header class="title is-5">
        1. Select any articles that helped inform your decision
    </header>
    <div
        class="block"
        style=" height: 30vh; overflow-x: hidden; overflow-y: auto;">
        <div class="tile is-ancestor">
            {#await newsRequest}
                <div
                    style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                    <p>Loading...</p>
                </div>
            {:then responses}
                <div class="tile is-parent is-vertical">
                    {#each responses.filter((_element, index) => index % 2 === 0) as response}
                        <NewsTile
                            {toggleArticle}
                            data={response}
                            bind:articles={article_evidence} />
                    {/each}
                </div>
                <div class="tile is-parent is-vertical">
                    {#each responses.filter((_element, index) => index % 2 === 1) as response}
                        <NewsTile
                            {toggleArticle}
                            data={response}
                            bind:articles={article_evidence} />
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
</div>
<a
    href={stepUrl(3, currentState)}
    class="button is-info"
    on:click={() => goto(stepUrl(3, currentState))}>Continue</a>
