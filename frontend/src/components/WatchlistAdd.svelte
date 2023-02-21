<script lang="ts">
    import { currentStock, stocks } from "$lib/stores";
    import { matchAny } from "$lib/functions";
    import AddItem from "./AddItem.svelte";

    let text = $currentStock.ticker;

    $: filteredStocks = $stocks.filter((s) => matchAny(text, [s.exchange, s.name, s.ticker]));

    let active = false;
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a on:click={() => (active = true)}><i class="fas fa-plus" /></a>
</span>

{#if active}
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div
            class="modal-background"
            on:click={() => {
                active = false;
                text = $currentStock.ticker;
            }} />
        <div class="modal-content">
            <p class="control has-icons-left m-2">
                <input
                    class="input is-large"
                    type="text"
                    placeholder="Search"
                    bind:value={text} />
                <span class="icon is-large is-left">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </p>

            <div class="table-container" style="overflow-y: auto;">
                <table class="table is-hoverable is-fullwidth is-dark">
                    <tbody>
                        {#each filteredStocks as stock}
                            <AddItem
                                {stock}
                                onClick={() => {
                                    text = "";
                                    active = false;
                                }} />
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
