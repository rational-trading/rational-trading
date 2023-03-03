<script lang="ts">
    import type { Activity } from "$lib/types";
    import { convertUnixDate } from "$lib/functions";

    export let data: Activity;

    const statusColors = {
        Filled: "success",
        Pending: "warning",
        Rejected: "danger",
    };

    $: color = statusColors[data.status];
</script>

<tr>
    <td class="has-text-left">{convertUnixDate(data.time * 1000)}</td>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-left">{data.quantity_bought >= 0 ? "Buy" : "Sell"}</td>
    <td class="has-text-left">{Math.abs(data.quantity_bought).toFixed(2)}</td>
    <td class="has-text-right">{Math.abs(data.price).toFixed(2)}</td>
    <td class="has-text-right"
        >{Math.abs(data.price * data.quantity_bought).toFixed(2)}</td
    >
    <td class="has-text-left has-text-{color}">{data.status}</td>
</tr>
