<script lang="ts">
    import type { Article } from "$lib/api/news";
    import { capitalize, timeAgo } from "$lib/functions";

    export let data: Article;
    export let selected: boolean = false;
    export let toggleArticle: ((id: string) => void) | null;
    export let light: boolean = false;
    export let description: boolean = true;

    const color = data.normalised_sentiment >= 0 ? "success" : "warning";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<article
    class="tile is-child box"
    class:has-background-grey-dark={light}
    on:click={() => (toggleArticle ? toggleArticle(data.article_id) : null)}
    style="background-color: {selected ? '#2C4869' : ''}"
    style:cursor={toggleArticle ? "pointer" : ""}
    class:hoverable={toggleArticle}>
    <p class="title is-5 mb-1">{data.title}</p>

    <div class="level">
        <!-- Left side -->
        <div class="level-left">
            <div class="level-item">
                <a
                    class="subtitle is-6 has-text-{color}"
                    href={data.url}
                    target="_blank"
                    rel="noreferrer"
                    on:click={(e) => e.stopPropagation()}>
                    {capitalize(timeAgo(new Date(data.date * 1000)))} · {data.publisher}
                </a>
            </div>
        </div>

        <!-- Right side -->
        <div class="level-right">
            <span class="icon has-text-{color}">
                <i
                    class="fas fa-arrow-trend-{data.normalised_sentiment >= 0
                        ? 'up'
                        : 'down'}" />
            </span>
        </div>
    </div>

    {#if description}
        <div class="content">
            <p>{data.description}</p>
        </div>
    {/if}
</article>

<style>
    article {
        transition: background-color 0s;
    }

    .hoverable:hover {
        background-color: #181818;
    }

    a:hover {
        text-decoration: underline;
    }
</style>
