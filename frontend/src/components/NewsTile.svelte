<script lang="ts">
    const sentiment = true;
    const color = "success";
    let selected = false;

    function click() {
        selected = !selected;
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<article
    class="tile is-child box"
    on:click={click}
    style="background-color: {selected ? '#133658' : ''}">
    <p class="title mb-1">Title</p>

    <nav class="level">
        <!-- Left side -->
        <div class="level-left">
            <div class="level-item">
                <p class="subtitle has-text-{color}">Some information</p>
            </div>
        </div>

        <!-- Right side -->
        <div class="level-right">
            <span class="icon has-text-{color}">
                <i class="fas fa-arrow-trend-{sentiment ? 'up' : 'down'}" />
            </span>
        </div>
    </nav>

    <div class="content">
        <p>The actual content.</p>
    </div>
</article>

<style>
    article {
        transition: background-color 0s;
    }

    article:hover {
        background-color: #303030;
    }
</style>
