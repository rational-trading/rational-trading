<script lang="ts">
    import AddItem from "./AddItem.svelte";
    import { displaySymbol } from "$lib/stores";

    let active = false;

    const addItems = [
        {
            symbol: "AAPL",
            company: "Apple Inc.",
            exchange: "NASDAQ",
        },
        {
            symbol: "TSLA",
            company: "Tesla, Inc.",
            exchange: "NASDAQ",
        },
        {
            symbol: "NFLX",
            company: "Netflix, Inc.",
            exchange: "NASDAQ",
        },
    ];
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a on:click={() => (active = true)}><i class="fas fa-plus" /></a>
</span>

{#if active}
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="modal-background" on:click={() => (active = false)} />
        <div class="modal-content">
            <p class="control has-icons-left m-2">
                <input
                    class="input is-large"
                    type="text"
                    value={$displaySymbol} />
                <span class="icon is-large is-left">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </p>

            <div class="table-container" style="overflow-y: auto;">
                <table class="table is-hoverable is-fullwidth is-dark">
                    <tbody>
                        {#each addItems as item}
                            <AddItem data={item} bind:active />
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
