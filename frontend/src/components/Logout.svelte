<script lang="ts">
    import { logout } from "$lib/auth";
</script>

<button class="button is-info" on:click={logout}>
    <strong>Log out</strong>
</button>
