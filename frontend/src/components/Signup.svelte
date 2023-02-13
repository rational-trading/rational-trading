<script lang="ts">
    let active = false;

    function isActive() {
        return active ? "is-active" : "";
    }
</script>

<style>
    .modal-content {
        width: 31.25em;
        height: 35.5em;
        background: #D9D9D9;
        border-radius: 7px;
    }

    .link:hover {
        text-decoration: underline;
        color: #276BB0;
    }

    #login-contents {
        margin: 2.5em 3.125em 0em;
    }
</style>

<button class="button is-info" on:click={() => { active = true; }}>
    <strong>Sign up</strong>
</button>

{#if active}
    <div class="modal is-active">
    <div class="modal-background" color=""/>
    <div class="modal-content">
        <div class="is-flex is-flex-direction-column">
            <div class="is-align-self-flex-end">
                <button class="delete is-large" style="background: #D9D9D9" aria-label="close" on:click={() => { active = false; }}></button>
            </div>
            <div class="is-flex is-flex-direction-column pt-4" id="login-contents">
                <p class="title is-1 has-text-dark">Sign up</p>

                <div class="field mt-5">
                    <div class="control">
                        <input class="input" type="email" placeholder="Email" />
                    </div>
                </div>
                <div class="field mt-3">
                    <div class="control">
                        <input class="input" type="password" placeholder="Password" />
                    </div>
                </div>

                <div class="field mt-3">
                    <div class="control">
                        <input class="input" type="password" placeholder="Repeat password" />
                    </div>
                </div>

                <div class="is-align-self-flex-end pt-5">
                    <div class="field">
                        <div class="control">
                            <button class="button is-link is-medium"><p class="px-3"><strong>Sign up</strong></p></button> 
                        </div>
                    </div>
                </div>


                <div class="is-align-self-center pt-6">
                    <p class="has-text-dark">Already have an account? Log in <a class="link" href="/">here</a>.</p>
                </div>
            </div>
        </div>
    </div>
    </div>
{/if}

