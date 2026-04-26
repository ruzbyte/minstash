<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		onfiles?: (files: FileList) => void;
		accept?: string;
		maxSizeLabel?: string;
	};

	let { onfiles, accept, maxSizeLabel = '2GB' }: Props = $props();

	let dragging = $state(false);
	let inputEl: HTMLInputElement | undefined = $state();

	function handleDragOver(e: DragEvent) {
		e.preventDefault();
		dragging = true;
	}

	function handleDragLeave() {
		dragging = false;
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		dragging = false;
		if (e.dataTransfer?.files) onfiles?.(e.dataTransfer.files);
	}

	function handleFiles(e: Event) {
		const target = e.currentTarget as HTMLInputElement;
		if (target.files) onfiles?.(target.files);
	}
</script>

<div
	role="button"
	tabindex="0"
	class="bg-gradient-glass glow-effect group relative flex h-[400px] cursor-pointer items-center justify-center overflow-hidden rounded-xl border border-dashed p-1 transition-all duration-500 {dragging
		? 'border-primary'
		: 'border-primary/30 hover:border-primary/60'}"
	ondragover={handleDragOver}
	ondragleave={handleDragLeave}
	ondrop={handleDrop}
	onclick={() => inputEl?.click()}
	onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && inputEl?.click()}
>
	<div
		class="absolute inset-0 bg-primary-container/10 transition-colors duration-500 group-hover:bg-primary-container/20"
	></div>

	<div class="relative z-10 flex flex-col items-center p-8 text-center">
		<div
			class="glass-panel mb-6 flex h-20 w-20 items-center justify-center rounded-full shadow-[0_0_30px_rgba(205,190,252,0.2)] transition-transform duration-500 ease-out group-hover:scale-110"
		>
			<Icon name="cloud_upload" class="text-4xl font-light text-primary" />
		</div>
		<h3 class="font-display mb-2 text-2xl font-bold text-on-surface">
			Drag &amp; Drop Files Here
		</h3>
		<p class="font-body mb-8 max-w-sm text-on-surface-variant">
			Support for high-resolution renders, CAD files, and architectural documentation up to {maxSizeLabel}.
		</p>
		<button
			type="button"
			class="glass-panel font-headline flex items-center gap-2 rounded-full border border-outline-variant/30 px-8 py-3 text-sm font-semibold text-on-surface transition-colors hover:bg-surface-bright"
			onclick={(e) => {
				e.stopPropagation();
				inputEl?.click();
			}}
		>
			<Icon name="folder_open" class="text-[1.125rem]" />
			Browse Files
		</button>
	</div>

	<input
		bind:this={inputEl}
		type="file"
		multiple
		{accept}
		class="hidden"
		onchange={handleFiles}
	/>
</div>
