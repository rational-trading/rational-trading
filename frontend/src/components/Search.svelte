<script lang="ts">
    let search = false;
</script>

<button
    class="button is-rounded"
    style="width: 100%"
    on:click={() => (search = true)}>
    <div class="level" style="width: 100%">
        <div class="level-left">
            <div class="level-item">
                <span class="icon">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </div>
            <div class="level-item">
                <p class="has-text-grey-lighter has-text-weight-light">
                    Search for a stock to display...
                </p>
            </div>
        </div>
    </div>
</button>

{#if search}
    <div class="modal is-active">
        <div class="modal-background" on:click={() => (search = false)} />
        <div class="modal-content">
            <p class="control has-icons-left m-2">
                <input
                    class="input is-large"
                    type="text"
                    style="color: #f5f5f5; background: #363636;"
                    value="AAPL" />
                <span class="icon is-large is-left">
                    <i class="fas fa-magnifying-glass" />
                </span>
            </p>
        </div>
    </div>
{/if}

<style>
    .modal-content {
        width: 31.25em;
        height: 35.5em;
        background: #363636;
        border-radius: 7px;
    }
</style>
