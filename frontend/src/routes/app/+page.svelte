<script lang="ts">
	import PageHeader from "$lib/components/dashboard/PageHeader.svelte";
	import FeaturedAsset from "$lib/components/dashboard/FeaturedAsset.svelte";
	import StatCard from "$lib/components/dashboard/StatCard.svelte";
	import CodeSnippetCard from "$lib/components/dashboard/CodeSnippetCard.svelte";
	import RecentAssets from "$lib/components/dashboard/RecentAssets.svelte";
</script>

<svelte:head>
	<title>Dashboard — Architectural Void</title>
</svelte:head>

<div class="mx-auto max-w-7xl space-y-12">
	<PageHeader />

	<div
		class="grid auto-rows-[minmax(200px,auto)] grid-cols-1 gap-6 md:grid-cols-3"
	>
		<FeaturedAsset />
		<StatCard />
		<CodeSnippetCard />
		<RecentAssets />
	</div>
</div>
