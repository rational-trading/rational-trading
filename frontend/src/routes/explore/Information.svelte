<script lang="ts">
    import {
        displaySymbol,
        displayCompany,
        displayExchange,
    } from "$lib/stores";

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
            Here is some {$displaySymbol}. Need some api or global dict to
            display company name as well.
        </p>
    </div>
{:else}
    <!-- Finances -->
    <div class="block mx-2">
        <p>Here is some other text.</p>
    </div>
{/if}
