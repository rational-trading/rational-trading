<script lang="ts">
  import api from "$lib/api";
  import { authenticated, authenticatedUser } from "$lib/stores";

  let active = false;

  let username = "";
  let password = "";
  let confirmPassword = "";

  async function handleSignup() {
    try {
      if (password != confirmPassword)
        throw new Error("Passwords have to match!");

      let jwt_token = await api.signup().post(username, password);
      authenticated.set(true);
      localStorage.setItem("access_token", jwt_token);

      let whoami = await api.whoami().get();
      authenticatedUser.set(whoami);

      active = false;
    } catch (error: any) {
      alert(error.message);
      authenticated.set(false);
      authenticatedUser.set("");
    }
  }
</script>

<button
  class="button is-info"
  on:click={() => {
    active = true;
  }}
>
  <strong>Sign up</strong>
</button>

{#if active}
  <div class="modal is-active">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="modal-background" on:click={() => (active = false)} />
    <div class="modal-content">
      <div class="is-flex is-flex-direction-column">
        <div class="is-align-self-flex-end">
          <button class="button is-ghost" on:click={() => (active = false)}>
            <span class="icon is-large">
              <i class="fas fa-xmark" />
            </span>
          </button>
        </div>
        <div class="is-flex is-flex-direction-column pt-0" id="login-contents">
          <p class="title is-1">Sign up</p>

          <div class="field mt-5">
            <div class="control">
              <input
                class="input"
                placeholder="Username"
                bind:value={username}
              />
            </div>
          </div>
          <div class="field mt-1">
            <div class="control">
              <input
                class="input"
                type="password"
                placeholder="Password"
                bind:value={password}
              />
            </div>
          </div>

          <div class="field mt-1">
            <div class="control">
              <input
                class="input"
                type="password"
                placeholder="Repeat password"
                bind:value={confirmPassword}
              />
            </div>
          </div>

          <div class="is-align-self-flex-end pt-5">
            <div class="field">
              <div class="control">
                <button
                  class="button is-link is-medium"
                  on:click={() => handleSignup()}
                  ><p class="px-3">
                    <strong>Sign up</strong>
                  </p></button
                >
              </div>
            </div>
          </div>

          <div class="is-align-self-center pt-6">
            <p>
              Already have an account? Log in <a class="link" href="/">here</a>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .modal-content {
    width: 31.25em;
    height: 35.5em;
    background: #363636;
    border-radius: 7px;
  }

  .link:hover {
    text-decoration: underline;
    color: #276bb0;
  }

  #login-contents {
    margin: 2.5em 3.125em 0em;
  }
</style>
