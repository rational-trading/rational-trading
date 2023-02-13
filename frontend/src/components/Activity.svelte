<script lang="ts">
    import type { Activity } from "$lib/types";

    export let data: Activity;

    const statusColors = {
        Filled: "success",
        Pending: "warning",
        Rejected: "danger",
    };

    $: color = statusColors[data.status];
</script>

<tr>
    <td class="has-text-left">{data.time}</td>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-left"
        >{data.quantity_bought >= 0 ? "bought" : "sold"}</td>
    <td class="has-text-left">{data.quantity_bought}</td>
    <td class="has-text-right">{data.price}</td>
    <td class="has-text-right">{data.price * data.quantity_bought}</td>
    <td class="has-text-left has-text-{color}">{data.status}</td>
</tr>
