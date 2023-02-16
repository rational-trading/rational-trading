<script lang="ts">
    let active = false;
</script>

<button
    class="button is-primary is-light has-text-light"
    on:click={() => {
        active = true;
    }}>
    <strong>Log in</strong>
</button>

{#if active}
    <div class="modal is-active">
        <div class="modal-background" color="" />
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
                <div
                    class="is-flex is-flex-direction-column pt-3"
                    id="login-contents">
                    <p class="title is-1">Log in</p>

                    <div class="field mt-5">
                        <div class="control">
                            <input
                                class="input"
                                type="email"
                                placeholder="Email" />
                        </div>
                    </div>
                    <div class="field mt-3">
                        <div class="control">
                            <input
                                class="input"
                                type="password"
                                placeholder="Password" />
                        </div>
                    </div>

                    <div>
                        <a class="link" href="/">Forgot your password?</a>
                    </div>

                    <div class="is-align-self-flex-end pt-5">
                        <div class="field">
                            <div class="control">
                                <button class="button is-link is-medium"
                                    ><p class="px-3">
                                        <strong>Log in</strong>
                                    </p></button>
                            </div>
                        </div>
                    </div>

                    <div class="is-align-self-center pt-6">
                        <p>
                            Don't have an account? Sign up <a
                                class="link"
                                href="/">here</a
                            >.
                        </p>
                    </div>
                </div>
            </div>
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

    .link:hover {
        text-decoration: underline;
        color: #276bb0;
    }

    #login-contents {
        margin: 2.5em 3.125em 0em;
    }
</style>
