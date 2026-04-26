<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		folder?: string;
		access?: 'private' | 'team';
	};

	let {
		folder = $bindable('/Installations/2024'),
		access = $bindable('private')
	}: Props = $props();
</script>

<div class="glass-panel relative overflow-hidden rounded-xl p-6">
	<div class="absolute top-0 right-0 h-32 w-32 rounded-full bg-primary/5 blur-[50px]"></div>

	<h4 class="font-display mb-6 flex items-center gap-2 text-lg font-bold text-on-surface">
		<Icon name="settings_suggest" class="text-[1.25rem] text-primary" />
		Upload Settings
	</h4>

	<div class="space-y-5">
		<div>
			<label
				for="upload-folder"
				class="font-label mb-2 block text-xs tracking-widest uppercase text-on-surface-variant"
			>
				Destination Folder
			</label>
			<button
				id="upload-folder"
				type="button"
				class="flex w-full cursor-pointer items-center justify-between rounded-t-md border-b border-outline-variant/50 bg-surface-container-low p-3 transition-colors hover:bg-surface-container"
			>
				<span class="font-body flex items-center gap-2 text-sm text-on-surface">
					<Icon name="folder" class="text-[1.125rem] text-primary/70" />
					{folder}
				</span>
				<Icon name="expand_more" class="text-[1.125rem] text-on-surface-variant" />
			</button>
		</div>

		<div>
			<span
				class="font-label mb-2 block text-xs tracking-widest uppercase text-on-surface-variant"
			>
				Access Level
			</span>
			<div class="flex gap-2">
				<button
					type="button"
					onclick={() => (access = 'private')}
					class="glass-panel flex-1 rounded-lg py-2 text-sm font-medium transition-colors {access ===
					'private'
						? 'border-primary/50 bg-primary/5 text-primary'
						: 'border-outline-variant/20 text-on-surface-variant hover:text-on-surface'}"
				>
					Private
				</button>
				<button
					type="button"
					onclick={() => (access = 'team')}
					class="glass-panel flex-1 rounded-lg py-2 text-sm font-medium transition-colors {access ===
					'team'
						? 'border-primary/50 bg-primary/5 text-primary'
						: 'border-outline-variant/20 text-on-surface-variant hover:text-on-surface'}"
				>
					Team
				</button>
			</div>
		</div>
	</div>
</div>
