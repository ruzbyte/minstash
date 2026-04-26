<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		filename?: string;
		language?: string;
		preview?: string;
		span?: 1 | 2;
		href?: string;
	};

	let {
		filename = 'init_sequence.py',
		language = 'Python',
		preview = '',
		span = 2,
		href = '/app/snippets'
	}: Props = $props();
</script>

<a
	{href}
	class="library-card group col-span-1 flex flex-col rounded-xl p-5 {span === 2
		? 'sm:col-span-2'
		: ''}"
>
	<div class="mb-4 flex items-start justify-between">
		<div class="flex items-center space-x-2">
			<span
				class="flex items-center justify-center rounded-lg bg-primary/10 p-1.5 text-primary"
			>
				<Icon name="code" class="text-sm" />
			</span>
			<span class="font-body text-sm font-medium text-on-surface">{filename}</span>
		</div>
		<span class="font-mono text-xs text-outline">{language}</span>
	</div>
	<div
		class="relative flex-1 overflow-hidden rounded-lg bg-[#0f0c19] p-4 font-mono text-xs text-outline-variant"
	>
		<div
			class="pointer-events-none absolute inset-0 z-10 bg-gradient-to-b from-transparent to-[#0f0c19]"
		></div>
		<pre class="whitespace-pre">{preview}</pre>
	</div>
</a>
