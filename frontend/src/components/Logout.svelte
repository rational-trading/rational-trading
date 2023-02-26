<script lang="ts">
    import { logout } from "$lib/auth";
</script>

<a class="navbar-item" href="/" on:click={logout}> Log out </a>
