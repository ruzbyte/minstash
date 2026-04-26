<script lang="ts">
	import LibraryHeader from '$lib/components/library/LibraryHeader.svelte';
	import LibraryGrid from '$lib/components/library/LibraryGrid.svelte';
	import SnippetCard from '$lib/components/library/SnippetCard.svelte';
	import MediaCard from '$lib/components/library/MediaCard.svelte';
	import DocumentCard from '$lib/components/library/DocumentCard.svelte';

	const initSequence = [
		'def initialize_void(config):',
		'    """',
		'    Bootstraps the primary ether connection.',
		'    Requires dimensional alignment.',
		'    """',
		"    if not config.get('alignment'):",
		'        raise AlignmentError("Void unstable")',
		'',
		'    session = EtherSession(',
		"        timeout=config.get('timeout', 30),",
		"        protocol='OBSIDIAN_V2'",
		'    )',
		'    return session.connect()'
	].join('\n');
</script>

<svelte:head>
	<title>Library — Architectural Void</title>
</svelte:head>

<LibraryHeader />

<LibraryGrid>
	<SnippetCard
		filename="init_sequence.py"
		language="Python"
		preview={initSequence}
		span={2}
	/>

	<MediaCard
		filename="nebula_render.png"
		gradient="from-tertiary-container/70 via-primary-container/40 to-[#15111f]"
	/>

	<DocumentCard
		title="Architecture Notes"
		excerpt="Initial thoughts on the structural integrity of the new layout system and color theory implementation."
		kind="Markdown"
		size="2kb"
		icon="description"
		iconTone="tertiary"
	/>

	<DocumentCard
		title="Design_Assets_v2.zip"
		excerpt="Contains raw Figma exports and localized token JSON files."
		kind="Archive"
		size="14MB"
		icon="folder_zip"
		iconTone="outline"
	/>

	<MediaCard
		filename="hero_bg_concept.jpg"
		gradient="from-primary/40 via-tertiary-container/50 to-[#0f0c19]"
		span={2}
	/>
</LibraryGrid>

<div class="h-24"></div>
