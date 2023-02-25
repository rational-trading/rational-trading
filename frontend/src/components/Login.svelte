<script lang="ts">
    import api from "$lib/api";
    import { user } from "$lib/stores";

    let active = false;

    let username = "";
    let password = "";

    async function handleLogin() {
        try {
            const jwtToken = await api.login().post(username, password);
            localStorage.setItem("access_token", jwtToken);

            const whoami = await api.whoami().get();
            user.set({ username: whoami });

            active = false;
        } catch (error: any) {
            alert("Incorrect credentials");
            user.set(null);
        }
    }
</script>

<button
    class="button is-primary is-light has-text-light"
    on:click={() => {
        active = true;
    }}
>
    <strong>Log in</strong>
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
                        on:click={() => (active = false)}
                    >
                        <span class="icon is-large">
                            <i class="fas fa-xmark" />
                        </span>
                    </button>
                </div>
                <div
                    class="is-flex is-flex-direction-column pt-3"
                    id="login-contents"
                >
                    <p class="title is-1">Log in</p>

                    <div class="field mt-5">
                        <div class="control">
                            <input
                                class="input"
                                placeholder="Username"
                                bind:value={username}
                            />
                        </div>
                    </div>
                    <div class="field mt-3">
                        <div class="control">
                            <input
                                class="input"
                                type="password"
                                placeholder="Password"
                                bind:value={password}
                            />
                        </div>
                    </div>

                    <div>
                        <a class="link" href="/">Forgot your password?</a>
                    </div>

                    <div class="is-align-self-flex-end pt-5">
                        <div class="field">
                            <div class="control">
                                <button
                                    class="button is-link is-medium"
                                    on:click={() => handleLogin()}
                                    ><p class="px-3">
                                        <strong>Log in</strong>
                                    </p></button
                                >
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
