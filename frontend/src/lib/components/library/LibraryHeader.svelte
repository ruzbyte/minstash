<script lang="ts">
	type Props = {
		title?: string;
		subtitle?: string;
	};

	let {
		title = 'Library',
		subtitle = 'All Stashed Artifacts'
	}: Props = $props();
</script>

<div class="mx-auto mb-12 max-w-5xl">
	<h2
		class="font-display mb-3 text-4xl font-bold tracking-tight text-on-surface md:text-5xl"
	>
		{title}
	</h2>
	<p
		class="font-body text-sm font-medium tracking-wide uppercase text-on-surface-variant opacity-80"
	>
		{subtitle}
	</p>
</div>
