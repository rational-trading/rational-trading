<script lang="ts" context="module">
    import Search from "$components/search/Search.svelte";
    import type { MakeTrade } from "$lib/api/trades";
    import { defaultForm } from "./+page.svelte";

    export function nextStepUrl(
        ticker: string,
        previousState: MakeTrade | null = null
    ) {
        const filledForm =
            previousState && previousState.ticker == ticker
                ? previousState
                : { ...defaultForm(), ticker };
        return stepUrl(2, filledForm);
    }
</script>

<script lang="ts">
    import { goto } from "$app/navigation";
    import { stepUrl } from "./Steps.svelte";

    export let initialState: MakeTrade;

    $: ({ ticker } = initialState);
</script>

<div class="level">
    <div class="level-item">
        <div>
            <h2 class="block title is-2">Select Stock</h2>
            <br />
            <div class="block">
                <Search
                    text={ticker}
                    onSelected={(stock) =>
                        goto(nextStepUrl(stock.ticker, initialState))} />
            </div>
        </div>
    </div>
</div>
