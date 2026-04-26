<script lang="ts">
	import Icon from '../Icon.svelte';
	import { sampleCode } from './sample';

	type Props = {
		filename?: string;
		code?: string;
		showLineNumbers?: boolean;
	};

	let {
		filename = 'component.tsx',
		code = $bindable(sampleCode),
		showLineNumbers = false
	}: Props = $props();

	const lineCount = $derived(code.split('\n').length);

	function handleCopy() {
		navigator.clipboard?.writeText(code);
	}
</script>

<div
	class="relative flex flex-col overflow-hidden rounded-xl border border-outline-variant/10 bg-surface-container-low shadow-[0_20px_50px_rgba(0,0,0,0.2)] backdrop-blur-xl lg:col-span-3"
>
	<div
		class="pointer-events-none absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent"
	></div>

	<!-- Editor header -->
	<div
		class="relative z-10 flex items-center justify-between border-b border-surface/50 bg-surface-container px-4 py-3"
	>
		<div class="flex items-center gap-3">
			<Icon name="code" class="text-sm text-primary" />
			<span class="font-body text-sm font-medium text-on-surface-variant">
				{filename}
			</span>
		</div>
		<div class="flex items-center gap-2">
			<button
				type="button"
				class="p-1 text-outline transition-colors hover:text-primary"
				aria-label="Copy"
				onclick={handleCopy}
			>
				<Icon name="content_copy" class="text-[20px]" />
			</button>
			<button
				type="button"
				class="p-1 text-outline transition-colors hover:text-primary"
				aria-label="Expand"
			>
				<Icon name="open_in_full" class="text-[20px]" />
			</button>
		</div>
	</div>

	<!-- Code area -->
	<div
		class="relative z-10 flex-1 overflow-auto bg-[#1e1e1e]/50 p-6 font-mono text-sm leading-relaxed text-[#d4d4d4]"
	>
		<div class="flex">
			{#if showLineNumbers}
				<div
					class="mr-4 shrink-0 border-r border-outline-variant/20 pr-3 text-right text-outline/60 select-none"
				>
					{#each Array.from({ length: lineCount }, (_, i) => i + 1) as n (n)}
						<div>{n}</div>
					{/each}
				</div>
			{/if}
			<textarea
				class="font-mono w-full flex-1 resize-none border-0 bg-transparent leading-relaxed text-[#d4d4d4] focus:ring-0 focus:outline-none"
				rows={Math.max(lineCount, 16)}
				bind:value={code}
				spellcheck="false"
			></textarea>
		</div>
	</div>
</div>
