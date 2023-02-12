<script lang="ts">
    interface Watchlist {
        symbol: string;
        last: number;
        chg: number;
        percentChg: number;
    }

    export let data: Watchlist;

    const color = data.chg >= 0 ? "success" : "warning";
    let selected = false;

    function click() {
        selected = !selected;
    }
</script>

<tr
    class={selected ? "is-selected" : ""}
    style="cursor: pointer;"
    on:click={() => click()}
>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-right">{data.last}</td>
    <td class="has-text-right has-text-{color}">{data.chg}</td>
    <td class="has-text-right has-text-{color}">{data.percentChg}%</td>
</tr>
