<script lang="ts">
    import api from "$lib/api";
    import { currentStock } from "$lib/stores";

    import {
        ColorType,
        CrosshairMode,
        type CandlestickData,
        type UTCTimestamp,
    } from "lightweight-charts";
    import { Chart, CandlestickSeries } from "svelte-lightweight-charts";

    import { browser } from "$app/environment";

    interface Dimensions {
        width: number;
        height: number;
    }

    export let dimensions: Dimensions;

    let request = api.pendingRequest<CandlestickData[]>();

    $: newRequest = () => api
        .price($currentStock.ticker)
        .history()
        .then((response) => response.map((price) => ({
            ...price,
            time: price.time as UTCTimestamp,
        })));

    $: if (browser) request = newRequest();

    const options = {
        layout: {
            background: {
                type: ColorType.Solid,
                color: "#303030",
            },
            textColor: "#f5f5f5",
        },
        grid: {
            vertLines: {
                color: "#4a4a4a",
            },
            horzLines: {
                color: "#4a4a4a",
            },
        },
        crosshair: {
            mode: CrosshairMode.Normal,
        },
        rightPriceScale: {
            borderColor: "#f5f5f5",
        },
        timeScale: {
            borderColor: "#f5f5f5",
        },
    };
</script>

{#await request}
    <p>Loading...</p>
{:then data}
    <Chart
        bind:width={dimensions.width}
        bind:height={dimensions.height}
        {...options}>
        <CandlestickSeries
            {data}
            upColor="#60c689"
            borderUpColor="#60c689"
            wickUpColor="#60c689"
            downColor="#e91e63"
            borderDownColor="#e91e63"
            wickDownColor="#e91e63" />
    </Chart>
{:catch error}
    <p>{error.message}</p>
{/await}
