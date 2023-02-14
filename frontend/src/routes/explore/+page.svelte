<script lang="ts">
    import Watchlist from "$components/Watchlist.svelte";
    import News from "$components/News.svelte";
    import Graph from "$components/Graph.svelte";

    const watchlist = [
        {
            symbol: "AAPL",
            last: 151.66,
            chg: -2.99,
            percentChg: -1.93,
        },
        {
            symbol: "TSLA",
            last: 199.68,
            chg: 2.87,
            percentChg: 1.45,
        },
        {
            symbol: "NFLX",
            last: 361.54,
            chg: -1.41,
            percentChg: -0.39,
        },
        {
            symbol: "NKE",
            last: 122.91,
            chg: -2.42,
            percentChg: -1.93,
        },
    ];
    const news = [
        {
            title: "Some Positive News About Apple",
            source: "Newswires",
            time: "1 hour ago",
            positive: true,
            url: "/",
        },
        {
            title: "Some Negative News About Apple",
            source: "Newswires",
            time: "2 hours ago",
            positive: false,
            url: "/",
        },
        {
            title: "Some Negative News About Apple",
            source: "Newswires",
            time: "3 hours ago",
            positive: false,
            url: "/",
        },
        {
            title: "Some Positive News About Apple",
            source: "Newswires",
            time: "5 hours ago",
            positive: true,
            url: "/",
        },
    ];
</script>

<!-- this fixes the issue of weird extra space to the right of the page -->
<div
    class="columns my-0"
    style="width: calc(100vw + 12px); height: calc(100vh - 53px);">
    <div class="column is-one-quarter has-background-grey-darker px-0">
        <nav class="level ml-5 mr-4 mt-2 mb-0">
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

        <div class="block pl-3 mt-3">
            <!-- Went very explicit on the alignment because it's never what you expect -->
            <div
                class="table-container"
                style="height: 100%; overflow-y: auto;">
                <table class="table is-hoverable is-fullwidth is-dark">
                    <thead>
                        <tr>
                            <th class="has-text-left ml-5">Symbol</th>
                            <th>Last</th>
                            <th><abbr title="Change">Chg</abbr></th>
                            <th><abbr title="Percent Change">Chg%</abbr></th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each watchlist as item}
                            <Watchlist data={item} />
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="column">
        <!--- right side header bar -->
        <nav class="level mx-2" style="width: 100%">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="subtitle is-5">Apple Inc.</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">•</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">NASDAQ</h1>
                </div>
            </div>

            <div class="level-right" style="width: 60%">
                <div class="level-item mr-3" style="width: 100%">
                    <button class="button is-rounded" style="width: 100%">
                        <div class="level" style="width: 100%">
                            <div class="level-left">
                                <p
                                    class="has-text-grey-lighter has-text-weight-light">
                                    Search for a stock to display...
                                </p>
                            </div>
                            <div class="level-right">
                                <span class="icon">
                                    <i class="fas fa-magnifying-glass" />
                                </span>
                            </div>
                        </div>
                    </button>
                </div>
            </div>
        </nav>

        <div class="columns" style="height: calc(100vh - 53px - 5.5rem)">
            <div class="column" style="height: 100%;">
                <div
                    class="block mx-2"
                    style="height: 50vh; display: flex; justify-content: center; align-items: center;">
                    <Graph />
                </div>

                <div class="tabs">
                    <ul>
                        <li class="is-active">
                            <a href="/">Key Stats</a>
                        </li>
                        <li><a href="/">Finances</a></li>
                    </ul>
                </div>

                <div class="block mx-2">
                    <p>Here is some text.</p>
                </div>
            </div>

            <div
                class="column is-one-third"
                style="height: 100%; border-left: 1px solid #4a4a4a;">
                <div class="block px-2" style="height: 85%; overflow: auto;">
                    <h1 class="title is-5">News</h1>
                    {#each news as item}
                        <News data={item} />
                    {/each}

                    <div class="block is-flex is-justify-content-center">
                        <button class="button is-small is-rounded"
                            >More news</button>
                    </div>
                </div>
                <hr style="background: #4a4a4a; height: 1px" />
                <div class="block is-flex is-justify-content-center">
                    <button class="button is-medium is-info">
                        <strong>Make a Rational Trade</strong>
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
