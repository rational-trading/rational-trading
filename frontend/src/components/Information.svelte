<script lang="ts">
    import type { Stock } from "$lib/types";
    import api from "$lib/api";
    import type { Financials } from "$lib/api/financials";
    import { browser } from "$app/environment";

    export let stock: Stock;

    let requestFinancials = api.pendingRequest<Financials>();
    const newRequestFinancials = () => api.financials().get(stock.ticker);

    $: if (browser) requestFinancials = newRequestFinancials();
</script>

<!-- Finances -->
<h1 class="title is-5">Financials</h1>

{#await requestFinancials}
    <div
        style="width: 100%; height: 3vh; display: flex; justify-content: center; align-items: center;">
        <p>Retrieving financial details...</p>
    </div>
{:then response}
    <div
        style="height: 20vh; width: 100%; display: flex; justify-content: center; align-items: center;">
        <nav class="level" style="width: 100%">
            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">Earnings per share</p>
                    <p class="title is-5">
                        {response.earnings_per_share.toFixed(3)}
                    </p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">P/E Ratio</p>
                    <p class="title is-5">
                        {response.price_earning_ratio.toFixed(3)}
                    </p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">D/E Ratio</p>
                    <p class="title is-5">
                        {response.debt_to_equity.toFixed(3)}
                    </p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">Current ratio</p>
                    <p class="title is-5">
                        {response.current_ratio.toFixed(3)}
                    </p>
                </div>
            </div>
        </nav>
    </div>
{:catch error}
    <div
        style="width: 100%; height: 3vh; display: flex; justify-content: center; align-items: center;">
        <p>{error.message}</p>
    </div>
{/await}
