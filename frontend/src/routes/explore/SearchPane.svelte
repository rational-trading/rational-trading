<script lang="ts">
    import Search from "$components/Search.svelte";
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
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="modal-background" on:click={() => (active = false)} />
        <div class="modal-content">
            <Search
                onSelected={(stock) => {
                    onSelected(stock);
                    active = false;
                }} />
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
