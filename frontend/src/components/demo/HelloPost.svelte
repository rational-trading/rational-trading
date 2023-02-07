<script lang="ts">
    import api from "$lib/api";

    let name: string = "";
    let request: Promise<string> = Promise.resolve("");
</script>

<h3 class="title is-3">Hello Post</h3>
<input class="input" bind:value={name} />
<br />
<br />
<button class="button" on:click={() => (request = api.hello().post(name))}
    >Send</button>
<br />
<br />
{#await request}
    <p>Waiting...</p>
{:then response}
    <p>{response}</p>
{/await}
