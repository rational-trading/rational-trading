<script lang="ts">
    import type { Stock } from "$lib/types";

    export let stock: Stock;

    let keyStats = true;

    function ksClick() {
        keyStats = true;
    }

    function fClick() {
        keyStats = false;
    }
</script>

<div class="tabs">
    <ul>
        <li class:is-active={keyStats}>
            <!-- svelte-ignore a11y-missing-attribute -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <a on:click={ksClick}>Key Stats</a>
        </li>
        <li class:is-active={!keyStats}>
            <!-- svelte-ignore a11y-missing-attribute -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <a on:click={fClick}>Finances</a>
        </li>
    </ul>
</div>

{#if keyStats}
    <!-- Key Stats -->
    <div class="block mx-2">
        <p>
            Current stock: {stock.ticker}, {stock.name}, {stock.exchange}
        </p>
    </div>
{:else}
    <!-- Finances -->
    <div class="block mx-2">
        <p>Here is some other text.</p>
    </div>
{/if}
