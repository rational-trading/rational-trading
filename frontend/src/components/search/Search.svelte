<script lang="ts">
    import { matchAny } from "$lib/functions";
    import { stocks } from "$lib/stores";
    import type { Stock } from "$lib/types";
    import SearchItem from "./SearchItem.svelte";

    export let onSelected: (s: Stock) => void;
    export let text = "";

    $: filteredStocks = $stocks.all.filter((s) =>
        matchAny(text, [s.exchange, s.name, s.ticker])
    );
</script>

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
                <SearchItem {stock} onClick={onSelected} />
            {/each}
        </tbody>
    </table>
</div>
