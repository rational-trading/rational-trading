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
</script>

<script lang="ts">
    import { page } from "$app/stores";

    import Steps from "./Steps.svelte";
    import StockSearch from "./StockSearch.svelte";
    import { browser } from "$app/environment";
    import AddEvidence from "./AddEvidence.svelte";
    import ChooseAmount from "./ChooseAmount.svelte";

    const steps = [
        {
            title: "Select Stock",
            icon: "mouse-pointer",
        },
        {
            title: "Add Evidence",
            icon: "plus",
        },
        {
            title: "Choose Amount",
            icon: "dollar",
        },
        {
            title: "Review",
            icon: "shopping-cart",
        },
        {
            title: "Confirmation",
            icon: "check",
        },
    ];
    let step: number;

    $: {
        const stepString =
            (browser ? $page.url.searchParams.get("step") : null) ?? "";
        const parsed = parseInt(stepString, 10);
        step = Number.isNaN(parsed)
            ? 1
            : Math.max(1, Math.min(parsed, steps.length));
    }

    let initialState = defaultForm();
    $: {
        const stateParam = browser ? $page.url.searchParams.get("state") : null;
        if (stateParam) {
            initialState = fromHex<MakeTrade>(stateParam);
        }
    }

    let currentState: MakeTrade = defaultForm();
</script>

<br />
<br />
<div class="columns" style="height: 17rem; width: calc(100vw + 12px);">
    <div class="column" />
    <div class="column is-four-fifths">
        <div class="box p-6 has-background-grey-darker">
            <Steps {steps} currentIndex={step - 1} {currentState} />
            <br />
            {#if step === 1}
                <StockSearch {initialState} />
            {:else if step === 2}
                <AddEvidence {initialState} bind:currentState />
            {:else if step === 3}
                <ChooseAmount {initialState} bind:currentState />
            {/if}
        </div>
    </div>
    <div class="column" />
</div>
