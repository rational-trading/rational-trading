<script lang="ts">
    interface News {
        positive: boolean;
        source: string;
        time: string;
        title: string;
    }

    export let data: News;

    const sentiment = data.positive ? "success" : "warning";
</script>

<div class="block card">
    <header class="card-header">
        <p class="card-header-title has-text-{sentiment} pr-0">
            {data.time} · {data.source}
        </p>
        <div class="card-header-icon has-text-{sentiment} pl-0">
            <span class="icon">
                <i class="fas fa-thumbs-{data.positive ? 'up' : 'down'}" />
            </span>
        </div>
    </header>

    <div class="card-content">
        <p class="title is-5">
            {data.title}
        </p>
    </div>
</div>
