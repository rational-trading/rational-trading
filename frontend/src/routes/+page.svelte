<script lang="ts">
    import data from "$lib/data";
    import { double } from "$common";
    import type { Post } from "$common";
    import Counter from "$components/Counter.svelte";

    let p: Post = { title: "GME Crashes", id: 4 };
    let items = ["Apples", "Bananas", "Oranges"];
</script>

<div class="columns m-6">
    <div class="column is-one-third" />
    <div class="column is-one-third">
        <div class="content">
            <h1>Test</h1>
            <p>Some data is: {data}</p>
            <p>The post title is: {p.title}</p>
            <p>The post id is {p.id}, and doubled is {double(p.id)}</p>
        </div>
        {#each items as label}
            <Counter {label} />
        {/each}
    </div>
    <div class="column is-one-third" />
</div>
