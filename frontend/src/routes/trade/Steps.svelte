<script lang="ts" context="module">
    import type { MakeTrade } from "$lib/api/trades";
    import { toHex } from "$lib/functions";

    export interface Step {
        title: string;
        icon: string;
    }

    export function stepUrl(step: number, currentForm: MakeTrade) {
        return `/trade/?step=${step}&state=${toHex<MakeTrade>(currentForm)}`;
    }
</script>

<script lang="ts">
    export let steps: Step[];
    export let currentIndex: number;
    export let currentState: MakeTrade;

    $: entries = Array.from(steps.entries());
</script>

<ul class="steps is-medium has-content-centered is-centered">
    {#each entries as [index, step]}
        <li class="steps-segment" class:is-active={index === currentIndex}>
            {#if index < currentIndex && currentIndex !== steps.length - 1}
                <a href={stepUrl(index + 1, currentState)}
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
