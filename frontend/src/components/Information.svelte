<script lang="ts">
    import type { Stock } from "$lib/types";
    import api from "$lib/api";
    import type { Financials } from "$lib/api/financials";
    import { browser } from "$app/environment";

    export let stock: Stock;

    let requestFinancials = api.pendingRequest<Financials>();
    const newRequestFinancials = () => api.financials().about(stock.ticker);

    $: if (browser) requestFinancials = newRequestFinancials();
</script>

<!-- Finances -->
{#await requestFinancials}
    <p>Retrieving stocks financial details...</p>
{:then response}
    <nav class="level" style="width: 80%">
        <div class="level-item has-text-centered">
            <div>
                <p class="heading">Price - Earning Ratio</p>
                <p class="title">
                    {response.price_earning_ratio.toFixed(3)}
                </p>
            </div>
        </div>
        <div class="level-item has-text-centered">
            <div>
                <p class="heading">Earnings per share</p>
                <p class="title">
                    {response.earnings_per_share.toFixed(3)}
                </p>
            </div>
        </div>
        <div class="level-item has-text-centered">
            <div>
                <p class="heading">Debt to equity</p>
                <p class="title">
                    {response.debt_to_equity.toFixed(3)}
                </p>
            </div>
        </div>
        <div class="level-item has-text-centered">
            <div>
                <p class="heading">Current ratio</p>
                <p class="title">
                    {response.current_ratio.toFixed(3)}
                </p>
            </div>
        </div>
    </nav>
{:catch error}
    console.log({error.message})
{/await}
