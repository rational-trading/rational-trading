<script lang="ts">
    import api from "$lib/api";

    let name: string = "";
    let request: Promise<string> = Promise.resolve("");
</script>

<h3 class="title is-3">Hello Get</h3>
<input class="input" bind:value={name} />
<br />
<br />
<button
    class="button"
    on:click={() => (request = api.hello().get(name === "" ? undefined : name))}
    >Send</button>
<br />
<br />
{#await request}
    <p>Waiting...</p>
{:then response}
    <p>{response}</p>
{:catch error}
    <p>{error.message}</p>
{/await}
