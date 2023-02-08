<script lang="ts">
  import "../app.scss";
</script>

<!-- the navbar -->
<nav class="navbar is-primary">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="/logo.png" width="177" height="50" alt="logo" />
    </a>

    <!-- mobile burger ignore for now
    <a
      role="button"
      class="navbar-burger"
      aria-label="menu"
      aria-expanded="false"
      data-target="navbarBasicExample"
    >
      <span aria-hidden="true" />
      <span aria-hidden="true" />
      <span aria-hidden="true" />
    </a>
  -->
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
          <a href="/" class="button is-primary">
            <strong>Log in</strong>
          </a>
          <a href="/" class="button is-info">
            <strong>Sign up</strong>
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>

<slot />
