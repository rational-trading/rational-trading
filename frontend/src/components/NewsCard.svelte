<script lang="ts">
    import { capitalize } from "$lib/functions";
    import type { News } from "$lib/api/news";
    import TimeAgo from "javascript-time-ago";
    const timeAgo = new TimeAgo("en-US");

    export let data: News;
    const color = data.normalised_sentiment >= 0 ? "success" : "warning";
</script>

<div class="block card" style="cursor: pointer;">
    <header class="card-header">
        <a class="card-header-title has-text-{color}" href={data.url}>
            {capitalize(timeAgo.format(new Date(data.date * 1000)))} · {data.publisher}
        </a>
        <div class="card-header-icon has-text-{color}">
            <span class="icon">
                <i
                    class="fas fa-arrow-trend-{data.normalised_sentiment >= 0
                        ? 'up'
                        : 'down'}" />
            </span>
        </div>
    </header>

    <div class="card-content">
        <p class="title is-5">
            {data.title}
        </p>
        <p>{data.description}</p>
    </div>
</div>
