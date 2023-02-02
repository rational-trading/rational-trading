<script lang="ts">
    import Counter from "$components/Counter.svelte";

    const items = ["Apples", "Bananas", "Oranges", "Peaches"];
</script>

{#each items as label}
    <Counter {label} />
{/each}
