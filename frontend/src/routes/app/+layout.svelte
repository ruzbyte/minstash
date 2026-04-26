<script lang="ts">
	import { goto } from "$app/navigation";
	import { page } from "$app/state";
	import { user } from "$lib/api/auth.svelte";
	import AppShell from "$lib/components/app/AppShell.svelte";
	import type { NavKey } from "$lib/components/app/SideNav.svelte";

	let { children } = $props();

	const active: NavKey = $derived.by(() => {
		const path = page.url.pathname;
		if (path.startsWith("/app/library")) return "library";
		if (path.startsWith("/app/snippets")) return "snippets";
		if (path.startsWith("/app/upload")) return "dashboard";
		return "dashboard";
	});
</script>

{#if user.isLoggedIn}
	<AppShell {active}>
		{@render children()}
	</AppShell>
{:else}
	<div
		class="flex flex-col min-h-screen items-center justify-center bg-background text-on-background"
	>
		<p class="text-lg">Please log in to access the dashboard.</p>
		<button
			onclick={() => goto("/login")}
			class="ml-4 rounded bg-primary px-4 py-2 text-sm text-white hover:bg-primary-hover"
		>
			Log In
		</button>
	</div>
{/if}
