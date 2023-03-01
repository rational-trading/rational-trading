<script lang="ts">
    import "../app.scss";
    import { user } from "$lib/stores";
    import { authenticate } from "$lib/auth";
    import { loadTickerDetails } from "$lib/stocks";
    import Login from "$components/Login.svelte";
    import Signup from "$components/Signup.svelte";
    import Logout from "$components/Logout.svelte";
    import TimeAgo from "javascript-time-ago";
    import en from "javascript-time-ago/locale/en";
    import { browser } from "$app/environment";

    TimeAgo.addDefaultLocale(en);

    // Attempt to re-authenticate on refresh.
    if (browser) {
        loadTickerDetails();
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

            {#if $user}
                <a class="navbar-item" href="/portfolio"> Portfolio </a>
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
