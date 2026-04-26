<script lang="ts">
	import Icon from '../Icon.svelte';

	type Asset = { icon: string; title: string; meta: string };

	type Props = { assets?: Asset[]; heading?: string };

	let {
		heading = 'Recent Assets',
		assets = [
			{
				icon: 'texture',
				title: 'Obsidian Surface Material',
				meta: 'High-res texture maps • 24MB'
			},
			{
				icon: 'view_in_ar',
				title: 'Floating Staircase Node',
				meta: '3D Geometry • 1.2MB'
			},
			{
				icon: 'animation',
				title: 'Ambient Light Pulse Sequence',
				meta: 'Animation Data • 450KB'
			}
		]
	}: Props = $props();
</script>

<div class="glass-card mt-4 rounded-xl p-8 md:col-span-3">
	<h3 class="font-headline mb-6 flex items-center gap-3 text-xl font-bold text-on-surface">
		<Icon name="folder_open" class="text-primary" />
		{heading}
	</h3>

	<div class="space-y-4">
		{#each assets as asset (asset.title)}
			<a
				href="#"
				class="group flex cursor-pointer items-center justify-between rounded-lg border border-transparent p-4 transition-all duration-300 hover:border-outline-variant/20 hover:bg-surface-container-high/40"
			>
				<div class="flex items-center gap-4">
					<div
						class="flex h-12 w-12 items-center justify-center rounded-lg border border-outline-variant/30 bg-surface-container-lowest transition-colors group-hover:border-primary/40"
					>
						<Icon name={asset.icon} class="text-on-surface-variant" />
					</div>
					<div>
						<p class="font-headline text-sm font-semibold text-on-surface">
							{asset.title}
						</p>
						<p class="font-body mt-0.5 text-xs text-outline-variant">{asset.meta}</p>
					</div>
				</div>
				<Icon
					name="arrow_forward"
					class="text-outline-variant transition-colors group-hover:text-primary"
				/>
			</a>
		{/each}
	</div>
</div>
