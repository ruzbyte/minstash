<script lang="ts">
	import UploadDropzone from "$lib/components/upload/UploadDropzone.svelte";
	import UploadSettings from "$lib/components/upload/UploadSettings.svelte";
	import UploadQueue from "$lib/components/upload/UploadQueue.svelte";
	import type { QueueItem } from "$lib/components/upload/UploadQueue.svelte";

	let queue = $state<QueueItem[]>([
		{
			id: "1",
			icon: "image",
			name: "render_final_v2.exr",
			size: "1.2 GB",
			state: "uploading",
			progress: 65,
		},
		{
			id: "2",
			icon: "description",
			name: "material_specs.pdf",
			size: "45 MB",
			state: "queued",
		},
	]);

	let folder = $state("/Installations/2024");
	let access = $state<"private" | "team">("private");

	function handleFiles(files: FileList) {
		for (const file of files) {
			queue.push({
				id: crypto.randomUUID(),
				icon: file.type.startsWith("image/") ? "image" : "description",
				name: file.name,
				size: formatSize(file.size),
				state: "queued",
			});
		}
	}

	function removeItem(id: string) {
		queue = queue.filter((item) => item.id !== id);
	}

	function formatSize(bytes: number) {
		if (bytes >= 1024 ** 3) return (bytes / 1024 ** 3).toFixed(1) + " GB";
		if (bytes >= 1024 ** 2) return (bytes / 1024 ** 2).toFixed(1) + " MB";
		if (bytes >= 1024) return (bytes / 1024).toFixed(1) + " KB";
		return bytes + " B";
	}
</script>

<svelte:head>
	<title>Upload — Architectural Void</title>
</svelte:head>

<div class="mx-auto mb-12 max-w-5xl">
	<h2
		class="font-display text-gradient mb-2 text-4xl font-extrabold tracking-tight md:text-5xl"
	>
		Upload Assets
	</h2>
	<p
		class="font-body text-sm tracking-widest uppercase text-on-surface-variant"
	>
		Architectural Void / Project Space
	</p>
</div>

<div class="mx-auto grid max-w-5xl grid-cols-1 gap-8 lg:grid-cols-12">
	<div class="lg:col-span-8">
		<UploadDropzone onfiles={handleFiles} />
	</div>

	<div class="flex flex-col gap-6 lg:col-span-4">
		<UploadSettings bind:folder bind:access />
		<UploadQueue items={queue} onremove={removeItem} />
	</div>
</div>
