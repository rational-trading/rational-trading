<div class="block">
    <h1 class="title is-1 has-text-light">Whatever topic.</h1>
    <h2 class="subtitle is-3 has-text-light">
        And maybe a little elaboration.
    </h2>
    <a class="button is-large is-info"><strong>Get started</strong></a>
</div>

<div class="bg-img" />
<slot />

<style>
    .block {
        margin-top: 10%;
        margin-left: 10%;
    }
    .bg-img {
        position: absolute;
        height: 100%;
        width: 100%;
        top: 0;
        background-image: url(home.jpeg);
        background-position: center center;
        background-repeat: no-repeat;
        background-size: cover;
        z-index: -1;
    }
</style>
