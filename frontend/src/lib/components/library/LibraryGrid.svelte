<script lang="ts">
	import type { Snippet } from 'svelte';

	type Props = { children: Snippet };
	let { children }: Props = $props();
</script>

<div
	class="mx-auto grid max-w-7xl auto-rows-[240px] grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
>
	{@render children()}
</div>
