<script lang="ts">
    import api from "$lib/api";
    import type { MathsResponse } from "$lib/api/maths";

    let token: string = "";
    let a = 0;
    let b = 0;
    let request: Promise<MathsResponse | undefined> =
        Promise.resolve(undefined);
</script>

<h3 class="title is-3">Maths Get</h3>
<p>
    <input class="input" bind:value={token} placeholder="Bearer token" />
</p>
<p>
    <input type="number" class="input" bind:value={a} placeholder="a" />
</p>
<p>
    <input type="number" class="input" bind:value={b} placeholder="b" />
</p>
<p>
    <button
        class="button"
        on:click={() => (request = api.maths(token).get(a, b))}>Send</button>
</p>
{#await request}
    <p>Waiting...</p>
{:then response}
    {#if response}
        <p>Added: {response.add}</p>
        <p>Multiplied: {response.multiply}</p>
        <p>User: {response.authenticated_user}</p>
    {/if}
{:catch error}
    <p>{error.message}</p>
{/await}
