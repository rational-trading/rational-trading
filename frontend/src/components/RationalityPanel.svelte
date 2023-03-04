<script lang="ts">
    import api from "$lib/api";
    import { browser } from "$app/environment";
    import Speedometer from "svelte-speedometer";
    import NewsTileStatic from "./NewsTileStatic.svelte";
    import type { News } from "$lib/api/news";

    // values should be somewhat normalized - i.e. it should be guaranteed that they fall within a constant range
    const controversy = 300;
    const risk = 500;
    const evidence = 700;

    let responses: News[] = [];
    const newNewsRequest = () => {
        api.news()
            .get("AAPL", 5)
            .then((response) => (responses = response));
    };

    $: if (browser) newNewsRequest();
</script>

<div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={close} />
    <div class="modal-content">
        <div style="display: flex; justify-content: right;">
            <button class="button is-ghost" on:click={close}>
                <span class="icon is-large">
                    <i class="fas fa-xmark" />
                </span>
            </button>
        </div>

        <div class="block mx-5">
            <header class="title is-3">Trade #86149</header>
            <hr style="background: #4a4a4a; height: 1px" />
        </div>

        <div class="block mx-5">
            <header class="title is-5">Scores</header>

            <div class="columns" style="height: 30vh">
                <div class="column">
                    <!-- workaround for weird spacing of the speedometer -->
                    <div style="height: 5vh" />
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
                            startColor="#e91e63"
                            endColor="#276cb0"
                            ringWidth={5}
                            textColor="#f5f5f5"
                            currentValueText="Controversy: {controversy > 500
                                ? 'High'
                                : 'Low'}"
                            paddingVertical={20} />
                    </div>
                    <p>
                        Placeholder: maybe some sort of explanation about what
                        this means?
                    </p>
                </div>
                <div class="column">
                    <div style="height: 5vh" />
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
                            startColor="#e91e63"
                            endColor="#276cb0"
                            ringWidth={5}
                            textColor="#f5f5f5"
                            currentValueText="Risk: {risk > 500
                                ? 'High'
                                : 'Low'}"
                            paddingVertical={20} />
                    </div>
                    <p>
                        Placeholder: maybe some sort of explanation about what
                        this means?
                    </p>
                </div>
                <div class="column">
                    <div style="height: 5vh" />
                    <div
                        style="height: 15vh; display: flex; justify-content: center; align-items: center;">
                        <Speedometer
                            value={evidence}
                            segments={1000}
                            maxSegmentLabels={0}
                            needleColor="#f5f5f5"
                            needleTransitionDuration={3000}
                            needleTransition="easeElastic"
                            needleHeightRatio={0.7}
                            startColor="#ffdd57"
                            endColor="#60c689"
                            ringWidth={5}
                            textColor="#f5f5f5"
                            currentValueText="Evidence: {evidence > 500
                                ? 'High'
                                : 'Low'}"
                            paddingVertical={20} />
                    </div>
                    <p>
                        Placeholder: maybe some sort of explanation about what
                        this means?
                    </p>
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
                        <th class="has-text-left">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="has-text-left">2023-02-08 21:09:19</td>
                        <th class="has-text-left">AAPL</th>
                        <td class="has-text-left">Buy</td>
                        <td class="has-text-left">10</td>
                        <td class="has-text-right">151.66</td>
                        <td class="has-text-right">1516.63</td>
                        <td class="has-text-left has-text-success">meh</td>
                    </tr>
                </tbody>
            </table>
            <hr style="background: #4a4a4a; height: 1px" />
        </div>

        <div class="block mx-5">
            <header class="title is-5">Rationalization</header>
            <p>Placeholder: possibly the free text stuff the user says</p>
            <div class="block">
                <div class="tile is-ancestor">
                    <div class="tile is-parent is-vertical">
                        {#each responses.filter((element, index) => index % 3 === 0) as response}
                            <NewsTileStatic data={response} />
                        {/each}
                    </div>
                    <div class="tile is-parent is-vertical">
                        {#each responses.filter((element, index) => index % 3 === 1) as response}
                            <NewsTileStatic data={response} />
                        {/each}
                    </div>
                    <div class="tile is-parent is-vertical">
                        {#each responses.filter((element, index) => index % 3 === 2) as response}
                            <NewsTileStatic data={response} />
                        {/each}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .modal-content {
        width: 90vw;
        height: 90vh;
        overflow-x: hidden;
        background: #363636;
        border-radius: 7px;
    }
</style>
