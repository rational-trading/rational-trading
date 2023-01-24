<script lang="ts">
    export let label: string;
    let counter = 0;
</script>

<div class="box">
    <h2 class="title is-3">{label}: {counter}</h2>
    <button
        class="button is-primary"
        on:click={() => counter++}
        disabled={counter >= 10}>Increment</button>
    <button
        class="button is-danger"
        on:click={() => counter--}
        disabled={counter <= 0}>Decrement</button>
</div>
