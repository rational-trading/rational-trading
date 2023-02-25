<script lang="ts">
    import { user } from "$lib/stores";

    function handleLogout() {
        user.set(null);
        localStorage.removeItem("access_token");
    }
</script>

<button class="button is-info" on:click={() => handleLogout()}>
    <strong>Log out</strong>
</button>
