<script lang="ts">
	import AuthBackground from './AuthBackground.svelte';

	type Props = { children: import('svelte').Snippet };
	let { children }: Props = $props();

	const footerLinks = [
		{ label: 'Privacy Protocol', href: '#' },
		{ label: 'Governance', href: '#' },
		{ label: 'Node Status', href: '#' }
	];
</script>

<!-- Floating top nav (Obsidian Ether style) -->
<nav
	class="fixed top-0 left-1/2 z-50 mx-auto mt-6 flex w-[92%] max-w-5xl -translate-x-1/2 items-center justify-between rounded-full border border-white/10 bg-surface/60 px-8 py-3 shadow-[0_8px_32px_rgba(75,62,115,0.2)] backdrop-blur-xl"
>
	<a href="/" class="font-headline text-2xl font-black tracking-tighter text-primary">
		Minstash
	</a>
	<div class="hidden items-center gap-8 md:flex">
		<a
			href="#"
			class="font-headline text-sm font-medium tracking-tight text-primary/60 transition-all duration-300 hover:text-primary"
		>
			Explore
		</a>
		<a
			href="#"
			class="font-headline text-sm font-medium tracking-tight text-primary/60 transition-all duration-300 hover:text-primary"
		>
			Features
		</a>
		<a
			href="#"
			class="font-headline text-sm font-medium tracking-tight text-primary/60 transition-all duration-300 hover:text-primary"
		>
			Showcase
		</a>
	</div>
	<div class="flex items-center gap-4">
		<a
			href="/login"
			class="font-headline hidden text-sm font-bold text-primary/80 transition-transform active:scale-95 sm:block"
		>
			Sign In
		</a>
		<a
			href="/register"
			class="rounded-full bg-gradient-to-br from-[#cdbefc] to-[#6b4cc8] px-6 py-2 text-sm font-bold text-on-primary shadow-lg shadow-accent/20 transition-transform active:scale-95"
		>
			Launch
		</a>
	</div>
</nav>

<div
	class="relative flex min-h-screen flex-col items-center justify-center overflow-hidden px-4 pt-24 pb-12"
>
	<AuthBackground />

	<!-- Brand anchor -->
	<div class="relative z-10 mb-10 text-center">
		<h1 class="font-headline text-5xl font-extrabold tracking-tighter text-white">
			minstash
		</h1>
		<p class="font-label mt-3 text-[10px] tracking-[0.3em] uppercase text-primary/60">
			Architectural Code Vault
		</p>
	</div>

	<!-- Auth card -->
	<main
		class="glass-morphism relative z-10 w-full max-w-md overflow-hidden rounded-2xl"
	>
		<div class="shimmer pointer-events-none absolute inset-0 opacity-30"></div>
		{@render children()}
		<!-- Bottom accent -->
		<div
			class="h-[1px] w-full bg-gradient-to-r from-transparent via-primary/30 to-transparent"
		></div>
	</main>

	<!-- Footer links -->
	<footer class="z-10 mt-12 flex flex-wrap justify-center gap-10">
		{#each footerLinks as link (link.label)}
			<a
				href={link.href}
				class="font-label text-[10px] tracking-[0.2em] uppercase text-white/30 transition-colors hover:text-primary"
			>
				{link.label}
			</a>
		{/each}
	</footer>
</div>
