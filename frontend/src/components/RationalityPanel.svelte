<script lang="ts">
    import api from "$lib/api";
    import Speedometer from "svelte-speedometer";
    import type { Article } from "$lib/api/news";
    import type { Trade } from "$lib/api/trades";
    import { convertUnixDate } from "$lib/functions";
    import ArcGauge from "$components/ArcGauge.svelte";
    import NewsTile from "$components/news/NewsTile.svelte";
    import { browser } from "$app/environment";

    let active = false;
    export let data: Trade;

    // values should be somewhat normalized - i.e. it should be guaranteed that they fall within a constant range
    $: controversy = data.controversy * 1000;
    $: risk = data.financial_risk * 1000;
    $: evidence = 5 + Math.round(data.evidence * 90);

    let responses: Article[] = [];
    const newNewsRequest = () => {
        api.news()
            .articles(data.article_evidence)
            .then((response) => (responses = response));
    };

    $: if (browser) newNewsRequest();
</script>

{#if active}
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="modal-background" on:click={() => (active = false)} />
        <div class="modal-content">
            <div style="display: flex; justify-content: right;">
                <button
                    class="button is-ghost"
                    on:click={() => (active = false)}>
                    <span class="icon is-large">
                        <i class="fas fa-xmark" />
                    </span>
                </button>
            </div>

            <div class="block mx-5">
                <header class="title is-3">Feedback</header>
                <hr style="background: #4a4a4a; height: 1px" />
            </div>

            <div class="block mx-5">
                <header class="title is-5">Scores</header>

                <div class="columns" style="height: 55vh">
                    <div class="column">
                        <!-- workaround for weird spacing of the speedometer -->
                        <div style="height: 10vh" />
                        <div
                            style="height: 15vh; display: flex; justify-content: center; align-items: center;">
                            <Speedometer
                                value={controversy}
                                segments={1000}
                                maxSegmentLabels={0}
                                needleColor="#f5f5f5"
                                needleTransitionDuration={3000}
                                needleTransition="easeElastic"
                                needleHeightRatio={0.7}
                                startColor="#276cb0"
                                endColor="#e91e63"
                                ringWidth={5}
                                textColor="#f5f5f5"
                                currentValueText="Controversy: {controversy >
                                500 ?
                                    'High' :
                                    'Low'}"
                                paddingVertical={20} />
                        </div>
                        {#if controversy > 500}
                            <p>
                                A higher controversy score means that the nature
                                of the trade deviates from the overall media
                                sentiment at the moment.
                            </p>
                        {:else}
                            <p>
                                A lower controversy score means that the nature
                                of the trade aligns with the overall media
                                sentiment at the moment.
                            </p>
                        {/if}
                    </div>
                    <div class="column">
                        <div style="height: 15vh" />
                        <div
                            style="height: 30vh; display: flex; justify-content: center; align-items: center;">
                            <ArcGauge gaugeValue={evidence} size={3} />
                        </div>
                        {#if evidence > 50}
                            <p>
                                A higher evidence score means that your
                                justifications provided are more likely to be
                                well-structured and reasonable.
                            </p>
                        {:else}
                            <p>
                                A lower evidence score means that your
                                justifications provided still have room for
                                improvements.
                            </p>
                        {/if}
                    </div>
                    <div class="column">
                        <div style="height: 10vh" />
                        <div
                            style="height: 15vh; display: flex; justify-content: center; align-items: center;">
                            <Speedometer
                                value={risk}
                                segments={1000}
                                maxSegmentLabels={0}
                                needleColor="#f5f5f5"
                                needleTransitionDuration={3000}
                                needleTransition="easeElastic"
                                needleHeightRatio={0.7}
                                startColor="#276cb0"
                                endColor="#e91e63"
                                ringWidth={5}
                                textColor="#f5f5f5"
                                currentValueText="Risk: {risk > 500 ?
                                    'High' :
                                    'Low'}"
                                paddingVertical={20} />
                        </div>
                        {#if risk > 500}
                            <p>
                                A higher risk score means that the company has a
                                higher financial risk based on its financial
                                data.
                            </p>
                        {:else}
                            <p>
                                A lower risk score means that the company has a
                                lower financial risk based on its financial
                                data.
                            </p>
                        {/if}
                    </div>
                </div>
                <hr style="background: #4a4a4a; height: 1px" />
            </div>

            <div class="block mx-5">
                <header class="title is-5">Overview</header>
                <table class="table is-fullwidth is-dark">
                    <thead>
                        <tr>
                            <th class="has-text-left">Time</th>
                            <th class="has-text-left">Symbol</th>
                            <th class="has-text-left">Side</th>
                            <th class="has-text-left"
                                ><abbr title="Quantity">Qty</abbr></th>
                            <th>Price</th>
                            <th>Total value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="has-text-left"
                                >{convertUnixDate(data.time * 1000)}</td>
                            <th class="has-text-left">{data.ticker}</th>
                            <td class="has-text-left"
                                >{data.units_change >= 0 ? "Buy" : "Sell"}</td>
                            <td class="has-text-left"
                                >{Math.abs(data.units_change).toFixed(2)}</td>
                            <td class="has-text-right"
                                >{Math.abs(
                                    data.balance_change / data.units_change,
                                ).toFixed(2)}</td>
                            <td class="has-text-right"
                                >{Math.abs(data.balance_change).toFixed(2)}</td>
                        </tr>
                    </tbody>
                </table>
                <hr style="background: #4a4a4a; height: 1px" />
            </div>

            <div class="block mx-5">
                <header class="title is-5">Articles</header>

                {#if data.article_evidence.length > 0}
                    <div class="block">
                        <div class="tile is-ancestor">
                            <div class="tile is-parent is-vertical">
                                {#each responses.filter((_element, index) => index % 3 === 0) as response}
                                    <NewsTile
                                        toggleArticle={null}
                                        data={response} />
                                {/each}
                            </div>
                            <div class="tile is-parent is-vertical">
                                {#each responses.filter((_element, index) => index % 3 === 1) as response}
                                    <NewsTile
                                        toggleArticle={null}
                                        data={response} />
                                {/each}
                            </div>
                            <div class="tile is-parent is-vertical">
                                {#each responses.filter((_element, index) => index % 3 === 2) as response}
                                    <NewsTile
                                        toggleArticle={null}
                                        data={response} />
                                {/each}
                            </div>
                        </div>
                    </div>
                {:else}
                    <div class="notification is-warning">
                        No articles were provided to support this trade.
                    </div>
                {/if}

                <hr style="background: #4a4a4a; height: 1px" />
            </div>

            <div class="block mx-5 mb-5">
                <header class="title is-5">Justification</header>

                {#if data.text_evidence !== ""}
                    <div class="box has-background-dark content">
                        <p>{data.text_evidence}</p>
                    </div>
                {:else}
                    <div class="notification is-warning">
                        No explanation was provided to support this trade.
                    </div>
                {/if}
            </div>
        </div>
    </div>
{/if}

<!-- svelte-ignore a11y-missing-attribute -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<a on:click={() => (active = true)}>View</a>

<style>
    a {
        color: #ffdd57;
    }

    a:hover {
        text-decoration: underline;
        color: #f5f5f5;
    }

    .modal-content {
        width: 90vw;
        height: 90vh;
        overflow-x: hidden;
        background: #363636;
        border-radius: 7px;
    }
</style>
