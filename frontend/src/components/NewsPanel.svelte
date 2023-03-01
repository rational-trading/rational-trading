<script lang="ts">
    import NewsTile from "./NewsTile.svelte";

    let active = false;

    function click() {
        active = true;
    }
</script>

<button class="button is-outline is-small is-rounded" on:click={click}>
    More news
</button>

{#if active}
    <div class="modal is-active">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="modal-background" on:click={() => (active = false)} />
        <div class="modal-content">
            <div class="is-flex is-flex-direction-column">
                <div class="is-align-self-flex-end">
                    <button
                        class="button is-ghost"
                        on:click={() => (active = false)}>
                        <span class="icon is-large">
                            <i class="fas fa-xmark" />
                        </span>
                    </button>
                </div>

                <header class="title is-1 mx-5">News</header>

                <div class="tile is-ancestor mx-3 mb-3">
                    <div class="tile is-vertical is-8">
                        <div class="tile">
                            <div class="tile is-parent is-vertical">
                                <NewsTile />
                                <NewsTile />
                                <NewsTile />
                                <NewsTile />
                            </div>
                            <div class="tile is-parent">
                                <NewsTile />
                            </div>
                        </div>
                        <div class="tile is-parent">
                            <NewsTile />
                        </div>
                    </div>
                    <div class="tile is-parent">
                        <NewsTile />
                    </div>
                </div>
            </div>
        </div>
    </div>
{/if}

<style>
    .modal-content {
        width: 80vw;
        height: 80vh;
        background: #363636;
        border-radius: 7px;
    }
</style>
