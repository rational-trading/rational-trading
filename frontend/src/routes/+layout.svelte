<script lang="ts">
  import "../app.scss";
</script>

<!-- the navbar -->
<nav class="navbar is-primary">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="/logo.png" width="177" height="50" />
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
          <a class="button is-info">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            <strong>Log in</strong>
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>

<div class="columns m-6">
  <div class="column is-one-third" />
  <div class="column is-one-third">
    <div class="level">
      <div class="level-item">
        <h1 class="title is-0">Rational Trading</h1>
      </div>
    </div>
    <div class="level">
      <div class="level-item"><a href="/">Home</a></div>
      <div class="level-item"><a href="/shopping">Shopping</a></div>
      <div class="level-item"><a href="/explore">Explore</a></div>
    </div>
    <br />
    <br />
    <slot />
  </div>
  <div class="column is-one-third" />
</div>
