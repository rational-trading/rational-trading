<script lang="ts">
    import "../app.scss";
    import { user } from "$lib/stores";
    import { authenticate } from "$lib/auth";
    import { loadTickerDetails } from "$lib/stocks";
    import Login from "$components/auth/Login.svelte";
    import Signup from "$components/auth/Signup.svelte";
    import Logout from "$components/auth/Logout.svelte";
    import { browser } from "$app/environment";

    // Attempt to re-authenticate on refresh.
    if (browser) {
        loadTickerDetails();
        authenticate().catch(() => {});
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

            <a class="navbar-item" href="/explore/"> Explore </a>

            {#if $user}
                <a class="navbar-item" href="/portfolio/"> Portfolio </a>
                <a class="navbar-item" href="/trade/"> Trade </a>
            {/if}
        </div>

        <div class="navbar-end">
            {#if $user}
                <div class="navbar-item has-dropdown is-hoverable">
                    <p class="navbar-link">{$user.username}</p>

                    <div class="navbar-dropdown">
                        <Logout />
                    </div>
                </div>
            {:else}
                <div class="navbar-item">
                    <div class="buttons">
                        <Signup />
                        <Login />
                    </div>
                </div>
            {/if}
        </div>
    </div>
</nav>

<slot />
