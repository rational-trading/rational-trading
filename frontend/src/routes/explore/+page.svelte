<script lang="ts">
    import data from "$lib/data";
</script>

<!-- this fixes the issue of weird extra space to the right of the page -->
<div
    class="columns my-0"
    style="width: calc(100vw + 12px); height: calc(100vh - 56px);"
>
    <div class="column is-one-quarter has-background-grey-darker">
        <nav class="level mx-4">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="title is-5">Watchlist</h1>
                </div>
            </div>

            <div class="level-right">
                <div class="level-item">
                    <span class="icon">
                        <a href="/"><i class="fas fa-plus" /></a>
                    </span>
                </div>
            </div>
        </nav>
        <slot />
    </div>

    <div class="column">
        <nav class="level mx-2">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="subtitle is-5">Apple Inc.</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">NASDAQ</h1>
                </div>
            </div>

            <div class="level-right">
                <div class="level-item">
                    <span class="icon">
                        <a href="/"><i class="fas fa-magnifying-glass" /></a>
                    </span>
                </div>
            </div>
        </nav>
        <div
            class="block mx-2"
            style="height: 50vh; display: flex; justify-content: center; align-items: center;"
        >
            Graph
        </div>

        <hr style="background: #4a4a4a;" />

        <div class="block mx-2">
            <h1 class="title is-5">Key Stats</h1>
            <p>{data}</p>
            <slot />
        </div>
    </div>

    <div class="column is-one-quarter has-background-grey-darker m-0">
        <div class="block mx-2" style="height: 40vh;">
            <h1 class="title is-5">News</h1>
        </div>
        <slot />
        <div class="block mx-2" style="height: 40vh;">
            <h1 class="title is-5">Financials</h1>
        </div>
        <slot />
        <div
            class="block mx-2"
            style="display: flex; justify-content: center; align-items: center;"
        >
            <button class="button is-medium is-info">
                <strong>Order Panel</strong>
            </button>
        </div>
    </div>
</div>
