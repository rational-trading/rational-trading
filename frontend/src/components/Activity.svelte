<script lang="ts">
    import type { Status } from "$types/status";

    interface Activity {
        time: string;
        symbol: string;
        side: string;
        qty: number;
        price: number;
        totalVal: number;
        status: Status;
    }

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
    <td class="has-text-left">{data.side}</td>
    <td class="has-text-left">{data.qty}</td>
    <td class="has-text-right">{data.price}</td>
    <td class="has-text-right">{data.totalVal}</td>
    <td class="has-text-left has-text-{color}">{data.status}</td>
</tr>
