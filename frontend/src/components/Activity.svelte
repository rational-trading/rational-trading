<script lang="ts">
    interface Activity {
        time: string;
        symbol: string;
        side: string;
        qty: number;
        price: number;
        totalVal: number;
        status: string;
    }

    export let data: Activity;

    let color = "warning";
    if (data.status == "Success") {
        color = "success";
    } else if (data.status == "Rejected") {
        color = "danger";
    }
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
