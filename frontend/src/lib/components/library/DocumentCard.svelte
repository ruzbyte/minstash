<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		title?: string;
		excerpt?: string;
		kind?: string;
		size?: string;
		icon?: string;
		iconTone?: 'tertiary' | 'outline' | 'primary';
		href?: string;
	};

	let {
		title = 'Architecture Notes',
		excerpt = 'Initial thoughts on the structural integrity of the new layout system and color theory implementation.',
		kind = 'Markdown',
		size = '2kb',
		icon = 'description',
		iconTone = 'tertiary',
		href = '#'
	}: Props = $props();

	const toneClass = $derived(
		iconTone === 'tertiary'
			? 'text-tertiary-container'
			: iconTone === 'primary'
				? 'text-primary'
				: 'text-outline'
	);
</script>

<a
	{href}
	class="library-card group col-span-1 flex flex-col justify-between rounded-xl p-5"
>
	<div class="mb-4 flex items-start justify-between">
		<div
			class="flex h-10 w-10 items-center justify-center rounded-full bg-surface-container-highest"
		>
			<Icon name={icon} class={toneClass} />
		</div>
		<button
			type="button"
			class="text-outline opacity-0 transition-opacity group-hover:opacity-100"
			aria-label="More options"
		>
			<Icon name="more_horiz" class="text-sm" />
		</button>
	</div>
	<div>
		<h3 class="mb-1 text-lg leading-tight font-medium text-on-surface">{title}</h3>
		<p class="mb-4 line-clamp-2 text-xs text-on-surface-variant">{excerpt}</p>
		<div
			class="flex items-center justify-between text-[10px] font-bold tracking-wider uppercase text-outline"
		>
			<span>{kind}</span>
			<span>{size}</span>
		</div>
	</div>
</a>
