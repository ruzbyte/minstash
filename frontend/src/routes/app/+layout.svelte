<script lang="ts">
	import { page } from '$app/state';
	import AppShell from '$lib/components/app/AppShell.svelte';
	import type { NavKey } from '$lib/components/app/SideNav.svelte';

	let { children } = $props();

	// Auth check goes here once wired (see +layout.ts).

	const active: NavKey = $derived.by(() => {
		const path = page.url.pathname;
		if (path.startsWith('/app/library')) return 'library';
		if (path.startsWith('/app/snippets')) return 'snippets';
		if (path.startsWith('/app/upload')) return 'dashboard';
		return 'dashboard';
	});
</script>

<AppShell {active}>
	{@render children()}
</AppShell>
