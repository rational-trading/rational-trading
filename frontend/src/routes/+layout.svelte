<script lang="ts">
  import "../app.scss";
  import Login from "../components/Login.svelte";
  import Signup from "../components/Signup.svelte";
</script>

<!-- the navbar -->
<nav class="navbar is-primary">
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
          <Signup />
          <Login />
        </div>
      </div>
    </div>
  </div>
</nav>

<slot />
