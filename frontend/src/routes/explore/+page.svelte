<script lang="ts">
    import WatchlistItem from "$components/watchlist/WatchlistItem.svelte";
    import WatchlistAdd from "$components/watchlist/WatchlistAdd.svelte";
    import WatchlistMinus from "$components/watchlist/WatchlistMinus.svelte";
    import Graph from "$components/Graph.svelte";
    import Information from "$components/Information.svelte";
    import NewsCard from "$components/news/NewsCard.svelte";
    import type { Article } from "$lib/api/news";

    import { defaultWatchlist, user, userWatchlist } from "$lib/stores";
    import api from "$lib/api";
    import type { Stock } from "$lib/types";
    import { browser } from "$app/environment";
    import SearchBar from "./SearchBar.svelte";
    import { goto } from "$app/navigation";

    let currentStock: Stock = {
        ticker: "AAPL",
        name: "Apple Inc.",
        exchange: "XNAS",
    };

    let graphWidth = 0;
    let graphHeight = 0;

    const newWatchlistRequest = () => api
        .user()
        .watchlist()
        .then((response) => {
            userWatchlist.set(response.tickers);
            return response.tickers;
        });

    $: if ($user && browser) newWatchlistRequest();

    let n = 5;

    let newsRequest = api.pendingRequest<Article[]>();
    $: newNewsRequest = () => api.news().about(currentStock.ticker, n);
    $: if (browser) newsRequest = newNewsRequest();

    function clickNews() {
        n += 5;
    }

    function setCurrentStock(stock: Stock) {
        if (currentStock !== stock) {
            currentStock = stock;
        }
    }
</script>

<!-- this fixes the issue of weird extra space to the right of the page -->
<div
    class="columns my-0"
    style="width: calc(100vw + 12px); height: calc(100vh - 53px);">
    <!-- watchlist column -->
    <div class="column is-one-quarter has-background-grey-darker px-0">
        <nav class="level ml-5 mr-4 mt-2 mb-0">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="title is-5">Watchlist</h1>
                </div>
            </div>

            <div class="level-right">
                <div class="level-item">
                    <WatchlistMinus {setCurrentStock} {currentStock} />
                </div>
                <div class="level-item">
                    <WatchlistAdd {currentStock} onAdd={setCurrentStock} />
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
                        {#each $user ? $userWatchlist : $defaultWatchlist as ticker (ticker)}
                            <WatchlistItem
                                {ticker}
                                onClick={setCurrentStock}
                                selected={ticker === currentStock.ticker} />
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- graph column -->
    <div class="column is-one-half" style="height: 100%;">
        <!-- graph side header bar -->
        <nav class="level mx-2" style="width: 100%">
            <div class="level-left">
                {#if currentStock.name === "Loading..."}
                    <div class="level-item">
                        <h1 class="subtitle is-5">{currentStock.name}</h1>
                    </div>
                {:else}
                    <div class="level-item">
                        <h1 class="subtitle is-5">{currentStock.name}</h1>
                    </div>
                    <div class="level-item">
                        <h1 class="subtitle is-5">•</h1>
                    </div>
                    <div class="level-item">
                        <h1 class="subtitle is-5">{currentStock.exchange}</h1>
                    </div>
                {/if}
            </div>

            <div class="level-right" style="width: 50%">
                <div class="level-item mr-3" style="width: 100%">
                    <SearchBar onSelected={setCurrentStock} />
                </div>
            </div>
        </nav>

        <!-- the graph itself -->
        <div
            style="height: 50vh; display: flex; justify-content: center; align-items: center;"
            bind:clientWidth={graphWidth}
            bind:clientHeight={graphHeight}>
            <Graph
                stock={currentStock}
                dimensions={{ width: graphWidth, height: graphHeight }} />
        </div>

        <hr style="background: #4a4a4a; height: 1px" />

        <!-- information tab -->
        <div style="height: 30vh; width: 100%;">
            <Information stock={currentStock} />
        </div>
    </div>

    <!-- news column -->
    <div
        class="column is-one-quarter mt-2"
        style="border-left: 1px solid #4a4a4a;">
        <div style="height: calc(100vh - 53px - 10rem); overflow: auto;">
            <div class="block">
                <h1 class="title is-5">News</h1>
                {#await newsRequest}
                    <div
                        style="width: 100%; height: 3vh; display: flex; justify-content: center; align-items: center;">
                        <p>Loading...</p>
                    </div>
                {:then responses}
                    {#each responses as response}
                        <NewsCard data={response} />
                    {/each}
                    <div class="block is-flex is-justify-content-center">
                        <button
                            class="button is-outline is-small is-rounded"
                            on:click={clickNews}>
                            More news
                        </button>
                    </div>
                {:catch error}
                    <div
                        style="width: 100%; height: 5vh; display: flex; justify-content: center; align-items: center;">
                        <p>{error.message}</p>
                    </div>
                {/await}
            </div>
        </div>
        <hr style="background: #4a4a4a; height: 1px" />
        <div class="block is-flex is-justify-content-center">
            <button
                class="button is-medium is-info"
                disabled={!$user}
                style="width: 100%"
                on:click={() => goto("/trade/")}>
                <strong>Make a Rational Trade</strong>
            </button>
        </div>
    </div>
</div>
