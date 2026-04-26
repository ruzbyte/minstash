<script lang="ts">
	type Link = { label: string; href: string; active?: boolean };

	type Props = {
		brand?: string;
		links?: Link[];
		ctaLabel?: string;
		ctaHref?: string;
		signInLabel?: string;
		signInHref?: string;
	};

	let {
		brand = 'Minstash',
		links = [
			{ label: 'Vault', href: '/', active: true },
			{ label: 'Security', href: '#' },
			{ label: 'Features', href: '#' },
			{ label: 'Pricing', href: '#' }
		],
		ctaLabel = 'Get Started',
		ctaHref = '/register',
		signInLabel = 'Login',
		signInHref = '/login'
	}: Props = $props();
</script>

<nav
	class="fixed top-6 left-1/2 z-50 flex w-[95%] max-w-6xl -translate-x-1/2 items-center justify-between rounded-full border border-white/10 bg-[#0e0b18]/60 px-6 py-3 shadow-[0_8px_32px_0_rgba(75,62,115,0.15)] backdrop-blur-2xl transition-all duration-500 ease-out"
>
	<a href="/" class="flex items-center gap-2">
		<span class="font-display text-2xl font-bold tracking-tighter text-white">{brand}</span>
	</a>

	<div class="hidden items-center gap-8 md:flex">
		{#each links as link (link.href + link.label)}
			<a
				href={link.href}
				class="font-headline pb-1 text-sm font-medium tracking-[0.1em] uppercase transition-colors {link.active
					? 'border-b border-primary/50 text-primary'
					: 'text-slate-400 hover:text-white'}"
			>
				{link.label}
			</a>
		{/each}
	</div>

	<div class="flex items-center gap-4">
		<a
			href={signInHref}
			class="font-label hidden text-sm text-on-surface transition-colors hover:text-primary md:block"
		>
			{signInLabel}
		</a>
		<a
			href={ctaHref}
			class="font-label rounded-full bg-gradient-to-br from-primary to-tertiary-container px-5 py-2 text-sm text-on-primary transition-opacity hover:opacity-90"
		>
			{ctaLabel}
		</a>
	</div>
</nav>
