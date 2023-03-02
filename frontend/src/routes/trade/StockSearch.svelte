<script lang="ts" context="module">
    import Search from "$components/search/Search.svelte";
    import type { MakeTrade } from "$lib/api/trades";
    import { toHex } from "$lib/functions";
    import { defaultForm } from "./+page.svelte";

    export function nextStepUrl(ticker: string): string {
        const filledForm = { ...defaultForm(), ticker };
        return `/trade/?step=2&state=${toHex<MakeTrade>(filledForm)}`;
    }
</script>

<script lang="ts">
    import { goto } from "$app/navigation";

    export let initialState: MakeTrade;

    $: ({ ticker } = initialState);
</script>

<Search text={ticker} onSelected={(stock) => goto(nextStepUrl(stock.ticker))} />
