<script lang="ts">
    import type { Trade } from "$lib/api/trades";
    import { convertUnixDate } from "$lib/functions";
    import RationalityPanel from "./RationalityPanel.svelte";

    export let data: Trade;
</script>

<tr>
    <td class="has-text-left">{convertUnixDate(data.time * 1000)}</td>
    <th class="has-text-left">{data.ticker}</th>
    <td class="has-text-left">{data.units_change >= 0 ? "Buy" : "Sell"}</td>
    <td class="has-text-left">{Math.abs(data.units_change).toFixed(2)}</td>
    <td class="has-text-right"
        >{Math.abs(data.balance_change / data.units_change).toFixed(2)}</td>
    <td class="has-text-right">{Math.abs(data.balance_change).toFixed(2)}</td>
    <td class="has-text-left"><RationalityPanel {data} /></td>
</tr>

<style>
    a.hover {
        text-decoration: underline;
        color: #276bb0;
    }
</style>
