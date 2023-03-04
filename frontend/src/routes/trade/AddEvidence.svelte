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

    $: ({ ticker, article_evidence, text_evidence } = initialState);
    $: currentState = { ...initialState, article_evidence, text_evidence };

    let newsRequest = api.pendingRequest<News[]>();
    $: newNewsRequest = () => api.news().get(ticker, 20);
    $: if (browser) newsRequest = newNewsRequest();

    function toggleArticle(id: string) {
        const index = article_evidence.indexOf(id);
        if (index === -1) {
            article_evidence.push(id);
        } else {
            article_evidence.splice(index, 1);
        }
        article_evidence = article_evidence;
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
        <div class="column is-half px-5">
            <header class="title is-4">
                Are there any relevant financial statistics?
            </header>

            <div class="columns mb-5">
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        Remember me
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        Remember me
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        Remember me
                    </label>
                </div>
                <div class="column">
                    <label class="checkbox">
                        <input type="checkbox" />
                        Remember me
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
                    value={text_evidence}
                    on:input={(e) =>
                        (text_evidence = e.currentTarget?.value ?? "")} />
            </div>
            <div class="block">
                <div class="columns">
                    <div class="column" style="text-align:right;">
                        <a
                            href={stepUrl(3, currentState)}
                            class="button is-info"
                            on:click={() => goto(stepUrl(3, currentState))}
                            >Continue</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
