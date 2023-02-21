<script lang="ts">
    import type { News } from "$lib/types";
    import { howLongAgo } from "$lib/functions";

    export let data: News;
    const color = data.sentiment ? "success" : "warning";
</script>

<div class="block card">
    <header class="card-header">
        <a class="card-header-title has-text-{color}" href={data.url}>
            {howLongAgo(data.published_utc)} · {data.publisher}
        </a>
        <div class="card-header-icon has-text-{color}">
            <span class="icon">
                <i
                    class="fas fa-arrow-trend-{data.sentiment ?
                        'up' :
                        'down'}" />
            </span>
        </div>
    </header>

    <div class="card-content">
        <p class="title is-5">
            {data.title}
        </p>
    </div>
</div>
