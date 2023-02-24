<script lang="ts">
    import { authenticated } from "$lib/stores";

    function handleLogout() {
        authenticated.set(false);
        localStorage.removeItem("access_token");
    }
</script>

<button class="button is-info" on:click={() => handleLogout()}>
    <strong>Log out</strong>
</button>
