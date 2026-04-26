<script lang="ts">
	const links = [
		{ label: 'Privacy Policy', href: '#' },
		{ label: 'Terms of Service', href: '#' },
		{ label: 'Security Whitepaper', href: '#' },
		{ label: 'Contact', href: '#' }
	];

	const year = new Date().getFullYear();
</script>

<footer
	class="relative z-10 grid w-full grid-cols-1 gap-8 border-t border-white/5 bg-[#0F0C19] px-8 pt-24 pb-12 md:grid-cols-2 md:px-16"
>
	<div class="flex flex-col gap-4">
		<span class="font-display text-lg font-black tracking-tighter text-white/90">Minstash</span>
		<p class="font-label text-sm text-slate-500">
			© {year} Minstash. Engineered for the Architectural Void.
		</p>
	</div>
	<div class="flex flex-wrap items-end gap-6 md:justify-end md:gap-8">
		{#each links as link (link.label)}
			<a
				href={link.href}
				class="font-headline text-xs tracking-widest uppercase text-slate-500 transition-colors duration-300 hover:text-primary"
			>
				{link.label}
			</a>
		{/each}
	</div>
</footer>
