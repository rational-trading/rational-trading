<script lang="ts">
    export let close: () => void;

    let buy = true;
</script>

<div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={close} />
    <div class="modal-content">
        <div class="is-flex is-flex-direction-column">
            <div class="is-align-self-flex-end">
                <button class="button is-ghost" on:click={close}>
                    <span class="icon is-large">
                        <i class="fas fa-xmark" />
                    </span>
                </button>
            </div>

            <div class="columns">
                <div
                    class="column is-one-third"
                    style="height: 75vh; border-right: 1px solid #4a4a4a;">
                    <div class="buttons has-addons is-centered">
                        <button
                            class="button is-large {buy
                                ? 'is-info is-selected'
                                : ''}"
                            on:click={() => (buy = true)}
                            style="width: 45%; justify-content: left; text-align: left">
                            <div>
                                <p class="title is-4">Buy</p>
                                <p class="subtitle is-5">153.22</p>
                            </div>
                        </button>
                        <button
                            class="button is-large {buy
                                ? ''
                                : 'is-info is-selected'}"
                            on:click={() => (buy = false)}
                            style="width: 45%; justify-content: right; text-align: right">
                            <div>
                                <p class="title is-4">Sell</p>
                                <p class="subtitle is-5">152.94</p>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .modal-content {
        width: 80vw;
        height: 80vh;
        background: #363636;
        border-radius: 7px;
    }
</style>
