<script lang="ts">
    import {
        ColorType,
        CrosshairMode,
        type CandlestickData,
    } from "lightweight-charts";
    import { Chart, CandlestickSeries } from "svelte-lightweight-charts";
    import { currentStock } from "$lib/stores";
    import api from "$lib/api";
    import { onDestroy } from "svelte";

    let data: CandlestickData[];

    const fetchData = async () => {
        const response = await api.price($currentStock.ticker).history();
        data = response.map(function (price) {
            return {
                time: new Date(price.time * 1000).toLocaleString(),
                open: price.open,
                low: price.low,
                high: price.high,
                close: price.close,
            };
        });
        return response;
    };

    let request = fetchData();

    const unsubscribe = currentStock.subscribe(() => {
        request = fetchData();
    });

    interface Dimensions {
        width: number;
        height: number;
    }

    export let dimensions: Dimensions;

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

    onDestroy(unsubscribe);
</script>

{#await request}
    <p>Loading...</p>
{:then}
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
