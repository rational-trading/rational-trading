<script lang="ts">
  import "../app.scss";
</script>

<div class="columns m-6">
  <div class="column is-one-fifth" />
  <div class="column is-three-fifths">
    <div class="level">
      <div class="level-item">
        <h1 class="title is-0">Rational Trading</h1>
      </div>
    </div>
    <div class="level">
      <div class="level-item"><a href="/">Home</a></div>
      <div class="level-item"><a href="/shopping">Shopping</a></div>
    </div>
    <br />
    <br />
    <slot />
  </div>
  <div class="column is-one-fifth" />
</div>
