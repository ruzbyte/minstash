<script lang="ts">
	import Icon from "../Icon.svelte";

	type Props = {
		searchPlaceholder?: string;
		notificationDot?: boolean;
	};

	let {
		searchPlaceholder = "Search the void...",
		notificationDot = false,
	}: Props = $props();
</script>

<header
	class="font-headline sticky top-0 z-50 flex w-full items-center justify-between bg-[#15111f]/60 px-8 py-3 tracking-tight shadow-[0_8px_32px_0_rgba(75,62,115,0.1)] backdrop-blur-2xl"
>
	<!-- Left: mobile brand & search -->
	<div class="flex flex-1 items-center space-x-6">
		<a
			href="/app"
			class="text-xl font-black tracking-tighter text-primary md:hidden"
		>
			Stash
		</a>

		<!-- Search bar -->
		<div
			class="glass-panel relative hidden w-full max-w-md rounded-full md:block"
		>
			<div
				class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-4"
			>
				<Icon name="search" class="text-outline" />
			</div>
			<input
				type="text"
				placeholder={searchPlaceholder}
				class="w-full border-none bg-transparent py-2.5 pr-4 pl-12 text-sm text-on-surface placeholder-outline focus:ring-0 focus:outline-none"
			/>
		</div>
	</div>

	<!-- Right: actions & profile -->
	<div class="flex items-center space-x-2">
		<a
			href="/app/snippets"
			class="rounded-full p-2 text-slate-400 transition-all duration-300 hover:bg-white/5 hover:text-primary"
			aria-label="New snippet"
		>
			<Icon name="add_circle" />
		</a>
		<a
			href="/app/upload"
			class="rounded-full p-2 text-slate-400 transition-all duration-300 hover:bg-white/5 hover:text-primary"
			aria-label="Upload"
		>
			<Icon name="cloud_upload" />
		</a>
		<button
			type="button"
			class="relative rounded-full p-2 text-slate-400 transition-all duration-300 hover:bg-white/5 hover:text-primary"
			aria-label="Settings"
		>
			<Icon name="settings" />
			{#if notificationDot}
				<span
					class="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-primary"
				></span>
			{/if}
		</button>
	</div>
</header>
