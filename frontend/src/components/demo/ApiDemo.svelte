<script lang="ts">
    import GetNews from "./GetNews.svelte";
    import PortfolioHoldings from "./PortfolioHoldings.svelte";
    import PriceHistory from "./PriceHistory.svelte";
    import PriceRecent from "./PriceRecent.svelte";
</script>

<div class="box">
    <h2 class="title is-2">API Demo</h2>
    <div class="columns">
        <div class="column is-one-third">
            <PriceHistory />
        </div>
        <div class="column is-one-third">
            <PriceRecent />
        </div>
        <div class="column is-one-third">
            <PortfolioHoldings />
            <hr />
            <GetNews />
        </div>
    </div>
</div>
