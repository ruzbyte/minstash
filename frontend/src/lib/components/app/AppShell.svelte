<script lang="ts">
	import SideNav from './SideNav.svelte';
	import AppTopBar from './AppTopBar.svelte';
	import type { Snippet } from 'svelte';
	import type { NavKey } from './SideNav.svelte';

	type Props = {
		active?: NavKey;
		notificationDot?: boolean;
		searchPlaceholder?: string;
		children: Snippet;
	};

	let {
		active = 'dashboard',
		notificationDot = false,
		searchPlaceholder = 'Search the void...',
		children
	}: Props = $props();
</script>

<div class="flex h-screen overflow-hidden bg-background text-on-background">
	<SideNav {active} />

	<main class="relative flex h-screen flex-1 flex-col md:ml-72">
		<AppTopBar {notificationDot} {searchPlaceholder} />

		<div class="flex-1 overflow-y-auto p-8 lg:p-12">
			{@render children()}
		</div>
	</main>
</div>
