<script lang="ts">
	import EditorHeader from '$lib/components/editor/EditorHeader.svelte';
	import EditorPane from '$lib/components/editor/EditorPane.svelte';
	import PropertiesPanel from '$lib/components/editor/PropertiesPanel.svelte';
	import { sampleCode } from '$lib/components/editor/sample';

	let title = $state('Architectural Card');
	let language = $state('TypeScript / React');
	let showLineNumbers = $state(true);
	let wordWrap = $state(false);

	let code = $state(sampleCode);

	function handleSave() {
		// hook your backend save here
	}

	function handleRevert() {
		// hook your backend revert here
	}

	function handleDelete() {
		// hook your backend delete here
	}
</script>

<svelte:head>
	<title>Snippet Editor — Architectural Void</title>
</svelte:head>

<div class="mx-auto flex w-full max-w-7xl flex-col gap-8">
	<EditorHeader onsave={handleSave} onrevert={handleRevert} />

	<div class="grid min-h-[600px] flex-1 grid-cols-1 gap-6 lg:grid-cols-4">
		<EditorPane
			filename="{title.toLowerCase().replaceAll(' ', '-')}.tsx"
			bind:code
			{showLineNumbers}
		/>
		<PropertiesPanel
			bind:title
			bind:language
			bind:showLineNumbers
			bind:wordWrap
			ondelete={handleDelete}
		/>
	</div>
</div>
