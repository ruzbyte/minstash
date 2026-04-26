<script lang="ts">
	import { onMount } from 'svelte';
	import Icon from '../Icon.svelte';

	let opened = $state(false);

	onMount(() => {
		const t = setTimeout(() => (opened = true), 350);
		return () => clearTimeout(t);
	});
</script>

<!--
	The Vault Transition: two heavy doors swing outward on mount,
	revealing the hero content (which scales/blurs in behind them).
-->
<div
	class="pointer-events-none fixed inset-0 z-40"
	class:pointer-events-auto={!opened}
	aria-hidden="true"
>
	<div
		class="vault-door absolute inset-y-0 left-0 w-1/2 origin-left bg-gradient-to-br from-[#15111f] via-[#1d1a27] to-[#0f0c19] shadow-[inset_-40px_0_120px_rgba(0,0,0,0.55)]"
		class:is-open-left={opened}
		style="--door-origin: left center;"
	>
		<div class="absolute inset-0 opacity-30">
			<div
				class="absolute top-1/2 right-6 h-40 w-40 -translate-y-1/2 rounded-full border border-primary/20"
			></div>
			<div
				class="absolute top-1/2 right-12 h-28 w-28 -translate-y-1/2 rounded-full border border-primary/10"
			></div>
			<div
				class="absolute top-1/2 right-20 h-16 w-16 -translate-y-1/2 rounded-full border border-primary/30"
			></div>
		</div>
		<div
			class="absolute top-1/2 right-4 h-14 w-3 -translate-y-1/2 rounded-full bg-gradient-to-b from-primary/40 via-primary/10 to-transparent"
		></div>
	</div>

	<div
		class="vault-door absolute inset-y-0 right-0 w-1/2 origin-right bg-gradient-to-bl from-[#15111f] via-[#1d1a27] to-[#0f0c19] shadow-[inset_40px_0_120px_rgba(0,0,0,0.55)]"
		class:is-open-right={opened}
		style="--door-origin: right center;"
	>
		<div class="absolute inset-0 opacity-30">
			<div
				class="absolute top-1/2 left-6 h-40 w-40 -translate-y-1/2 rounded-full border border-primary/20"
			></div>
			<div
				class="absolute top-1/2 left-12 h-28 w-28 -translate-y-1/2 rounded-full border border-primary/10"
			></div>
			<div
				class="absolute top-1/2 left-20 h-16 w-16 -translate-y-1/2 rounded-full border border-primary/30"
			></div>
		</div>
		<div
			class="absolute top-1/2 left-4 h-14 w-3 -translate-y-1/2 rounded-full bg-gradient-to-b from-primary/40 via-primary/10 to-transparent"
		></div>
	</div>

	<div
		class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 transition-opacity duration-700"
		class:opacity-0={opened}
	>
		<div
			class="glass-panel relative flex h-28 w-28 items-center justify-center rounded-2xl border border-primary/30 shadow-[0_0_120px_rgba(205,190,252,0.25)]"
		>
			<Icon name="lock" class="text-4xl text-primary" />
			<div
				class="absolute inset-0 animate-pulse rounded-2xl border border-primary/20"
			></div>
		</div>
	</div>
</div>
