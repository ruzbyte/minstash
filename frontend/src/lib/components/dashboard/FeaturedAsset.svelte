<script lang="ts">
	type Props = {
		badge?: string;
		timestamp?: string;
		title?: string;
		description?: string;
	};

	let {
		badge = 'Featured Asset',
		timestamp = 'Added 2 hrs ago',
		title = 'Monolithic Glass Module',
		description = 'A scalable architectural snippet designed for high-density virtual environments. Includes responsive structural nodes.'
	}: Props = $props();
</script>

<div
	class="glass-card group relative flex cursor-pointer flex-col justify-end overflow-hidden rounded-xl p-8 transition-all duration-500 hover:shadow-[0_20px_40px_rgba(107,76,200,0.15)] md:col-span-2 md:row-span-2"
>
	<!-- Architectural void mock background -->
	<div
		class="absolute inset-0 z-0 opacity-50 transition-opacity duration-700 group-hover:opacity-70"
	>
		<div
			class="absolute inset-0 bg-gradient-to-br from-tertiary-container/60 via-primary-container/40 to-surface-dim"
		></div>
		<div
			class="absolute -top-24 -right-16 h-72 w-72 rounded-full bg-primary/30 blur-[80px]"
		></div>
		<div
			class="absolute -bottom-32 -left-16 h-80 w-80 rounded-full bg-tertiary-container/40 blur-[100px]"
		></div>
		<!-- Faux structural lines -->
		<div
			class="absolute top-1/4 left-1/3 h-48 w-px bg-gradient-to-b from-transparent via-primary/40 to-transparent"
		></div>
		<div
			class="absolute top-1/3 right-1/3 h-64 w-px rotate-12 bg-gradient-to-b from-transparent via-primary/30 to-transparent"
		></div>
	</div>

	<div
		class="absolute inset-0 z-10 bg-gradient-to-t from-surface-dim via-surface-dim/40 to-transparent"
	></div>

	<div class="relative z-20">
		<div class="mb-3 flex items-center gap-2">
			<span
				class="rounded-full border border-outline-variant/30 bg-surface-container-high/80 px-3 py-1 text-[0.65rem] font-bold tracking-widest uppercase text-primary backdrop-blur-md"
			>
				{badge}
			</span>
			<span class="font-body text-xs text-on-surface-variant/70">{timestamp}</span>
		</div>
		<h3 class="font-headline mb-2 text-3xl font-bold text-on-surface">{title}</h3>
		<p class="font-body max-w-md text-sm text-on-surface-variant/80">{description}</p>
	</div>
</div>
