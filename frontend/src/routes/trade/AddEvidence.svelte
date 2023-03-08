<script lang="ts">
    import type { MakeTrade } from "$lib/api/trades";
    import api from "$lib/api";
    import type { Article } from "$lib/api/news";
    import NewsTile from "$components/news/NewsTile.svelte";
    import { browser } from "$app/environment";
    import { stepUrl } from "./Steps.svelte";
    import { goto } from "$app/navigation";

    export let initialState: MakeTrade;
    export let currentState: MakeTrade;

    $: ({
        ticker,
        article_evidence: articleEvidence,
        text_evidence: textEvidence,
    } = initialState);
    $: currentState = {
        ...initialState,
        article_evidence: articleEvidence,
        text_evidence: textEvidence,
    };

    let newsRequest = api.pendingRequest<Article[]>();
    $: newNewsRequest = () => api.news().about(ticker, 20);
    $: if (browser) newsRequest = newNewsRequest();

    function toggleArticle(id: string) {
        const index = articleEvidence.indexOf(id);
        if (index === -1) {
            articleEvidence.push(id);
        } else {
            articleEvidence.splice(index, 1);
        }
        articleEvidence = articleEvidence;
    }
</script>

<div class="block mr-5">
    <div class="columns">
        <div class="column is-half px-5">
            <header class="title is-4">
                Which articles helped you decide on your position?
            </header>
            <div
                class="block"
                style="height: 50vh; overflow-x: hidden; overflow-y: auto;">
                <div class="tile is-ancestor px-2">
                    {#await newsRequest}
                        <div
                            style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                            <p>Loading...</p>
                        </div>
                    {:then responses}
                        <div class="tile is-parent is-vertical">
                            {#each responses as response}
                                <NewsTile
                                    {toggleArticle}
                                    data={response}
                                    selected={articleEvidence.includes(
                                        response.article_id,
                                    )} />
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
        <div class="column is-half px-5">
            <header class="title is-4">
                Are there any relevant financial statistics?
            </header>

            <div class="columns mb-5">
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        EPS
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        P/E ratio
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        D/E ratio
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        Current ratio
                    </label>
                </div>
            </div>
            <br />
            <br />
            <div class="block">
                <header class="title is-4">
                    Why does this evidence justify your position?
                </header>
                <textarea
                    class="textarea"
                    style="height: 24vh;"
                    placeholder="Share your insights..."
                    value={textEvidence}
                    on:input={(e) => (textEvidence = e.currentTarget?.value ?? "")} />
            </div>
            <div class="block">
                <div class="columns">
                    <div class="column" style="text-align:right;">
                        <button
                            class="button is-text"
                            on:click={() => goto(stepUrl(1, currentState))}
                            >Back (Select Stock)</button>
                        <a
                            href={stepUrl(3, currentState)}
                            class="button is-info">Continue</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
