<script lang="ts">
    import {
        defaultWatchlist, stocks, user, userWatchlist,
    } from "$lib/stores";
    import { matchAny } from "$lib/functions";
    import type { Stock } from "$lib/types";
    import WatchlistAddItem from "./WatchlistAddItem.svelte";

    export let stock: Stock;
    export let onAdd: (stock: Stock) => void;

    let text = stock.ticker;

    $: filteredStocks = $stocks.all.filter((s) => matchAny(text, [s.exchange, s.name, s.ticker]));

    let active = false;
</script>

<span class="icon">
    <!-- svelte-ignore a11y-missing-attribute -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <a
        on:click={() => {
            active = true;
            if (
                ($user && $userWatchlist.includes(stock.ticker)) ||
                (!$user && $defaultWatchlist.includes(stock.ticker))
            ) {
                text = "";
            } else {
                text = stock.ticker;
            }
        }}><i class="fas fa-plus" /></a>
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
                            <WatchlistAddItem
                                {stock}
                                onClick={(s) => {
                                    active = false;
                                    onAdd(s);
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
