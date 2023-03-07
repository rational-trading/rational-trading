<script>
    // https://caniuse.com/#feat=css-conic-gradients
    // https://css-tricks.com/snippets/css/css-conic-gradient/
    // https://developer.mozilla.org/en-US/docs/Web/CSS/conic-gradient

    // https://stackoverflow.com/questions/2465405/svg-angular-gradient
    // https://stackoverflow.com/questions/18206361/svg-multiple-color-on-circle-stroke

    // https://bl.ocks.org/mbostock/4163057
    // https://github.com/d3/d3/issues/2427#issuecomment-100759055
    // https://github.com/mnsht/gradient-path

    // https://svelte.dev/repl/09711e43a1264ba18945d7db7cab9335?version=3.38.2
    // https://codepen.io/simeydotme/pen/rrOEmO/

    // Adopted from https://svelte.dev/repl/82e6803a2e3e4862ba292838fb7ace50?version=3.44.2

    import { spring } from "svelte/motion";
    import { arc as d3arc } from "d3-shape";
    import { scaleLinear } from "d3-scale";
    import { onMount } from "svelte";
    import { interpolateColors } from "$lib/functions";

    export let size = 1;

    const width = 150 * size;
    const height = 150 * size;

    let value = spring(0, { stiffness: 0.1 });
    export let gaugeValue = 0;

    const min = 0;
    const max = 100;

    const startAngle = -120;
    const endAngle = 120;
    const cornerRadius = 5;
    const innerRadius = 50 * size;
    const outerRadius = 50 * size + cornerRadius;

    $: scale = scaleLinear().domain([min, max]).range([startAngle, endAngle]);

    $: valueAngle = scale($value);

    $: arc = d3arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius)
        .startAngle((startAngle * Math.PI) / 180)
        .endAngle((valueAngle * Math.PI) / 180)
        .cornerRadius(cornerRadius);

    $: trackArc = d3arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius)
        .startAngle((startAngle * Math.PI) / 180)
        .endAngle((endAngle * Math.PI) / 180)
        .cornerRadius(cornerRadius);

    $: trackArcCentroid = trackArc.centroid();
    // $: console.log(trackArcCentroid)

    let trackArcEl;
    $: boundingBox = trackArc && trackArcEl ? trackArcEl.getBBox() : {};
    // $: console.log(boundingBox)

    $: textArcCenterOffset = {
        x: outerRadius - boundingBox.width / 2,
        // x: 0,
        y: (outerRadius - boundingBox.height / 2) * -1,
    };
    // $: console.log(textArcCenterOffset)

    $: textArcBottomOffset = {
        x: outerRadius - boundingBox.width / 2,
        // x: 0,
        y: (outerRadius - boundingBox.height) * -1,
    };
    // $: console.log(textArcBottomOffset)

    const showTextSvgCenter = false;
    const showTextArcCenter = false;
    const showTextArcBottom = true;
    const showTextArcCentroid = false;
    const showCenterGuide = false;

    export let startColor = "rgb(255,221,87)";
    export let endColor = "rgb(35,209,96)";
    const colors = interpolateColors(startColor, endColor, 100);

    onMount(() => {
        $value = gaugeValue;
    });
</script>

<svg {width} {height}>
    <path
        d={trackArc()}
        transform="translate({width / 2}, {height / 2})"
        class="track"
        bind:this={trackArcEl} />
    <path d={arc()} transform="translate({width / 2}, {height / 2})" />

    {#if showTextSvgCenter}
        <text transform="translate({width / 2}, {height / 2})" dy={16}>
            Evidence: {$value > 50 ? "High" : "Low"}
        </text>
    {/if}

    {#if showTextArcCenter}
        <text
            x={textArcCenterOffset.x}
            y={textArcCenterOffset.y}
            transform="translate({width / 2}, {height / 2})"
            dy={16}>
            Evidence: {$value > 50 ? "High" : "Low"}
        </text>
    {/if}

    {#if showTextArcBottom}
        <text
            x={textArcBottomOffset.x}
            y={textArcBottomOffset.y}
            transform="translate({width / 2}, {height / 2})"
            dy={0}>
            Evidence: {$value > 50 ? "High" : "Low"}
        </text>
    {/if}

    {#if showTextArcCentroid}
        <text
            x={trackArcCentroid[0]}
            y={trackArcCentroid[1]}
            transform="translate({width / 2}, {height / 2})"
            dy={16}>
            Evidence: {$value > 50 ? "High" : "Low"}
        </text>
    {/if}

    {#if showCenterGuide}
        <text transform="translate({width / 2}, {height / 2})" dy={16}>
            +
        </text>
    {/if}

    <defs>
        <linearGradient id="fillGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color={startColor} />
            <stop offset="100%" stop-color={colors[gaugeValue]} />
        </linearGradient>
    </defs>
</svg>

<style>
    path {
        fill: url(#fillGradient);
    }

    .track {
        stroke: hsla(0, 0%, 100%, 0.2);
        stroke-width: 1px;
        fill: none;
    }

    text {
        fill: #f5f5f5;
        font-size: 16px;
        font-weight: bold;
        text-anchor: middle;
    }
</style>
