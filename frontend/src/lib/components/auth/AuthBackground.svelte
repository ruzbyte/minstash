<script lang="ts">
	const topConfig = `export const config = {
  vault: "secured",
  encryption: "AES-256",
  monolith: true,
  access: "granted",
  theme: "obsidian-ether"
};

function initAuth() {
  const kernel = await load();
  return kernel.bind();
}`;

	const bottomConfig = `{
  "project": "minstash",
  "version": "5.0.0-violet",
  "architecture": "obsidian-ether",
  "dependencies": {
    "logic": "heavy",
    "design": "glassy"
  }
}`;
</script>

<!-- Architectural background: ambient blobs + decorative code -->
<div class="pointer-events-none absolute inset-0 overflow-hidden">
	<div
		class="absolute top-[-10%] left-[-10%] h-[60%] w-[60%] animate-pulse rounded-full bg-accent/10 blur-[140px]"
	></div>
	<div
		class="absolute right-[-10%] bottom-[-10%] h-[50%] w-[50%] rounded-full bg-secondary-container/30 blur-[120px]"
	></div>
</div>

<div
	class="pointer-events-none fixed top-32 right-24 hidden rotate-12 select-none opacity-[0.05] lg:block"
>
	<pre class="font-mono text-sm leading-relaxed text-primary">{topConfig}</pre>
</div>
<div
	class="pointer-events-none fixed bottom-32 left-24 hidden -rotate-6 select-none opacity-[0.05] lg:block"
>
	<pre class="font-mono text-sm leading-relaxed text-primary">{bottomConfig}</pre>
</div>
