<script lang="ts">
  import "../app.scss";
  import { authenticated, authenticatedUser } from "$lib/stores";
  import Login from "../components/Login.svelte";
  import Signup from "../components/Signup.svelte";
  import Logout from "../components/Logout.svelte";
  

  let authenticatedValue: boolean;
  let authenticatedUserValue: string;

  authenticated.subscribe((value) => {
      authenticatedValue = value;
  });

  authenticatedUser.subscribe((value) => {
      authenticatedUserValue = value;
  });
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
          {#if !authenticatedValue}
            <Signup />
            <Login />
          {:else}
            <p class="navbar-item mx-3">{authenticatedUserValue}</p>
            <Logout />
          {/if}
        </div>
      </div>
    </div>
  </div>
</nav>

<slot />
