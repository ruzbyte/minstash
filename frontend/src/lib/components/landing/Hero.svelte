<script lang="ts">
	import Icon from '../Icon.svelte';
	import VaultMockup from './VaultMockup.svelte';

	type Props = { revealed?: boolean };
	let { revealed = false }: Props = $props();
</script>

<header
	class="relative flex min-h-screen flex-col items-center justify-center overflow-hidden px-6 pt-32 pb-24"
>
	<!-- Atmospheric glow -->
	<div
		class="pointer-events-none absolute top-1/2 left-1/2 h-[800px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary-container/10 blur-[120px]"
	></div>

	<div
		class="vault-content relative z-10 mx-auto flex max-w-4xl flex-col items-center text-center"
		class:is-revealed={revealed}
	>
		<h1
			class="font-display mb-6 text-5xl leading-[1.1] font-extrabold tracking-tighter md:text-7xl lg:text-8xl"
		>
			Stash it once.<br />
			<span class="text-gradient">Find it forever.</span>
		</h1>
		<p class="font-body mb-12 max-w-2xl text-lg text-on-surface-variant md:text-xl">
			A sanctuary for your digital life. Engineered for the architectural void.
		</p>
		<div class="flex flex-col items-center gap-4 sm:flex-row">
			<a
				href="/login"
				class="font-label group relative overflow-hidden rounded-xl bg-gradient-to-br from-primary to-tertiary-container px-8 py-4 text-lg font-medium text-on-primary transition-opacity hover:opacity-90"
			>
				<span class="relative z-10 flex items-center gap-2">
					Enter the Vault
					<Icon name="arrow_forward" class="text-sm" />
				</span>
				<div
					class="absolute inset-0 bg-primary-container/20 blur-md transition-colors group-hover:bg-primary-container/40"
				></div>
			</a>
			<button
				type="button"
				class="glass-panel font-label rounded-xl px-8 py-4 text-lg font-medium text-on-surface transition-colors hover:bg-surface-bright/50"
			>
				View Demo
			</button>
		</div>
	</div>

	<div class="vault-content w-full" class:is-revealed={revealed}>
		<VaultMockup />
	</div>
</header>
