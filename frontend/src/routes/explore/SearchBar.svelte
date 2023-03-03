<script lang="ts">
    import SearchPane from "$components/search/SearchPane.svelte";
    import type { Stock } from "$lib/types";

    export let onSelected: (stock: Stock) => void;
    let active = false;
</script>

<button
    class="button is-rounded"
    style="width: 100%"
    on:click={() => {
        active = true;
    }}>
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
    <SearchPane
        {onSelected}
        exit={() => {
            active = false;
        }} />
{/if}
