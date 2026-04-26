<script lang="ts">
	import Icon from '../Icon.svelte';

	type Props = {
		filename?: string;
		gradient?: string;
		span?: 1 | 2;
		href?: string;
	};

	let {
		filename = 'nebula_render.png',
		gradient = 'from-tertiary-container/70 via-primary-container/40 to-[#15111f]',
		span = 1,
		href = '#'
	}: Props = $props();
</script>

<a
	{href}
	class="library-card group relative col-span-1 flex flex-col overflow-hidden rounded-xl {span ===
	2
		? 'sm:col-span-2'
		: ''}"
>
	<div
		class="absolute top-4 left-4 z-20 flex items-center space-x-2 rounded-full border border-white/10 bg-background/80 px-2.5 py-1 backdrop-blur-md"
	>
		<Icon name="image" class="text-xs text-primary" />
		<span class="font-body text-xs font-medium text-on-surface">{filename}</span>
	</div>

	<!-- Procedural gradient artwork (no external image) -->
	<div class="relative w-full flex-1 overflow-hidden">
		<div
			class="absolute inset-0 bg-gradient-to-br {gradient} transition-transform duration-700 group-hover:scale-105"
		></div>
		<div
			class="absolute -top-12 -left-12 h-40 w-40 rounded-full bg-primary/30 blur-[60px]"
		></div>
		<div
			class="absolute right-8 bottom-8 h-32 w-32 rounded-full bg-tertiary-container/40 blur-[80px]"
		></div>
		<!-- subtle grain stars -->
		<div class="pointer-events-none absolute inset-0 opacity-50 mix-blend-screen">
			<div class="absolute top-[20%] left-[30%] h-1 w-1 rounded-full bg-white/70"></div>
			<div class="absolute top-[60%] left-[70%] h-1 w-1 rounded-full bg-white/50"></div>
			<div class="absolute top-[40%] left-[55%] h-0.5 w-0.5 rounded-full bg-white/80"></div>
			<div class="absolute top-[80%] left-[25%] h-0.5 w-0.5 rounded-full bg-white/60"></div>
		</div>
		<div class="absolute inset-0 bg-gradient-to-t from-[#15111f] to-transparent opacity-50"></div>
	</div>
</a>
