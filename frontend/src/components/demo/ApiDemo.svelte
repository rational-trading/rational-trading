<script lang="ts">
    import HelloGet from "./HelloGet.svelte";
    import HelloPost from "./HelloPost.svelte";
    import MathsGet from "./MathsGet.svelte";
    import PriceHistory from "./PriceHistory.svelte";
</script>

<div class="box">
    <h2 class="title is-2">API Demo</h2>
    <div class="columns">
        <div class="column is-one-third">
            <HelloGet />
        </div>
        <div class="column is-one-third">
            <HelloPost />
        </div>
        <div class="column is-one-third">
            <MathsGet />
        </div>
    </div>

    <div class="columns">
        <div class="column is-one-third">
            <PriceHistory />
        </div>
        <div class="column is-one-third" />
        <div class="column is-one-third" />
    </div>
</div>
