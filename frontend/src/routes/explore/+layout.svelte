<script lang="ts">
    import data from "$lib/data";
</script>

<div class="columns">
    <div
        class="column is-one-quarter has-text-light has-background-grey-darker "
    >
        <nav class="level m-4">
            <div class="level-left">
                <div class="level-item">
                    <span class="icon has-text-light">
                        <i class="fas fa-eye" />
                    </span>
                </div>
                <div class="level-item">
                    <h1 class="title is-5">Watchlist</h1>
                </div>
            </div>

            <div class="level-right">
                <div class="level-item">
                    <span class="icon has-text-light">
                        <a><i class="fas fa-plus" /></a>
                    </span>
                </div>
            </div>
        </nav>
        <slot />
    </div>

    <div class="column">
        <nav class="level m-4">
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
                    <span class="icon has-text-light">
                        <a><i class="fas fa-magnifying-glass" /></a>
                    </span>
                </div>
            </div>
        </nav>
        <div class="block m-4">Graph</div>
        <div class="content">
            <p>Some data is: {data}</p>
        </div>

        <div class="columns m-6">
            <div class="column is-one-third" />
            <div class="column is-one-third">
                <div class="level">
                    <div class="level-item">
                        <h1 class="title is-0">Rational Trading</h1>
                    </div>
                </div>
                <div class="level">
                    <div class="level-item"><a href="/">Home</a></div>
                    <div class="level-item">
                        <a href="/shopping">Shopping</a>
                    </div>
                    <div class="level-item"><a href="/explore">Explore</a></div>
                </div>
                <br />
                <br />
                <slot />
            </div>
            <div class="column is-one-third" />
        </div>
    </div>
    <div
        class="column is-one-quarter has-text-light has-background-grey-darker"
    >
        <div class="block m-4">
            <h1 class="title is-5">News</h1>
        </div>
        <slot />
        <div class="block m-4">
            <h1 class="title is-5">Financials</h1>
        </div>
        <slot />
    </div>
</div>
