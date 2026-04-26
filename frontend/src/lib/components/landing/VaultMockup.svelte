<script lang="ts">
	import Icon from '../Icon.svelte';
</script>

<div
	class="pointer-events-none relative mx-auto mt-24 flex h-[600px] w-full max-w-5xl items-center justify-center"
>
	<!-- Central cube -->
	<div
		class="glass-panel relative z-20 flex h-64 w-64 items-center justify-center rounded-2xl border border-primary/20 bg-gradient-to-br from-surface-container/80 to-surface/40 shadow-[0_0_80px_rgba(205,190,252,0.1)]"
	>
		<Icon name="inventory_2" class="text-6xl text-primary/50" />
	</div>

	<!-- Floating snippet card (left) -->
	<div
		class="glass-panel float-y-slow absolute top-1/4 left-1/4 w-48 rotate-[-12deg] rounded-xl border border-outline-variant/30 p-4 shadow-lg"
		style="--float-rotate: rotate(-12deg);"
	>
		<div
			class="mb-2 flex h-24 w-full items-center justify-center rounded bg-surface-container-low"
		>
			<Icon name="code" class="text-outline" />
		</div>
		<div class="h-2 w-3/4 rounded bg-surface-variant"></div>
	</div>

	<!-- Floating image card (right) -->
	<div
		class="glass-panel float-y absolute right-1/4 bottom-1/3 z-30 w-56 rotate-[8deg] rounded-xl border border-outline-variant/30 p-4 shadow-lg"
		style="--float-rotate: rotate(8deg);"
	>
		<div
			class="relative mb-2 h-32 w-full overflow-hidden rounded bg-gradient-to-br from-tertiary-container/40 via-primary-container/30 to-surface-container-low"
		>
			<div
				class="absolute -top-6 -left-6 h-24 w-24 rounded-full bg-primary/30 blur-2xl"
			></div>
			<div
				class="absolute right-2 bottom-2 h-16 w-16 rounded-full bg-tertiary-container/50 blur-xl"
			></div>
		</div>
		<div class="mb-1 h-2 w-1/2 rounded bg-surface-variant"></div>
		<div class="h-2 w-1/3 rounded bg-surface-variant"></div>
	</div>

	<!-- Floating note card (small) -->
	<div
		class="glass-panel float-y-fast absolute top-1/2 right-1/3 w-32 rotate-[25deg] rounded-lg border border-outline-variant/30 p-3 shadow-lg"
		style="--float-rotate: rotate(25deg);"
	>
		<div class="mb-2 flex items-center gap-2">
			<Icon name="description" class="text-xs text-primary" />
			<div class="h-1.5 w-12 rounded bg-surface-variant"></div>
		</div>
		<div class="space-y-1">
			<div class="h-1 w-full rounded bg-surface-variant"></div>
			<div class="h-1 w-4/5 rounded bg-surface-variant"></div>
			<div class="h-1 w-full rounded bg-surface-variant"></div>
		</div>
	</div>
</div>
