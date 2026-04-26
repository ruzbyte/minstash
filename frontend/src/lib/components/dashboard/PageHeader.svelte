<script lang="ts">
	type Props = {
		title?: string;
		subtitle?: string;
	};

	let {
		title = 'Dashboard',
		subtitle = 'Latest updates and drops',
	}: Props = $props();
</script>

<div class="flex flex-col gap-2">
	<h2
		class="font-headline text-glow text-5xl font-extrabold tracking-tight text-on-surface md:text-6xl"
	>
		{title}
	</h2>
	<p class="font-body pl-1 text-sm tracking-widest uppercase text-on-surface-variant">
		{subtitle}
	</p>
</div>
