<script lang="ts">
    export let steps: string[];
    export let currentIndex: number;

    $: entries = Array.from(steps.entries());
</script>

<ul class="steps has-content-centered">
    {#each entries as [index, step]}
        <li class="steps-segment" class:is-active={index === currentIndex}>
            <span class="steps-marker" />
            <div class="steps-content">
                {#if index === currentIndex}
                    <p class="is-size-5"><b>{step}</b></p>
                {:else}
                    <p class="has-text-grey-lighter">{step}</p>
                {/if}
            </div>
        </li>
    {/each}
</ul>
