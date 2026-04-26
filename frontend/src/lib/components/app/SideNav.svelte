<script lang="ts">
	import Icon from "../Icon.svelte";
	import { user } from "$lib/api/auth.svelte";
	export type NavKey =
		| "dashboard"
		| "library"
		| "snippets"
		| "documents"
		| "media"
		| "archive";

	type Item = { key: NavKey; label: string; icon: string; href: string };

	type Props = { active?: NavKey };
	let { active = "dashboard" }: Props = $props();

	const items: Item[] = [
		{
			key: "dashboard",
			label: "Dashboard",
			icon: "dashboard",
			href: "/app",
		},
		{
			key: "library",
			label: "Library",
			icon: "grid_view",
			href: "/app/library",
		},
		{
			key: "snippets",
			label: "Snippets",
			icon: "code",
			href: "/app/snippets",
		},
		{
			key: "documents",
			label: "Documents",
			icon: "description",
			href: "#",
		},
		{ key: "media", label: "Media", icon: "perm_media", href: "#" },
		{ key: "archive", label: "Archive", icon: "inventory_2", href: "#" },
	];
</script>

<nav
	class="font-headline fixed top-0 left-0 z-40 hidden h-screen w-72 flex-col border-r border-white/5 bg-[#15111f] pt-8 pb-4 text-sm tracking-widest uppercase md:flex"
>
	<!-- Brand -->
	<a href="/app" class="mb-8 flex items-center space-x-3 px-6">
		<div
			class="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-primary to-tertiary-container shadow-[0_0_20px_rgba(107,76,200,0.3)]"
		>
			<Icon name="widgets" class="text-on-primary" filled />
		</div>
		<div>
			<h1
				class="text-lg font-bold tracking-tighter text-primary normal-case"
			>
				{user.username || "Architect"}
			</h1>
			<p
				class="font-body text-xs font-medium text-on-surface-variant normal-case"
			>
				{user.id ? `ID: ${user.id}` : "Vault Access"}
			</p>
		</div>
	</a>

	<!-- CTA -->
	<div class="mb-8 px-6">
		<a
			href="/app/upload"
			class="flex w-full items-center justify-center space-x-2 rounded-xl bg-gradient-to-br from-primary to-tertiary-container px-4 py-3 font-bold text-on-primary shadow-[0_4px_20px_rgba(107,76,200,0.2)] transition-all duration-300 hover:shadow-[0_4px_24px_rgba(107,76,200,0.4)]"
		>
			<Icon name="add" class="text-sm" />
			<span class="normal-case">New Stash</span>
		</a>
	</div>

	<!-- Main nav -->
	<div class="flex-1 overflow-y-auto">
		<div class="space-y-1">
			{#each items as item (item.key)}
				{@const isActive = item.key === active}
				<a
					href={item.href}
					class="mb-2 flex items-center space-x-3 px-6 py-3 transition-all duration-300 {isActive
						? 'rounded-r-full border-l-2 border-primary bg-gradient-to-r from-primary/10 to-transparent font-bold text-primary'
						: 'text-slate-500 hover:translate-x-1 hover:text-primary'}"
				>
					<Icon name={item.icon} filled={isActive} />
					<span>{item.label}</span>
				</a>
			{/each}
		</div>
	</div>

	<!-- Footer nav -->
	<div class="mx-6 mt-auto space-y-1 border-t border-white/5 pt-4">
		<a
			href="#"
			class="flex items-center space-x-3 px-4 py-3 text-slate-500 transition-all duration-300 hover:translate-x-1 hover:text-primary"
		>
			<Icon name="settings" />
			<span>Settings</span>
		</a>
		<a
			href="#"
			class="flex items-center space-x-3 px-4 py-3 text-slate-500 transition-all duration-300 hover:translate-x-1 hover:text-primary"
		>
			<Icon name="help" />
			<span>Help</span>
		</a>
		<a
			href="/login"
			class="flex items-center space-x-3 px-4 py-3 text-slate-500 transition-all duration-300 hover:translate-x-1 hover:text-error"
		>
			<Icon name="logout" />
			<span>Sign Out</span>
		</a>
	</div>
</nav>
