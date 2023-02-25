<script lang="ts">
    import "../app.scss";
    import { user } from "$lib/stores";
    import { authenticate } from "$lib/auth";
    import Login from "$components/Login.svelte";
    import Signup from "$components/Signup.svelte";
    import Logout from "$components/Logout.svelte";
    import { browser } from "$app/environment";

    // Attempt to re-authenticate on refresh.
    if (browser) {
        try {
            authenticate();
        } catch {
            // Silently ignore if token has expired (authenticate automatically logs them out).
        }
    }
</script>

<!-- the navbar -->
<nav class="navbar is-primary is-fixed-top">
    <div class="navbar-brand">
        <a class="navbar-item" href="/">
            <img src="/logo.png" width="177" height="50" alt="logo" />
        </a>
    </div>

    <div class="navbar-menu">
        <div class="navbar-start">
            <a class="navbar-item" href="/"> Home </a>

            <a class="navbar-item" href="/explore"> Explore </a>

            <a class="navbar-item" href="/portfolio"> Portfolio </a>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    {#if $user}
                        <p class="navbar-item mx-3">{$user.username}</p>
                        <Logout />
                    {:else}
                        <Signup />
                        <Login />
                    {/if}
                </div>
            </div>
        </div>
    </div>
</nav>

<slot />
