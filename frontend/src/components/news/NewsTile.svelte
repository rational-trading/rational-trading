<script lang="ts">
    import type { News } from "$lib/api/news";
    import { capitalize, timeAgo } from "$lib/functions";

    export let data: News;
    const color = data.normalised_sentiment >= 0 ? "success" : "warning";

    export let articles: string[];

    export let toggleArticle: (id: string) => void;

    $: selected = articles.includes(data.article_id);
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<article
    class="tile is-child box"
    on:click={() => toggleArticle(data.article_id)}
    style="background-color: {selected ? '#2C4869' : ''}">
    <p class="title is-5 mb-1">{data.title}</p>

    <nav class="level">
        <!-- Left side -->
        <div class="level-left">
            <div class="level-item">
                <a
                    class="subtitle is-6 has-text-{color}"
                    href={data.url}
                    target="_blank"
                    rel="noreferrer">
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
    </nav>

    <div class="content">
        <p>{data.description}</p>
    </div>
</article>

<style>
    article {
        transition: background-color 0s;
    }

    article:hover {
        background-color: #181818;
    }

    a:hover {
        text-decoration: underline;
    }
</style>
