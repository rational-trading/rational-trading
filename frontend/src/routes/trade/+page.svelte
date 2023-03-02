<script lang="ts">
    import { page } from "$app/stores";
    import Steps from "./Steps.svelte";

    let steps = ["Select Stock", "Add Evidence", "Create Order", "Confirm"];
    let step: number;

    $: {
        let stepString = $page.url.searchParams.get("step") ?? "";
        let parsed = parseInt(stepString);
        step = isNaN(parsed)
            ? 0
            : Math.max(1, Math.min(parsed, steps.length)) - 1;
    }
</script>

<div class="block mt-5 ml-5">
    <h1 class="title is-2">Select Trade</h1>
</div>

<div class="columns mt-5" style="height: 17rem; width: calc(100vw + 12px);">
    <div class="column is-one-fifth" />
    <div class="column is-three-fifths">
        <div class="box mx-5 has-background-grey-darker">
            <Steps {steps} currentIndex={step} />
            <div>
                <p class="heading">Current value</p>
                <p class="title">£13,267.39</p>
            </div>
            <div class="block" style="height: 20%" />
            <div class="columns">
                <div class="column">
                    <div>
                        <p class="heading">Today's gain/loss</p>
                        <p class="subtitle has-text-success">£28.27 (1.50%)</p>
                    </div>
                </div>
                <div class="column">
                    <div>
                        <p class="heading">Overall gain/loss</p>
                        <p class="subtitle has-text-success">
                            £1,937.25 (14.60%)
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="column is-one-fifth" />
</div>
