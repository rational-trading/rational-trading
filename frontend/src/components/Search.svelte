<script lang="ts">
    import SearchItem from "./SearchItem.svelte";
    import { currentStock } from "$lib/stores";

    let active = false;

    const searchItems = [
        {
            ticker: "AAPL",
            name: "Apple Inc",
            exchange: "NASDAQ",
        },
        {
            ticker: "TSLA",
            name: "Tesla, Inc.",
            exchange: "NASDAQ",
        },
        {
            ticker: "NFLX",
            name: "Netflix, Inc.",
            exchange: "NASDAQ",
        },
    ];
</script>

<button
    class="button is-rounded"
    style="width: 100%"
    on:click={() => (active = true)}>
    <div class="level" style="width: 100%">
        <div class="level-left">
            <div class="level-item">
                <span class="icon">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </div>
            <div class="level-item">
                <p class="has-text-grey-lighter has-text-weight-light">
                    Search for a stock to display...
                </p>
            </div>
        </div>
    </div>
</button>

{#if active}
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="modal-background" on:click={() => (active = false)} />
        <div class="modal-content">
            <p class="control has-icons-left m-2">
                <input
                    class="input is-large"
                    type="text"
                    value={$currentStock.ticker} />
                <span class="icon is-large is-left">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </p>

            <div class="table-container" style="overflow-y: auto;">
                <table class="table is-hoverable is-fullwidth is-dark">
                    <tbody>
                        {#each searchItems as item}
                            <SearchItem data={item} bind:active />
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
{/if}

<style>
    .modal-content {
        width: 40vw;
        height: 60vh;
        background: #363636;
        border-radius: 7px;
    }
</style>
