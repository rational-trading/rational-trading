<script lang="ts">
    import Search from "$components/search/Search.svelte";
    import type { Stock } from "$lib/types";

    export let onSelected: (stock: Stock) => void;
    export let exit: () => void;
</script>

<div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={exit} />
    <div class="modal-content">
        <Search
            onSelected={(stock) => {
                onSelected(stock);
                exit();
            }} />
    </div>
</div>

<style>
    .modal-content {
        width: 40vw;
        height: 60vh;
        background: #363636;
        border-radius: 7px;
    }
</style>
