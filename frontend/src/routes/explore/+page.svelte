<script lang="ts">
    import Watchlist from "$components/Watchlist.svelte";
    import WatchlistAdd from "$components/WatchlistAdd.svelte";
    import WatchlistMinus from "$components/WatchlistMinus.svelte";
    import Search from "$components/Search.svelte";
    import Graph from "$components/Graph.svelte";
    import Information from "$components/Information.svelte";
    import News from "$components/News.svelte";
    import NewsPanel from "$components/NewsPanel.svelte";
    import TradePanel from "$components/TradePanel.svelte";

    import {
        defaultWatchlist,
        currentStock,
        user,
        userWatchlist,
    } from "$lib/stores";
    import api from "$lib/api";
    import { browser } from "$app/environment";

    let graphWidth = 0;
    let graphHeight = 0;

    let activeTrade = false;

    function click() {
        if ($user) {
            activeTrade = true;
        } else {
            alert("Please log in first.");
        }
    }

    const newWatchlistRequest = () => api
        .user()
        .watchlist()
        .then((response) => {
            userWatchlist.set(response.tickers);
            return response.tickers;
        });

    $: if ($user && browser) newWatchlistRequest();

    $: news = [
        {
            title: "Why one strategist sees a real risk of World War 3.1, whose battleground will be microchips",
            publisher: "MarketWatch",
            published_utc: "2023-02-26T13:56:00Z",
            description:
                "Peter Tchir, head of macro strategy at Academy Securities, dubs a potential war over semiconductors World War 3.1",
            url: "https://www.marketwatch.com/story/why-one-strategist-sees-a-real-risk-of-world-war-3-1-whose-battleground-will-be-microchips-8eec0e96",
            sentiment: true,
        },
        {
            title: `Some Negative News About ${$currentStock.name}`,
            publisher: "Newswires",
            published_utc: "2023-02-21T10:00:00Z",
            description: "Some description",
            url: "/",
            sentiment: false,
        },
        {
            title: `Some Negative News About ${$currentStock.name}`,
            publisher: "Newswires",
            published_utc: "2023-02-20T18:11:51Z",
            description: "Some description",
            url: "/",
            sentiment: false,
        },
        {
            title: `Some Positive News About ${$currentStock.name}`,
            publisher: "Newswires",
            published_utc: "2023-02-20T13:00:00Z",
            description: "Some description",
            url: "/",
            sentiment: true,
        },
    ];
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
                    <WatchlistMinus />
                </div>
                <div class="level-item">
                    <WatchlistAdd />
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
                        {#if $user}
                            {#each $userWatchlist as ticker}
                                <Watchlist {ticker} />
                            {/each}
                        {:else}
                            {#each $defaultWatchlist as ticker}
                                <Watchlist {ticker} />
                            {/each}
                        {/if}
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
                <div class="level-item">
                    <h1 class="subtitle is-5">{$currentStock.name}</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">•</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">{$currentStock.exchange}</h1>
                </div>
            </div>

            <div class="level-right" style="width: 50%">
                <div class="level-item mr-3" style="width: 100%">
                    <Search />
                </div>
            </div>
        </nav>

        <!-- the graph itself -->
        <div
            style="height: 50vh; display: flex; justify-content: center; align-items: center;"
            bind:clientWidth={graphWidth}
            bind:clientHeight={graphHeight}>
            <Graph dimensions={{ width: graphWidth, height: graphHeight }} />
        </div>

        <!-- information tab -->
        <Information />
    </div>

    <!-- news column -->
    <div
        class="column is-one-quarter mt-2"
        style="border-left: 1px solid #4a4a4a;">
        <div style="height: calc(100vh - 53px - 10rem); overflow: auto;">
            <div class="block">
                <h1 class="title is-5">News</h1>
                {#each news as item}
                    <News data={item} />
                {/each}

                <div class="block is-flex is-justify-content-center">
                    <NewsPanel />
                </div>
            </div>
        </div>
        <hr style="background: #4a4a4a; height: 1px" />
        <div class="block is-flex is-justify-content-center">
            <button class="button is-medium is-info" on:click={click}>
                <strong>Make a Rational Trade</strong>
            </button>
        </div>
    </div>
</div>

{#if activeTrade}
    <TradePanel close={() => (activeTrade = false)} />
{/if}
