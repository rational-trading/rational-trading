<script lang="ts">
    import News from "$components/News.svelte";
    import data from "$lib/data";
</script>

<!-- this fixes the issue of weird extra space to the right of the page -->
<div
    class="columns my-0"
    style="width: calc(100vw + 12px); height: calc(100vh - 56px);">
    <div class="column is-one-quarter has-background-grey-darker px-0">
        <nav class="level is-mobile ml-5 mr-4 my-0">
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
                style="height: 100%; overflow-y: scroll;">
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
                        <tr class="is-selected" style="cursor: pointer;">
                            <th class="has-text-left">AAPL</th>
                            <td class="has-text-right">151.66</td>
                            <td class="has-text-right has-text-warning"
                                >-2.99</td>
                            <td class="has-text-right has-text-warning"
                                >-1.93%</td>
                        </tr>
                        <tr style="cursor: pointer;">
                            <th class="has-text-left">TSLA</th>
                            <td class="has-text-right">199.68</td>
                            <td class="has-text-right has-text-success"
                                >2.87</td>
                            <td class="has-text-right has-text-success"
                                >1.45%</td>
                        </tr>
                        <tr style="cursor: pointer;">
                            <th class="has-text-left">NFLX</th>
                            <td class="has-text-right">361.54</td>
                            <td class="has-text-right has-text-warning"
                                >-1.41</td>
                            <td class="has-text-right has-text-warning"
                                >-0.39%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="column" style="height: calc(100vh - 56px); overflow: auto;">
        <nav class="level mx-2">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="subtitle is-5">Apple Inc.</h1>
                </div>
                <div class="level-item">
                    <h1 class="subtitle is-5">·</h1>
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
            style="height: 50vh; display: flex; justify-content: center; align-items: center;">
            Graph
        </div>

        <div class="tabs">
            <ul>
                <li class="is-active">
                    <a>Key Stats</a>
                </li>
                <li><a>Finances</a></li>
            </ul>
        </div>

        <div class="block mx-2">
            <h1 class="title is-5">Key Stats</h1>
            <p>{data}</p>
        </div>
    </div>

    <div class="column is-one-quarter has-background-grey-darker p-5">
        <div style="height: calc(100vh - 56px - 10rem); overflow: auto;">
            <div class="block pr-4">
                <h1 class="title is-5">News</h1>
                <News
                    data={{
                        title: "Some Positive News About Apple",
                        source: "Newswires",
                        time: "1 hour ago",
                        positive: true,
                    }} />
                <News
                    data={{
                        title: "Some Negative News About Apple",
                        source: "Newswires",
                        time: "2 hours ago",
                        positive: false,
                    }} />
                <News
                    data={{
                        title: "Some Negative News About Apple",
                        source: "Newswires",
                        time: "3 hours ago",
                        positive: false,
                    }} />
                <News
                    data={{
                        title: "Some Positive News About Apple",
                        source: "Newswires",
                        time: "5 hours ago",
                        positive: true,
                    }} />
                <div class="block is-flex is-justify-content-center">
                    <button class="button is-dark is-small is-rounded"
                        >More news</button>
                </div>
            </div>
        </div>
        <hr />
        <div class="block is-flex is-justify-content-center">
            <button class="button is-medium is-info">
                <strong>Make a Rational Trade</strong>
            </button>
        </div>
    </div>
</div>
