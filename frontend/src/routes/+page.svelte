<script lang="ts">
    import data from "$lib/data";
    import { double } from "$common";
    import type { Post } from "$common";

    const p: Post = { title: "GME Crashes", id: 4 };
</script>

<div class="content">
    <p>Some data is: {data}</p>
    <p>The post title is: {p.title}</p>
    <p>The post id is {p.id}, and doubled is {double(p.id)}</p>
</div>
