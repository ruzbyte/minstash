<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		title?: string;
		subtitle?: string;
		onrevert?: () => void;
		onsave?: () => void;
	};

	let {
		title = 'Snippet Editor',
		subtitle = 'Refine the Structure',
		onrevert,
		onsave
	}: Props = $props();
</script>

<header class="mb-4 flex flex-col justify-between gap-4 sm:flex-row sm:items-end">
	<div>
		<h1 class="font-display mb-2 text-4xl font-extrabold tracking-tight text-on-surface sm:text-5xl">
			{title}
		</h1>
		<p class="font-label text-sm tracking-widest uppercase text-primary">
			{subtitle}
		</p>
	</div>
	<div class="flex gap-3">
		<button
			type="button"
			onclick={onrevert}
			class="flex items-center gap-2 rounded-xl border border-outline-variant/20 bg-surface-bright/50 px-6 py-2 text-sm font-medium text-on-surface backdrop-blur-md transition-colors hover:bg-surface-bright"
		>
			<Icon name="history" class="text-lg" />
			Revert
		</button>
		<button
			type="button"
			onclick={onsave}
			class="flex items-center gap-2 rounded-xl bg-gradient-to-br from-primary to-tertiary-container px-6 py-2 text-sm font-bold text-on-primary shadow-[0_0_20px_rgba(107,76,200,0.3)] transition-all hover:shadow-[0_0_30px_rgba(107,76,200,0.5)]"
		>
			<Icon name="save" class="text-lg" />
			Save Changes
		</button>
	</div>
</header>
