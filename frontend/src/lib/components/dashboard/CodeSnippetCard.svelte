<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = { title?: string };
	let { title = 'Core Initialization' }: Props = $props();
</script>

<div class="glass-card group relative overflow-hidden rounded-xl p-6">
	<div
		class="absolute -top-10 -right-10 h-32 w-32 rounded-full bg-primary/10 blur-3xl transition-all duration-700 group-hover:bg-primary/20"
	></div>
	<h4 class="font-headline mb-4 flex items-center gap-2 text-sm font-semibold text-primary">
		<Icon name="code" class="text-base" />
		{title}
	</h4>
	<div
		class="space-y-2 rounded-lg border border-outline-variant/20 bg-surface-container-lowest/50 p-4 font-mono text-xs text-on-surface-variant/80"
	>
		<p>
			<span class="text-tertiary">import</span> {'{ VoidSystem }'}
			<span class="text-tertiary">from</span>
			<span class="text-error">'@alpha/core'</span>;
		</p>
		<p>
			<span class="text-primary">const</span> engine =
			<span class="text-secondary">new</span> VoidSystem({'{'}
		</p>
		<p class="pl-4">
			renderMode: <span class="text-error">'volumetric'</span>,
		</p>
		<p class="pl-4">
			ambientLight: <span class="text-secondary">true</span>
		</p>
		<p>{'});'}</p>
		<p>engine.<span class="text-primary">mount</span>();</p>
	</div>
</div>
