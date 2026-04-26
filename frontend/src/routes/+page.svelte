<script lang="ts">
	import { onMount } from 'svelte';
	import TopNav from '$lib/components/TopNav.svelte';
	import SiteFooter from '$lib/components/SiteFooter.svelte';
	import Hero from '$lib/components/landing/Hero.svelte';
	import VaultTransition from '$lib/components/landing/VaultTransition.svelte';

	let revealed = $state(false);

	onMount(() => {
		const t = setTimeout(() => (revealed = true), 700);
		return () => clearTimeout(t);
	});
</script>

<svelte:head>
	<title>Minstash | The Architectural Void</title>
	<meta
		name="description"
		content="A sanctuary for your digital life. Engineered for the architectural void."
	/>
</svelte:head>

<div class="min-h-screen overflow-x-hidden bg-background text-on-background">
	<VaultTransition />
	<TopNav />
	<Hero {revealed} />
	<SiteFooter />
</div>
