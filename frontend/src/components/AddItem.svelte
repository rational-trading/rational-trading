<script lang="ts">
    import {
        displaySymbol,
        displayCompany,
        displayExchange,
        watchSymbols,
        currentStock,
    } from "$lib/stores";

    interface AddItem {
        symbol: string;
        company: string;
        exchange: string;
    }

    export let data: AddItem;
    export let active = true;

    function click() {
        watchSymbols.update((symbols) => {
            if (symbols.indexOf(data.symbol) == -1) {
                return [...symbols, data.symbol];
            } else {
                return symbols;
            }
        });
        active = false;
    }
</script>

<tr style="cursor: pointer;" on:click={click}>
    <th class="has-text-left">{data.symbol}</th>
    <td class="has-text-left">{data.company}</td>
    <td class="has-text-right">{data.exchange}</td>
</tr>
