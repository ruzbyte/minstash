<script lang="ts">
	import Icon from '../Icon.svelte';

	export type QueueItem = {
		id: string;
		icon: string;
		name: string;
		size: string;
		state: 'uploading' | 'queued' | 'done' | 'error';
		progress?: number;
	};

	type Props = {
		items?: QueueItem[];
		onremove?: (id: string) => void;
		onprocess?: () => void;
	};

	let {
		items = [
			{
				id: '1',
				icon: 'image',
				name: 'render_final_v2.exr',
				size: '1.2 GB',
				state: 'uploading',
				progress: 65
			},
			{
				id: '2',
				icon: 'description',
				name: 'material_specs.pdf',
				size: '45 MB',
				state: 'queued'
			}
		],
		onremove,
		onprocess
	}: Props = $props();
</script>

<div class="glass-panel flex flex-1 flex-col rounded-xl p-6">
	<h4 class="font-display mb-6 flex items-center justify-between text-lg font-bold text-on-surface">
		<span class="flex items-center gap-2">
			<Icon name="format_list_bulleted" class="text-[1.25rem] text-primary" />
			Queue
		</span>
		<span
			class="font-body rounded-md bg-surface-container-high px-2 py-1 text-xs font-normal text-on-surface-variant"
		>
			{items.length} {items.length === 1 ? 'File' : 'Files'}
		</span>
	</h4>

	<div class="flex-1 space-y-3">
		{#each items as item (item.id)}
			{@const isUploading = item.state === 'uploading'}
			<div
				class="group relative overflow-hidden rounded-lg border bg-surface-container-low p-4 {item.state ===
				'queued'
					? 'border-outline-variant/10 opacity-60'
					: 'border-outline-variant/20'}"
			>
				{#if isUploading && item.progress !== undefined}
					<div
						class="absolute bottom-0 left-0 h-1 bg-primary shadow-[0_0_10px_rgba(205,190,252,0.8)]"
						style="width: {item.progress}%"
					></div>
				{/if}
				<div class="flex items-start justify-between">
					<div class="flex items-center gap-3">
						<Icon
							name={item.icon}
							class={isUploading ? 'text-primary/70' : 'text-on-surface-variant'}
						/>
						<div>
							<p class="font-body w-40 truncate text-sm font-medium text-on-surface">
								{item.name}
							</p>
							<p class="font-body text-xs text-on-surface-variant">
								{item.size} •
								{#if isUploading}
									{item.progress}%
								{:else if item.state === 'queued'}
									Queued
								{:else if item.state === 'done'}
									Complete
								{:else}
									Failed
								{/if}
							</p>
						</div>
					</div>
					<button
						type="button"
						onclick={() => onremove?.(item.id)}
						class="text-on-surface-variant transition-colors hover:text-error"
						aria-label="Remove {item.name}"
					>
						<Icon name="close" class="text-[1.125rem]" />
					</button>
				</div>
			</div>
		{/each}
	</div>

	<button
		type="button"
		onclick={onprocess}
		class="font-headline mt-4 w-full rounded-lg border border-primary/20 bg-surface-container-high px-4 py-3 text-sm font-semibold text-primary transition-colors hover:bg-surface-bright"
	>
		Process Queue
	</button>
</div>
