<script lang="ts" context="module">
    import { fromHex, toHex } from "$lib/functions";
    import type { MakeTrade } from "$lib/api/trades";

    export function defaultForm(): MakeTrade {
        return {
            ticker: "",
            side: "BUY",
            type: "UNITS",
            amount: 0,
            text_evidence: "",
            article_evidence: [],
        };
    }

    export function stepUrl(step: number, currentForm: MakeTrade) {
        return `/trade/?step=${step}&state=${toHex<MakeTrade>(currentForm)}`;
    }
</script>

<script lang="ts">
    import { page } from "$app/stores";

    import Steps from "./Steps.svelte";
    import StockSearch from "./StockSearch.svelte";
    import { browser } from "$app/environment";

    const steps = ["Select Stock", "Add Evidence", "Create Order", "Confirm"];
    let step: number;

    $: {
        const stepString =
            (browser ? $page.url.searchParams.get("step") : null) ?? "";
        const parsed = parseInt(stepString, 10);
        step = Number.isNaN(parsed) ?
            1 :
            Math.max(1, Math.min(parsed, steps.length));
    }

    let initialState = defaultForm();
    $: {
        const stateParam = browser ? $page.url.searchParams.get("state") : null;
        if (stateParam) {
            initialState = fromHex<MakeTrade>(stateParam);
        }
    }
</script>

<div class="block mt-5 ml-5">
    <h1 class="title is-2">Select Trade</h1>
</div>

<div class="columns mt-5" style="height: 17rem; width: calc(100vw + 12px);">
    <div class="column is-one-fifth" />
    <div class="column is-three-fifths">
        <div class="box mx-5 has-background-grey-darker">
            <Steps {steps} currentIndex={step - 1} />
            {#if step === 1}
                <StockSearch {initialState} />
            {/if}
        </div>
    </div>
    <div class="column is-one-fifth" />
</div>
