<script lang="ts">
    interface News {
        positive: boolean;
        source: string;
        time: string;
        title: string;
        url: string;
    }

    export let data: News;

    const sentiment = data.positive ? "success" : "warning";
</script>

<div class="block card">
    <header class="card-header">
        <a class="card-header-title has-text-{sentiment}" href={data.url}>
            {data.time} · {data.source}
        </a>
        <div class="card-header-icon has-text-{sentiment}">
            <span class="icon">
                <i class="fas fa-arrow-trend-{data.positive ? 'up' : 'down'}" />
            </span>
        </div>
    </header>

    <div class="card-content">
        <p class="title is-5">
            {data.title}
        </p>
    </div>
</div>
