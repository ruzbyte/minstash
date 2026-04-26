<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		title?: string;
		language?: string;
		showLineNumbers?: boolean;
		wordWrap?: boolean;
		ondelete?: () => void;
	};

	let {
		title = $bindable('Architectural Card'),
		language = $bindable('TypeScript / React'),
		showLineNumbers = $bindable(true),
		wordWrap = $bindable(false),
		ondelete
	}: Props = $props();

	const languages = ['TypeScript / React', 'HTML / CSS', 'Python', 'Rust', 'Go'];
</script>

<div
	class="relative flex flex-col gap-6 overflow-hidden rounded-xl border border-outline-variant/10 bg-surface-container-low p-6 backdrop-blur-xl"
>
	<div
		class="pointer-events-none absolute inset-0 bg-gradient-to-t from-surface-container/50 to-transparent"
	></div>

	<h3
		class="font-display relative z-10 border-b border-outline-variant/20 pb-3 text-lg font-bold text-on-surface"
	>
		Properties
	</h3>

	<div class="relative z-10 space-y-5">
		<div>
			<label
				for="prop-language"
				class="font-label mb-2 block text-xs tracking-wider uppercase text-outline"
			>
				Language
			</label>
			<div class="relative">
				<select
					id="prop-language"
					bind:value={language}
					class="w-full appearance-none rounded-t-md border-b border-outline-variant/50 bg-surface-container py-2 pr-8 pl-3 text-sm text-on-surface transition-colors focus:border-primary focus:outline-none"
				>
					{#each languages as lang (lang)}
						<option value={lang}>{lang}</option>
					{/each}
				</select>
				<Icon
					name="expand_more"
					class="pointer-events-none absolute top-1/2 right-2 -translate-y-1/2 text-outline"
				/>
			</div>
		</div>

		<div>
			<label
				for="prop-title"
				class="font-label mb-2 block text-xs tracking-wider uppercase text-outline"
			>
				Snippet Title
			</label>
			<input
				id="prop-title"
				type="text"
				bind:value={title}
				class="w-full rounded-t-md border-b border-outline-variant/50 bg-surface-container px-3 py-2 text-sm text-on-surface transition-all focus:border-b-2 focus:border-primary focus:outline-none"
			/>
		</div>

		<div class="space-y-3 pt-2">
			<label class="group flex cursor-pointer items-center justify-between">
				<span
					class="font-body text-sm text-on-surface-variant transition-colors group-hover:text-on-surface"
				>
					Show Line Numbers
				</span>
				<input
					type="checkbox"
					bind:checked={showLineNumbers}
					class="peer sr-only"
				/>
				<div
					class="relative h-5 w-10 rounded-full p-0.5 transition-colors {showLineNumbers
						? 'bg-primary/20'
						: 'bg-surface-variant'}"
				>
					<div
						class="absolute h-4 w-4 rounded-full transition-all duration-200 {showLineNumbers
							? 'right-0.5 bg-primary shadow-[0_0_10px_rgba(205,190,252,0.5)]'
							: 'left-0.5 bg-outline'}"
					></div>
				</div>
			</label>

			<label class="group flex cursor-pointer items-center justify-between">
				<span
					class="font-body text-sm text-on-surface-variant transition-colors group-hover:text-on-surface"
				>
					Word Wrap
				</span>
				<input type="checkbox" bind:checked={wordWrap} class="peer sr-only" />
				<div
					class="relative h-5 w-10 rounded-full p-0.5 transition-colors {wordWrap
						? 'bg-primary/20'
						: 'bg-surface-variant'}"
				>
					<div
						class="absolute h-4 w-4 rounded-full transition-all duration-200 {wordWrap
							? 'right-0.5 bg-primary shadow-[0_0_10px_rgba(205,190,252,0.5)]'
							: 'left-0.5 bg-outline'}"
					></div>
				</div>
			</label>
		</div>
	</div>

	<div class="relative z-10 mt-auto pt-6">
		<button
			type="button"
			onclick={ondelete}
			class="flex w-full items-center justify-center gap-2 rounded-xl border border-error/30 bg-surface-bright/30 py-3 text-sm font-medium text-error transition-colors hover:border-error/50 hover:bg-error/10"
		>
			<Icon name="delete" class="text-[18px]" />
			Delete Snippet
		</button>
	</div>
</div>
