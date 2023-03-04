<script lang="ts" context="module">
    export interface Step {
        title: string;
        icon: string;
    }
</script>

<script lang="ts">
    export let steps: Step[];
    export let currentIndex: number;

    $: entries = Array.from(steps.entries());
</script>

<ul class="steps is-medium has-content-centered is-centered">
    {#each entries as [index, step]}
        <li class="steps-segment" class:is-active={index === currentIndex}>
            {#if index < currentIndex}
                <a href="/"
                    ><span class="steps-marker">
                        <span class="icon">
                            <i class="fa fa-{step.icon}" />
                        </span></span>
                    <div class="steps-content">
                        <p class="has-text-grey-lighter">{step.title}</p>
                    </div>
                </a>
            {:else}
                <span class="steps-marker">
                    <span class="icon">
                        <i class="fa fa-{step.icon}" />
                    </span>
                </span>
                <div class="steps-content">
                    {#if index === currentIndex}
                        <p class="has-text-white is-size-5">
                            <b>{step.title}</b>
                        </p>
                    {:else}
                        <p class="has-text-grey-lighter">{step.title}</p>
                    {/if}
                </div>
            {/if}
        </li>
    {/each}
</ul>

<style>
    .icon {
        padding-left: 2px;
    }
</style>
