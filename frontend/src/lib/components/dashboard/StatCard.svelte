<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		icon?: string;
		version?: string;
		label?: string;
		value?: string;
	};

	let {
		icon = 'data_object',
		version = 'v2.4.1',
		label = 'Active Snippets',
		value = '1,024'
	}: Props = $props();
</script>

<div
	class="glass-card flex flex-col justify-between rounded-xl p-6 transition-colors duration-300 hover:bg-surface-container-high/40"
>
	<div class="flex items-start justify-between">
		<Icon name={icon} class="text-3xl text-primary" />
		<span class="font-mono text-xs text-outline-variant">{version}</span>
	</div>
	<div>
		<p class="font-body mb-1 text-xs tracking-wider uppercase text-on-surface-variant">
			{label}
		</p>
		<p class="font-headline text-4xl font-extrabold text-on-surface">{value}</p>
	</div>
</div>
