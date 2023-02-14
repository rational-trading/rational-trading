<script lang="ts">
    interface Asset {
        company: string;
        symbol: string;
        qty: number;
        currentVal: number;
        glToday: number;
        glOverall: number;
    }

    export let data: Asset;

    const colorToday = data.glToday >= 0 ? "success" : "warning";
    const colorOverall = data.glOverall >= 0 ? "success" : "warning";
</script>

<div class="block">
    <div class="columns mx-2 is-vcentered" style="margin: auto;">
        <div class="column is-2 has-text-centered">
            <div>
                <p class="heading">Company</p>
                <p class="title is-5">{data.company}</p>
            </div>
        </div>
        <div class="column has-text-centered">
            <div>
                <p class="heading">Symbol</p>
                <p class="title is-5">{data.symbol}</p>
            </div>
        </div>
        <div class="column has-text-centered">
            <div>
                <p class="heading">Qty</p>
                <p class="title is-5">{data.qty}</p>
            </div>
        </div>
        <div class="column is-2 has-text-centered">
            <div>
                <p class="heading">Current value</p>
                <p class="title is-5">£{data.currentVal}</p>
            </div>
        </div>
        <div class="column is-2 has-text-centered">
            <div>
                <p class="heading">Today's gain/loss</p>
                <p class="title is-5 has-text-{colorToday}">
                    {data.glToday >= 0 ? "" : "-"}£{Math.abs(data.glToday)} ({(
                        (data.glToday / (data.currentVal - data.glToday)) *
                        100
                    ).toFixed(2)}%)
                </p>
            </div>
        </div>
        <div class="column is-2 has-text-centered">
            <div>
                <p class="heading">Overall gain/loss</p>
                <p class="title is-5 has-text-{colorOverall}">
                    {data.glOverall >= 0 ? "" : "-"}£{Math.abs(data.glOverall)} ({(
                        (data.glOverall / (data.currentVal - data.glOverall)) *
                        100
                    ).toFixed(2)}%)
                </p>
            </div>
        </div>
        <div class="column has-text-centered">
            <button class="button is-info">Buy / Sell</button>
        </div>
    </div>
</div>
